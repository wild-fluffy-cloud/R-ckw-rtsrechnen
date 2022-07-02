from rueckwaertsrechnung import listenpreis

def test_list_price_should_account_for_discount():
    assert 100 == listenpreis(gewinn=90, rabatt=10)
