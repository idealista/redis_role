#!/bin/bash
echo never | tee /sys/kernel/mm/transparent_hugepage/enabled 
exit 0
