#!/bin/bash
if ! [[ "$#" = "2" || "$#" = "3" ]]; then
	exit 1
fi

if ! [[ -e "$1" && -e "$1" ]]; then
	exit 1
fi

if ! [[ -f $1 && -f $2 ]]; then
	exit 1
fi

if ! [[ -r $1 || -r $2 ]]; then
	exit 1
fi

if [[ "$#" = "3" ]]; then
	if ! [[ "$3" = "-v" ]]; then
		exit 1
	fi
	str1=""
	str2=""
	IFS_OLD="$IFS"
	count="0"
	myfile1="$(mktemp)"
	DONE=false
	until $DONE ;
	do
    read -r y || DONE=true
		for i in $y;
		do
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.]?[0-9]*[eE][-+]?[0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
		done
	done < "$1"
	if [[ $count == "0" ]]; then
		rm "$myfile1"
		exit 1
	fi
	count="0"
	myfile2="$(mktemp)"
	DONE=false
	until $DONE ;do
    read -r y || DONE=true
		for i in $y;
		do
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.]?[0-9]*[eE][-+]?[0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
		done
	done < "$2"
	IFS="$IFS_OLD"
	if [[ $count == "0" ]]; then
		rm "$myfile1" "$myfile2"
		exit 1
	fi
	count="0"
	if cmp -s "$myfile1" "$myfile2" ; then
		echo "Files are similar"
		rm "$myfile1" "$myfile2"
		exit 0
	else
		echo "Files are not similar"
		rm "$myfile1" "$myfile2"
		exit 1
	fi
else
	str1=""
	str2=""
	IFS_OLD="$IFS"
	count="0"
	myfile1="$(mktemp)"
	DONE=false
	until $DONE ;do
    read -r y || DONE=true
		for i in $y;
		do
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.]?[0-9]*[eE][-+]?[0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile1"
				count=$(($count + 1))
			fi
		done
	done < "$1"
	if [[ $count == "0" ]]; then
		rm "$myfile1"
		exit 1
	fi
	count="0"
	myfile2="$(mktemp)"
	DONE=false
	until $DONE ;do
    read -r y || DONE=true
		for i in $y;
		do
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*[.]?[0-9]*[eE][-+]?[0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
			if [[ "$i" =~ ^[+-]?[0-9][0-9]*$ ]] ;  then
				echo "$i " >> "$myfile2"
				count=$(($count + 1))
			fi
		done
	done < "$2"
	IFS="$IFS_OLD"
	if [[ $count == "0" ]]; then
		rm "$myfile1" "$myfile2"
		exit 1
	fi
	count="0"
	if cmp -s "$myfile1" "$myfile2" ; then
		rm "$myfile1" "$myfile2"
		exit 0
	else
		rm "$myfile1" "$myfile2"
		exit 1
	fi
fi
