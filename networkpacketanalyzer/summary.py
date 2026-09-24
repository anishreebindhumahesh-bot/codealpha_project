from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw


# Counters
total_packets = 0
tcp_packets = 0
udp_packets = 0
icmp_packets = 0
other_packets = 0


def analyze_packet(packet):

    global total_packets
    global tcp_packets
    global udp_packets
    global icmp_packets
    global other_packets

    total_packets += 1

    print("\n" + "=" * 60)

    # IP information
    if IP in packet:
        print("Source IP       :", packet[IP].src)
        print("Destination IP  :", packet[IP].dst)

    elif IPv6 in packet:
        print("Source IPv6     :", packet[IPv6].src)
        print("Destination IPv6:", packet[IPv6].dst)

    else:
        print("Non-IP packet")
        other_packets += 1
        return

    # Protocol information
    if TCP in packet:

        tcp_packets += 1

        print("Protocol        : TCP")
        print("Source Port     :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

    elif UDP in packet:

        udp_packets += 1

        print("Protocol        : UDP")
        print("Source Port     :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    elif ICMP in packet:

        icmp_packets += 1

        print("Protocol        : ICMP")

    else:

        other_packets += 1

        print("Protocol        : Other")

    # Packet size
    print("Packet Size     :", len(packet), "bytes")

    # Payload
    if Raw in packet:

        payload = packet[Raw].load

        print("Payload Present : Yes")
        print("Payload Size    :", len(payload), "bytes")
        print("Payload Preview :", payload[:30])

    else:

        print("Payload Present : No")


# Start capture
print("=" * 60)
print("       NETWORK PACKET ANALYZER")
print("=" * 60)

print("Capturing 20 packets...")
print("Open a website to generate network traffic.")

sniff(
    count=20,
    prn=analyze_packet,
    store=False
)


# Summary
print("\n")
print("=" * 60)
print("             CAPTURE SUMMARY")
print("=" * 60)

print("Total Packets :", total_packets)
print("TCP Packets   :", tcp_packets)
print("UDP Packets   :", udp_packets)
print("ICMP Packets  :", icmp_packets)
print("Other Packets :", other_packets)

print("=" * 60)
print("Packet capture completed.")