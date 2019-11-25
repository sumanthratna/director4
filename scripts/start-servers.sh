#!/bin/bash
cd "$(dirname -- "$(readlink -f "$0")")/.."

tmux new-session -c manager "expect ../scripts/launch-and-interact.exp 'fab runserver'" ';' split-window -p 50 -c orchestrator "expect ../scripts/launch-and-interact.exp 'fab runserver'"