from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'enbparblob'
    account_key = 'nuV9KDe+97fPEo6nE12KyIY76tRLvRsjc5fUKxciPp1Ad7w1F/OU4JcTGp5uS6Yix2PfCnBkKnb7+AStcTHaWg=='
    azure_container = 'media'
    expiration_secs = None
    

class AzureStaticStorage(AzureStorage):
    account_name = 'enbparblob'
    account_key = 'nuV9KDe+97fPEo6nE12KyIY76tRLvRsjc5fUKxciPp1Ad7w1F/OU4JcTGp5uS6Yix2PfCnBkKnb7+AStcTHaWg=='
    azure_container = 'static'
    expiration_secs = None
