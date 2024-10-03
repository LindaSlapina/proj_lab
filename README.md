# Projektēšanas laboratorija
## Iztrādātāji

- Jūlija Sokolova
- Georgijs Jefimovs
- Diana Sorokina
- Linda Slapiņa
- Vitalijs Vasiļjevs



## Ievads
-  Problēmas nostādne : *Drukāšanas pasūtījumu izpildes plānošana*

## Līdzīgo risinājumu pārskats un to apraksts

### APS 

&nbsp;&nbsp;&nbsp;Advanced Planning and Scheduling algoritms analizē pieprasījuma, resursu un termiņu datus, lai izveidotu optimālu ražošanas plānu. Tas apkopo informāciju par pasūtījumiem, ražošanas jaudu un pieejamajiem materiāliem, ņemot vērā visus ierobežojumus. Algoritms var prioritizēt uzdevumus, pamatojoties uz pasūtījumu steidzamību un sarežģītību. Ja apstākļi mainās, piemēram, parādās jauni steidzami pasūtījumi vai rodas kavējumi piegādēs, APS automātiski pārskata un atjaunina plānus, lai pielāgotos jaunajai situācijai un uzlabotu efektivitāti.

### ERP

&nbsp;&nbsp;&nbsp;Sistēma attiecas uz programmatūras veidu, ko organizācijas izmanto, lai pārvaldītu ikdienas biznesa darbības, piemēram, grāmatvedību, ražošanu, projekta vadību, iepirkumus un citi. Visvienkāršākajā līmenī ERP palīdz efektīvi pārvaldīt visus šos procesus integrētā sistēmā un optimizēt darbu. Apkopojot organizācijas kopīgotos darījumu datus no vairākiem avotiem, ERP sistēmas novērš datu dublēšanos, ļaujot dinamiski pielāgot plānus, pamatojoties uz pašreizējo jaudu, krājumu līmeni un aprīkojuma pieejamību. Piemērs: ERP sistēma var automātiski ieteikt vispirms strādāt ar pasūtījumu B, ja tā pamana, ka pasūtījuma A materiāli aizkavējas vai pasūtījumam A nepieciešamais aprīkojums jau ir pilns.

### Maksimizācija (Klientu prioritāte)

&nbsp;&nbsp;&nbsp;Metode balstās uz pasūtījumi prioritizāciju, balstoties uz ienesīgumu. Galvenā ideja ir optimizēt resursus un sasniegt lielāko peļņu ar ierobežotu resursu skaitu vai izmantojot vismazāko resursu skaitu. Tā efektivitāti sasniedz ar svērtās vērtēšanas algoritmu (weighted scoring model), kura darbība tiek nodrošināta izvērtējot svarīgākos faktorus. 
Par tādiem faktoriem var uzskatīt: 
*   pasūtījuma apjomu, 
*   izpildes termiņus,
*   pasūtījumi, kam ir soda nauda par kavēšanu arī skaitīsies prioritārāki, 
*   kā arī klienti, kas ir uzticīgāki un sadarbojas ne pirmo reizi arī uzskatīsies prioritārāki.

### Apjoms un sarežģītība
&nbsp;&nbsp;&nbsp;Plānošanas princips, kas balstīts uz darba apjomu un sarežģītību, ir viena no galvenajām stratēģijām pasūtījumu izpildes optimizēšanai. Šī stratēģija ļauj efektīvi izmantot aprīkojumu un nodrošināt stabilu darba plūsmu.
Izpildes ātrums: ražotājs var vispirms izpildīt pasūtījumu ar mazāku apjomu un zemāko sarežģītība, lai vēlāk atbrīvotu aprīkojumu sarežģītākiem uzdevumiem un izvairītos no dīkstāves.
Resursu efektivitāte: Sāk ar mazākam pasūtījumiem ir efektīvāk, jo lielākiem un sarežģītākiem pasūtījumiem nepieciešama lielāka aprīkojuma sagatavošana un iestatīšana, kas var izraisīt vieglo pasūtījumu aizkavēšanos.
Kavēšanās minimizācija: ja uzņēmums vispirms koncentrējas uz lieliem pasūtījumiem, gaidīšanas laiks palielināsies, jo aprīkojums būs aizņemts. Tāpēc nelielu un vieglu pasūtījumu izpilde samazinās kavēšanos.

## Līdzīgo risinājumu apkopota novērtējuma tabula

| Veidi         | Plusi | Mīnusi |
|--------------------|-------|-------|
| ERP                | Nodrošina datu pieejamību visā organizācijā reāllaikā, izmaksas optimizācija  un produktivitātes paaugstināšanā.  |  Uzturēšanas un atjaunināšanas izmaksas, sarežģītība un laika patēriņš ieviešanā|
| Klientu prioritāte  |Ātra izskaitļošana izmantojot formulu un precīza efektivitātes plānošana| Nepareizi izvēlēti faktori var samazināt efektivitāti.   |
| APS                | Paaugstināta efektivitāte, elastība un izmaksu samazināšana, pateicoties resursu optimizācijai. | Augstas ieviešanas izmaksas, sarežģīta integrācija ar citām sistēmām un atkarība no precīziem datiem reāllaikā, lai maksimāli izmantotu iespējas.  |
| Apjoms un sarežģītība| Uzlabota kopējā produktivitāte. Klientu apmierinātība. Elastīgums  | Prioritātes piešķiršana tikai nelieliem pasūtījumiem var izraisīt lielu pasūtījumu izpildes aizkavēšanos, kas novedīs pie neapmierinātiem klientiem. |



## Lietotāju stāsti


## Konceptu modelis



