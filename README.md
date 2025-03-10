# Projektēšanas laboratorija
## Iztrādātāji

- Jūlija Sokolova
- Georgijs Jefimovs
- Diana Sorokina
- Linda Slapiņa
- Vitālijs Vasiļjevs



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

- Klients vēlas pasūtīt druku tiešsaites veikalā, jo var ātri apskatīt kā izskatīsies druka un nav jāapmeklē klātienes tipogrāfija. 
- Tipogrāfija vēlas saņemt pasūtījumus tiešsaites veikalā, jo nav jāuztur administrators.
- Apmeklētāji vēlas saņemt pasūtījumu ar piegādi, lai nav jāapmeklē veikals. 
- Darbinieks vēlas strādāt pie vienas un tās pašas drukāšanas iekārtas, lai nevajadzētu apmācīties darboties ar katru iekārtu.
- Tipogrāfija vēlas pasūtīt materiālus lielos apjomos, lai gala cena būtu lētāka. 
- Tipogrāfija vēlās zināt un paredzēt nepieciešamos materiālu daudzumus, lai pasūtītu pietiekami daudz materiālu nākamiem pasūtījumiem.
- Tipogrāfija vēlas drukāt dārgākos un izdevīgākos pasūtījumus pirmos, lai saņemtu labāku peļņu.
- Klients vēlas saņemt noteiktu piegādes datumu, lai varētu plānot laiku. 
- Tipogrāfija vēlas, lai klienti rakstītu atsauksmes, lai būtu vairāk pasūtījumu



## Konceptu modelis

![](KONCEPTU_MODELIS2.png)

## Tehnoloģiju steks

| SERVERA PUSE: Tipogrāfija |      
|--------------------|
|Satvars: Flask|
|Programmēšanas valoda: Python|
|Datu bāze: SQLite|
|Tīmekļa serveris: Nginx|
|OS: Ubuntu|
|Virtualizācija: VMware|

| KLIENTA PUSE: Tipogrāfija | 
|--------------------|
|JavaScript|
|CSS|
|HTML|
|Pārlūks|


## Blokshēma 
![](blokshema.png)


## Pseidokods

BEGIN MAIN_PROGRAM 

    MATERIALA_PARB1
    IF MATERIALS == EXIST THEN
        PRIORITATES_APR1
            PRIORITATES APREKINASANA = X
            RINDA ADD(X) PASUTIJUMA NUMURS
                IF PRINTERIS == BRIVS THEN
                    REPEAT
                        DRUKASANA
                        IF PASUTIJUMS != BRAKIS THEN
                            UNTIL PASUTIJUMS GATAVS
                        END IF
                    PASUTIJUMA PECAPSTRADE
                ELSE
                    RINDA ADD(1)
                END IF
    ELSE
        MATERIALA PASUTISANA
        IF MATERIALS == EXIST THEN
            GOTO PRIORITATES_APR1
        ELSE
            WAIT (24 H)
            GOTO MATERIALA_PARB1
        END IF
    END IF

END MAIN_PROGRAM

## Plakāts
![](projektesana_plakats.png)
