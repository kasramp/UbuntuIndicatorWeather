# This file is part of indicator-weather
# Indicator Weather is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation.
#
# Indicator Weather is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.  <http://www.gnu.org/licenses/>
#
# Author(s):
# © 2015-2018 Kasra Madadipouya <kasra@madadipouya.com>

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
