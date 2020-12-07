#!/bin/bash

# Generate file of size from 1M to 100M, with a stepsize of 5
dd if=/dev/zero of=file.1M bs=1M count=1
for size in {5..100..5}
do
	dd if=/dev/zero of=file.${size}M bs=${size}M count=1
done