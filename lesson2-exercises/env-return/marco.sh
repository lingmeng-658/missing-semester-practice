#!/usr/bin/env bash

marco(){
    MARCO_DIR="$(pwd)"
    
    
    echo "Saved current directory: $MARCO_DIR"
}

polo() {
    if [[ -z "$MARCO_DIR" ]]; then
        echo "marco has not been called yet."
        return 1
    fi

    cd "$MARCO_DIR" || return 1
}
