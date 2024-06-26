# First Decision: Analista Python
## Teste 2

### ***Questão 1:*** Como você gerenciaria exceções em um script Python? 

<ins> Resposta: </ins> Para gerenciar exceções em um script em Python eu utilizaria a estrutura try - except.

### ***Questão 2:*** Explique a diferença entre uma função e um método em Python.

<ins> Resposta: </ins> Uma função podemos utilizar em qualquer local do código, já um método só podemos usar dentro de uma classe.

### ***Questão 3:*** Descreva um cenário em que você automatizaria uma tarefa em um ambiente Linux.

<ins> Reposta: </ins>  Eu automatizaria backups no meu ambiente Linux para garantir que meus dados estejam sempre protegidos. Faria cópias automáticas de diretórios importantes e enviaria de maneira segura para a nuvem.
Após cada backup, faria o script verificar automaticamente a integridade dos dados para evitar qualquer problema de corrupção. Além disso, colocaria para receber notificações por e-mail para ficar atualizada sobre o status dos backups. Isso me dá tranquilidade, sabendo que meus dados estão seguros, sem precisar ficar constantemente verificando manualmente.

### ***Questão 4:*** Como você lidaria com dados ausentes em um DataFrame do Pandas?

Reposta: Depende o caso. Podemos excluir linhas ou colunas com dados ausentes usando o comando DataFrame.dropna() ou preencher o dado ausente com algum valor, seja ele a média, mediana, interpolação, etc, usando o comando DataFrame.fillna(). Para excluir linhas ou colunas precisamos considerar a natureza dos dados e o impacto que uma exclusão vai ter na análise.  Porém, se uma coluna por exemplo tiver muitos valores ausentes, talvez excluí-la pode ser o melhor caminho. 

### ***Questão 5:*** Qual é a diferença entre uma API RESTful e uma API SOAP?

<ins> Resposta: </ins> Uma API RESTful é um estilo de arquitetura da Web que utiliza os verbos HTTP para realizar operações CRUD em recursos. Ela é stateless, ou seja, cada solicitação é independente. Já uma API SOAP é um protocolo de comunicação baseado em XML que utiliza mensagens SOAP para representar as operações e os dados. Ela é stateful, ou seja, cada solicitação depende das solicitações anteriores. Em resumo, a API RESTful é mais leve e fácil de implementar, enquanto a API SOAP é mais complexa e requer uma infraestrutura mais robusta.

### ***Questão 6:*** Como você autenticaria solicitações de API em Python?

<ins> Resposta: </ins> Existe mais de uma mandeira para autenticar API em Python, mas pela facilidade, usando uma API Key.
Esta chave é incluída no cabeçalho da solicitação para verificar a identidade do usuário e permitir o acesso aos dados da API.

### ***Questão 7:*** Descreva o que é um conflito de merge em Git e como você resolveria um. Como você reverteria um commit específico em Git?

<ins> Resposta: </ins> Um conflito de merge no Git ocorre quando o versionamento não consegue  conciliar automaticamente as diferenças entre dois commits durante um merge. Isso ocorre quando duas ramificações diferentes modificam o mesmo trecho de código. Quando isso acontece, o Git não consegue decidir qual alteração deve prevalecer e solicita que o usuário resolva o conflito manualmente.
Para reverter um commit espeífico podemos usar o git reset ou git revert. 
git revert cria um novo commit que desfaz as mudanças de um commit específico, preservando o histórico, enquanto git reset move o ponteiro HEAD para um commit anterior, podendo reescrever o histórico e descartar mudanças dependendo do modo usado (--soft, --mixed, --hard).

### ***Questão 8:*** Qual é a diferença entre um banco de dados SQL e um banco de dados NoSQL?

<ins> Resposta: </ins> Os bancos de dados SQL estruturam, armazenam e gerenciam os dados de modo diferente do NoSQL. Enquanto SQL é baseado em tabelas contendo em linhas e colunas, com estrutura fixa, NoSQL é baseado em documentos, gráficos, colunas ou pares chave-valor, com estrutura variável.

### ***Questão 9:*** Quais são algumas técnicas comuns de debugging em Python?

<ins> Resposta: </ins> O comando print pode ser usado como técnica de debbuging assim como usar breakpoints em IDEs nas linha de código onde desejamos que a execução do programa pare durante a depuração.

### ***Questão 10:*** Por que é importante documentar código? Quais são os elementos-chave que você incluiria em uma documentação de código?

<ins> Resposta: </ins> Por experiência própria, não documentar o código pode causar muitos problemas. Muitas vezes me deparei com código que eu mesmo havia escrito e precisei relê-lo ou até mesmo reescrevê-lo completamente para entender o que havia sido feito e por quê. Portanto, documentar o código é essencial para facilitar sua reutilização e compreensão, não apenas para outros desenvolvedores, mas também para mim no futuro. Elementos-chave que eu incluiria em uma documentação de código são uma descrição geral do propósito e funcionamento do código, requisitos e dependências necessárias, estrutura do código, e exemplos práticos de uso do código.

### ***Questão 11:*** Descreva como você usaria o Docker em um ambiente de desenvolvimento.

### ***Questão 12:*** Quais são as considerações ao desenvolver uma aplicação que precisa ser executada em várias plataformas?

### ***Questão 13:*** Como você escreveria um teste unitário em Python? Qual é o ciclo básico de desenvolvimento no TDD?

<ins> Resposta </ins> Usaria o unittest ou o pytest.
Exemplo: 

``` 
import unittest

def multiplica_por_dois(a):
    return 2 * a

class TestMultiplicaPorDois(unittest.TestCase):
    def test_multiplica_por_dois_positivo(self):
        self.assertEqual(multiplica_por_dois(2), 4)

    def test_multiplica_por_dois_negativo(self):
        self.assertEqual(multiplica_por_dois(-2), -4)

    def test_multiplica_por_dois_com_zero(self):
        self.assertEqual(multiplica_por_dois(0), 0)

if __name__ == '__main__':
    unittest.main()
```

Quanto ao TDD (Test-Driven-Development) segue o ciclo red, green e refactor. Red: escrevemos um pequeno teste automatizado que, ao ser executado, irá falhar; Green: um código que seja suficiente para ser aprovado no teste recém-escrito; Refactor: refatoramos o código, a fim dele ser melhorado, deixando-o mais funcional e mais limpo.


### ***Questão 14:*** Quais são as principais diferenças entre a configuração de servidores Linux e Windows?

<ins> Resposta: </ins> Existem várias diferenças entre os dois sistemas operacionais. Algumas delas são:
Linux é um código aberto e gratuito, enquanto que o Windows requerer licenciamento; 
Além disso, o Linux é considerado mais seguro por conta da sua arquitetura;
A interface gráfica também é diferente. windows tem uma interface padrão enquanto que o Linux possui mais de uma;
Compatibilidade com o hardware, o Windows é conhecido por ter suporte para a maioria dos dispositivos de hardware e o Linux nem tanto. 
Entre outras diferenças.


### ***Questão 15:*** Qual é a diferença entre o Django e o Flask? Em que tipo de projeto você escolheria usar o Django em vez do Flask, e vice-versa?

<ins> Resposta: </ins> Django é ideal para estruturas robustas, enquanto Flask é mais adequado para projetos enxutos e flexíveis.
Escolheria Django para projetos grandes e complexos que exigem muitas funcionalidades integradas, como autenticação, administração, e ORM. Já o Flask seria minha escolha para pequenas aplicações e microsserviços, como APIs, onde a simplicidade e a velocidade de desenvolvimento são prioridades.