#!/bin/bash
apt install gir1.2-appindicator3-0.1 gir1.2-notify-0.7 python python-gtk2 python-gi python-retrying 
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
