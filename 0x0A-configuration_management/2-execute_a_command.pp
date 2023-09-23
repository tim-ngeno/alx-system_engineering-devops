# Kills a process named `killmenow`
exec { 'kill-process-killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
