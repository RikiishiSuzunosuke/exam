email = input(' メールアドレスを入力してください : ')

def get_domain(mail):
	split_mail = mail.split('@')
	domain = split_mail[1]
	return domain

domain = get_domain(email)
print(f'メールアドレス({email})のドメイン：{domain}')