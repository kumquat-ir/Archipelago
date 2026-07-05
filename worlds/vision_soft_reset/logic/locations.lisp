(location-list
 (location "Decryptor: Charge Shot"     100
           :region "Ship")
 (location "Decryptor: Charge Magnet"   101
           :region "Ship"
           :condition charge-wall)
 (location "Decryptor: Altered Shot"    102
           :region "Above First Puzzle")
 (location "Decryptor: Charge Grip"     103
           :region "Power Area")
 (location "Decryptor: Wall Run"        104
           :region "Wall Run Area")
 (location "Decryptor: Spin Dodge"      105
           :region "Spin Dodge Area")
 (location "Decryptor: Heat Resist"     106
           :region "Mountain Chamber"
           :condition (and any-vertical
                           ;; charge wall here is 1.5 minute obsidian vines
                           ;; these paths are the only ones fast enough to get there in time
                           charge-wall
                           (or (entrance? "Above First Puzzle" "Mountain Chamber")
                               (and (entrance? "Ship" "Mountain Water Run")
                                    (entrance? "Mountain Water Run" "Mountain Chamber")))))
 (location "Decryptor: Mental Recovery" 107
           :region "Lower Floatlands")
 (location "Decryptor: Energy Claw"     108
           :region "Griger"
           :condition any-vertical)
 (location "Decryptor: Strip Suit"      109
           :region "Warehouse"
           :condition (and both-vertical
                           virus))
 (location "Decryptor: Shell Escape"    110
           :region "Underwater"
           :condition larva-mode)
 (location "Decryptor: Speed Boost"     111
           :region "Solatia Run")
 (location "Decryptor: Vile Claw"       112
           :region "Hot Water Area"
           :condition nonboostable-claw-wall)
 (location "Decryptor: Piercing Speed"  113
           :region "Upper Mountain"
           :condition (and both-vertical
                           (or (items "Speed Boost")
                               (items "Spin Double"
                                      "Twister Jump"))))
 (location "Decryptor: Golden View"     114
           :region "Power Area"
           :condition power-on)
 (location "Decryptor: d#Z 5~qn. P"     115
           :region "Orb C")
 (location "Decryptor: Virus Wipe"      116
           :region "Warehouse"
           :condition (and both-vertical
                           virus))
 (location "Decryptor: Double Shot"     117
           :region "Mountain Water Run"
           :condition (items "Speed Boost"))
 (location "Card 01: Magoom"     201
           :region "Power Area"
           :condition power-on)
 (location "Card 02: Ciurivy"    202
           :region "Ship")
 (location "Card 03: Smosey"     203
           :region "Past First Puzzle"
           :condition (and both-vertical
                           (or (option 'HardLogic true)
                               (items "Charge Shot"))))
 (location "Card 04: Wavemoth"   204
           :region "Griger's Base (Right)"
           :condition any-vertical)
 (location "Card 05: Midow"      205
           :region "Past First Puzzle")
 (location "Card 06: Prittle"    206
           :region "First Puzzle Solution")
 (location "Card 07: Sealime"    207
           :region "Ship"
           :condition (or boost-climb
                          (and spin-double
                               (items "Wall Run"))))
 (location "Card 08: Toucade"    208
           :region "Past First Puzzle" ; requires getting here without solving the puzzle
           :condition both-vertical)
 (location "Card 09: Shaifi"     209
           :region "Beach")
 (location "Card 10: Pengrunt"   210
           :region "Griger's Base (Powerless Room)")
 (location "Card 11: Cottospark" 211
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical))
 (location "Card 12: Cottocache" 212
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical))
 (location "Card 13: Drilbas"    213
           :region "Left of Ship"
           :condition both-vertical)
 (location "Card 14: Jinvell"    214
           :region "Beach"
           :condition (items "Speed Boost"
                             "Wall Run"
                             "Spin Dodge"))
 (location "Card 15: Royalrose"  215
           :region "Upper Floatlands")
 (location "Card 16: Rupo"       216
           :region "Orb B"
           :condition boost-climb)
 (location "Card 17: Froesburn"  217
           :region "Mountain Fall"
           :condition larva-mode)
 (location "Card 18: Ghostily"   218
           :region "Underwater"
           :condition larva-mode)
 (location "Card 19: Sherivice"  219
           :region "Right Floatlands")
 (location "Card 20: Griger"     220
           :region "Griger"
           :condition (and any-vertical
                           (items "Energy Claw")))
 (location "Card 21: Solatia"    221
           :region "Solatia")
 (location "Card 22: Salesman"   222
           :region "Upper Mountain"
           :condition (and (region? "Ship") ; ship, first puzzle
                           (region? "First Puzzle Solution")
                           (region? "Past First Puzzle")
                           (region? "Endoplanetary Shield")
                           (region? "Power Area")
                           (region? "Griger's Base (Top)")
                           (region? "Underwater")
                           (region? "Orb A")
                           (region? "Claw Bounce Area")
                           (region? "Floatlands Entry")
                           (region? "Solatia Run")
                           (region? "Mountain Chamber")
                           (region? "Mountain Fall")
                           (region? "Warehouse")
                           can-escape-warehouse
                           (region? "Mountaintop")))
 (location "Card 23: Oracle"     223
           :region "Orb D")
 (location "Card 24: Oracle-L"   224
           :region "Ship"
           :condition larva-mode)
 (event "Defeat Salesman" "Victory"
        :region "Mountaintop"))
;; ambush clears?
;; physical item finds? (not necessarily shuffling them)
