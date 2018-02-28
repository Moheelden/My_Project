import models
import store

post_store = store.PostStore()
post_store.add(models.Post("Life", "Life is alawys great"))
post_store.add(models.Post("Sunshine", "Sunshine is amazing"))
post_store.add(models.Post("Medicine", "Medicine is great"))
post_store.add(models.Post("Architecture", "Spectacular art"))
post_store.add(models.Post("Astronomy", "Space is awesome"))
post_store.add(models.Post("Geology", "Earth is our friend"))

post_store.add(models.Post("..............", "............."))
