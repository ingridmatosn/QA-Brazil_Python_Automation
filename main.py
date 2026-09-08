import data
import helpers


class TestUrbanRoutes:

    # Executado uma vez antes de todos os testes: verifica se o servidor Urban Routes está no ar
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para selecionar a tarifa")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para adicionar o cartão de crédito")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para escrever a mensagem para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para pedir cobertor e lenços de papel")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        print("função criada para pedir 2 sorvetes")
        for i in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para verificar se o modal de busca do carro aparece")
        pass
