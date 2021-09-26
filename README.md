# Drama Queens' fake thesis subject creator

L'équipe Drama Queens a été constituée pour le Hackathon de l'ADEMEC 2021 a choisi de travailler sur un tableau CSV contenant les métadonnées de thèses soutenues à l'École des chartes. À partir de ces données, nous créons un quizz présentant à l'utilisateurice un titre de thèse et lui demandant s'il est un véritable sujet ou bien un sujet inventé.

Pour produire les sujets inventé, nous avons utilisé deux méthodes :
- une méthode dite "machine learning", utilisant [GPT-fr](https://github.com/AntoineSimoulin/gpt-fr), 
- une méthode dite "mashup" utilisant des expressions régulières et des scripts Python, consistant à extraire des expressions d'époques historiques, créer des banques de données thématiques et générer des noms selon des structures syntaxiques définies.

Nous avons conservé les deux méthodes de création dans deux buts :
- pouvoir évaluer, en fonction des réponses des utilisateurices, quelle méthode est la plus efficace pour tromper le public,
- pouvoir présenter, en plus de faux titres crédibles, des faux titres absurdes, à des fins humoristiques.
