$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \ 
-file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py \
-input /user/input/input/* -output /user/output1
