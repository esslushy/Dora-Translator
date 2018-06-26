EngtoSpa = {"city" : "ciudad", "map" : "mapa", "cake" : "pastel", 
            "mountain":"montana", "banana" : "plátano", "hair":"pelo", 
            "cow":"vaca", "pig":"puerco", "chicken":"pollo", 
            "insect":"insecto", "spider":"araña", "apple":"manzana", "lion":"león", "elephant":"elefante"}
text = "the city on the map was made of cake and was next to a banana mountain. The mayor is said to have beautiful hair that rivals anything. In a nearby farm with a cow pig and chicken there was an insect who had a spider friend, but was trapped in another spiders web. The cow saved the insect and was loved by the chicken who gave him an apple. Then a lion came and ate the apple, but was then squashed by an elephant.  Then the city through a party for the elefant and the cow."
text = text.lower()
for eng in EngtoSpa:
    word = ()
    text = text.replace(eng, EngtoSpa[eng] + "(" + eng + ")")
    
print(text)