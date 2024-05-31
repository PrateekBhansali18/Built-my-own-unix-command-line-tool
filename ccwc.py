import sys
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-l',"--line",action='store_true', help="display the number of lines in a file")
parser.add_argument('-w',"--word",action='store_true', help="display the number of words in a file")
parser.add_argument('-m',"--character",action='store_true', help="display the number of characters in a file")
parser.add_argument('-c',"--byte",action='store_true', help="display the number of bytes in a file")
parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()
#print(args)

ln = -1
wc=-1
mc=-1
cc=-1
if(args.line):
        ln=0
if(args.word):
        wc=0
if(args.character):
        mc=0
if(args.byte):
        cc=0

def count_file(ln, wc, mc, cc, fileName):
        try:
                # print(type(fileName))
                file = open(fileName, 'r')
                # print(file)
        except:
                print('No such File or Directory:::::')
                return [-1]

        cnt_l=0
        cnt_w=0
        cnt_c=0
        line=file.readline()
        while line:
                cnt_l = cnt_l + 1
                cnt_c = cnt_c + len(line)

                if(line!='\n'):
                        y=line.split()
                        cnt_w = cnt_w + len(y)
                line=file.readline()
        cnt_c = cnt_c + cnt_l
        stats = os.stat(fileName)
        cnt_b = stats.st_size
        ans = []
        if(ln!=-1):
                ans.append(cnt_l)
        if(wc!=-1):
                ans.append(cnt_w)
        if(mc!=-1):
                ans.append(cnt_c)
        if(cc!=-1):
                ans.append(cnt_b)
        if((ln==-1) & (wc==-1) & (mc==-1) & (cc==-1)):
                ans.append(cnt_l)
                ans.append(cnt_w)
                ans.append(cnt_b)
        file.close()        
        return ans
def count_stdin(ln, wc, mc, cc, stdin):
    cnt_l=0
    cnt_w=0
    cnt_c=0
    cnt_b=0
    line=stdin.readline()
    while line:
            cnt_l = cnt_l + 1
            cnt_c = cnt_c + len(line)
            cnt_b = cnt_b + len(line.encode('utf-8'))
            if(line!='\n'):
                    y=line.split()
                    cnt_w = cnt_w + len(y)
            line=stdin.readline()
    # cnt_c = cnt_c + cnt_l
    
    
    ans = []
    if(ln!=-1):
            ans.append(cnt_l)
    if(wc!=-1):
            ans.append(cnt_w)
    if(mc!=-1):
            ans.append(cnt_c)
    if(cc!=-1):
            ans.append(cnt_b)
    if((ln==-1) & (wc==-1) & (mc==-1) & (cc==-1)):
            ans.append(cnt_l)
            ans.append(cnt_w)
            ans.append(cnt_b)
    # file.close()
    return ans
# print(args.filename.name)
# print(type(args.filename.name))


if(args.filename.name=='<stdin>'):
        ans = count_stdin(ln, wc, mc, cc,args.filename)
        print(str(ans)[1:-1])
else:
        ans = count_file(ln, wc, mc, cc, args.filename.name)
        ans.append(args.filename.name)
        print(str(ans)[1:-1])
# print('##################')