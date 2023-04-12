'''
    Settings
'''

from pydantic import BaseSettings


#export MAIN_URL - всегда с большой буквы
class Settings(BaseSettings):
    ''' Settings class '''
    main_url: str = '/status'


settings = Settings()
