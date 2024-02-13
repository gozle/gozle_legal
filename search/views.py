from django.shortcuts import render
from django_elasticsearch_dsl import search
from documents.models import Document  # Import the Document model from your main app

def search_view(request):
    query = request.GET.get('q', '')  # Get the search query from the request

    # Perform a search query using Django Elasticsearch DSL
    response = search.Search(using='default').query("match", header=query).execute()

    # Extract the hits from the response and build a list of data
    data_list = []
    for hit in response:
        data_list.append({
            'id': hit.meta.id,  # Document ID
            'header': hit.header,  # Document header
            # Add more fields as needed
        })

    # Render a template with the search results
    return render(request, 'search/search-results.html', {'query': query, 'data_list': data_list})
