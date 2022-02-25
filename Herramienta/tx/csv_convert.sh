#!/bin/bash
ip_dst=$1
tx_rx=$2
ip_src=$3

valor="TX"

if [[ $tx_rx = $valor ]]; then
 echo "TX"
 #thr
 tshark -w th.pcap -r trafico_total.pcap ip.src==$ip_dst and udp.port==6000

 tshark -w th_audio.pcap -r trafico_total.pcap ip.src==$ip_dst and udp.port==6002


 #delay
 tshark -V -r trafico_total.pcap udp.port==5005 or udp.port==5001 > delay/trafico_tx.txt

 tshark -V -r trafico_total.pcap udp.port==5007 or udp.port==5003 > delay_audio/trafico_tx.txt 
 
 #pl
 tshark -V -r trafico_total.pcap udp.port==6005 and  rtcp.ssrc.fraction > fraction_loss/trafico_tx.txt

 tshark -V -r trafico_total.pcap udp.port==6007 and  rtcp.ssrc.fraction > fraction_loss_audio/trafico_tx.txt


else 

 #thr
 tshark -w th.pcap -r trafico_total.pcap ip.src==$ip_dst and udp.port==5000

 tshark -w th_audio.pcap -r trafico_total.pcap ip.src==$ip_dst and udp.port==5002


 #delay
 tshark -V -r trafico_total.pcap udp.port==6005 or udp.port==6001 > delay/trafico_tx.txt

 tshark -V -r trafico_total.pcap udp.port==6007 or udp.port==6003 > delay_audio/trafico_tx.txt 

 #pl
 tshark -V -r trafico_total.pcap udp.port==5005 and  rtcp.ssrc.fraction > fraction_loss/trafico_tx.txt

 tshark -V -r trafico_total.pcap udp.port==5007 and  rtcp.ssrc.fraction > fraction_loss_audio/trafico_tx.txt
fi


#el que llama usa los puertos 6000 para el throughput y 5000 para el delay
#el llamado al revez
