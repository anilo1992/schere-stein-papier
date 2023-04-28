# schere-stein-papier

Ein "Schere, Stein, Papier"-Terminal-Spiel entwickelt von Anil Coban. 

Ziel dieses oft programmierte Spiel ist die Veranschaulichung meiner Herangehensweise. Nicht der beste Ansatz, den Sie sehen werden, bin dennoch stolz, dass ich es in weniger als 15 Zeilen geschafft habe. 

Schere, Stein, Papier ist ein weltverbreitetes Spiel. Zwei Spieler wählen jeweils eines der folgenden Zeichen: Schere, Stein oder Papier und zeigen dies per Hand auf Kommando gleichzeitig. Folgende Gewinnmuster gibt es bei dem Spiel, bei denen Erstere gewinnt: Schere schneidet Papier, Papier ummantelt Stein und Stein zerstört die Schere. Haben beide Spieler das selbe Zeichen, so wird das Spiel als unentschieden gewertet.

Ich habe die Sublisten so angeordnet, dass das erste Element jeder Subliste dem nächsten Element in der selben Subliste überlegen ist. Umgekehrt ist das Element dem vorherigen Element unterlegen:

```gewinn_muster = [['Schere', 'Papier'], ['Papier', 'Stein'], ['Stein', 'Schere']]```

Habe ich in dem Fall ein Element ausgewählt, das im nullten (ich hoffe, das Wort existiert) Index ist, gewinne ich. Andernfalls verliere ich, wenn der Computer das erste Element ausgewählt hat.
