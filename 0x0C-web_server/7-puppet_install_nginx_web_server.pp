# Install and configure Nginx web server using puppet
include stdlib

# Update apt repositories
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'Nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

# Run Nginx service
service { 'nginx service':
  ensure    => running,
  enable    => true,
  require   => Package['Nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}

# NGINX CONFIGURATION
$nginx_configuration = @("EOT")
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    locatioin / {
      try_files ${uri} ${uri}/ =404;
    }

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
| EOT

# Default configuration for nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $nginx_configuration,
  require => Package['Nginx'],
}


# Content for html page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!\n',
  require => Package['Nginx'],
}

exec { 'reload configuration':
  command => '/usr/sbin/service nginx restart',
  require => Package['Nginx'],
}
