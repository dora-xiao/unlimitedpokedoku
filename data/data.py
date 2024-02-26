# # import pokebase as pb
# import requests

# d = {}
# # Region
# d["generation-i"] = []
# d["generation-ii"] = []
# d["generation-iii"] = []
# d["generation-iv"] = []
# d["generation-v"] = []
# d["generation-vi"] = []
# d["generation-vii"] = []
# d["generation-viii"] = []
# d["generation-ix"] = []
# d["hisui"] = []
# # Type
# d["normal"] = []
# d["fire"] = []
# d["water"] = []
# d["electric"] = []
# d["grass"] = []
# d["ice"] = []
# d["fighting"] = []
# d["poison"] = []
# d["ground"] = []
# d["flying"] = []
# d["psychic"] = []
# d["bug"] = []
# d["rock"] = []
# d["ghost"] = []
# d["dragon"] = []
# d["dark"] = []
# d["steel"] = []
# d["fairy"] = []
# # Color
# d["red"] = []
# d["blue"] = []
# d["yellow"] = []
# d["green"] = []
# d["black"] = []
# d["brown"] = []
# d["purple"] = []
# d["gray"] = []
# d["white"] = []
# d["pink"] = []

# d["dual"] = []
# d["mono"] = []

# d["mythical"] = []
# d["legendary"] = []
# d["baby"] = []

# d["hasform"] = [] # only counts the base species (ex: rotom has form but you can't put rotom-heat)

# d["hasgenderdifferences"] = []
# d["genderless"] = []

# # quag is height 14 and weight 750
# d["taller"] = []
# d["shorter"] = []
# d["heavier"] = []
# d["lighter"] = []

# d["mega"] = []

# # EVOLUTION CHAIN API ENDPOINT IS REALLY MESSY - TODO LATER
# # noevo = []
# # firstoftwo = []
# # firstofthree = []
# # secondoftwo = []
# # secondofthree = []
# # thirdofthree = []
# # splitevo = []
# # evolvesbyitem = []
# # evolvesbyfriendship = []

# # TODO: add ultra beasts

# # base species (1 to 1025) and forms (10001 to 10277)
# idtoname = [""]*1026
# formidtoname = [""]*278
# idtoimg = [""]*1026
# formidtoimg = [""]*278

# # iterate through 1025 base species but add all forms as well
# for i in range(1025):
#     print(i)
#     data = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i+1}').json()
#     varieties = data["varieties"]

#     for v in varieties:
#         formdata = requests.get(v["pokemon"]["url"]).json()

#         id = formdata["id"]
#         if(id > 10000): # form
#             formidtoname[id-10000] = formdata["name"]
#             formidtoimg[id-10000] = formdata["sprites"]["other"]["official-artwork"]["front_default"]
#         else: # basic species
#             idtoname[id] = formdata["name"]
#             idtoimg[id] = formdata["sprites"]["other"]["official-artwork"]["front_default"]
#             d[data["color"]["name"]].append(id)
#             if(len(varieties) > 1): d["hasform"].append(id)
        
#         if(data["is_baby"]): d["baby"].append(id)
#         if(data["is_mythical"]): d["mythical"].append(id)
#         if(data["is_legendary"]): d["legendary"].append(id)
#         if(data["gender_rate"] == -1): d["genderless"].append(id)
#         if(data["has_gender_differences"]): d["hasgenderdifferences"].append(id)
#         if("mega" in formdata["name"]): d["mega"].append(id)

#         if("alola" in formdata["name"]): 
#             d["generation-vii"].append(id)
#         elif("galar" in formdata["name"]): 
#             d["generation-viii"].append(id)
#         elif("hisui" in formdata["name"]): 
#             d["hisui"].append(id)
#         elif("paldea" in formdata["name"]): 
#             d["generation-ix"].append(id)
#         else:
#             d[data["generation"]["name"]].append(id)
        
#         if(formdata["weight"] > 750):
#              d["heavier"].append(id)
#         else: 
#              d["lighter"].append(id)

#         if(formdata["height"] > 14):
#              d["taller"].append(id)
#         else: 
#              d["shorter"].append(id)

#         types = formdata["types"]
#         if(len(types) == 1): 
#             d["mono"].append(id)
#             d[types[0]["type"]["name"]].append(id)
#         else:
#             d["dual"].append(id)
#             d[types[0]["type"]["name"]].append(id)
#             d[types[1]["type"]["name"]].append(id)

#         # evodata = requests.get(data["evolution_chain"]["url"]).json()["chain"]
#         # level = 1
#         # if(len(evodata["evolves_to"]))
        
#         # noevo = []
#         # firstoftwo = []
#         # firstofthree = []
#         # secondoftwo = []
#         # secondofthree = []
#         # thirdofthree = []
#         # splitevo
#         # evolvesbyitem = []
#         # evolvesbyfriendship = []
            
s = """1
Bulbasaur
2
Ivysaur
3
Venusaur
4
Charmander
5
Charmeleon
6
Charizard
7
Squirtle
8
Wartortle
9
Blastoise
10
Caterpie
11
Metapod
12
Butterfree
13
Weedle
14
Kakuna
15
Beedrill
16
Pidgey
17
Pidgeotto
18
Pidgeot
19
Rattata
20
Raticate
21
Spearow
22
Fearow
23
Ekans
24
Arbok
25
Pikachu
26
Raichu
27
Sandshrew
28
Sandslash
29
Nidoran F
30
Nidorina
31
Nidoqueen
32
Nidoran M
33
Nidorino
34
Nidoking
35
Clefairy
36
Clefable
37
Vulpix
38
Ninetales
39
Jigglypuff
40
Wigglytuff
41
Zubat
42
Golbat
43
Oddish
44
Gloom
45
Vileplume
46
Paras
47
Parasect
48
Venonat
49
Venomoth
50
Diglett
51
Dugtrio
52
Meowth
53
Persian
54
Psyduck
55
Golduck
56
Mankey
57
Primeape
58
Growlithe
59
Arcanine
60
Poliwag
61
Poliwhirl
62
Poliwrath
63
Abra
64
Kadabra
65
Alakazam
66
Machop
67
Machoke
68
Machamp
69
Bellsprout
70
Weepinbell
71
Victreebel
72
Tentacool
73
Tentacruel
74
Geodude
75
Graveler
76
Golem
77
Ponyta
78
Rapidash
79
Slowpoke
80
Slowbro
81
Magnemite
82
Magneton
83
Farfetch'd
84
Doduo
85
Dodrio
86
Seel
87
Dewgong
88
Grimer
89
Muk
90
Shellder
91
Cloyster
92
Gastly
93
Haunter
94
Gengar
95
Onix
96
Drowzee
97
Hypno
98
Krabby
99
Kingler
100
Voltorb
101
Electrode
102
Exeggcute
103
Exeggutor
104
Cubone
105
Marowak
106
Hitmonlee
107
Hitmonchan
108
Lickitung
109
Koffing
110
Weezing
111
Rhyhorn
112
Rhydon
113
Chansey
114
Tangela
115
Kangaskhan
116
Horsea
117
Seadra
118
Goldeen
119
Seaking
120
Staryu
121
Starmie
122
Mr. Mime
123
Scyther
124
Jynx
125
Electabuzz
126
Magmar
127
Pinsir
128
Tauros
129
Magikarp
130
Gyarados
131
Lapras
132
Ditto
133
Eevee
134
Vaporeon
135
Jolteon
136
Flareon
137
Porygon
138
Omanyte
139
Omastar
140
Kabuto
141
Kabutops
142
Aerodactyl
143
Snorlax
144
Articuno
145
Zapdos
146
Moltres
147
Dratini
148
Dragonair
149
Dragonite
150
Mewtwo
151
Mew
152
Chikorita
153
Bayleef
154
Meganium
155
Cyndaquil
156
Quilava
157
Typhlosion
158
Totodile
159
Croconaw
160
Feraligatr
161
Sentret
162
Furret
163
Hoothoot
164
Noctowl
165
Ledyba
166
Ledian
167
Spinarak
168
Ariados
169
Crobat
170
Chinchou
171
Lanturn
172
Pichu
173
Cleffa
174
Igglybuff
175
Togepi
176
Togetic
177
Natu
178
Xatu
179
Mareep
180
Flaaffy
181
Ampharos
182
Bellossom
183
Marill
184
Azumarill
185
Sudowoodo
186
Politoed
187
Hoppip
188
Skiploom
189
Jumpluff
190
Aipom
191
Sunkern
192
Sunflora
193
Yanma
194
Wooper
195
Quagsire
196
Espeon
197
Umbreon
198
Murkrow
199
Slowking
200
Misdreavus
201
Unown
202
Wobbuffet
203
Girafarig
204
Pineco
205
Forretress
206
Dunsparce
207
Gligar
208
Steelix
209
Snubbull
210
Granbull
211
Qwilfish
212
Scizor
213
Shuckle
214
Heracross
215
Sneasel
216
Teddiursa
217
Ursaring
218
Slugma
219
Magcargo
220
Swinub
221
Piloswine
222
Corsola
223
Remoraid
224
Octillery
225
Delibird
226
Mantine
227
Skarmory
228
Houndour
229
Houndoom
230
Kingdra
231
Phanpy
232
Donphan
233
Porygon2
234
Stantler
235
Smeargle
236
Tyrogue
237
Hitmontop
238
Smoochum
239
Elekid
240
Magby
241
Miltank
242
Blissey
243
Raikou
244
Entei
245
Suicune
246
Larvitar
247
Pupitar
248
Tyranitar
249
Lugia
250
Ho-Oh
251
Celebi
252
Treecko
253
Grovyle
254
Sceptile
255
Torchic
256
Combusken
257
Blaziken
258
Mudkip
259
Marshtomp
260
Swampert
261
Poochyena
262
Mightyena
263
Zigzagoon
264
Linoone
265
Wurmple
266
Silcoon
267
Beautifly
268
Cascoon
269
Dustox
270
Lotad
271
Lombre
272
Ludicolo
273
Seedot
274
Nuzleaf
275
Shiftry
276
Taillow
277
Swellow
278
Wingull
279
Pelipper
280
Ralts
281
Kirlia
282
Gardevoir
283
Surskit
284
Masquerain
285
Shroomish
286
Breloom
287
Slakoth
288
Vigoroth
289
Slaking
290
Nincada
291
Ninjask
292
Shedinja
293
Whismur
294
Loudred
295
Exploud
296
Makuhita
297
Hariyama
298
Azurill
299
Nosepass
300
Skitty
301
Delcatty
302
Sableye
303
Mawile
304
Aron
305
Lairon
306
Aggron
307
Meditite
308
Medicham
309
Electrike
310
Manectric
311
Plusle
312
Minun
313
Volbeat
314
Illumise
315
Roselia
316
Gulpin
317
Swalot
318
Carvanha
319
Sharpedo
320
Wailmer
321
Wailord
322
Numel
323
Camerupt
324
Torkoal
325
Spoink
326
Grumpig
327
Spinda
328
Trapinch
329
Vibrava
330
Flygon
331
Cacnea
332
Cacturne
333
Swablu
334
Altaria
335
Zangoose
336
Seviper
337
Lunatone
338
Solrock
339
Barboach
340
Whiscash
341
Corphish
342
Crawdaunt
343
Baltoy
344
Claydol
345
Lileep
346
Cradily
347
Anorith
348
Armaldo
349
Feebas
350
Milotic
351
Castform
352
Kecleon
353
Shuppet
354
Banette
355
Duskull
356
Dusclops
357
Tropius
358
Chimecho
359
Absol
360
Wynaut
361
Snorunt
362
Glalie
363
Spheal
364
Sealeo
365
Walrein
366
Clamperl
367
Huntail
368
Gorebyss
369
Relicanth
370
Luvdisc
371
Bagon
372
Shelgon
373
Salamence
374
Beldum
375
Metang
376
Metagross
377
Regirock
378
Regice
379
Registeel
380
Latias
381
Latios
382
Kyogre
383
Groudon
384
Rayquaza
385
Jirachi
386
Deoxys Normal
387
Turtwig
388
Grotle
389
Torterra
390
Chimchar
391
Monferno
392
Infernape
393
Piplup
394
Prinplup
395
Empoleon
396
Starly
397
Staravia
398
Staraptor
399
Bidoof
400
Bibarel
401
Kricketot
402
Kricketune
403
Shinx
404
Luxio
405
Luxray
406
Budew
407
Roserade
408
Cranidos
409
Rampardos
410
Shieldon
411
Bastiodon
412
Burmy
413
Wormadam Plant
414
Mothim
415
Combee
416
Vespiquen
417
Pachirisu
418
Buizel
419
Floatzel
420
Cherubi
421
Cherrim
422
Shellos
423
Gastrodon
424
Ambipom
425
Drifloon
426
Drifblim
427
Buneary
428
Lopunny
429
Mismagius
430
Honchkrow
431
Glameow
432
Purugly
433
Chingling
434
Stunky
435
Skuntank
436
Bronzor
437
Bronzong
438
Bonsly
439
Mime Jr.
440
Happiny
441
Chatot
442
Spiritomb
443
Gible
444
Gabite
445
Garchomp
446
Munchlax
447
Riolu
448
Lucario
449
Hippopotas
450
Hippowdon
451
Skorupi
452
Drapion
453
Croagunk
454
Toxicroak
455
Carnivine
456
Finneon
457
Lumineon
458
Mantyke
459
Snover
460
Abomasnow
461
Weavile
462
Magnezone
463
Lickilicky
464
Rhyperior
465
Tangrowth
466
Electivire
467
Magmortar
468
Togekiss
469
Yanmega
470
Leafeon
471
Glaceon
472
Gliscor
473
Mamoswine
474
Porygon-Z
475
Gallade
476
Probopass
477
Dusknoir
478
Froslass
479
Rotom
480
Uxie
481
Mesprit
482
Azelf
483
Dialga
484
Palkia
485
Heatran
486
Regigigas
487
Giratina Altered
488
Cresselia
489
Phione
490
Manaphy
491
Darkrai
492
Shaymin Land
493
Arceus
494
Victini
495
Snivy
496
Servine
497
Serperior
498
Tepig
499
Pignite
500
Emboar
501
Oshawott
502
Dewott
503
Samurott
504
Patrat
505
Watchog
506
Lillipup
507
Herdier
508
Stoutland
509
Purrloin
510
Liepard
511
Pansage
512
Simisage
513
Pansear
514
Simisear
515
Panpour
516
Simipour
517
Munna
518
Musharna
519
Pidove
520
Tranquill
521
Unfezant
522
Blitzle
523
Zebstrika
524
Roggenrola
525
Boldore
526
Gigalith
527
Woobat
528
Swoobat
529
Drilbur
530
Excadrill
531
Audino
532
Timburr
533
Gurdurr
534
Conkeldurr
535
Tympole
536
Palpitoad
537
Seismitoad
538
Throh
539
Sawk
540
Sewaddle
541
Swadloon
542
Leavanny
543
Venipede
544
Whirlipede
545
Scolipede
546
Cottonee
547
Whimsicott
548
Petilil
549
Lilligant
550
Basculin Red Striped
551
Sandile
552
Krokorok
553
Krookodile
554
Darumaka
555
Darmanitan Standard
556
Maractus
557
Dwebble
558
Crustle
559
Scraggy
560
Scrafty
561
Sigilyph
562
Yamask
563
Cofagrigus
564
Tirtouga
565
Carracosta
566
Archen
567
Archeops
568
Trubbish
569
Garbodor
570
Zorua
571
Zoroark
572
Minccino
573
Cinccino
574
Gothita
575
Gothorita
576
Gothitelle
577
Solosis
578
Duosion
579
Reuniclus
580
Ducklett
581
Swanna
582
Vanillite
583
Vanillish
584
Vanilluxe
585
Deerling
586
Sawsbuck
587
Emolga
588
Karrablast
589
Escavalier
590
Foongus
591
Amoonguss
592
Frillish
593
Jellicent
594
Alomomola
595
Joltik
596
Galvantula
597
Ferroseed
598
Ferrothorn
599
Klink
600
Klang
601
Klinklang
602
Tynamo
603
Eelektrik
604
Eelektross
605
Elgyem
606
Beheeyem
607
Litwick
608
Lampent
609
Chandelure
610
Axew
611
Fraxure
612
Haxorus
613
Cubchoo
614
Beartic
615
Cryogonal
616
Shelmet
617
Accelgor
618
Stunfisk
619
Mienfoo
620
Mienshao
621
Druddigon
622
Golett
623
Golurk
624
Pawniard
625
Bisharp
626
Bouffalant
627
Rufflet
628
Braviary
629
Vullaby
630
Mandibuzz
631
Heatmor
632
Durant
633
Deino
634
Zweilous
635
Hydreigon
636
Larvesta
637
Volcarona
638
Cobalion
639
Terrakion
640
Virizion
641
Tornadus Incarnate
642
Thundurus Incarnate
643
Reshiram
644
Zekrom
645
Landorus Incarnate
646
Kyurem
647
Keldeo Ordinary
648
Meloetta Aria
649
Genesect
650
Chespin
651
Quilladin
652
Chesnaught
653
Fennekin
654
Braixen
655
Delphox
656
Froakie
657
Frogadier
658
Greninja
659
Bunnelby
660
Diggersby
661
Fletchling
662
Fletchinder
663
Talonflame
664
Scatterbug
665
Spewpa
666
Vivillon
667
Litleo
668
Pyroar
669
Flabebe
670
Floette
671
Florges
672
Skiddo
673
Gogoat
674
Pancham
675
Pangoro
676
Furfrou
677
Espurr
678
Meowstic Male
679
Honedge
680
Doublade
681
Aegislash Shield
682
Spritzee
683
Aromatisse
684
Swirlix
685
Slurpuff
686
Inkay
687
Malamar
688
Binacle
689
Barbaracle
690
Skrelp
691
Dragalge
692
Clauncher
693
Clawitzer
694
Helioptile
695
Heliolisk
696
Tyrunt
697
Tyrantrum
698
Amaura
699
Aurorus
700
Sylveon
701
Hawlucha
702
Dedenne
703
Carbink
704
Goomy
705
Sliggoo
706
Goodra
707
Klefki
708
Phantump
709
Trevenant
710
Pumpkaboo Average
711
Gourgeist Average
712
Bergmite
713
Avalugg
714
Noibat
715
Noivern
716
Xerneas
717
Yveltal
718
Zygarde 50%
719
Diancie
720
Hoopa
721
Volcanion
722
Rowlet
723
Dartrix
724
Decidueye
725
Litten
726
Torracat
727
Incineroar
728
Popplio
729
Brionne
730
Primarina
731
Pikipek
732
Trumbeak
733
Toucannon
734
Yungoos
735
Gumshoos
736
Grubbin
737
Charjabug
738
Vikavolt
739
Crabrawler
740
Crabominable
741
Oricorio Baile
742
Cutiefly
743
Ribombee
744
Rockruff
745
Lycanroc Midday
746
Wishiwashi Solo
747
Mareanie
748
Toxapex
749
Mudbray
750
Mudsdale
751
Dewpider
752
Araquanid
753
Fomantis
754
Lurantis
755
Morelull
756
Shiinotic
757
Salandit
758
Salazzle
759
Stufful
760
Bewear
761
Bounsweet
762
Steenee
763
Tsareena
764
Comfey
765
Oranguru
766
Passimian
767
Wimpod
768
Golisopod
769
Sandygast
770
Palossand
771
Pyukumuku
772
Type: Null
773
Silvally
774
Minior Red Meteor
775
Komala
776
Turtonator
777
Togedemaru
778
Mimikyu Disguised
779
Bruxish
780
Drampa
781
Dhelmise
782
Jangmo-O
783
Hakamo-O
784
Kommo-O
785
Tapu Koko
786
Tapu Lele
787
Tapu Bulu
788
Tapu Fini
789
Cosmog
790
Cosmoem
791
Solgaleo
792
Lunala
793
Nihilego
794
Buzzwole
795
Pheromosa
796
Xurkitree
797
Celesteela
798
Kartana
799
Guzzlord
800
Necrozma
801
Magearna
802
Marshadow
803
Poipole
804
Naganadel
805
Stakataka
806
Blacephalon
807
Zeraora
808
Meltan
809
Melmetal
810
Grookey
811
Thwackey
812
Rillaboom
813
Scorbunny
814
Raboot
815
Cinderace
816
Sobble
817
Drizzile
818
Inteleon
819
Skwovet
820
Greedent
821
Rookidee
822
Corvisquire
823
Corviknight
824
Blipbug
825
Dottler
826
Orbeetle
827
Nickit
828
Thievul
829
Gossifleur
830
Eldegoss
831
Wooloo
832
Dubwool
833
Chewtle
834
Drednaw
835
Yamper
836
Boltund
837
Rolycoly
838
Carkol
839
Coalossal
840
Applin
841
Flapple
842
Appletun
843
Silicobra
844
Sandaconda
845
Cramorant
846
Arrokuda
847
Barraskewda
848
Toxel
849
Toxtricity Amped
850
Sizzlipede
851
Centiskorch
852
Clobbopus
853
Grapploct
854
Sinistea
855
Polteageist
856
Hatenna
857
Hattrem
858
Hatterene
859
Impidimp
860
Morgrem
861
Grimmsnarl
862
Obstagoon
863
Perrserker
864
Cursola
865
Sirfetch'd
866
Mr. Rime
867
Runerigus
868
Milcery
869
Alcremie
870
Falinks
871
Pincurchin
872
Snom
873
Frosmoth
874
Stonjourner
875
Eiscue Ice
876
Indeedee Male
877
Morpeko Full Belly
878
Cufant
879
Copperajah
880
Dracozolt
881
Arctozolt
882
Dracovish
883
Arctovish
884
Duraludon
885
Dreepy
886
Drakloak
887
Dragapult
888
Zacian
889
Zamazenta
890
Eternatus
891
Kubfu
892
Urshifu Single Strike
893
Zarude
894
Regieleki
895
Regidrago
896
Glastrier
897
Spectrier
898
Calyrex
899
Wyrdeer
900
Kleavor
901
Ursaluna
902
Basculegion Male
903
Sneasler
904
Overqwil
905
Enamorus Incarnate
906
Sprigatito
907
Floragato
908
Meowscarada
909
Fuecoco
910
Crocalor
911
Skeledirge
912
Quaxly
913
Quaxwell
914
Quaquaval
915
Lechonk
916
Oinkologne
917
Tarountula
918
Spidops
919
Nymble
920
Lokix
921
Pawmi
922
Pawmo
923
Pawmot
924
Tandemaus
925
Maushold
926
Fidough
927
Dachsbun
928
Smoliv
929
Dolliv
930
Arboliva
931
Squawkabilly
932
Nacli
933
Naclstack
934
Garganacl
935
Charcadet
936
Armarouge
937
Ceruledge
938
Tadbulb
939
Bellibolt
940
Wattrel
941
Kilowattrel
942
Maschiff
943
Mabosstiff
944
Shroodle
945
Grafaiai
946
Bramblin
947
Brambleghast
948
Toedscool
949
Toedscruel
950
Klawf
951
Capsakid
952
Scovillain
953
Rellor
954
Rabsca
955
Flittle
956
Espathra
957
Tinkatink
958
Tinkatuff
959
Tinkaton
960
Wiglett
961
Wugtrio
962
Bombirdier
963
Finizen
964
Palafin
965
Varoom
966
Revavroom
967
Cyclizar
968
Orthworm
969
Glimmet
970
Glimmora
971
Greavard
972
Houndstone
973
Flamigo
974
Cetoddle
975
Cetitan
976
Veluza
977
Dondozo
978
Tatsugiri
979
Annihilape
980
Clodsire
981
Farigiraf
982
Dudunsparce
983
Kingambit
984
Great Tusk
985
Scream Tail
986
Brute Bonnet
987
Flutter Mane
988
Slither Wing
989
Sandy Shocks
990
Iron Treads
991
Iron Bundle
992
Iron Hands
993
Iron Jugulis
994
Iron Moth
995
Iron Thorns
996
Frigibax
997
Arctibax
998
Baxcalibur
999
Gimmighoul
1000
Gholdengo
1001
Wo-Chien
1002
Chien-Pao
1003
Ting-Lu
1004
Chi-Yu
1005
Roaring Moon
1006
Iron Valiant
1007
Koraidon
1008
Miraidon
1009
Walking Wake
1010
Iron Leaves
1011
Dipplin
1012
Poltchageist
1013
Sinistcha
1014
Okidogi
1015
Munkidori
1016
Fezandipiti
1017
Ogerpon
1018
Archaludon
1019
Hydrapple
1020
Gouging Fire
1021
Raging Bolt
1022
Iron Boulder
1023
Iron Crown
1024
Terapagos
1025
Pecharunt
10001
Deoxys Attack
10002
Deoxys Defense
10003
Deoxys Speed
10004
Wormadam Sandy
10005
Wormadam Trash
10006
Shaymin Sky
10007
Giratina Origin
10008
Rotom Heat
10009
Rotom Wash
10010
Rotom Frost
10011
Rotom Fan
10012
Rotom Mow
10013
Castform Sunny
10014
Castform Rainy
10015
Castform Snowy
10016
Basculin Blue Striped
10017
Darmanitan Zen
10018
Meloetta Pirouette
10019
Tornadus Therian
10020
Thundurus Therian
10021
Landorus Therian
10022
Kyurem Black
10023
Kyurem White
10024
Keldeo Resolute
10025
Meowstic Female
10026
Aegislash Blade
10027
Pumpkaboo Small
10028
Pumpkaboo Large
10029
Pumpkaboo Super
10030
Gourgeist Small
10031
Gourgeist Large
10032
Gourgeist Super
10033
Venusaur Mega
10034
Charizard Mega X
10035
Charizard Mega Y
10036
Blastoise Mega
10037
Alakazam Mega
10038
Gengar Mega
10039
Kangaskhan Mega
10040
Pinsir Mega
10041
Gyarados Mega
10042
Aerodactyl Mega
10043
Mewtwo Mega X
10044
Mewtwo Mega Y
10045
Ampharos Mega
10046
Scizor Mega
10047
Heracross Mega
10048
Houndoom Mega
10049
Tyranitar Mega
10050
Blaziken Mega
10051
Gardevoir Mega
10052
Mawile Mega
10053
Aggron Mega
10054
Medicham Mega
10055
Manectric Mega
10056
Banette Mega
10057
Absol Mega
10058
Garchomp Mega
10059
Lucario Mega
10060
Abomasnow Mega
10061
Floette Eternal
10062
Latias Mega
10063
Latios Mega
10064
Swampert Mega
10065
Sceptile Mega
10066
Sableye Mega
10067
Altaria Mega
10068
Gallade Mega
10069
Audino Mega
10070
Sharpedo Mega
10071
Slowbro Mega
10072
Steelix Mega
10073
Pidgeot Mega
10074
Glalie Mega
10075
Diancie Mega
10076
Metagross Mega
10077
Kyogre Primal
10078
Groudon Primal
10079
Rayquaza Mega
10080
Pikachu Rock Star
10081
Pikachu Belle
10082
Pikachu Pop Star
10083
Pikachu Phd
10084
Pikachu Libre
10085
Pikachu Cosplay
10086
Hoopa Unbound
10087
Camerupt Mega
10088
Lopunny Mega
10089
Salamence Mega
10090
Beedrill Mega
10091
Rattata Alola
10092
Raticate Alola
10093
Raticate Totem Alola
10094
Pikachu Original Cap
10095
Pikachu Hoenn Cap
10096
Pikachu Sinnoh Cap
10097
Pikachu Unova Cap
10098
Pikachu Kalos Cap
10099
Pikachu Alola Cap
10100
Raichu Alola
10101
Sandshrew Alola
10102
Sandslash Alola
10103
Vulpix Alola
10104
Ninetales Alola
10105
Diglett Alola
10106
Dugtrio Alola
10107
Meowth Alola
10108
Persian Alola
10109
Geodude Alola
10110
Graveler Alola
10111
Golem Alola
10112
Grimer Alola
10113
Muk Alola
10114
Exeggutor Alola
10115
Marowak Alola
10116
Greninja Battle Bond
10117
Greninja Ash
10118
Zygarde 10 Power Construct
10119
Zygarde 50 Power Construct
10120
Zygarde Complete
10121
Gumshoos Totem
10122
Vikavolt Totem
10123
Oricorio Pom-Pom
10124
Oricorio Pa'u
10125
Oricorio Sensu
10126
Lycanroc Midnight
10127
Wishiwashi School
10128
Lurantis Totem
10129
Salazzle Totem
10130
Minior Orange Meteor
10131
Minior Yellow Meteor
10132
Minior Green Meteor
10133
Minior Blue Meteor
10134
Minior Indigo Meteor
10135
Minior Violet Meteor
10136
Minior Red
10137
Minior Orange
10138
Minior Yellow
10139
Minior Green
10140
Minior Blue
10141
Minior Indigo
10142
Minior Violet
10143
Mimikyu Busted
10144
Mimikyu Totem Disguised
10145
Mimikyu Totem Busted
10146
Kommo O Totem
10147
Magearna Original
10148
Pikachu Partner Cap
10149
Marowak Totem
10150
Ribombee Totem
10151
Rockruff Own Tempo
10152
Lycanroc Dusk
10153
Araquanid Totem
10154
Togedemaru Totem
10155
Necrozma Dusk
10156
Necrozma Dawn
10157
Necrozma Ultra
10158
Pikachu Starter
10159
Eevee Starter
10160
Pikachu World Cap
10161
Meowth Galar
10162
Ponyta Galar
10163
Rapidash Galar
10164
Slowpoke Galar
10165
Slowbro Galar
10166
Farfetch'd Galar
10167
Weezing Galar
10168
Mr. Mime Galar
10169
Articuno Galar
10170
Zapdos Galar
10171
Moltres Galar
10172
Slowking Galar
10173
Corsola Galar
10174
Zigzagoon Galar
10175
Linoone Galar
10176
Darumaka Galar
10177
Darmanitan Galar Standard
10178
Darmanitan Galar Zen
10179
Yamask Galar
10180
Stunfisk Galar
10181
Zygarde 10%
10182
Cramorant Gulping
10183
Cramorant Gorging
10184
Toxtricity Low Key
10185
Eiscue Noice
10186
Indeedee Female
10187
Morpeko Hangry
10188
Zacian Crowned
10189
Zamazenta Crowned
10190
Eternatus Eternamax
10191
Urshifu Rapid Strike
10192
Zarude Dada
10193
Calyrex Ice
10194
Calyrex Shadow
10195
Venusaur Gmax
10196
Charizard Gmax
10197
Blastoise Gmax
10198
Butterfree Gmax
10199
Pikachu Gmax
10200
Meowth Gmax
10201
Machamp Gmax
10202
Gengar Gmax
10203
Kingler Gmax
10204
Lapras Gmax
10205
Eevee Gmax
10206
Snorlax Gmax
10207
Garbodor Gmax
10208
Melmetal Gmax
10209
Rillaboom Gmax
10210
Cinderace Gmax
10211
Inteleon Gmax
10212
Corviknight Gmax
10213
Orbeetle Gmax
10214
Drednaw Gmax
10215
Coalossal Gmax
10216
Flapple Gmax
10217
Appletun Gmax
10218
Sandaconda Gmax
10219
Toxtricity Amped Gmax
10220
Centiskorch Gmax
10221
Hatterene Gmax
10222
Grimmsnarl Gmax
10223
Alcremie Gmax
10224
Copperajah Gmax
10225
Duraludon Gmax
10226
Urshifu Single Strike Gmax
10227
Urshifu Rapid Strike Gmax
10228
Toxtricity Low Key Gmax
10229
Growlithe Hisui
10230
Arcanine Hisui
10231
Voltorb Hisui
10232
Electrode Hisui
10233
Typhlosion Hisui
10234
Qwilfish Hisui
10235
Sneasel Hisui
10236
Samurott Hisui
10237
Lilligant Hisui
10238
Zorua Hisui
10239
Zoroark Hisui
10240
Braviary Hisui
10241
Sliggoo Hisui
10242
Goodra Hisui
10243
Avalugg Hisui
10244
Decidueye Hisui
10245
Dialga Origin
10246
Palkia Origin
10247
Basculin White Striped
10248
Basculegion Female
10249
Enamorus Therian
10250
Tauros Paldea Combat Breed
10251
Tauros Paldea Blaze Breed
10252
Tauros Paldea Aqua Breed
10253
Wooper Paldea
10254
Oinkologne Female
10255
Dudunsparce Three Segment
10256
Palafin Hero
10257
Maushold Family Of Three
10258
Tatsugiri Droopy
10259
Tatsugiri Stretchy
10260
Squawkabilly Blue Plumage
10261
Squawkabilly Yellow Plumage
10262
Squawkabilly White Plumage
10263
Gimmighoul Roaming
10264
Koraidon Limited Build
10265
Koraidon Sprinting Build
10266
Koraidon Swimming Build
10267
Koraidon Gliding Build
10268
Miraidon Low Power Mode
10269
Miraidon Drive Mode
10270
Miraidon Aquatic Mode
10271
Miraidon Glide Mode
10272
Ursaluna Bloodmoon
10273
Ogerpon Wellspring Mask
10274
Ogerpon Hearthflame Mask
10275
Ogerpon Cornerstone Mask
10276
Terapagos Terastal
10277
Terapagos Stellar
"""
lines = s.splitlines()
basename = ['']
formname = ['']

for i in range(len(lines) // 2):
    if(int(lines[2*i]) > 10000):
        formname.append(lines[2*i+1])
    else:
        basename.append(lines[2*i+1])

f = open("temp.txt", "w")
f.write("const basename = " + str(basename))
f.write("const formname = " + str(formname))
f.close()