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
	count=0
	count1=0
	count2=0
	str2=""
	IFS_OLD="$IFS"
	IFS=''
  	count="0"
	myfile1="$(mktemp)"
	DONE=false
	until $DONE ;do
		read -r y || DONE=true
		if [[ $count == 0 ]]; then
			if [[ "$y" == *"string:"* ]]; then
	    		count1=$(($count1+1))
	    		count=$(($count+1))
	    		echo "$(echo "$y" | grep -Eo "string:.*")" >> "$myfile1"
	  		fi
		else
	  		count1=$(($count1+1))
	 		echo "$y" >> "$myfile1"
		fi
  	done < "$1"
  	if [[ $count -eq 0 ]]; then
  		rm "$myfile1"
		echo "The 'string:' is not found"
		exit 1
	fi
	count=0
	myfile2="$(mktemp)"
	DONE=false
	until $DONE ;do
		read -r y || DONE=true
		if [[ $count == 0 ]]; then
			if [[ "$y" == *"string:"* ]]; then
				count2=$(($count2+1))
				count=$(($count+1))
				echo "$(echo "$y" | grep -Eo "string:.*")" >> "$myfile2"
			fi
		else
			count2=$(($count2+1))
			echo "$y" >> "$myfile2"
		fi
	done < "$2"
  
	if [[ $count -eq 0 ]]; then
		rm "$myfile1" "$myfile2"
		echo "The 'string:' is not found"
		exit 1
	fi
  
	if ! [[ "$count1" == "$count2" ]]; then
		rm "$myfile1" "$myfile2"
		echo "Files are different"
		exit 1
	fi
  
	count=0
	IFS="$IFS_OLD"
  	if cmp -s "$myfile1" "$myfile2" ; then
  		rm "$myfile1" "$myfile2"
  	    echo "Files are similar"
		exit 0
	else
		rm "$myfile1" "$myfile2"
	    echo "Files are different"
		exit 1
	fi
else
	str1=""
	count=0
	count1=0
	count2=0
	str2=""
	IFS_OLD="$IFS"
	IFS=''
  	count="0"
	myfile1="$(mktemp)"
	DONE=false
	until $DONE ;do
		read -r y || DONE=true
		if [[ $count == 0 ]]; then
			if [[ "$y" == *"string:"* ]]; then
        		count1=$(($count1+1))
        		count=$(($count+1))
        		echo "$(echo "$y" | grep -Eo "string:.*")" >> "$myfile1"
      		fi
    	else
      		count1=$(($count1+1))
     		echo "$y" >> "$myfile1"
    	fi
  	done < "$1"
  	if [[ $count -eq 0 ]]; then
  		rm "$myfile1"
		exit 1
	fi
	count=0
	myfile2="$(mktemp)"
	DONE=false
	until $DONE ;do
		read -r y || DONE=true
		if [[ $count == 0 ]]; then
			if [[ "$y" == *"string:"* ]]; then
				count2=$(($count2+1))
				count=$(($count+1))
				echo "$(echo "$y" | grep -Eo "string:.*")" >> "$myfile2"
			fi
		else
			count2=$(($count2+1))
			echo "$y" >> "$myfile2"
		fi
	done < "$2"
  
	if [[ $count -eq 0 ]]; then
		rm "$myfile1" "$myfile2"
		exit 1
	fi
  
	if ! [[ "$count1" == "$count2" ]]; then
		rm "$myfile1" "$myfile2"
		exit 1
	fi
  
	count=0
	IFS="$IFS_OLD"
  	if cmp -s "$myfile1" "$myfile2" ; then
  		rm "$myfile1" "$myfile2"
		exit 0
	else
		rm "$myfile1" "$myfile2"
		exit 1
	fi
fi
