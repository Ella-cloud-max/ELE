<img align="left" src="https://upload.wikimedia.org/wikipedia/en/thumb/7/78/University_of_Amsterdam_logo.svg/750px-University_of_Amsterdam_logo.svg.png?20110613131626" height="70px">

# &nbsp; ELE Protein pow(d)er <br clear="left"/>

Minor Programmeren - Universiteit van Amsterdam \
[Algoritmen en Heuristieken](https://studiegids.uva.nl/xmlpages/page/2022-2023/zoek-vak/vak/99363)


## Case

Proteïnen zijn lange strengen van aminozuren die veel belangrijke processen in het menselijk lichaam beregelen. Het is bekend dat proteïnen ‘opgevouwen’ in de lichaamscellen opgeborgen zitten, en dat de specifieke vouwing bepalend is voor het functioneren; verkeerd gevouwen proteïnen staan aan de basis van onder andere kanker, Alzheimer en taaislijmziekte. Het is daarom van groot belang voor zowel de farmaceutische industrie als de medische wetenschap om iets te kunnen zeggen over de exacte vorm van de vouwing.

Aminozuren kunnen worden ingedeeld in drie verschillende klasses Polair (P), Hydrofoob (H) en Cysteine (C).
Als twee hydrofobe of cysteine aminozuren naast elkaar liggen ontstaat er een ‘H-bond’ door de aantrekkende kachten tussen de twee. En hoe meer bonds, hoe stabieler het proteïne. Voor de wetenschappers en farmaceuten is het belangrijk om te weten tot welke stabiliteit van het proteïne maximaal gevouwen zou kunnen worden. Het doel is dus de gegeven proteïnen zo op te vouwen, dat ze zo stabiel mogelijk zijn.

Om dit doel te behalen zijn er verschillende soorten algoritmes geschreven. Dit zijn random, constructieve en iteratieve algoritmes. [**Meer informatie over de algorithmes kan hier gevonden worden.**](https://github.com/Ella-cloud-max/ELE/tree/main/code/algorithms)

#### Score
De stabiliteits score wordt berekend door de hoeveelheid bonds die ontstaan door een vouwing te tellen. H-H en H-C bonds leveren een stabiliteits score van -1 op, terwijl C-C bonds een stabiliteits score opleveren van -5.

## Gebruik
Download de nodigde python modules met onderstaand command:
```
 python -m pip install -r requirements.txt
```

Het volgende commando kan gebruikt worden om een van de algoritme te draaien

```
python main.py algoritme input_filename output_filename
```

Voor de algoritmes kan gekozen worden uit de volgende opties:
- baseline
- random
- greedy
- depth  
- breadth
- hill climbing
- simulated annealing


De input files zijn csv bestanden die zich in het mapje proteins bevinden. \
Een voorbeeld van een commando om een greedy algoritm te runnen op het protein in protein1.csv is als volgt.

```
python main.py greedy protein1 output_protein1
```

#### Visualisatie
Er zijn twee manieren om het opgevouwen proteïne te visualiseren. Het proteine kan in de terminal geprint worden, of opgeslagen in een png bestand.

**Terminal** \
Om de visualisatie in de terminal te printen kan het onderstaand command gebruiken. Het output bestand moet in het csv formaat opgeslagen liggen in de output folder.

```
python code/visualisation/visualisatie.py example_output
```

<img src="/docs/terminal_visualisation.png" height="100px">

\
**Bestand** \
Gebruik het onderstaande command om de visualisatie op te slaan als een png bestand. Het plaatje wordt als een png bestand opgeslagen in het mapje output/visualisation.

```
python code/visualisation/plot.py example_output visualisation_output_file
```
<img src="/docs/plot_visualisation.png" height="200px">

#### Experiment
Om een experiment te runnen gebruik het volgende command:

```
python experiment.py algoritme input_filename
```
Voor 100 seconden wordt het algoritm zo vaak als mogelijk is gedraaid. Een lijst met alle uitkomsten wordt in het bestand experiment_algoritme_input_filename.csv opgeslagen in het mapje output/experiment. Een histogram van de output wordt in het bestand histogram_algoritme_input_filename.png opgeslagen in het zelfde mapje.

<img src="/docs/histogram_example.png" height="200px">


## Structuur
[/code](https://github.com/Ella-cloud-max/ELE/tree/main/code): alle code geschreven tijdens dit project \
[/code/classes](https://github.com/Ella-cloud-max/ELE/tree/main/code/classes): bevat de benodigde classes voor dit project \
[/code/algorithms](https://github.com/Ella-cloud-max/ELE/tree/main/code/algorithms): bevat de code voor algoritmes \
[/code/visualisation](https://github.com/Ella-cloud-max/ELE/tree/main/code/visualisation): bevat de code voor de visualisaties \
[/docs](https://github.com/Ella-cloud-max/ELE/tree/main/docs): bestanden gemaakt tijdens dit bestanden \
[/proteins](https://github.com/Ella-cloud-max/ELE/tree/main/proteins): bevat alle input bestanden met proteinen \
[/output](https://github.com/Ella-cloud-max/ELE/tree/main/output): bevat alle outputs \
[/output/experiment](https://github.com/Ella-cloud-max/ELE/tree/main/output/experiment): bevat alle outputs van de experimenten \
[/output/visualisation](https://github.com/Ella-cloud-max/ELE/tree/main/output): bevat alle visualisations van de outputs

#### Auteurs
[Ella van Loenen](https://github.com/Ella-cloud-max) \
[Liesbet Ooghe](https://github.com/liesbeto) \
[Eric van Huizen](https://github.com/Eric3107)
