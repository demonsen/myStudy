
export HISTSIZE=10000
readonly PROMPT_COMMAND='{ msg=$(history 1 | { read x y; echo $y; });logger -p local1.info "[euid=$(whoami)][$(who am i)][$(pwd)]:$msg"; }'
export PROMPT_COMMAND
export HISTTIMEFORMAT="%F %T `whoami`> "
