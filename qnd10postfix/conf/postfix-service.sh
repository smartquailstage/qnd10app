#!/bin/bash

function log {
  echo "$(date) $ME - $@"
}

function addUserInfo {
  # Add user 'info' if it doesn't exist
  if ! id -u info &>/dev/null; then
    log "Adding user 'info'"
    adduser -D -H info
  else
    log "User 'info' already exists"
  fi
}

function createVirtualDomainsTable {
  log "Creating virtual_domains table in PostgreSQL..."
  psql -U "$POSTFIX_POSTGRES_USER" -d "$POSTFIX_POSTGRES_DB" -h "$POSTFIX_POSTGRES_HOST" -c "CREATE TABLE IF NOT EXISTS virtual_domains (
    id SERIAL PRIMARY KEY,
    domain VARCHAR(255) NOT NULL UNIQUE
  );"

  log "Granting SELECT permission on virtual_domains table to $POSTFIX_POSTGRES_USER..."
  psql -U "$POSTFIX_POSTGRES_USER" -d "$POSTFIX_POSTGRES_DB" -h "$POSTFIX_POSTGRES_HOST" -c "GRANT SELECT ON TABLE virtual_domains TO $POSTFIX_POSTGRES_USER;"
}

function serviceConf {
  # Check hostname variable
  if [[ ! ${HOSTNAME} =~ \. ]]; then
    HOSTNAME=$HOSTNAME.$DOMAIN
  fi

  # Substitute configuration
  for VARIABLE in $(env | cut -f1 -d=); do
    VAR=${VARIABLE//:/_}
    sed -i "s={{ $VAR }}=${!VAR}=g" /etc/postfix/*.cf
  done

  # Override Postfix configuration
  if [ -f /overrides/postfix.cf ]; then
    while read -r line; do
      [[ -n "$line" && "$line" != [[:blank:]#]* ]] && postconf -e "$line"
    done < /overrides/postfix.cf
    echo "Loaded '/overrides/postfix.cf'"
  else
    echo "No extra postfix settings loaded because optional '/overrides/postfix.cf' not provided."
  fi

  # Include table-map files
  if ls -A /overrides/*.map 1> /dev/null 2>&1; then
    cp /overrides/*.map /etc/postfix/
    postmap /etc/postfix/*.map
    rm /etc/postfix/*.map
    chown root:root /etc/postfix/*.db
    chmod 0600 /etc/postfix/*.db
    echo "Loaded 'map files'"
  else
    echo "No extra map files loaded because optional '/overrides/*.map' not provided."
  fi
}

function serviceStart {
  addUserInfo
  createVirtualDomainsTable  # Llama a la función para crear la tabla virtual_domains y otorgar permisos
  serviceConf
  # Actually run Postfix
  log "[ Starting Postfix... ]"
  /usr/sbin/postfix start-fg
}

export DOMAIN=${DOMAIN:-"localdomain"}
export HOSTNAME=${HOSTNAME:-"localhost"}
export MESSAGE_SIZE_LIMIT=${MESSAGE_SIZE_LIMIT:-"50000000"}
export RELAYNETS=${RELAYNETS:-""}
export RELAYHOST=${RELAYHOST:-""}

export POSTFIX_POSTGRES_DB=${POSTFIX_POSTGRES_DB}
export POSTFIX_POSTGRES_PASSWORD=${POSTFIX_POSTGRES_PASSWORD}
export POSTFIX_POSTGRES_USER=${POSTFIX_POSTGRES_USER}
export POSTFIX_POSTGRES_HOST=${POSTFIX_POSTGRES_HOST}

serviceStart &>> /proc/1/fd/1
