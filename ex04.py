id = input( ' IDを入力してください : ' )
pwd = input( ' パスワードを入力してください : ' )
trueID = 'rikiishi'
truePwd = 'kv9934'

def check(id, pwd):
	if id == trueID and pwd == truePwd :
		flg=0
	else:
		flg=1
	return flg

flg = check(id, pwd)
if flg==0 :
	print('OKです')
else:
	print('IDかパスワードが違います')