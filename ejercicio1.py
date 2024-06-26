import json
from collections import defaultdict

def calcular_indice_h(citas):
    if not citas:
        return 0
    citas.sort(reverse=True)
    h_index = 0
    for i, cita in enumerate(citas):
        if cita >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

def calculate_h_index_from_json(n, articles):
    author_citations = defaultdict(list)
    
    for article_json in articles:
        article = json.loads(article_json)
        authors = article['authors']['authors']
        
        for author in authors:
            author_name = author['full_name']
            citations = article['citing_paper_count']
            author_citations[author_name].append(citations)
    
    author_h_index = {}
    
    for author, citations in author_citations.items():
        h_index = calcular_indice_h(citations)
        author_h_index[author] = h_index
    
    sorted_authors = sorted(author_h_index.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    for author, h_index in sorted_authors:
        result.append(f"{author} {h_index}")
    
    return result

def main():
    n = int(input())
    articles = []
    for i in range(n):
        line = input()
        articles.append(line)
    
    output = calculate_h_index_from_json(n, articles)
    for line in output:
        print(line)

if __name__ == "__main__":
    main()
