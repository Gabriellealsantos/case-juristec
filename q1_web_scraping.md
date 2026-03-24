## Resolução - Questão 1: Web Scraping

### Problema 1: Tabela não aparece no HTML e demora 2 segundos para carregar
* **Causa:** O site utiliza renderização do lado do cliente (Client-Side Rendering) com JavaScript. O `requests` do Python baixa apenas o HTML estático inicial, que não contém a tabela.
* **Investigação:** Eu abriria o navegador, pressionaria `F12` (Developer Tools) e iria na aba **Network (Rede)**. Filtraria por requisições `Fetch/XHR` para ver se, durante os 2 segundos de atraso, o site faz uma requisição para uma API oculta que retorna os dados da tabela em formato JSON.
* **Solução Estratégica:** 1.  **Ideal:** Se a API oculta existir, eu alteraria o script para fazer o `requests.get()` direto para o endpoint dessa API, consumindo o JSON limpo.
    2.  **Alternativa:** Se não houver API clara (ou for criptografada), eu substituiria a biblioteca `requests` por ferramentas de automação de navegador como **Playwright** ou **Selenium**. Elas abrem um navegador real, aguardam o JavaScript executar e renderizar a tabela, e então extraem o HTML final.

### Problema 2: Bloqueio de requisições e Erro HTTP 403 (Forbidden)
* **Causa:** O servidor web ou firewall (como Cloudflare) identificou o script como um "bot" devido a requisições muito rápidas ou pela ausência de cabeçalhos (Headers) de navegador válidos.
* **Investigação:** Verificaria no script original se os `headers` da requisição estão vazios e se existe algum intervalo de tempo entre as chamadas.
* **Solução Estratégica:**
    1.  **Headers:** Adicionar um `User-Agent` realista no cabeçalho do `requests` para simular que o acesso vem de um navegador comum (ex: Chrome no Windows).
    2.  **Throttling:** Implementar a biblioteca `time` e usar `time.sleep()` para adicionar pausas aleatórias (ex: 2 a 5 segundos) entre as requisições, simulando o comportamento de leitura de um ser humano.
    3.  **Rotação:** Caso o bloqueio persista (bloqueio por IP), utilizaria um serviço de rotação de Proxies para distribuir as requisições.
