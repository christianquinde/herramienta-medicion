#!/bin/bash
piso=$1
tx=$2
ip_src=$3
ip_dst=$4
tx_rx=$5


sudo killall trafico.sh
echo "Conviertiendo a .csv ......."
sleep 4

./csv_convert.sh $ip_dst $tx_rx $ip_src

mv trafico_total.pcap pcaps_total/piso${piso}_tx${tx}.pcap # pcap de todo lo capturado

cd fraction_loss
mv trafico_tx.txt piso${piso}_tx${tx}.txt #cambio nombre fl

cd ../fraction_loss_audio
mv trafico_tx.txt piso${piso}_tx${tx}.txt #cambio nombre fl

cd ..
mv th.pcap throughput/total_piso${piso}_tx${tx}.pcap #cambio de nombre pcap de throu
mv th_audio.pcap throughput_audio/total_piso${piso}_tx${tx}.pcap #cambio de nombre pcap de throu de audio

mv delay/trafico_tx.txt delay/piso${piso}_tx${tx}.txt 
mv delay_audio/trafico_tx.txt delay_audio/piso${piso}_tx${tx}.txt 

echo "Conversion Finalizada ......."

echo "--------------------------------FIN DE LA CONVERSION-----------------------------------"