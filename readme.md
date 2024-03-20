
# CONFRONT Scores

This repository was made to calculate the scores of the challenge 
[**CONFRONT**] (https://sites.unica.it/net4u/confront-challenge-on-wifi-frame-fingerprinting-for-people-counting-and-trackingconfront/) 
(Challenge ON wifi FRame fingerprinting for people cOunting aNd Tracking).

In the folder "/src/data/ground_truth" you can find the challenge files in .pcap format and the ground truth in .csv format.

In order to run the program you must:
1. install the requirements listed in the "/src/requirements.txt" file;
2. create the folder "/src/data/participants/" and inside a folder with your name or id;
3. copy the files of your experiment in "/src/data/participants/my_name/";
4. rename the files of your experiments as "capture_A.csv", "capture_B.csv", and "capture_C.csv";
5. run the main;
6. your results will be stored in the folder "/src/data/reports/".

Note: the format of your files should be:
- capture_A.csv: a csv file with two columns called id and labels; every row refers to a packet of the pcap file.
- capture_B.csv: a csv file with two columns called id and labels; every row refers to a packet of the pcap file.
- capture_C.csv: a csv file with two columns called devices and discarded; there is only one row with the number of devices counted by the algorithm and the number of discarded samples.

All csv files should use "," as column separator.