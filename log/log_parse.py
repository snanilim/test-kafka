

def parseLog(filename):
    print('function call')
    print(filename)
    infile = filename

    parse_arr = []
    keep_phrases = "src-mac"

    with open(infile) as f:
        f = f.readlines()

    for line in f:
        # string = 'Jul 22 10:54:38 gateway firewall,info prerouting: in:ether6.8-STL-CLOUD out:(unknown 0), src-mac 6e:24:74:00:39:1d, proto TCP (ACK,FIN), 103.78.248.25:3306->198.20.103.242:37310, len 52'
        if keep_phrases in line:
            split_arr = line.split()

            month = split_arr[0]
            date = split_arr[1]
            time = split_arr[2]

            totalDate = month + ' ' + date + ' ' + time

            index_src_mac = split_arr.index('src-mac')
            if split_arr[index_src_mac] == 'src-mac':
                src_mac_add = split_arr[index_src_mac + 1]
                src_mac_add = src_mac_add.replace(',', '')

            index_proto = split_arr.index('proto')
            if split_arr[index_proto] == 'proto':
                src_dst_add = split_arr[index_proto + 3]
                src_dst_arr = src_dst_add.split('->')

                src_add = src_dst_arr[0]
                src_add_arr = src_add.split(':')
                src_add_ip = src_add_arr[0]
                src_add_port = src_add_arr[1]


                src_dst = src_dst_arr[1]
                src_dst_arr = src_dst.split(':')
                src_dst_ip = src_dst_arr[0]
                src_dst_port = src_add_arr[1]

            info = {'date':totalDate, 'src_mac':src_mac_add, 'src_ip':src_add_ip, 'src_port':src_add_port, 'dst_ip':src_dst_ip, 'dst_port':src_dst_port}
            
            parse_arr.append(info)
            print(totalDate, src_mac_add, src_add_ip, src_add_port, src_dst_ip, src_dst_port)
            # return True

        else:
            return False

    print(parse_arr)
    return parse_arr
            
