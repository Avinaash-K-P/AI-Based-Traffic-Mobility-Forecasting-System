from sqlalchemy.orm import Query

def paginate(
    query: Query,
    page: int = 1,
    page_size: int = 20
):
    
    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 20

    total_records = query.count()
    total_pages = ((total_records + page_size - 1)// page_size )    

    records = (
        query
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return {
        "page": page,
        "page_size": page_size,
        "total_records": total_records,
        "total_pages": total_pages,
        "items": records
    }