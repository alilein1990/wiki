from django.shortcuts import render
from markdown2 import Markdown


from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    md_convert = convert_md_to_html(title)
    if md_convert == None:
        return render(request, "encyclopedia/error.html", {
            "message":"requested page was not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": md_convert
        })

#def entry(request, entry):
    #markdowner = Markdown()
   # entryPage = util.get_entry(entry)
    #if entryPage is None:
       # return render(request, "encyclopedia/error.html", {
            #"message": "This entry does not exists"
        #})
    #else:
        #return render(request, "encyclopedia/entry.html", {
            #"title": entry,
            #"content": markdowner.convert(entryPage)     
         #})

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })


