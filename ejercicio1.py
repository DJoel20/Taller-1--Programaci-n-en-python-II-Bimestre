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
        authors = article['authors']['authors']  # Acceder a la lista de autores
        
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

n = 10
articles = [
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 1","article_number": "1","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}]},"title": "Article Title 2","article_number": "2","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Delta"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}, {"author_order": 4,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 3","article_number": "3","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 4","article_number": "4","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 5","article_number": "5","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 5,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 6","article_number": "6","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}]},"title": "Article Title 7","article_number": "7","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 8","article_number": "8","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}, {"author_order": 2,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 9","article_number": "9","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}',
    '{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Bravo"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 10","article_number": "10","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}'
]

output = calculate_h_index_from_json(n, articles)
for line in output:
    print(line)