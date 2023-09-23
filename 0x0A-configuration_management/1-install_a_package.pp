# Install flask from pip3
# Ensure pip3 is installed
package { 'python3-pip':
  ensure   => 'installed',
  provider => 'apt',
}

# Install flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
