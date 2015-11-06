 #Hyo Kim 100560568
#!/bin/bash

#store argument
k=$(($1 + 1))
m=$2
fileName=$3 
head -n -$m "$fileName" | tail -n +$k