## Algoritmes

Om de meest stabiele proteine opvouwing te vinden hebben wij verschillende algoritmes geschreven die op verschillende wijze de proteinen opvouwen.

### Baseline
Het baseline algoritme is een random algoritme, dat willekeurig elk van de aminos in het proteine een richting toewijst. Vervolgens worden die richtingen gebruikt om elk aminozuur coordinaten te geven. Doordat het voor kan komen dat meerdere aminozuren op dezelfde coordinaten liggen, levert dit algoritme ook invalide opties.

### Random plus
Random plus is een verbetering op het baseline algoritme. Aminozuren kunnen niet meer de de coordinaten krijgen waar het vorige aminozuur ligt. Ook levert dit algoritme alleen maar valide proteinen, als een proteine invalide is wordt het algoritme opnieuw gerunt, totdat er een valide proteine wordt gegeven.

### Greedy
Het greedy alogritme is een nog verdere uitbreiding op het random algoritme. Het eerste amino krijgt een willekeurige richting, maar alle volgende aminos krijgen de richting mee waarbij de score het meest verlaagt wordt. Als er meerdere opties met dezelfde score zijn wordt een ervan willekeurig gekozen. Ook zijn er een extra functies toegevoegd, die voorkomen dat een proteine in een spiraal terecht kan komen. Als dit gebeurt, loopt een algoritme vast omdat er aminozuren zijn die geen enkele plek hebben waar ze geldig kunnen liggen.

### Depth First
Het depth first algoritme is een constructief algoritme, dat systematisch door de mogelijke opvouwingen van een proteine gaat. Het begint door het eerste aminozuur van de proteine te selecteren dat nog geen coördinaten heeft en alle mogelijke opties vanaf dit punt toe te voegen aan een stack. Het algoritme gaat vervolgens door totdat alle aminozuren coördinaten hebben en er een valide vouwing is ontstaan. Dan wordt de score gecheckt en vergeleken met andere behaalde scores. Als er geen valide vouwingen meer zijn om te verkennen vanuit het huidige aminozuur, wordt er teruggaan naar het vorige beslissingspunt op de stack. Uiteindelijk wordt de gevonden vouwing met de laagst behaalde score teruggeven.

### Breadth first
Het breadth first algoritme is net als het depth first een constructief algoritme dat systematisch door de mogelijke opvouwingen van een proteine gaat. Het gedraagt zich vergelijkbaar met een depth first algoritme, maar met een belangrijk verschil: het maakt gebruik van een queue in plaats van een stack. Dat betekend dat eerste alle opties voor the eerste aminozuur in de queue worden geplaatst, vervolgens die van de tweede enzovoort. Het grootte verschil is dat een breadth first algoritme gebruikt maakt van een queue, waardoor alle mogelijke opties eerst worden opgeslagen, en er geen sprake is van teruggaan.

### Hill climb
Hill climb is een iteratief algoritme. Dit betekent dat het begint met een start opvouwing en probeert deze vervolgens te verbeteren. Dit wordt gedaan aan de hand van twee mutaties rotate en pull moves. \
<img src="/docs/pull_moves.png" height="200px">
<img src="/docs/rotate_moves.png" height="200px"> \
*De verschillende mutaties: pull moves (links) en rotate moves (rechts)*

### Simulated annealing
Simulated annealing is een voortbouwing op hill climb, waarbij ook eventuele verslechtering kunnen worden genomen. Door het accepteren van verslechterende stappen op korte termijn, hoopt simulated annealing betere opvouwingen te ontdekken op de lange termijn. Simulated annealing heeft een temperatuurparameter die in de loop van het algoritme wordt verlaagd. In het begin staat het algoritme toe dat meer verslechterende stappen worden geaccepteerd, maar naarmate de temperatuur daalt, wordt de acceptatie van verslechterende stappen verminderd.
