
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

./testtask_hadoop.sh 1 /user/ecc290/HW1data/parking-violations.csv,/user/ecc290/HW1data/open-violations.csv $1 
./testtask_hadoop.sh 2 /user/ecc290/HW1data/parking-violations.csv $1
./testtask_hadoop.sh 3 /user/ecc290/HW1data/open-violations.csv $1
./testtask_hadoop.sh 4 /user/ecc290/HW1data/parking-violations.csv $1
./testtask_hadoop.sh 5 /user/ecc290/HW1data/parking-violations.csv $1
./testtask_hadoop.sh 6 /user/ecc290/HW1data/parking-violations.csv $1
./testtask_hadoop.sh 7 /user/ecc290/HW1data/parking-violations.csv $1
./testtask_hadoop.sh 8 /user/ecc290/HW1data/parking-violations.csv $1

