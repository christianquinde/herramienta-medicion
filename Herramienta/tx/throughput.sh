#!/bin/bash
intervalo=0.1
piso=$1
tx=$2
tcpstat -r throughput/total_piso${piso}_tx${tx}.pcap $intervalo > throughput/thro_piso${piso}_tx${tx}.csv
tcpstat -r throughput_audio/total_piso${piso}_tx${tx}.pcap $intervalo > throughput_audio/thro_piso${piso}_tx${tx}.csv

