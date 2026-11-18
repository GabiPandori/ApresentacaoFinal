from sqlalchemy import select, func
from service.db_service import db


def paginar(query, pag, por_pagina):
    """Executa LIMIT/OFFSET e devolve (itens, total de registros)."""
    total = db.session.scalar(select(func.count()).select_from(query.order_by(None).subquery())) or 0
    itens = db.session.execute(query.limit(por_pagina).offset((pag - 1) * por_pagina)).scalars().all()
    return itens, total
