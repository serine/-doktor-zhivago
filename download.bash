
for i in {1..229}
do
  echo ${i}
  if [[ $i -lt 10 ]]
  then
    ./p.py $i > book/00${i}.Rmd
  elif [[ $i -lt 100 ]]
  then
    ./p.py $i > book/0${i}.Rmd
  else
    ./p.py $i > book/$i.Rmd
  fi
done
