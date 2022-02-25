#!/bin/bash
ip=$1
sudo ntpdate -u $ip
ntpq -pn