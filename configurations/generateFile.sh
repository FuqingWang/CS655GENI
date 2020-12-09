#!/bin/bash

# make two folders
mkdir cache
mkdir nocache

cd cache/
# Generate file of size from 5M to 100M, with a stepsize of 5
for size in {5..100..5}
do
	dd if=/dev/zero of=file.${size}M bs=${size}M count=1
done

cd ../nocache/
# Generate file of size from 5M to 100M, with a stepsize of 5
for size in {5..100..5}
do
	dd if=/dev/zero of=file.${size}M.nocache bs=${size}M count=1
done
