# Nombre_Premier 


Ce programme est une fonction Python appelée is_prime(n) qui prend un entier positif n en entrée et retourne True si n est un nombre premier, et False sinon.

La fonction commence par vérifier si n est égal à 1, car 1 n'est pas considéré comme un nombre premier. Si c'est le cas, la fonction retourne False.

Ensuite, la fonction utilise une boucle for pour parcourir tous les nombres de 2 à la racine carrée de n (inclus). Pour chaque nombre i, la fonction vérifie si n est divisible par i. Si c'est le cas, cela signifie que n n'est pas un nombre premier, et la fonction retourne False. Si aucun des nombres i n'est divisible par n, cela signifie que n est un nombre premier, et la fonction retourne True.

Notez que la fonction vérifie si n est égal à 1 deux fois: une fois au début pour éviter de traiter 1 comme un nombre premier, et une fois dans la boucle for pour s'assurer qu'aucun nombre autre que 1 ne peut diviser n. 

Cependant, la deuxième vérification est redondante car elle est déjà prise en compte dans la boucle for.
