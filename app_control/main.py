from factories import ProviderFactory

posts = ProviderFactory.create_batch(10)

for post in posts:
    print(post)