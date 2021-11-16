#!/bin/bash

echo "Create Collections to GeneralDB...\n"
mongo generaldb --eval 'db.createCollection(actors);'
mongo generaldb --eval 'db.createCollection(actresses);'
mongo generaldb --eval 'db.createCollection(shows);'
mongo generaldb --eval 'db.createCollection(voice_actors);'
mongo generaldb --eval 'db.createCollection(voice_actresses);'
echo

echo "Create Collections to ChavesDB...\n"
mongo chavesdb --eval 'db.createCollection(characters);'
mongo chavesdb --eval 'db.createCollection(episodes);'
mongo chavesdb --eval 'db.createCollection(quotes);'
echo

echo "Create Collections to ChapolinDB...\n"
mongo chapolindb --eval 'db.createCollection(characters);'
mongo chapolindb --eval 'db.createCollection(episodes);'
mongo chapolindb --eval 'db.createCollection(quotes);'
echo

echo "Create Collections to ChespiritoDB..."
mongo chespiritodb --eval 'db.createCollection(characters);'
mongo chespiritodb --eval 'db.createCollection(episodes);'
mongo chespiritodb --eval 'db.createCollection(quotes);'
mongo chespiritodb --eval 'db.createCollection(sketches);'
echo

echo "Insert a actor...\n"
mongo generaldb --eval 'db.actors.insertOne({"_id": 1,"nome":"Roberto Mario Gómez y Bolaños","nome_artistico":"Chespirito","data_nascimento":"21/02/1929","data_falecimento":"28/11/2014","programas":["Chaves","Chapolin","Chespirito"],"personagens":["Chaves","Chapolin Colorado","Doutor Chapatin","Chaveco","Chaplin","Dom Caveira","Pancada Bonaparte","Vicente Chambón"]})'
echo

echo "Insert a actress...\n"
mongo generaldb --eval 'db.actresses.insertOne({"_id": 1,"nome":"María Antonieta Gómez Rodriguéz","nome_artistico":"Maria Antonieta de las Nieves","data_nascimento":"22/12/1949","data_falecimento":null,"programas":["Chaves","Chapolin","Chespirito"],"personagens":["Bruxa Baratuxa","Chiquinha","Dona Neves","Marujinha"]})'
echo

echo "Insert a chaves episode...\n"
mongo chavesdb --eval 'db.episodes.insertOne({"_id": 1,"ano_exibicao": 1973,"titulo":"Boas festas / Balões","situacao_mexico":"Comum","estreia_mexico":"26/02/1973","quadros":[{"id_quadro":"a","nome_quadro":"Os ladrões","titulo_pt":"Boas festas","titulo_es":"Rateros torpes","situacao_brasil":"Comum","dublagem":["Maga"],"dubladores":["Marcelo Gastaldi","Carlos Seidl","Nelson Machado"],"sinopse":"Peterete se dá conta que a janela de uma casa está aberta e chama Beterraba para ajudá-lo a entrar nela.","direcao":"Roberto Gómez Bolaños","elenco":["Roberto Gómez Bolaños","Ramón Valdés","Carlos Villagrán"],"exibido_por":["SBT","Multishon","Amazon Prime","TLN","Netflix","Cartoon Network","Boomerang","TBS","Televisa"]},{"id_quadro":"b","nome_quadro":"Chaves","titulo_pt":"Balões","titulo_es":"Los globos","situacao_brasil":"Comum","dublagem":["Maga"],"dubladores":["Marcelo Gastaldi","Carlos Seidl","Nelson Machado","Sandra Mara Azevedo","Mário Vilela","Marta Volpiani"],"sinopse":"Quico e Chiquinha disputam para ver quem tem o balão maior, enquanto Chaves tenta estourá-los.","direcao":"Roberto Gómez Bolaños","elenco":["Roberto Gómez Bolaños","Ramón Valdés","Carlos Villagrán","Maria Antonieta de las Nieves","Edgar Vivar","Florinda Meza"],"exibido_por":["SBT","Multishon","Amazon Prime","TLN","Netflix","Cartoon Network","Boomerang","TBS","Televisa"]}]})'
echo

exit 0