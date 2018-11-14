Two packages are used in this program: xlrd and argparse.
There are two arguments required to run this program, which are -gem and -diag. -gem is the path of I10gem, -diag is the path of ICD9 diagnosis file.
You can run this file with command like this in your command line:

python Resolving.py -gem ./2018_I10gem.txt -diag ./2015-pdd-diagnosis-code-frequencies20160715.xlsx


Note: I left the code that responsible for converting ICD9 diagnosis file into plain text file as comments at the top of the program, since I think it is unnecessary to create such file.