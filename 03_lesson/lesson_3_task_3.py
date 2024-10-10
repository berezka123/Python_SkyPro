from address import Address
from mailing import Mailing

sender = Address("186930", "Костомукша", "ул. Ленина", 188, 8)
receiver = Address("265315", "Кострома", "ул. Троцкого", 26, 66)

package = Mailing(sender, receiver, 500, "18693012345678")

print(f"Отправление {package.track} из {package.from_address.postcode}, \
{package.from_address.city}, {package.from_address.street}, \
{package.from_address.house} - {package.from_address.flat} в \
{package.to_address.postcode}, {package.to_address.city}, \
{package.to_address.street}, {package.to_address.house} - \
{package.to_address.flat}.")
print(f"Стоимость {package.cost} рублей.")
