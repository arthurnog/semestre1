#Arthur Lucas da Silva Nogueira
#213293
#  Funcao: removePalavras
#
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
#
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
	s1 = s.split()
	for i in range(len(vs)):
		if vs[i] in s1:
			while s1.count(vs[i]) != 0:
				a = s1.index(vs[i])
				del s1[a]
	s = " ".join(s1)
	return s

#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(palavrasPagina, termosBusca):
	resp = []
	count = 0
	numPag = len(palavrasPagina)
	for i in range(numPag):
		lis = palavrasPagina[i].split()
		for j in range(len(termosBusca)):
			flag = 0
			if termosBusca[j] in lis and flag == 0:
				count += 1
				flag = 1
		if count == len(termosBusca):
			resp.append(1)
		else:
			resp.append(0)
		count = 0
	return resp


#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
	lis = [0 for i in range(len(links))]
	for i in range(len(resp)):
		if resp[i] == 1:
			for j in range(len(links)):
				if links[j][i] == 1 and resp[j] != 0:
					lis[i] += 1
		elif resp[i] == 0:
			lis[i] -= 1
	return lis
