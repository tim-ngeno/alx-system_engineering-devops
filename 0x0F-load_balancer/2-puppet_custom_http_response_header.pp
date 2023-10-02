# Ensure the nginx package is installed
exec { 'update apt':
  command => 'sudo apt-get update',
}

exec { 'install nginx':
  command => 'sudo apt-get install -y nginx',
  require => Exec['update apt']
}

package { 'nginx':
  ensure  => present,
  require => Exec['install nginx'],
}

# Ensure nginx service is running and enabled at boot
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'], # Start service after installation
}

# Add the custom header to nginx configuration
file_line { 'nginx_custom_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  notify  => Service['nginx'],
  require => Package['nginx'],
}
