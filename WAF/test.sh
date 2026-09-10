#!/bin/bash

for x in {1..200}
do
    output=$(curl -s <LOAD_BALANCER_DNS>/ | grep h1)
    echo $x - $output
    sleep 0.5
done