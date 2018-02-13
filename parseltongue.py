from scapy.all import *
import binascii
import sys

# Soz about the magic file paths, will update in a future version
# Grab a pcap file and give me a readable output for qiMessaging network
# protocol plz

# script name fin fout
argz = len(sys.argv)
if argz == 3:
    fin = sys.argv[1] + ".pcap"
    fout = sys.argv[2] + ".txt"
elif argz == 2:
     fin = sys.argv[1] + ".pcap"
     fout = sys.argv[1] + "_out.txt"
else:
    print "Syntax: python parseltongue <file in> <file out>"
    sys.exit()

print "Loading packets from C:/Users/meg/Documents/Uni/VRES/pcaps/" + fin + " ..."
fin = "C:/Users/meg/Documents/Uni/VRES/pcaps/" + fin
# packets = rdpcap('C:/Users/meg/Documents/Uni/VRES/pcaps/video_start_stop.pcap')
packets = rdpcap(fin)
counter = 0

# f = open("decode.txt", "a")

fout = "C:/Users/meg/Documents/Uni/VRES/pcaps/parsed_out/" + fout
print "Output will be saved as: " + fout
f = open(fout, "a")
#f = open("raw.txt", "a")

print "Ready to begin..."
#iterate through every packet
for packet in packets:
    ip_from = packet.getlayer(IP).src
    ip_to = packet.getlayer(IP).dst
    port_from = packet.getlayer(TCP).sport
    port_to = packet.getlayer(TCP).dport
    data = packet.payload.payload.payload
    
    # data = packet.getlayer(Raw)
    counter = counter + 1
   # pkt = packet[Raw]
    #data = pkt[Raw].load
    #f2.write("Packet" + counter + ": \n" +data + "\n\n")
    decode = binascii.hexlify(str(data))
    #decode = str(data)
    #f.write(decode + "\n")
    #f = open("testdata.txt","a")
    f.write("Packet " + str(counter) + "\n")
    f.write("FROM: %s : %s\n" % (str(ip_from), str(port_from)))
    f.write("TO: %s : %s\n" % (str(ip_to), str(port_to)))
    magic = decode[0:8]
    f.write("MAGIC: " + magic + " | " + magic.decode("hex") + "\n")
    id_text = decode[8:16]
    f.write("ID: " + id_text + " | " + id_text.decode("hex") + "\n")
    size_text = decode[16:24]
    f.write("SIZE: " + size_text + " | " + size_text.decode("hex") + "\n")
    version_text = decode[24:28]
    f.write("VERSION: " + version_text + " | " + version_text.decode("hex")  + "\n")
    type_text = decode[28:32]
    f.write("TYPE: " + type_text + " | " + type_text.decode("hex")  + "\n")
    service_text = decode[32:40]
    f.write("SERVICE ID: " + service_text + " | " + service_text.decode("hex")  + "\n")
    object_text = decode[40:48]
    f.write("OBJECT ID: " + type_text + " | " + type_text.decode("hex")  + "\n")
    function_text = decode[48:56]
    f.write("FUNCTION ID: " + function_text + " | " + function_text.decode("hex")  + "\n")
    payz = decode[56:]
    f.write("PAYLOAD BABY: " + payz + "\n\n")
    f.write("ASCII PAYLOAD: " + payz.decode("hex") + "\n")

    f.write("\n\n\n")
    
    #f2.close()

    string = "." * (counter % 3)
    print string

f.close()
print "Doneski!"
