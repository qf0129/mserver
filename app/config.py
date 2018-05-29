
class DevConfig():
    TEXT = 'DEV'

class ProdConfig():
    TEXT = 'PROD'

configs = {
    'dev': DevConfig,
    'prod': ProdConfig
}