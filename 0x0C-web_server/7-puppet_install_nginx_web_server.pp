# Install and configure Nginx with puppet

include stdlib

$link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$mod_configuration = "\trewrite ^/redirect_me/$ ${link} permanent;"

exec { 'update apt repository':
  command => '/usr/bin/apt-get update'
}

package { 'Nginx':
  ensure  => 'installed',
  require => Exec['update apt repository']
}

exec { 'restart service nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['Nginx']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { '301 redirect':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  line     =>  $mod_configuration,
  multiple => true,
  notify   => Exec['restart service nginx'],
  require  => File['/var/www/html/index.html']
}
