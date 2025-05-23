from app import app

def test_cast_spell():
    client = app.test_client()
    response = client.get('/spell?name=fireball')
    data = response.get_json()

    assert response.status_code == 200
    assert data['spell'] == 'fireball'
    assert 'Fireball spell has been cast!' in data['effect']
