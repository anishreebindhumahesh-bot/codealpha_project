from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw


def analyze_packet(packet):

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
        return

    # Protocol and ports
    if TCP in packet:
        print("Protocol        : TCP")
        print("Source Port     :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

    elif UDP in packet:
        print("Protocol        : UDP")
        print("Source Port     :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    elif ICMP in packet:
        print("Protocol        : ICMP")

    else:
        print("Protocol        : Other")

    # Packet size
    print("Packet Size     :", len(packet), "bytes")

    # Payload analysis
    if Raw in packet:

        payload = packet[Raw].load

        print("Payload Present : Yes")
        print("Payload Size    :", len(payload), "bytes")

        # Display first 50 bytes
        print("Payload Preview :", payload[:50])

    else:

        print("Payload Present : No")


print("=" * 60)
print("       NETWORK PACKET ANALYZER")
print("=" * 60)

print("Capturing 10 packets...")
print("Open a website to generate traffic.")

sniff(
    count=10,
    prn=analyze_packet,
    store=False
)

print("\nPacket capture completed.")