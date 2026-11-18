from math import ceil
from model.entities import (Paciente, Profissional, Diario, Tecnica,
                            PacienteTecnica, Evento, Livro, FraseDiaria)


def _iso(valor):
    return valor.isoformat() if valor else None


def serializar(obj):
    if isinstance(obj, Diario):
        return {"idDiario": obj.idDiario, "idPaciente": obj.idPaciente, "texto": obj.texto,
                "data": _iso(obj.data), "enviado": obj.enviado, "resposta": obj.resposta,
                "idProfissionalResposta": obj.idProfissionalResposta,
                "dataResposta": _iso(obj.dataResposta),
                "paciente": obj.paciente.nome if obj.paciente else None,
                "profissional": obj.profissional.nome if obj.profissional else None}
    if isinstance(obj, Evento):
        return {"idEvento": obj.idEvento, "tema": obj.tema, "data": _iso(obj.data), "descricao": obj.descricao}
    if isinstance(obj, Tecnica):
        return {"idTecnica": obj.idTecnica, "tipo": obj.tipo, "descricao": obj.descricao}
    if isinstance(obj, PacienteTecnica):
        return {"idPacienteTecnica": obj.idPacienteTecnica, "idPaciente": obj.idPaciente,
                "idTecnica": obj.idTecnica, "dataUtilizacao": _iso(obj.dataUtilizacao),
                "tecnica": serializar(obj.tecnica) if obj.tecnica else None}
    if isinstance(obj, Livro):
        return {"idLivro": obj.idLivro, "titulo": obj.titulo, "mes": obj.mes, "ano": obj.ano, "autor": obj.autor}
    if isinstance(obj, FraseDiaria):
        return {"idFrase": obj.idFrase, "data": _iso(obj.data), "frase": obj.frase}
    if isinstance(obj, Paciente):
        return {"idPaciente": obj.idPaciente, "nome": obj.nome, "telefone": obj.telefone,
                "dataNasc": _iso(obj.dataNasc), "genero": obj.genero, "email": obj.email, "tipo": "paciente"}
    if isinstance(obj, Profissional):
        return {"idProfissional": obj.idProfissional, "nome": obj.nome, "telefone": obj.telefone,
                "dataNasc": _iso(obj.dataNasc), "genero": obj.genero, "documentoCip": obj.documentoCip,
                "email": obj.email, "tipo": "profissional"}
    return {}


def montar_pagina(resultado, pag, por_pagina):
    """Recebe (itens, total) do DAO e monta a resposta paginada com metadados."""
    itens, total = resultado
    return {"itens": [serializar(x) for x in itens],
            "paginacao": {"total": total, "pag": pag, "por_pagina": por_pagina,
                          "total_paginas": ceil(total / por_pagina) if total else 0}}
