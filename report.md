Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable.
Explain what problem they solve and why you chose to implement them in this way.

Technical element 1:
Probleem: De geselecteerde data werd niet leesbaar en overzichtelijk weergegeven.
Oplossing: Tabulate Module
Omschrijving: 
Ik heb voor de Tabeluate module gekozen omdat deze module ervoor zorgt dat de data goed en overzichtelijk in een tabel wordt weergegeven. De module zorgt er o.a. voor dat de data in een tabel met headers wordt weergegeven. Ik heb gekozen voor de "fancy_grid" om dat deze naar mijn mening het overzichtelijkste is. Het is ook mogelijk dat bepaalde waardes niet worden weergegeven zoals bijv. nan. (Dit heb ik gebruikt in bijv. in de reports).

Technical element 2:
Probleem: Elk product een uniek product_id geven.
Oplossing: max_id = df_sold['product_id'].max() / max_id+1
Omschrijving:
Ik wou graag elk product in een csv file een uniek product_id toekennen. Hiermee moest ik rekening houden dat er geen dubbelingen werden aangemaakt en dat deze opeenvolgend was van de laatst aangemaakte. Ik ervoor gekozen om de in de column van de product_id de .max (het hoogste id-nr) op te zoeken en bij het aanmaken van een nieuw product deze met 1 verhoogd.

Technical element 3:
Probleem: Omslachtig gebruik van de data uit parser
Oplossing: Panda Module
Omschrijving:
Ik merkte dat ik de manier van het gebruik van data welke ik d.m.v de input van parser verkreeg omslachtig vond. Ik ben gaan zoeken op internet en kwam al snel bij een veel gebruikte module binnen Python "Panda". Door deze module te gebruiken, werd het werken met de data een stuk makkelijker. Zo heb ik de data in de tabellen al een default waarde van date gegeven met een format van %Y%m%d. Ook zijn de columns snel toegankelijk en kun je hierdoor met relatief weinig code de waardes gebruiken. Zie bijv. df_sold["Total_product_revenue"] = df_sold["product_amount"] * (df_sold["selling_price"] - df_sold["purchase_price"]). Hiermee bereken ik de total revenue van het product. Het resultaat wordt in een nieuw column genaamd "Total_product_revenue" achteraan de tabel toegevoegd.
