# Test
echo "$(cat 'FILE_INPUT.txt')" | python mapper.py | sort -k1,1 | python reducer.py

# Start ssh Server
systemctl start sshd

# Start Hadoop
hadoop namenode -format
start-dfs.sh

# Hadoop Prep
$HADOOP_HOME/bin/hadoop dfs -ls /user/input
$HADOOP_HOME/bin/hadoop dfs -mkdir /user/input/sertanejo
$HADOOP_HOME/bin/hadoop dfs -copyFromLocal /home/letras/sertanejo/* /user/input/sertanejo
$HADOOP_HOME/bin/hadoop dfs -ls /user/input
...
$HADOOP_HOME/bin/hadoop dfs -mkdir /user/results

# MapReduce Execution
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \ 
-file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py \
-input /user/input/sertanejo/* -output /user/results

# Getting Results
$HADOOP_HOME/bin/hadoop dfs -ls /user/results #Show result files
$HADOOP_HOME/bin/hadoop dfs -cat /user/results/OUTFILE  # Visualize results
$HADOOP_HOME/bin/hadoop dfs -get /user/results/ /home/hadoop/ # Get results
