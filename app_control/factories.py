import factory
import factory.fuzzy

from models import (Provider)

class ProviderFactory(factory.Factory):

    class Meta:
        model = Provider

    name = factory.Faker("company", locale="es_MX")
    legal_name = factory.fuzzy.FuzzzyChoice(choices=[name+" S.A.S", name+" S.A", name+"LTDA"])
    nit = factory.Faker("pyint", min_value=0, max_value=999999999)
    email = factory.Faker("email")
    bank_account = factory.Faker("credit_card_number")

    

