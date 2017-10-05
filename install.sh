#!/bin/bash
input="debian/install"
while IFS= read -r line
do
	space_separated_line=(`echo $line`)
	src=$space_separated_line
	target="/${space_separated_line[1]}"
	`cp $src $target`
    if [ $? -eq 0 ]
	then
		echo "$src copied to $target"
	fi
done < "$input"
