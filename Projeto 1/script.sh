# Test
echo "$(cat 'FILE_INPUT.txt')" | python mapper.py | sort -k1,1 | python reducer.py

# Start ssh Server
systemctl start sshd

# Start Hadoop
hadoop namenode -format # If needed
start-dfs.sh
start-yarn.sh

# Hadoop Prep
$HADOOP_HOME/bin/hadoop fs -ls /user/input
$HADOOP_HOME/bin/hadoop fs -mkdir /user
$HADOOP_HOME/bin/hadoop fs -mkdir /user/input
$HADOOP_HOME/bin/hadoop fs -mkdir /user/input/sertanejo
$HADOOP_HOME/bin/hadoop fs -copyFromLocal /home/letras/sertanejo/* /user/input/sertanejo
$HADOOP_HOME/bin/hadoop fs -ls /user/input
...
$HADOOP_HOME/bin/hadoop fs -mkdir /user/output

# Other commands
stop-all.sh
$HADOOP_HOME/bin/hadoop fs -rm -r <directory> # Remove Folder, if needed

# MapReduce Execution
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \ 
-file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py \
-input /user/input/sertanejo/* -output /user/output

# Getting Results
$HADOOP_HOME/bin/hadoop fs -ls /user/output #Show result files
$HADOOP_HOME/bin/hadoop fs -cat /user/output/OUTFILE  # Visualize results
$HADOOP_HOME/bin/hadoop fs -get /user/output/ /home/hadoop/ # Get results
