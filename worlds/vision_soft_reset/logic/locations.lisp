(location-list
 (location "Decryptor: Charge Shot"     100
           :region "Ship"
           :decryptor-id "CHARGE_SHOT")
 (location "Decryptor: Charge Magnet"   101
           :region "Ship"
           :condition charge-wall
           :decryptor-id "CHARGE_MAGNET")
 (location "Decryptor: Altered Shot"    102
           :region "Above First Puzzle"
           :decryptor-id "ALTERED_SHOT")
 (location "Decryptor: Charge Grip"     103
           :region "Power Area"
           :decryptor-id "CHARGE_GRIP")
 (location "Decryptor: Wall Run"        104
           :region "Wall Run Area"
           :decryptor-id "WALL_RUN")
 (location "Decryptor: Spin Dodge"      105
           :region "Spin Dodge Area"
           :decryptor-id "SPIN_DODGE")
 (location "Decryptor: Heat Resist"     106
           :region "Mountain Chamber"
           :condition (and any-vertical
                           ;; charge wall here is 1.5 minute obsidian vines
                           ;; these paths are the only ones fast enough to get there in time
                           charge-wall
                           (or (entrance? "Above First Puzzle" "Mountain Chamber")
                               (and (entrance? "Ship" "Mountain Water Run")
                                    (entrance? "Mountain Water Run" "Mountain Chamber"))))
           :decryptor-id "HEAT_RESIST")
 (location "Decryptor: Mental Recovery" 107
           :region "Lower Floatlands"
           :decryptor-id "MENTAL_RECOVERY")
 (location "Decryptor: Energy Claw"     108
           :region "Griger"
           :condition (and any-vertical
                           (or (option 'RequireBossCards false)
                               (items "Card: Griger")))
           :decryptor-id "ENERGY_CLAW")
 (location "Decryptor: Strip Suit"      109
           :region "Warehouse"
           :condition (and both-vertical
                           virus)
           :decryptor-id "STRIP_SUIT")
 (location "Decryptor: Shell Escape"    110
           :region "Underwater"
           :condition larva-mode
           :decryptor-id "NO_OBJECTIONS")
 (location "Decryptor: Speed Boost"     111
           :region "Solatia Run"
           :decryptor-id "SPEED_BOOST")
 (location "Decryptor: Vile Claw"       112
           :region "Hot Water Area"
           :condition nonboostable-claw-wall
           :decryptor-id "CLAW_BREAKS_CHARGE_SHOT")
 (location "Decryptor: Piercing Speed"  113
           :region "Upper Mountain"
           :condition (and both-vertical
                           (or (items "Speed Boost")
                               (items "Spin Double"
                                      "Twister Jump")))
           :decryptor-id "SPEED_BOOST_BREAKS_CLAW")
 (location "Decryptor: Golden View"     114
           :region "Power Area"
           :condition power-on
           :decryptor-id "SHOW_IMPORTANT")
 (location "Decryptor: d#Z 5~qn. P"     115
           :region "Orb C"
           :decryptor-id "VIRUS")
 (location "Decryptor: Virus Wipe"      116
           :region "Warehouse"
           :condition (and both-vertical
                           virus)
           :decryptor-id "VIRUS_WIPE")
 (location "Decryptor: Double Shot"     117
           :region "Mountain Water Run"
           :condition (items "Speed Boost")
           :decryptor-id "DOUBLE_SHOT")
 (location "Card 01: Magoom"     201
           :region "Power Area"
           :condition power-on
           :card-id 1)
 (location "Card 02: Ciurivy"    202
           :region "Ship"
           :card-id 2)
 (location "Card 03: Smosey"     203
           :region "Past First Puzzle"
           :condition (and both-vertical
                           (or (option 'HardLogic true)
                               (items "Charge Shot")))
           :card-id 3)
 (location "Card 04: Wavemoth"   204
           :region "Griger's Base (Right)"
           :condition any-vertical
           :card-id 4)
 (location "Card 05: Midow"      205
           :region "Past First Puzzle"
           :card-id 5)
 (location "Card 06: Prittle"    206
           :region "First Puzzle Solution"
           :card-id 6)
 (location "Card 07: Sealime"    207
           :region "Ship"
           :condition (or boost-climb
                          (and spin-double
                               (items "Wall Run")))
           :card-id 7)
 (location "Card 08: Toucade"    208
           :region "Past First Puzzle" ; requires getting here without solving the puzzle
           :condition both-vertical
           :card-id 8)
 (location "Card 09: Shaifi"     209
           :region "Beach"
           :card-id 9)
 (location "Card 10: Pengrunt"   210
           :region "Griger's Base (Powerless Room)"
           :card-id 10)
 (location "Card 11: Cottospark" 211
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical)
           :card-id 12)
 (location "Card 12: Cottocache" 212
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical)
           :card-id 13)
 (location "Card 13: Drilbas"    213
           :region "Left of Ship"
           :condition both-vertical
           :card-id 14)
 (location "Card 14: Jinvell"    214
           :region "Beach"
           :condition (items "Speed Boost"
                             "Wall Run"
                             "Spin Dodge")
           :card-id 15)
 (location "Card 15: Royalrose"  215
           :region "Upper Floatlands"
           :card-id 16)
 (location "Card 16: Rupo"       216
           :region "Orb B"
           :condition boost-climb
           :card-id 17)
 (location "Card 17: Froesburn"  217
           :region "Mountain Fall"
           :condition larva-mode
           :card-id 18)
 (location "Card 18: Ghostily"   218
           :region "Underwater"
           :condition larva-mode
           :card-id 19)
 (location "Card 19: Sherivice"  219
           :region "Right Floatlands"
           :card-id 20)
 (location "Card 20: Griger"     220
           :region "Griger"
           :condition (and any-vertical
                           (items "Energy Claw")
                           (or (option 'RequireBossCards false)
                               (items "Card: Griger")))
           :card-id 21)
 (location "Card 21: Solatia"    221
           :region "Solatia"
           :card-id 22)
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
                           (region? "Mountaintop"))
           :card-id 23)
 (location "Card 23: Oracle"     223
           :region "Orb D"
           :card-id 24)
 (location "Card 24: Oracle-L"   224
           :region "Ship"
           :condition larva-mode
           :card-id 25)
 (location "First Ambush" 300
           :region "Ship"
           :include-option "add_ambushes"
           :ambush-coords '(15 21))
 (location "Ambush Before Charge Shot" 301
           :region "Ship"
           :include-option "add_ambushes"
           :ambush-coords '(21 20))
 (location "Power Area Lower Ambush" 302
           :region "Power Area"
           :include-option "add_ambushes"
           :ambush-coords '(10 16))
 (location "Power Area Upper Ambush" 303
           :region "Under Beach"
           :include-option "add_ambushes"
           :ambush-coords '(6 18))
 (location "Pre-Spin Dodge Ambush" 304
           :region "Pre-Spin Dodge"
           :include-option "add_ambushes"
           :ambush-coords '(24 14))
 (location "Cottospark Ambush" 305
           :region "Griger's Base (Right)"
           :condition here-be-cottosparks
           :include-option "add_ambushes"
           :ambush-coords '(17 14))
 (location "Block Puzzle Ambush" 306
           :region "Griger's Base (Bottom Left)"
           :condition here-be-cottosparks
           :include-option "add_ambushes"
           :ambush-coords '(14 11))
 (location "Underwater Ambush" 307
           :region "Underwater"
           :include-option "add_ambushes"
           :ambush-coords '(5 8))
 (location "Claw Bounce Ambush" 308
           :region "Claw Bounce Area"
           :condition here-be-cottosparks
           :include-option "add_ambushes"
           :ambush-coords '(12 9))
 (location "Floatlands Ambush" 309
           :region "Floatlands Ambush"
           :include-option "add_ambushes"
           :ambush-coords '(12 27))
 (location "First Health Upgrade" 400
           :region "Ship"
           :include-option "add_physical"
           :health-upgrade-id "HU0")
 (location "Pre-Spin Dodge Health Upgrade" 401
           :region "Pre-Spin Dodge"
           :include-option "add_physical"
           :health-upgrade-id "HU1")
 (location "Floatlands Health Upgrade" 402
           :region "Upper Floatlands"
           :include-option "add_physical"
           :health-upgrade-id "HU2")
 (location "Warehouse Entry Health Upgrade" 403
           :region "Warehouse"
           :include-option "add_physical"
           :health-upgrade-id "HU3")
 (location "Phase Upgrade Left of Ship" 404
           :region "Left of Ship"
           :include-option "add_physical"
           :phase-upgrade-id "PU0")
 (location "Phase Upgrade Outside Griger's Base" 405
           :region "Griger's Base (Left)"
           :include-option "add_physical"
           :phase-upgrade-id "PU1")
 (location "Lower Mountain Phase Upgrade" 406
           :region "Mountain Fall"
           :include-option "add_physical"
           :phase-upgrade-id "PU2")
 (location "Upper Mountain Phase Upgrade" 407
           :region "Upper Mountain"
           :include-option "add_physical"
           :phase-upgrade-id "PU3")
 (location "Orb A" 408
           :region "Orb A"
           :condition (or (items "Spin Dodge")
                          boost-climb)
           :include-option "add_physical"
           :orb-id "ORB0")
 (location "Orb B" 409
           :region "Orb B"
           :condition (or (items "Spin Dodge")
                          (entrance? "Upper Floatlands" "Orb B")
                          boost-climb)
           :include-option "add_physical"
           :orb-id "ORB1")
 (location "Orb C" 410
           :region "Orb C"
           :condition (or (items "Wall Run")
                          spin-double
                          twister-jump)
           :include-option "add_physical"
           :orb-id "ORB2")
 (location "Orb D" 411
           :region "Orb D"
           :include-option "add_physical"
           :orb-id "ORB3")
 (event "Defeat Salesman" "Victory"
        :region "Mountaintop"
        :condition (or (option 'RequireBossCards false)
                       (items "Card: Salesman"))))
;; ambush clears?
;; physical item finds? (not necessarily shuffling them)
