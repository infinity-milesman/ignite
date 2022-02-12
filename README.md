To run app:-
####Create virtualenv
>install requirements.txt
####run server by 
> python3 wsgi.py



public url:- [URL](https://igniteappinfinity.herokuapp.com/)

Url: http://192.168.0.102:8089/book/book_api

####JSON params:-
```json
{
    "per_page": 100,
    "page": 3,
    "author_name":"abc",
    "title":"ds",
    "book_id_number":23,
    "mime_type":"text/plain",
    "language_code":"en",
    "topic":"wew"
}
```


#####RESPONSE:

```json{
    "data": [
        {
            "Author": "Jefferson, Thomas",
            "Bookshelf": "United States Law",
            "Subject": "United States -- History -- Revolution, 1775-1783 -- Sources",
            "code": "en",
            "title": "The Declaration of Independence of the United States of America",
            "url": "http://www.gutenberg.org/ebooks/1.rdf"
        }
    ],
    "next_page": 4,
    "page": 3,
    "per_page": 100,
    "prev_page": 2,
    "total_pages": 2989,
    "total_records": 298800
}
```