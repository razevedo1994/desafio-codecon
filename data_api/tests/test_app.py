from http import HTTPStatus


def test_post_users(client):
    response = client.post(
        "/users",
        json=[
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "nome": "string",
                "idade": 0,
                "score": 0,
                "ativo": True,
                "pais": "string",
                "equipe": {
                    "nome": "string",
                    "lider": True,
                    "projetos": [{"nome": "string", "concluido": True}],
                },
                "logs": [{"date": "2025-04-30", "action": "string"}],
            }
        ],
    )

    assert response.status_code == HTTPStatus.OK
