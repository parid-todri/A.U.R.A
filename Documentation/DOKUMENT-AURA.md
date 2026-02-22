DOKUMENTI I SHKRUAR I PROJEKTIT
Festivali Kombëtar i Shkencës

Titulli i projektit: AURA - Çanta e Shpinës Inteligjente dhe Terapeutike (Sistem AAC)
Fusha tematike: Inxhinieri dhe Teknologji
Shkolla: New York High School
ZVAP / DRAP: ZVAP Tiranë
Ekipi: Parid Todri, Kaltri Kuka, Elio Dikolli, Dea Vasili
Mësuese koordinatore: Olgena Thoma
 
1. Të dhëna të përgjithshme
Titulli i projektit: AURA - Çanta e Shpinës Inteligjente dhe Terapeutike (Sistem AAC)
Emri i shkollës: New York High School
ZVAP / DRAP: ZVAP Tiranë
Emrat e nxënësve përbërës të ekipit: Parid Todri, Kaltri Kuka, Elio Dikolli, Dea Vasili
Emri i mësuesit koordinator: Olgena Thoma
Fusha tematike: Inxhinieri dhe Teknologji
1.1 Profili administrativ dhe shkencor i projektit
Projekti AURA është konceptuar si një prototip funksional i një pajisjeje të veshshme ndihmëse, e cila ndërthur komunikimin zëvendësues dhe shtesë (AAC), bashkërregullimin emocional dhe inxhinierinë e sistemeve të integruara. Në aspektin administrativ, projekti paraqitet si punë ekipore e nivelit të arsimit të mesëm të lartë, ndërsa në aspektin teknik ai përfshin projektim harduerik, programim në Python, menaxhim të memories në Linux dhe dizajn ndërfaqeje me ngarkesë të ulët njohëse.
Objekti fizik i projektit është një çantë shpine inteligjente, e cila ruan pamjen e një sendi të përditshëm për të shmangur stigmatizimin, por në brendësi përmban një sistem elektronik dhe softuerik të dedikuar. Kjo e bën AURA-n një shembull tipik të teknologjisë asistive të orientuar nga përdoruesi dhe nga konteksti real i përdorimit (shkollë, rrugë, mjedise publike, aktivitete sociale).
Dokumenti i mëposhtëm paraqet në mënyrë të strukturuar problemin kërkimor, qëllimet, metodologjinë, procesin e zhvillimit, rezultatet, reflektimin dhe zbatueshmërinë e projektit. Qasja është shkencore dhe inxhinierike, por njëkohësisht e ndërtuar mbi parimin e empatisë dhe përfshirjes.
2. Përshkrimi i shkurtër i projektit
AURA është një pajisje mjekësore e veshshme në formën e një çante shpine inteligjente, e projektuar si sistem AAC (Komunikim Zëvendësues dhe Shtesë) për fëmijët me Çrregullim të Spektrit të Autizmit (ÇSA) ose për fëmijët që përjetojnë episode të mbingarkesës shqisore. Pajisja përdor tetë butona fizikë mekanikë, të lidhur me një Raspberry Pi 4, për të mundësuar komunikim të menjëhershëm në momente kur të folurit, navigimi në ekran ose ndërveprimi me pajisje touch mund të bëhen shumë të vështira.
Sistemi ka dy kanale dalëse të sinkronizuara. Kanali i parë është individual: përmes kufjeve, fëmija merr terapi zanore qetësuese dhe udhëzime të thjeshta bashkërregulluese. Kanali i dytë është social: në një ekran LCD të montuar në pjesën e pasme të çantës shfaqet një mesazh i qartë për të rriturit (prindër, mësues, kujdestarë) mbi gjendjen emocionale ose nevojën aktuale të fëmijës. Kjo ndarje e informacionit sipas marrësit është thelbësore për përdorshmërinë e sistemit.
Softueri është zhvilluar nga e para në Python duke përdorur Tkinter dhe Pygame, ekzekutohet në Headless Linux dhe përdor një arkitekturë të personalizuar "Hybrid RAM Cache" për të shmangur rrëzimin e sistemit nga Linux OOM Killer dhe për të ruajtur reagim shumë të shpejtë. Qëllimi kryesor i AURA-s është bashkërregullimi emocional dhe komunikimi i shpejtë, dinjitoz dhe me ngarkesë minimale njohëse për fëmijët jo-verbalë ose përkohësisht jo-verbalë gjatë krizës.
Në thelb, AURA nuk synon të zëvendësojë terapi profesionale ose sisteme klinike, por të ofrojë një mjet ndërmjetësues të menjëhershëm në jetën e përditshme, veçanërisht në mjedise të zhurmshme ku zgjidhjet tradicionale AAC humbasin efektivitetin praktik.
3. Problemi / Pyetja kërkimore
3.1 Konteksti neuro-sensor dhe komunikues
Një numër fëmijësh me ÇSA përjetojnë ndjeshmëri të lartë ndaj stimujve shqisorë si zhurma, drita, kontaktet sociale të papritura, mbipopullimi i hapësirës dhe ndryshimet e menjëhershme të rutinës. Kur intensiteti i këtyre stimujve tejkalon kapacitetin e përpunimit të fëmijës, mund të ndodhë mbingarkesë shqisore, gjendje e cila shoqërohet me stres të lartë emocional dhe fiziologjik.
Në kushte të tilla, aftësitë e komunikimit verbal shpesh bien ndjeshëm. Fëmija mund të mos arrijë të flasë, të mos arrijë të shpjegojë çfarë e shqetëson, të mos përpunojë pyetje të shumta ose të mos tolerojë ndërveprim të komplikuar me teknologjinë. Në praktikë, kjo gjendje mund të shfaqet si mutizëm i përkohshëm funksional, qarje, panik, izolim ose tentativa për t'u larguar nga mjedisi. Problemi, pra, nuk është mungesa e inteligjencës apo e dëshirës për të komunikuar, por bllokimi i përkohshëm i kanalit të komunikimit në momentin kritik.
3.2 Pse mjetet tradicionale AAC shpesh dështojnë gjatë krizës
Metodat AAC ekzistuese kanë vlerë të lartë në kontekste të strukturuara, por jo gjithmonë janë efektive në kulmin e mbingarkesës shqisore. Kartat PECS kërkojnë kërkim vizual, zgjedhje, mbajtje dhe shpesh ndërmjetësim nga një i rritur. Tabletët dhe telefonat me aplikacione AAC kërkojnë zhbllokim, hapje aplikacioni, navigim në menu dhe prekje të sakta në ekran. Të gjitha këto veprime rrisin ngarkesën njohëse në një moment kur ajo duhet të jetë minimale.
Për më tepër, ekranet me ndriçim, alarmet ose ikonografia e tepërt mund të shtojnë stresin shqisor. Në shumë raste, koha që humbet për të gjetur funksionin e duhur është pikërisht koha kur episodi mund të përshkallëzohet. Kjo e bën të nevojshme krijimin e një mjeti më të thjeshtë, më taktil dhe më të menjëhershëm, i cili të aktivizohet me një shtypje të vetme fizike.
3.3 Rëndësia e problemit në kontekstin shkollor dhe publik
Në klasë, korridore, aktivitete shkollore, qendra tregtare ose transport publik, reagimi i shpejtë dhe i saktë i të rriturit mund të bëjë diferencë të madhe në sigurinë dhe mirëqenien e fëmijës. Kur i rrituri nuk kupton gjendjen e fëmijës, ai mund të japë udhëzime të papërshtatshme, të insistojë në komunikim verbal ose të interpretojë gabim sjelljen. Kjo mund të rrisë ankthin, të zgjasë krizën dhe të krijojë përvojë traumatike.
Prandaj, problemi që trajton AURA është njëkohësisht teknik, pedagogjik dhe human: si të krijohet një kanal komunikimi emergjent që ruan autonominë e fëmijës, redukton ngarkesën njohëse dhe ndihmon të rriturin të reagojë me qetësi dhe saktësi.
3.4 Pyetja kërkimore
A mund të inxhinierohet një pajisje e veshshme AAC, e bazuar në butona fizikë dhe në dy dalje të sinkronizuara (audio për fëmijën dhe ekran vizual për të rriturin), që të ulë ngarkesën njohëse dhe të mundësojë komunikim të shpejtë gjatë episodeve të mbingarkesës shqisore?
3.5 Hipoteza funksionale e projektit
Hipoteza funksionale e ekipit ishte se një sistem me input taktil (butona fizikë), me hartë të drejtpërdrejtë funksionesh dhe me dalje të dyfishta të ndara sipas marrësit, do të ishte më efektiv në situata krize sesa ndërfaqet e bazuara në menu dhe ekran me prekje. Kjo hipotezë u testua në nivel prototipi përmes ndërtimit teknik dhe testimeve iterative të reagimit, stabilitetit dhe përdorshmërisë funksionale.
4. Qëllimi dhe rezultatet e pritshme të projektit
4.1 Qëllimi i përgjithshëm
Qëllimi i përgjithshëm i projektit është projektimi, ndërtimi dhe programimi i një prototipi funksional të një pajisjeje AAC të veshshme, të integruar në çantë shpine, e cila mundëson komunikim të menjëhershëm dhe bashkërregullim emocional për fëmijët me ÇSA ose mbingarkesë shqisore, veçanërisht në mjedise me zhurmë dhe shpërqendrim të lartë.
4.2 Objektivat specifike
•	Të ndërtohet një prototip harduerik i qëndrueshëm me Raspberry Pi 4, ekran LCD, 8 butona mekanikë dhe furnizim portativ me energji.
•	Të zhvillohet softueri në Python (Tkinter + Pygame) që lexon inputet nga GPIO dhe aktivizon dy kanalet dalëse në mënyrë të sinkronizuar.
•	Të implementohet një arkitekturë e personalizuar Hybrid RAM Cache për të reduktuar përdorimin kritik të memories dhe për të shmangur rrëzimet e sistemit nga Linux OOM Killer.
•	Të lokalizohet sistemi në gjuhën shqipe (mesazhe vizuale dhe strukturë funksionale) për zbatim të mundshëm në shkolla dhe familje në Shqipëri.
4.3 Rezultate konkrete dhe të matshme (deliverables)
1.	Ndërtimi i prototipit harduerik funksional me 8/8 butona të lexueshëm në GPIO dhe ekran LCD operacional.
2.	Krijimi i një aplikacioni Python të personalizuar që aktivizon audio dhe mesazhe vizuale për çdo input të butonave.
3.	Implementimi dhe testimi i logjikës Hybrid RAM Cache për stabilitet të memories gjatë ekzekutimit.
4.	Konfigurimi i ekzekutimit në Headless Linux (pa desktop) për nisje më të shpejtë dhe konsum më të ulët burimesh.
5.	Lokalizimi bazë i gjendjeve/nevojave në gjuhën shqipe dhe demonstrimi i funksionimit në skenarë përdorimi.
4.4 Tregues funksionalë të performancës së prototipit
Për një projekt të këtij niveli, suksesi u vlerësua jo vetëm nga ndërtimi fizik, por nga kombinimi i treguesve funksionalë: reagim i shpejtë pas shtypjes së butonit, stabilitet i sistemit në aktivizime të përsëritura, qartësi e mesazheve për të rriturin dhe nisje e sigurt e audio-s qetësuese. Në testimet tona praktike, prototipi arriti reagim të perceptueshëm si i menjëhershëm, me vonesë rreth 0.1 sekonda, çka është e përshtatshme për përdorim në kontekst krizash.
4.5 Tabela përmbledhëse e objektivave dhe rezultateve
Objektivi	Veprimet kryesore	Rezultati i pritshëm / i arritur
Harduer prototip	Montim Raspberry Pi 4, LCD, 8 butona, bateri	Prototip funksional i integruar në çantë
Softuer Python	Lexim GPIO, UI Tkinter, audio Pygame	Aktivizim i saktë i dy kanaleve dalëse
Stabilitet memorie	Hybrid RAM Cache dhe optimizim runtime	Eliminim i rrëzimeve nga OOM në testimet iterative
Lokalizim në shqip	Mesazhe dhe logjikë e përshtatur	Përdorshmëri më e lartë në kontekst shqiptar
5. Metodologjia e punës
5.1 Qasja metodologjike e kombinuar
Metodologjia e projektit AURA u organizua si një qasje e kombinuar kërkimore-inxhinierike me cikle iterative. Në fillim u identifikua problemi dhe u formulua pyetja kërkimore; më pas nevoja humane u përkthye në kërkesa teknike (shpejtësi reagimi, përdorshmëri taktile, dy dalje të sinkronizuara, stabilitet në Linux). Kjo u ndoq nga ndërtimi i prototipit, testimi, diagnostikimi i gabimeve dhe rishikimi i zgjidhjeve deri në arritjen e një sistemi të qëndrueshëm.
Kjo metodologji u zgjodh sepse AURA nuk është thjesht një aplikacion, por një sistem i integruar ku ndërveprojnë elektronika, sistemi operativ, menaxhimi i memories, audio, vizualja dhe ergonomia. Për këtë arsye, puna u zhvillua në faza të koordinuara, por me kthime të vazhdueshme mbrapa për përmirësim.
5.2 Faza e kërkimit dhe analizës së nevojës
Në fazën e parë u analizuan parimet bazë të komunikimit AAC dhe sfidat e mbingarkesës shqisore. Ekipi u fokusua në pyetjen praktike: cilat ndërveprime janë realisht të realizueshme nga një fëmijë në krizë? Kjo fazë çoi në vendimin për të përdorur input taktil (butona fizikë) dhe jo ndërfaqe me menu. U mor në konsideratë edhe parimi i bashkërregullimit, pra nevoja që pajisja të ndihmojë fëmijën dhe njëkohësisht të informojë të rriturin.
Paralelisht, u mendua për lokalizimin në gjuhën shqipe, në mënyrë që mesazhet e ekranit të jenë të kuptueshme pa përkthim. Kjo e bëri projektin më të zbatueshëm në kontekstin e shkollave dhe familjeve shqiptare.
5.3 Inxhinieria e harduerit
5.3.1 Komponentët kryesorë
•	Raspberry Pi 4 si njësi qendrore e përpunimit dhe kontrollit.
•	8 butona mekanikë fizikë (tip arcade/me feedback taktil) të vendosur ergonomikisht në rripin e çantës ose zonë të arritshme.
•	Ekran LCD në pjesën e pasme të çantës për shfaqjen e gjendjes emocionale ose udhëzimeve për të rriturit.
•	Kufje për fëmijën si dalje audio qetësuese dhe udhëzuese.
•	Bateri/power bank 25,000 mAh për furnizim portativ me energji.
•	Kabllo, konektorë, materiale izolimi dhe fiksimi për integrim të sigurt në strukturën e çantës.
5.3.2 Lidhja e butonave me GPIO dhe logjika elektrike
Butonat u lidhën në kunjat GPIO të Raspberry Pi me konfigurim që përdor rezistenca të brendshme pull-up dhe aktivizim përmes lidhjes me GND. Kjo qasje ul kompleksitetin e qarkut, stabilizon leximin e inputeve dhe thjeshton diagnostikimin. Gjatë montimit u kushtua rëndësi izolimit të nyjeve dhe organizimit të kabllimit për të shmangur ndërprerje ose gabime të shkaktuara nga lëvizja e çantës.
5.3.3 Integrimi fizik në çantë
Një kriter i rëndësishëm metodologjik ishte që pajisja të mos duket si instrument klinik i jashtëm, por si objekt i përditshëm. Për këtë arsye, komponentët kryesorë u integruan në brendësi të çantës, ndërsa ekrani u vendos në pjesën e pasme për lexim nga të rriturit. Kjo qasje mbështet ruajtjen e dinjitetit të fëmijës dhe redukton stigmatizimin. Gjithashtu u mendua pozicionimi i butonave në mënyrë që aktivizimi të jetë i mundur edhe pa fokus të drejtpërdrejtë vizual.
5.4 Inxhinieria e softuerit
5.4.1 Teknologjitë e përdorura
Softueri u zhvillua në Python nga e para. Tkinter u përdor për menaxhimin e komponentit vizual dhe shfaqjen e mesazheve në ekranin LCD, ndërsa Pygame u përdor për menaxhimin e audios (luajtje klipesh, kontroll volumesh, sinkronizim i kanaleve). Python u zgjodh për shkak të shpejtësisë së prototipimit, lexueshmërisë së kodit dhe mbështetjes së mirë në Raspberry Pi.
5.4.2 Arkitektura funksionale e aplikacionit
Aplikacioni u ndërtua me logjikë me gjendje (state-based logic) dhe me module të ndara: lexim inputi (GPIO), hartë funksionesh (buton -> gjendje/nevojë), menaxhim audio, ndërfaqe vizuale, kohëmatës auto-reset, pastrim i burimeve dhe menaxhim i memories. Kjo ndarje e rrit modularitetin dhe lehtëson testimin dhe mirëmbajtjen.
5.4.3 Headless Linux dhe modaliteti i ekzekutimit
Sistemi u konfigurua të ekzekutohet në Linux pa ndërfaqe desktop (Headless Linux), me nisje të drejtpërdrejtë të aplikacionit në boot. Kjo ul konsumimin e burimeve, zvogëlon proceset në sfond dhe i jep pajisjes karakteristikat e një sistemi të dedikuar, jo të një kompjuteri të përgjithshëm. Si rezultat, përmirësohen koha e nisjes, stabiliteti dhe parashikueshmëria e sjelljes së sistemit.
5.5 Materialet dhe mjedisi i punës
Për realizimin e prototipit u përdorën materiale elektronike dhe kompjuterike të disponueshme në treg, mjete bazë montimi dhe mjedis programimi në Linux/Python. Testimet u kryen në kushte të kontrolluara laboratorike-demonstrative, me qëllim verifikimin e funksionalitetit, reagimit dhe stabilitetit teknik, jo vlerësimin klinik terapeutik.
5.6 Metodat e testimit
•	Testim individual i çdo butoni për lexim korrekt në GPIO.
•	Testim i sekuencave të përsëritura të aktivizimit për të verifikuar stabilitetin e runtime-it.
•	Testim i reagimit të sinkronizuar audio + ekran për secilin input.
•	Testim i konsumit të memories gjatë përdorimit të aseteve audio dhe vizuale.
•	Testim i mbylljes/rinisjes së aplikacionit për të verifikuar pastrimin e GPIO dhe shmangien e gabimit 'GPIO busy'.
•	Testim i auto-reset për rikthimin automatik në gjendjen 'Gati' pas periudhës së caktuar.
5.7 Kufizimet metodologjike
Ky projekt është një prototip shkencor në nivel shkolle dhe nuk përfshin validim klinik me kampion të strukturuar përdoruesish. Testimet janë fokusuar kryesisht në funksionalitetin teknik, stabilitetin e sistemit dhe përdorshmërinë konceptuale. Për të kaluar në fazë zbatimi më të gjerë, nevojiten partneritete me profesionistë të fushës (psikologë, terapistë, mësues të edukimit special) dhe protokolle testimi etike dhe të standardizuara.
5.8 Tabela e materialeve kryesore
Komponenti	Roli në sistem	Arsyeja e zgjedhjes	Statusi në prototip
Raspberry Pi 4	Njësia qendrore e kontrollit	Mbështetje e mirë për Linux, Python dhe GPIO	I integruar dhe funksional
8 butona mekanikë	Input taktil me ngarkesë të ulët njohëse	Klikim fizik i qartë, tolerancë ndaj gabimit	Të integruar
Ekran LCD	Dalje vizuale për të rriturit	Lexim i shpejtë i gjendjes/nevojës	I montuar
Kufje	Dalje audio për fëmijën	Mbështetje qetësuese e menjëhershme	Funksionale
Bateri 25,000 mAh	Furnizim portativ me energji	Autonomi e mirë për testim/demonstrim	Funksionale, por e rëndë
6. Zhvillimi i projektit dhe rezultatet
6.1 Ecuria e zhvillimit nga koncepti te prototipi
Zhvillimi i AURA-s u realizua në mënyrë iterative. Versioni fillestar synonte vetëm sinjalizim me butona, por gjatë konceptimit u pa qartë se kjo nuk e zgjidhte plotësisht nevojën reale të fëmijës në krizë. Për këtë arsye u shtua kanali audio qetësues në kufje dhe u ndërtua arkitektura me dy dalje. Ky ndryshim e transformoi AURA-n nga panel sinjalizimi në sistem bashkërregullimi dhe komunikimi.
Në fazat e para u bë montimi bazë harduerik dhe një version minimal i softuerit për testim inputesh dhe shfaqje në ekran. Më pas u integrua menaxhimi i audios, kontrolli i volumit dhe funksioni i auto-reset. Problemet më të mëdha u shfaqën gjatë testimit të performancës dhe të mbylljes/rinisjes së sistemit, ku u evidentuan çështjet e memories dhe të GPIO.
6.2 Procesi i ndërtimit harduerik
Procesi i ndërtimit harduerik përfshiu planifikimin e vendosjes së komponentëve brenda çantës, menaxhimin e kabllimit dhe sigurimin e aksesit të lehtë në butona. U krye montimi i ekranit në pjesën e pasme dhe u testua lexueshmëria e tij nga distanca të ndryshme të zakonshme shkollore. Po ashtu u testua qëndrueshmëria e lidhjeve gjatë lëvizjes së çantës, për të shmangur shkëputje aksidentale gjatë përdorimit.
Një aspekt i rëndësishëm praktik ishte balanca ndërmjet funksionalitetit dhe ergonomisë: sistemi duhej të ishte mjaftueshëm i fuqishëm për të funksionuar në mënyrë të besueshme, por edhe i integruar në mënyrë diskrete dhe të sigurt. Kjo kërkoi disa rikonfigurime të brendshme gjatë fazave të prototipimit.
6.3 Procesi i zhvillimit të softuerit
Softueri u shkrua modularisht. Fillimisht u testua moduli i leximit të butonave dhe mapimit të tyre me funksione specifike. Më pas u ndërtua komponenti vizual me Tkinter dhe u shtua menaxhimi i audios me Pygame. Integrimi i këtyre moduleve kërkoi sinkronizim të kujdesshëm të rrjedhës së ngjarjeve, në mënyrë që aktivizimi i një butoni të shkaktojë menjëherë veprime të koordinuara pa konflikte ose bllokime.
Në vazhdim, u implementuan funksione sigurie dhe përdorshmërie: kufizim i volumit, logjikë e fikjes së sigurt (për të shmangur fikjen aksidentale) dhe auto-reset pas 60 sekondash. Këto shtesa rritën besueshmërinë e prototipit dhe e bënë sjelljen e sistemit më të parashikueshme.
6.4 Sfida kryesore 1: Problemi i memories (Linux OOM Killer)
Gjatë testimeve me asetet audio-vizuale, veçanërisht kur përmbajtja vizuale ngarkohej në mënyrë jo optimale, u vu re rritje e papritur e përdorimit të RAM-it. Në raste të tilla, sistemi operativ Linux aktivizonte mekanizmin OOM Killer (Out Of Memory Killer), i cili mbyllte procesin e aplikacionit për të mbrojtur sistemin. Kjo sjellje ishte e papranueshme për një pajisje që synon të funksionojë pikërisht në momente kritike.
Analiza e problemit tregoi se rrënja e tij nuk ishte vetëm madhësia e aseteve, por mënyra e ngarkimit dhe mbajtjes së tyre në memorie gjatë runtime-it. Në sistemet embedded, menaxhimi joefikas i memories mund të prodhojë rrëzime edhe kur logjika funksionale e aplikacionit duket e saktë.
6.4.1 Zgjidhja: Arkitektura 'Hybrid RAM Cache'
Për të adresuar problemin, ekipi krijoi një arkitekturë të personalizuar të memories të quajtur "Hybrid RAM Cache". Parimi i saj është ndarja e aseteve sipas rëndësisë kohore dhe kostos së ngarkimit:
•	Asetet audio kritike, të cilat duhet të nisin menjëherë, parangarkohen në RAM gjatë ndezjes së sistemit.
•	Përmbajtja vizuale menaxhohet më dinamikisht dhe nuk mbahet e gjitha njëkohësisht në RAM.
•	Lirohen burimet që nuk nevojiten menjëherë pas përdorimit, për të shmangur akumulimin e panevojshëm.
•	Ruhet balanca midis shpejtësisë së reagimit dhe stabilitetit të memories.
Pas implementimit të kësaj arkitekture, prototipi tregoi stabilitet dukshëm më të lartë dhe eliminim të rrëzimeve të lidhura me OOM gjatë testimeve iterative. Kjo zgjidhje përbën një nga kontributet më origjinale teknike të ekipit në projekt.
6.5 Sfida kryesore 2: Bllokimi i harduerit (GPIO Busy)
Gjatë cikleve të testimit, pas mbylljes së aplikacionit dhe rinisjes së tij, në disa raste shfaqej gabimi 'GPIO busy', i cili tregon se disa burime GPIO nuk ishin liruar siç duhej. Kjo e bënte testimin dhe përdorimin jo të besueshëm, sepse kërkonte ndërhyrje manuale.
Kjo sfidë lidhej me mënyrën e mbylljes së proceseve, me mbetjen e proceseve fantazmë dhe me menaxhimin e burimeve në nivel userspace/kernel. Në sisteme reale, këto probleme janë të zakonshme dhe kërkojnë zgjidhje procedurale, jo vetëm logjikë funksionale.
6.5.1 Zgjidhja: Cleanup automatik dhe kontroll i proceseve
Për zgjidhjen e problemit, u implementuan mekanizma të pastrimit automatik (cleanup) në kodin Python, me lirimin e GPIO në mbyllje dhe trajtimin e skenarëve të ndalimit të papastër. Gjithashtu u shtuan procedura kontrolli për mbylljen e proceseve fantazmë gjatë testimeve, përfshirë përdorim të komandave të sistemit në skenarët e zhvillimit (p.sh. logjikë e tipit killall kur nevojitej).
Pas këtyre ndërhyrjeve, rinisja e sistemit u bë dukshëm më e qëndrueshme dhe gabimi 'GPIO busy' u reduktua ndjeshëm, duke e bërë prototipin më të besueshëm për demonstrim dhe përdorim të përsëritur.
6.6 Rezultatet funksionale të prototipit
•	Prototipi lexon input nga 8 butona fizikë dhe aktivizon funksionet e programuara.
•	Audio qetësuese dhe mesazhi vizual në LCD nisen në mënyrë të sinkronizuar pas inputit.
•	Sistemi operon në Headless Linux dhe sillet si pajisje e dedikuar (appliance-like).
•	Arkitektura Hybrid RAM Cache rrit stabilitetin dhe ul rrezikun e rrëzimit nga OOM.
•	Logjika e cleanup përmirëson rikuperimin pas ndalimit/rinisjes dhe shmang bllokimet e GPIO.
•	Auto-reset pas 60 sekondash rikthen pajisjen në gjendjen 'Gati' për përdorimin e radhës.
6.7 Performanca e reagimit
Në testimet praktike të prototipit, koha e reagimit nga shtypja e butonit deri në aktivizimin funksional të daljes (audio/ekran) u vlerësua rreth 0.1 sekonda (afërsisht 100 ms), me variacione të vogla sipas ngarkesës së momentit. Në kontekst përdorimi, ky reagim perceptohet si pothuajse i menjëhershëm dhe është i përshtatshëm për nevojën e komunikimit emergjent gjatë krizës.
6.8 Tabela e hartës funksionale të 8 butonave (shembull prototipi)
Butoni	Funksioni/Gjendja	Dalja për fëmijën (audio)	Dalja për të rriturin (LCD)
B1	Jam i mbingarkuar	Audio qetësuese + udhëzim frymëmarrjeje	Jam i mbingarkuar. Ju lutem ulni zhurmën.
B2	Kam nevojë për qetësi	Tingull qetësues / noise profil	Kam nevojë për një vend të qetë.
B3	Kam frikë/ankth	Mesazh sigurues i strukturuar	Ju lutem qëndroni pranë me qetësi.
B4	Kam nevojë për pushim	Audio ritmike e butë	Kam nevojë për pushim të shkurtër.
B5	Jam i lodhur	Audio e ulët relaksuese	Jam i lodhur; ju lutem ngadalësoni ritmin.
B6	Nuk dua prekje	Udhëzim vetë-rregullues	Ju lutem mos më prekni tani.
B7	Kam nevojë për ujë	Sinjal audio i shkurtër	Kam nevojë për ujë.
B8	Jam gati / po qetësohem	Konfirmim audio i butë	Po qetësohem / jam më mirë.
Shënim: tabela e mësipërme paraqet një model të mundshëm hartimi funksional për prototipin dhe shërben si ilustrim i logjikës së sistemit. Në zbatime të ardhshme, përmbajtja dhe kategorizimi mund të personalizohen sipas profilit të fëmijës dhe rekomandimeve të specialistëve.
7. Përfundime dhe reflektim
7.1 Çfarë u arrit
Projekti AURA arriti të demonstrojë se është e mundur të ndërtohet një prototip AAC i veshshëm, i integruar në një çantë shpine, që kombinon komunikimin emergjent dhe bashkërregullimin emocional. Nga një ide fillestare konceptuale, projekti u zhvillua në një sistem teknik funksional që lexon input taktil, aktivizon audio për fëmijën dhe shfaq mesazhe për të rriturin në kohë shumë të shpejtë.
Një arritje e rëndësishme ishte transformimi i prototipit në një sistem të qëndrueshëm përmes zgjidhjes së dy problemeve kritike të inxhinierisë së sistemeve të integruara: menaxhimi i memories (OOM Killer) dhe bllokimet e GPIO. Kjo tregon se ekipi nuk u fokusua vetëm te funksioni demonstrativ, por edhe te besueshmëria reale e sistemit.
7.2 Çfarë funksionoi më mirë
•	Koncepti i inputit me butona fizikë mekanikë, i cili redukton ngarkesën njohëse dhe ofron feedback taktil.
•	Ndarja e informacionit në dy kanale dalëse (audio për fëmijën, ekran për të rriturin), që rrit qartësinë e ndërhyrjes.
•	Arkitektura software e ndarë në module dhe implementimi i Hybrid RAM Cache për stabilitet.
•	Lokalizimi në gjuhën shqipe, që e bën sistemin më të aksesueshëm në kontekstin shqiptar.
7.3 Çfarë mund të përmirësohet
Versioni aktual i AURA-s është prototip funksional, por jo ende produkt i standardizuar për përdorim afatgjatë. Përmirësimet më të rëndësishme lidhen me peshën totale të çantës, paketimin e komponentëve, rezistencën mekanike dhe zgjerimin e testimeve me përdorues realë. Bateria 25,000 mAh ofron autonomi të mirë, por është relativisht e rëndë dhe ndikon në ergonomi, veçanërisht për fëmijë të vegjël.
Një tjetër fushë përmirësimi është personalizimi më i thellë i profileve audio dhe i hartës së butonave sipas nevojave individuale. Edhe pse prototipi është i lokalizuar në shqip dhe funksional, efektiviteti praktik mund të rritet ndjeshëm me bashkëpunim ndërdisiplinor me terapistë, psikologë dhe mësues të edukimit special.
7.4 Çfarë mësuam si ekip
Nga ana teknike, projekti na mësoi parime të rëndësishme të inxhinierisë së sistemeve të integruara: planifikimin e ndërveprimit hardware-software, debugimin në Linux, menaxhimin e proceseve dhe optimizimin e memories. Kuptuam se ndërtimi i një prototipi nuk mbaron te 'funksionon një herë'; sistemi duhet të jetë i qëndrueshëm, i rikuperueshëm dhe i parashikueshëm.
Nga ana metodologjike, mësuam vlerën e testimit iterativ: çdo problem i gjetur gjatë provave çoi në analizë, zgjidhje dhe përmirësim. Kjo na ndihmoi të kalojmë nga qasja e thjeshtë e ndërtimit në qasjen e vërtetë inxhinierike të validimit dhe optimizimit.
Nga ana njerëzore, mësuam se teknologjia më e mirë është ajo që ndërtohet me empati. AURA na tregoi se dizajni nuk duhet të fokusohet vetëm te funksionet, por te gjendja reale e përdoruesit. Qëllimi nuk është ta detyrojmë fëmijën të përshtatet me pajisjen, por të ndërtojmë pajisjen që i përgjigjet fëmijës në momentin kur ai ka më shumë nevojë për mbështetje.
8. Ndikimi dhe zbatueshmëria
8.1 Ndikimi i mundshëm për shkollat dhe familjet në Shqipëri
AURA ka potencial të lartë ndikimi si mjet mbështetës në shkolla dhe në mjedise publike, sepse adreson një nevojë konkrete dhe shpesh të nëntrajtuar: komunikimin e menjëhershëm gjatë mbingarkesës shqisore. Për mësuesit dhe prindërit, një mjet i tillë mund të shërbejë si udhëzues i shpejtë për të kuptuar gjendjen e fëmijës dhe për të shmangur reagime që mund ta përkeqësojnë situatën.
Lokalizimi në gjuhën shqipe e bën AURA-n veçanërisht të rëndësishme për kontekstin shqiptar. Shumë zgjidhje teknologjike ndërkombëtare janë të fuqishme teknikisht, por të vështira për t'u përdorur pa përkthim ose personalizim. AURA e vendos përdorshmërinë lokale si kriter bazë, gjë që rrit gjasat e zbatimit praktik.
8.2 Zbatueshmëria teknike dhe praktike
Nga pikëpamja teknike, projekti demonstron se koncepti mund të realizohet me komponentë relativisht të disponueshëm dhe me mjedis software të hapur. Përdorimi i Raspberry Pi dhe Python e bën prototipin fleksibël për modifikime të mëtejshme, ndërsa arkitektura modulare e softuerit lejon shtim funksionesh pa rindërtim të plotë të sistemit.
Megjithatë, për zbatim të gjerë institucional nevojiten disa hapa shtesë: standardizim i paketimit harduerik, testime me përdorues realë, protokolle përdorimi për stafin arsimor dhe bashkëpunim me specialistë. Këto hapa janë të realizueshëm dhe përfaqësojnë fazën natyrore pas suksesit të prototipit demonstrues.
8.3 Çështje etike dhe të sigurisë (parime orientuese)
Si projekt teknologjik që lidhet me fëmijët dhe me sjelljet gjatë stresit, AURA duhet të zhvillohet me kujdes etik. Versionet e ardhshme duhet të respektojnë privatësinë, dinjitetin dhe autonominë e përdoruesit, si dhe të shmangin mbledhjen e panevojshme të të dhënave personale. Çdo testim me përdorues realë duhet të kryhet me pëlqim të informuar të prindërve/kujdestarëve dhe në bashkëpunim me profesionistë.
Nga ana e sigurisë teknike, duhet të garantohen izolimi elektrik, kontrolli i volumit në nivele të sigurta, mbrojtja mekanike e komponentëve dhe sjellja e parashikueshme e softuerit. Këto parime janë pjesë e filozofisë së projektit dhe do të jenë prioritare në zhvillimet e ardhshme.
8.4 Vizioni i së ardhmes: AURA 2.0
Versioni 2.0 i AURA-s synon ta shndërrojë pajisjen nga sistem reaktiv në sistem më inteligjent dhe më të personalizueshëm. Drejtimet kryesore të zhvillimit përfshijnë sensorë biometrikë, lidhje Bluetooth dhe aplikacion shoqërues për prindërit/kujdestarët, si dhe përmirësime të paketimit harduerik.
8.4.1 Sensorë biometrikë për parashikim të hershëm
Një zhvillim i mundshëm është integrimi i sensorëve për rrahjet e zemrës dhe tregues të tjerë fiziologjikë, me qëllim identifikimin e shenjave të hershme të stresit. Nëse sistemi arrin të njohë rritje të ngarkesës para kulmit të krizës, ai mund të aktivizojë mbështetje qetësuese në mënyrë proaktive. Ky hap do ta çonte AURA-n drejt një qasjeje më parandaluese.
8.4.2 Integrimi Bluetooth dhe aplikacioni për prindërit
Integrimi Bluetooth do të mundësonte dërgimin e njoftimeve te prindërit/kujdestarët dhe ruajtjen e logjeve të përdorimit (p.sh. cilat gjendje aktivizohen më shpesh, në çfarë orari). Këto të dhëna, nëse menaxhohen me kujdes etik dhe privatësi, mund të ndihmojnë specialistët dhe familjet të kuptojnë më mirë shkaktarët mjedisorë dhe të ndërtojnë strategji mbështetjeje të personalizuar.
8.4.3 Përmirësime harduerike
Për përdorim më të gjatë dhe më komod, rekomandohet zëvendësimi i baterisë aktuale me zgjidhje litiumi më të lehta dhe integrim më kompakt i elektronikës. Gjithashtu, një strehim i personalizuar me printim 3D dhe mbrojtje më e mirë ndaj lagështisë do ta rrisnin qëndrueshmërinë e pajisjes në përdorim të përditshëm.
8.5 Vlera edukative dhe shoqërore e projektit
Përveç ndikimit të drejtpërdrejtë potencial te përdoruesit finalë, AURA ka vlerë edhe si model edukativ i STEM-it me ndikim shoqëror. Projekti tregon se nxënësit e arsimit të mesëm mund të ndërtojnë zgjidhje të avancuara kur kombinojnë shkencën, programimin, inxhinierinë dhe ndjeshmërinë sociale. Kjo e bën AURA-n jo vetëm një prototip teknik, por edhe një shembull të mësimit aktiv dhe të përgjegjshëm shoqërisht.
9. Burimet dhe referencat
Për ndërtimin e kuadrit teorik dhe teknik të projektit u përdorën burime akademike dhe dokumentacione zyrtare. Referencat e mëposhtme paraqiten në formatin APA dhe mbështesin aspektet kryesore të projektit: kuptimin e ÇSA dhe komunikimit AAC, programimin në Python, si dhe dokumentimin e platformës Raspberry Pi.
6.	American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.; DSM-5-TR). American Psychiatric Association Publishing.
7.	Mirenda, P. (2003). Toward functional augmentative and alternative communication for students with autism: Manual signs, graphic symbols, and voice output communication aids. Language, Speech, and Hearing Services in Schools, 34(3), 203-216.
8.	Raspberry Pi Ltd. (n.d.). Raspberry Pi documentation (hardware, Linux, and GPIO documentation). Raspberry Pi Documentation.
9.	Python Software Foundation. (n.d.). tkinter - Python interface to Tcl/Tk (Python standard library documentation). Python Documentation.
10.	Pygame Community. (n.d.). Pygame documentation. Pygame Documentation.
9.1 Shënim mbi përdorimin e burimeve
Burimet e mësipërme janë përdorur për orientim teorik dhe teknik gjatë konceptimit dhe zhvillimit të prototipit. Projekti AURA është një punë origjinale e ekipit në nivelin e prototipit shkencor dhe nuk përfaqëson një pajisje klinike të certifikuar.

