#!/bin/bash

which find > /dev/null || exit 1
which sha1sum > /dev/null || exit 2

rm -f .sha-sums

for file in $(find -type f)
do
    sha1sum $file >> .sha-sums
done

echo "Deleting files"
for duplicate in $(cat .sha-sums | python3 files-to-delete.py)
do
    echo "$duplicate"
    rm -f $duplicate
done
