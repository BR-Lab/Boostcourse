import configparser

config =configparser.ConfigParser()
config.sections()

config.read('example.cfg')
print(config.sections())

print(config['SectionTwo'])
for key in config['SectionTwo']:
    value = config['SectionTwo'][key]
    print("{0} : {1}".format(key, value))

