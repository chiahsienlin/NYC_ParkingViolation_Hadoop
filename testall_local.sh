
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

./testtask_local.sh 1 parking-violations.csv,open-violations.csv $1
./testtask_local.sh 2 parking-violations.csv $1
./testtask_local.sh 3 open-violations.csv $1
./testtask_local.sh 4 parking-violations.csv $1
./testtask_local.sh 5 parking-violations.csv $1
./testtask_local.sh 6 parking-violations.csv $1
./testtask_local.sh 7 parking-violations.csv $1
./testtask_local.sh 8 parking-violations.csv $1

###rm parking-violations.csv
###rm open-violations.csv
