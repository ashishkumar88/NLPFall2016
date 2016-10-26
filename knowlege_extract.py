import re

file = open("output.txt","r")
parse_list = []
temp_list = []
for line in file:
    if line == "\n":
        parse_list.append(temp_list)
        temp_list = []
    else:
        line = line.replace("\n","")
        temp_list.append(line)
item = parse_list[2]
reg_one = re.compile('^nsubj.*')
reg_two = re.compile('^advcl.*')
reg_third = re.compile('^neg.*')
reg_fourth = re.compile('^(dobj|iobj|case).*')
res1 = filter(reg_one.match,item)
res2 = filter(reg_two.match,item)
res3 = filter(reg_third.match,item)
res4 = filter(reg_fourth.match,item)
#print res1, res2
nsubj_1 = res1[0].split(',')[0].split('(')[1].split('-')[0]
nsubj_2 = res1[0].split(',')[1].split('-')[0]
print "first nsubj : ",nsubj_1,",",nsubj_2
advcl_1 = res2[0].split(',')[0].split('(')[1].split('-')[0]
advcl_2 = res2[0].split(',')[1].split('-')[0]
print "advcl : ", advcl_1,",",advcl_2
nsubj_1_1 = res1[1].split(',')[0].split('(')[1].split('-')[0]
nsubj_1_2 = res1[1].split(',')[1].split('-')[0]
print "second nsubj : ",nsubj_1_1,",",nsubj_1_2
dobj_1 = res4[0].split(',')[0].split('(')[1].split('-')[0]
dobj_2 = res4[0].split(',')[1].split('-')[0]
print "dobj : ", dobj_1,",",dobj_2
if len(res3) != 0:
    neg_1 = res3[0].split(',')[0].split('(')[1].split('-')[0]
    neg_2 = res3[0].split(',')[1].split('-')[0]
    #print "neg : ",neg_1,",",neg_2
if len(res3) != 0:
    str = nsubj_2+"."+advcl_2+" = false may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
else:
    str = nsubj_2+"."+advcl_2+" = true may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
print str
###################
#item = parse_list[2]
#reg_one = re.compile('^nsubj.*')
#reg_two = re.compile('^advcl.*')
#reg_third = re.compile('^neg.*')
#reg_fourth = re.compile('^dobj.*')
#res1 = filter(reg_one.match,item)
#res2 = filter(reg_two.match,item)
#res3 = filter(reg_third.match,item)
#res4 = filter(reg_fourth.match,item)
#print res1, res2
#nsubj_1 = res1[0].split(',')[0].split('(')[1].split('-')[0]
#nsubj_2 = res1[0].split(',')[1].split('-')[0]
#print "first nsubj : ",nsubj_1,",",nsubj_2
#advcl_1 = res2[0].split(',')[0].split('(')[1].split('-')[0]
#advcl_2 = res2[0].split(',')[1].split('-')[0]
#print "advcl : ", advcl_1,",",advcl_2
#nsubj_1_1 = res1[1].split(',')[0].split('(')[1].split('-')[0]
#nsubj_1_2 = res1[1].split(',')[1].split('-')[0]
#print "second nsubj : ",nsubj_1_1,",",nsubj_1_2
#dobj_1 = res4[0].split(',')[0].split('(')[1].split('-')[0]
#dobj_2 = res4[0].split(',')[1].split('-')[0]
#print "dobj : ", dobj_1,",",dobj_2
#if len(res3) != 0:
#    neg_1 = res3[0].split(',')[0].split('(')[1].split('-')[0]
#    neg_2 = res3[0].split(',')[1].split('-')[0]
    #print "neg : ",neg_1,",",neg_2
#if len(res3) != 0:
#    str = nsubj_2+"."+advcl_1+" = false may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
#else:
#    str = nsubj_2+"."+advcl_1+" = true may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
#print str
