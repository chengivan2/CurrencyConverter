
import freecurrencyapi
client = freecurrencyapi.Client('YOUR-API-KEY')


base_currency='USD'
currencies=['EUR', 'CAD']
result_one = client.latest(base_currency, currencies)


result_two = client.currencies(currencies= ['EUR', 'CAD', base_currency])
print(result_two)


print(result_one)
print(result_one['data'])
print('1 {base_currency} = {amount} {name}'.format(base_currency=result_two['data'][base_currency]['name_plural'], amount=result_one['data'][currencies[0]], name=result_two['data'][currencies[0]]['name_plural'])) 
print('1 {base_currency} = {amount} {name}'.format(base_currency=result_two['data'][base_currency]['name_plural'], amount=result_one['data'][currencies[1]], name=result_two['data'][currencies[1]]['name_plural']))