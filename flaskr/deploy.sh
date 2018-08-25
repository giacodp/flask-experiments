# For logging:  create a variabile LOGGING with the logging-file name called in log.py
#               create a variabile DT (the same you can find on setup.cfg
#               adding "$DT" at the beginning of every line you want to log
#               adding "| tee -a $LOGGING" at the end of every line you want to log

LOGGING="logging.log"
DT=$(date '+[%d/%m/%Y %H:%M:%S UTC%z(%Z)]')

# log stuff
echo "$DT <<<<<----- Starting deploy ----->>>>>" | tee -a $LOGGING
pwd | tee -a $LOGGING

# the stuff the script does (I don't want to show them)
echo "Bitbucket Repo: $1, GitHub Repo: $2, Bitbucket Branch: $3" > /home/giacomo/Documenti/temp/output.txt

# other log stuff
echo "$DT ----->>>>> Deploy ended <<<<<-----" | tee -a $LOGGING
