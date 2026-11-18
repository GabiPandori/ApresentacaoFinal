from datetime import date
from sqlalchemy import select
from service.db_service import db
from model.entities import Tecnica, Evento, Livro, FraseDiaria


def inicializar_banco():
    """Cria as tabelas (se não existirem) e insere os dados iniciais uma única vez."""
    db.create_all()
    if not db.session.scalar(select(Tecnica.idTecnica).limit(1)):
        for tipo, descricao in [
            ("Respiração", "Exercícios de respiração consciente."),
            ("Aterramento", "Técnicas para direcionar a atenção ao momento presente."),
            ("Meditação", "Práticas de atenção plena."),
            ("Alongamentos", "Movimentos leves de alongamento."),
            ("Calistenia", "Movimentos com o peso do próprio corpo.")]:
            db.session.add(Tecnica(tipo=tipo, descricao=descricao))
    if not db.session.scalar(select(Evento.idEvento).limit(1)):
        for tema, data, descricao in [
            ("Imersão", "2026-07-16", "Uma experiência de autoconhecimento em grupo."),
            ("Filhos emocionalmente inteligentes", "2026-03-25", "Conversa sobre educação emocional."),
            ("Melhorando seu casamento", "2026-08-31", "Encontro sobre relações e diálogo."),
            ("Ressignificação de traumas", "2026-05-12", "Encontro sobre acolhimento e saúde emocional.")]:
            db.session.add(Evento(tema=tema, data=date.fromisoformat(data), descricao=descricao))
    if not db.session.scalar(select(Livro.idLivro).limit(1)):
        db.session.add(Livro(titulo="Tríade do poder", mes="Fevereiro", ano=2026, autor="Márcio Michelli"))
    if not db.session.scalar(select(FraseDiaria.idFrase).limit(1)):
        db.session.add(FraseDiaria(data=date.today(), frase="É importante agradecer pelo hoje e não desistir do amanhã."))
    db.session.commit()
