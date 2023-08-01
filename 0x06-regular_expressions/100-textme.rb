#!/usr/bin/env ruby
sender, receiver, flags = ARGV[0].match(/from:(\+?\w+)\W+to:(\+?\w+)\W+flags:((\W?\d:?)+)/).captures
puts "#{sender},#{receiver},#{flags}"
