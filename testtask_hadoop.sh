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


cdir=$(pwd)

cat map.sh | sed -e "s/\$1/"$1"/" > "$3"/"task$1"/map.sh
cat reduce.sh | sed -e "s/\$1/"$1"/" > "$3"/"task$1"/reduce.sh


cd "$3"
/usr/bin/hadoop fs -rm -r -f "task$1tmp.out"

MAPPER=$(echo "task$1"/*map*.sh)
REDUCER=$(echo "task$1"/*reduce*.sh)


if [ "$1" -eq 5 ] || [ "$1" -eq 6 ] || [ "$1" -eq 8 ]
then
	/usr/bin/hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapreduce.job.reduces=1 -files "task$1/" -mapper "$MAPPER" -reducer "$REDUCER" -input "$2" -output "task$1tmp.out" 

	/usr/bin/hadoop fs -getmerge "task$1tmp.out" "task$1/task$1tmp.out"
else
	/usr/bin/hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapreduce.job.reduces=2 -files "task$1/" -mapper "$MAPPER" -reducer "$REDUCER" -input "$2" -output "task$1tmp.out"
	/usr/bin/hadoop fs -getmerge "task$1tmp.out" "task$1/task$1tmp2.out"
	cat "task$1/task$1tmp2.out" | sort -n > "task$1/task$1tmp.out"
fi



outputlines=$(cat "task$1/task$1tmp.out"| wc -l)
if [ -e "task$1/task$1tmp.out" ] && [ ! "$outputlines" -eq 0  ]
then

#	DIFF=$(diff -w "$cdir/keys/task$1.out" "task$1/task$1tmp.out")
#	DIFFC=$(diff -w -y --suppress-common-lines "$cdir/keys/task$1.out" "task$1/task$1tmp.out")
	DIFF=$(diff -w <(sort "$cdir/keys/task$1.out") <(sort "task$1/task$1tmp.out"))
	DIFFC=$(diff -w -y --suppress-common-lines <(sort "$cdir/keys/task$1.out") <(sort "task$1/task$1tmp.out"))
	if [ "$DIFF" ]
	then 
		echo "$DIFFC" > "$cdir/results/task$1_hadoop.diff"
		echo "Task $1: Failed. See errors in results/task$1_hadoop.diff"
		echo "Task $1: Failed. See errors in results/task$1_hadoop.diff" > "$cdir/results/task$1_hadoop.res"
	else
		echo "Task $1: Passed."
		echo "Task $1: Passed." > "$cdir/results/task$1_hadoop.res"
	fi
else
	echo "Task $1: Failed; no output generated."
	echo "Task $1: Failed; no output generated." > "$cdir/results/task$1_hadoop.res"
fi
rm -f "task$1/task$1tmp2.out"
rm -f "task$1/task$1tmp.out"
rm -r "task$1"/.*.crc
rm "task$1"/map.sh
rm "task$1"/reduce.sh

/usr/bin/hadoop fs -rm -r -f "task$1tmp.out"

cd "$cdir"
