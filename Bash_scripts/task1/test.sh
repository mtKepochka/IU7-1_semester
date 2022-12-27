echo "TEST1 - similar file"
bash comparator1.sh ./tests/1.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "1" ]]; then
	echo "TEST1 - FAILED"
fi
if [[ "$VAR1" == "0" ]]; then
	echo "TEST1 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST1 - ERROR"
fi
echo "TEST2 - changed 1 value"
bash comparator1.sh ./tests/3.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "0" ]]; then
	echo "TEST2 - FAILED"
fi
if [[ "$VAR1" == "1" ]]; then
	echo "TEST2 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST2 - ERROR"
fi
echo "TEST3 - changed value inside word"
bash comparator1.sh ./tests/4.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "1" ]]; then
	echo "TEST3 - FAILED"
fi
if [[ "$VAR1" == "0" ]]; then
	echo "TEST3 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST3 - ERROR"
fi
echo "TEST4 - changed 2 values"
bash comparator1.sh ./tests/5.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "0" ]]; then
	echo "TEST4 - FAILED"
fi
if [[ "$VAR1" == "1" ]]; then
	echo "TEST4 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST4 - ERROR"
fi
echo "TEST5 - no values"
bash comparator1.sh ./tests/6.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "0" ]]; then
	echo "TEST5 - FAILED"
fi
if [[ "$VAR1" == "1" ]]; then
	echo "TEST5 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST5 - ERROR"
fi
echo "TEST6 - only similar values with no text"
bash comparator1.sh ./tests/7.txt ./tests/2.txt 
VAR1="$?"
if [[ "$VAR1" == "1" ]]; then
	echo "TEST6 - FAILED"
fi
if [[ "$VAR1" == "0" ]]; then
	echo "TEST6 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST6 - ERROR"
fi
echo "TEST7 - only 1 argument given"
bash comparator1.sh ./tests/1.txt
VAR1="$?"
if [[ "$VAR1" == "0" ]]; then
	echo "TEST7 - FAILED"
fi
if [[ "$VAR1" == "1" ]]; then
	echo "TEST7 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST7 - ERROR"
fi
echo "TEST8 - fake files given"
bash comparator1.sh ./tests/8.txt ./tests/9.txt
VAR1="$?"
if [[ "$VAR1" == "0" ]]; then
	echo "TEST8 - FAILED"
fi
if [[ "$VAR1" == "1" ]]; then
	echo "TEST8 - PASSED"
fi
if [[ "$VAR1" == "2" ]]; then
	echo "TEST8 - ERROR"
fi
