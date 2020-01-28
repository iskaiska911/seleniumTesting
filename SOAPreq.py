from zeep import Client,Settings
settings = Settings(strict=False, xml_huge_tree=True,raw_response=True)
client = Client('http://users.bugred.ru/tasks/soap/WrapperSoapServer.php?wsdl',settings=settings)
result=client.service.doRegister('pythonsaoptest11@gmail.com','iska19922991gggg','12334')
assert result.status_code==200





