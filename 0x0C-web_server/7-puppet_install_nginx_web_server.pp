# Install and configure Nginx web server using puppet
include stdlib

$link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'

package { 'Nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "rewrite ^/redirect_me ${link} permanent;",
}

exec { 'reload configuration':
  command => '/usr/sbin/service nginx restart',
  require => Package['Nginx'],
}
