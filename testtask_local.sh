
module load python/gnu/3.4.4

if [ ! -f parking-violations.csv ]
then
        /usr/bin/hadoop fs -get /user/ecc290/HW1data/parking-violations.csv
fi
if [ ! -f open-violations.csv ]
then
        /usr/bin/hadoop fs -get /user/ecc290/HW1data/open-violations.csv
fi


###rm -r -f results
if [ ! -d results ]
then
        mkdir results
fi

MAPPER=$(echo "$3/task$1"/*map*.py)
REDUCER=$(echo "$3/task$1"/*reduce*.py)
DIFFFILE="results/task$1.diff"
TMPFILE="$3/task$1/task$1tmp.out"
if [ -e "$DIFFFILE" ]; then
	rm "$DIFFFILE" 
fi
if [ "$1" -eq 1 ]
then
	export mapreduce_map_input_file="parking-violations.csv"
	cat parking-violations.csv | python3 "$MAPPER" > t1tmp.txt
	export mapreduce_map_input_file="open-violations.csv"
	cat open-violations.csv | python3 "$MAPPER" >> t1tmp.txt
	cat t1tmp.txt | sort -n | python3 "$REDUCER" | sort -n > "$TMPFILE"
	rm t1tmp.txt
else
	if [ "$1" -eq 8 ] || [ "$1" -eq 6 ]
	then
		cat "$2" | python3 "$MAPPER" | sort -n | python3 "$REDUCER"  > "$TMPFILE"
	
	else
		cat "$2" | python3 "$MAPPER" | sort -n | python3 "$REDUCER" | sort -n > "$TMPFILE"
	fi
fi


if [ -e "$TMPFILE" ]
then
	#DIFF=$(diff -w "keys/task$1.out" "$TMPFILE")
	#DIFFC=$(diff -w -y "keys/task$1.out" "$TMPFILE")
	DIFF=$(diff -w <(sort "keys/task$1.out") <(sort "$TMPFILE"))
	DIFFC=$(diff -w -y --suppress-common-lines <(sort "keys/task$1.out") <(sort "$TMPFILE"))
	if [ "$DIFF" ]
	then 
		echo "$DIFFC" > "results/task$1_local.diff"
		echo "Task $1: Failed. See errors in results/task$1_local.diff"
		echo "Task $1: Failed. See errors in results/task$1_local.diff" > "results/task$1_local.res"
	else
		echo "Task $1: Passed."
		echo "Task $1: Passed." > "results/task$1_local.res"
	fi
else
	echo "Task $1: Failed; no output generated."
	echo "Task $1: Failed; no output generated." > "results/task$1_local.res"
fi
#rm -f "$TMPFILE"  


