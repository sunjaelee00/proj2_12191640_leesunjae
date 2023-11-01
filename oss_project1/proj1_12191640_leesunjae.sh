#! /bin/bash

echo "-----------------------------------"
echo "User Name: leesunjae"
echo "Student Number: 12191640"
echo "[  MENU  ]"
echo "1. Get the data of the movie identified by a specific 'movie id' from 'u.item'"
echo "2. Get the data of action genre movies from 'u.item'"
echo "3. Get the average 'rating' of the movie identified by specific 'movie id' from 'u.data'"
echo "4. Delete the 'IMDb URL' from 'u.item'"
echo "5. Get the data about users from 'u.user'"
echo "6. Modify the format of 'release date' in 'u.item'"
echo "7. Get the data of movies rated by a specific 'user id' from 'u.data'"
echo "8. Get the average 'rating' of movies rated by users with 'age' between 20 and 29 and 'occupation' as 'programmer'"
echo "9. Exit"
echo "-----------------------------------"

choice=0
val=0
while ((choice != 9))
do
read -p  "Enter your choice [ 1-9 ] " choice 
case $choice in
1)
read -p  "Please enter the 'movie id' (1 ~ 1682): " val
cat $1 | awk -F\| '$1=='"$val"' {print $0}'
;;
2)
read -p "Do you want to get the data of 'action' genre movies from 'u.item'? (y/n) : " val
if [ ${val} == "y" ]
then cat $1 | awk -F\| '$7==1 {print $1,$2}' | awk 'FNR<=10{print $0}'
else
echo "You answered no."
fi
;;
3)
read -p "Please enter the 'movie id' (1 ~ 1682): " val
cat $2 | awk '$2=="'$val'"{print $3}' | awk '{sum += $1} END {printf("average rating of %d: %.5f\n", "'$val'",sum/FNR)}' 
;;
4)
read -p  "Do you want to delete the 'IMDb URL' from 'u.item'? (y/n): " val
if [ ${val} == "y" ]
then cat $1 | sed -E 's/http[^\|]*\|//g' | awk 'FNR<=10{print $0}'
else 
echo "you answered no."
fi
;;
5)
read -p "Do you want to get the data about users from 'u.user'? (y/n): " val
if [ ${val} == "y" ] 
then cat $3 | awk -F\| '{print $1,$2,$3,$4}' | sed -E 's/M/male/g' | sed -E 's/F/female/g' |  sed -E 's/([0-9]+) ([0-9]+) (.*) (.*)/user \1 is \2 years old \3 \4/' | awk 'FNR<=10{print $0}'
else
echo "you answered no."
fi
;;
6)
read -p "Do you want to Modify the format of 'realease data' in 'u.item'? (y/n): " val
if [ ${val} == "y" ] 
then cat $1 | sed -E 's/([0-9]+)-(.*)-([0-9]+)/\3\2\1/' | sed -E 's/Jan/01/g' | sed -E 's/Feb/02/g' |sed -E 's/Mar/03/g' | sed -E 's/Sep/09/g' | sed -E 's/Oct/10/g' | sed -E 's/Apr/04/g' | sed -E 's/May/05/g' | sed -E 's/Jun/06/g' | sed -E 's/Jul/07/g' | sed -E 's/Aug/08/g' | sed -E 's/Nov/11/g' | sed -E 's/Dec/12/g' | awk 'FNR>1672 {print $0}'
else
echo "you answered no."
fi
;;
7)
read -p "Please enter the 'user id' (1~943): " val
movie=$(cat $2 | awk '$1 == "'$val'" {print $2}' | sort -n)
cat $2 | awk '$1 == "'$val'" {print $2}' | sort -n | awk '{printf("%d|", $1)}'
echo "" 
echo ""
for m in $movie
do
	the_movie+=$(cat $1 | awk -F\| '$1 == "'$m'" {print $1"|"$2}')
	the_movie+=$'\n'
done
echo "$the_movie" | awk 'FNR<=10 {print $0}'
;;
8)
read -p "Do you want to get the average 'rating' of movies rated by users with 'age' between 20 and 29 and 'occupation' as 'programmer'? (y/n) :" val
if [ ${val} == "y" ] 
then user=$(cat $3 | awk -F\| '$2 >= 20 && $2 <30 && $4 == "programmer" {print $1}')
movie=0
movide_onlyid=0
for u in $user
do 
	movie+=$(cat $2 | awk '$1 == "'$u'" {print $2,$3}')
	movie+=$'\n'
	movie_onlyid+=$(cat $2 | awk '$1 == "'$u'" {print $2}')
	movie_onlyid+=$'\n'
done
movie_sort_withrate=$(echo -n "$movie" | sort -n)
movie_sort=$(echo -n "$movie_onlyid" | sort -n -u)
round(){
	echo $(printf %.5f $(echo "scale=5;(((10^5)*$1)+0.5)/(10^5)" | bc)) 
}
for u in $movie_sort
do
        s=0
	echo "$movie_sort_withrate" | awk '$1 == "'$u'" {print $0}' | awk -v sum=$s '{sum+=$2} 
        END {avg=round sum/FNR
             print $1, avg}'
done
else
echo "you answered no."
fi
;;
9)
;;
esac
done
echo "Bye!" 
