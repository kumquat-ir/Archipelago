(location-list
 (location "Decryptor: Charge Shot"     100
           :region "Ship"
           :decryptor-id "CHARGE_SHOT"
           :coords '(22 19))
 (location "Decryptor: Charge Magnet"   101
           :region "Ship"
           :condition charge-wall
           :decryptor-id "CHARGE_MAGNET"
           :coords '(16 20))
 (location "Decryptor: Altered Shot"    102
           :region "Above First Puzzle"
           :decryptor-id "ALTERED_SHOT"
           :coords '(18 21))
 (location "Decryptor: Charge Grip"     103
           :region "Power Area"
           :decryptor-id "CHARGE_GRIP"
           :coords '(10 17))
 (location "Decryptor: Wall Run"        104
           :region "Wall Run Area"
           :decryptor-id "WALL_RUN"
           :coords '(18 9))
 (location "Decryptor: Spin Dodge"      105
           :region "Spin Dodge Area"
           :decryptor-id "SPIN_DODGE"
           :coords '(26 13))
 (location "Decryptor: Heat Resist"     106
           :region "Mountain Chamber"
           :condition (and any-vertical
                           ;; charge wall here is 1.5 minute obsidian vines
                           ;; these paths are the only ones fast enough to get there in time
                           charge-wall
                           (or (entrance? "Above First Puzzle" "Mountain Chamber")
                               (and (entrance? "Ship" "Mountain Water Run")
                                    (entrance? "Mountain Water Run" "Mountain Chamber"))))
           :decryptor-id "HEAT_RESIST"
           :coords '(23 24))
 (location "Decryptor: Mental Recovery" 107
           :region "Lower Floatlands"
           :decryptor-id "MENTAL_RECOVERY"
           :coords '(12 25))
 (location "Decryptor: Energy Claw"     108
           :region "Griger"
           :condition (and any-vertical
                           (or (option 'RequireBossCards false)
                               (items "Card: Griger")))
           :decryptor-id "ENERGY_CLAW"
           :tracker-group "Griger Fight"
           :coords '(14 18))
 (location "Decryptor: Strip Suit"      109
           :region "Warehouse"
           :condition (and both-vertical
                           virus)
           :decryptor-id "STRIP_SUIT"
           :tracker-group "Post-Glitch Fight"
           :coords '(32 10))
 (location "Decryptor: Shell Escape"    110
           :region "Underwater"
           :condition larva-mode
           :decryptor-id "NO_OBJECTIONS"
           :tracker-group "Ghostily Chase"
           :coords '(2 11))
 (location "Decryptor: Speed Boost"     111
           :region "Solatia Run"
           :decryptor-id "SPEED_BOOST"
           :coords '(15 27))
 (location "Decryptor: Vile Claw"       112
           :region "Hot Water Area"
           :condition nonboostable-claw-wall
           :decryptor-id "CLAW_BREAKS_CHARGE_SHOT"
           :coords '(30 3))
 (location "Decryptor: Piercing Speed"  113
           :region "Upper Mountain"
           :condition (and both-vertical
                           (or (items "Speed Boost")
                               (items "Spin Double"
                                      "Twister Jump")))
           :decryptor-id "SPEED_BOOST_BREAKS_CLAW"
           :coords '(29 30))
 (location "Decryptor: Golden View"     114
           :region "Power Area"
           :condition power-on
           :decryptor-id "SHOW_IMPORTANT"
           :coords '(7 18))
 (location "Decryptor: d#Z 5~qn. P"     115
           :region "Orb C"
           :decryptor-id "VIRUS"
           :coords '(28 22))
 (location "Decryptor: Virus Wipe"      116
           :region "Warehouse"
           :condition (and both-vertical
                           virus)
           :decryptor-id "VIRUS_WIPE"
           :tracker-group "Post-Glitch Fight")
 (location "Decryptor: Double Shot"     117
           :region "Mountain Water Run"
           :condition (items "Speed Boost")
           :decryptor-id "DOUBLE_SHOT"
           :coords '(22 21))
 (location "Card 01: Magoom"     201
           :region "Power Area"
           :condition power-on
           :card-id 1
           :coords '(9 17))
 (location "Card 02: Ciurivy"    202
           :region "Ship"
           :card-id 2
           :coords '(13 22))
 (location "Card 03: Smosey"     203
           :region "Past First Puzzle"
           :condition (and both-vertical
                           (or (option 'HardLogic true)
                               (items "Charge Shot")))
           :card-id 3
           :coords '(21 17))
 (location "Card 04: Wavemoth"   204
           :region "Griger's Base (Right)"
           :condition any-vertical
           :card-id 4
           :coords '(16 16))
 (location "Card 05: Midow"      205
           :region "Past First Puzzle"
           :card-id 5
           :coords '(20 16))
 (location "Card 06: Prittle"    206
           :region "First Puzzle Solution"
           :card-id 6
           :coords '(25 18))
 (location "Card 07: Sealime"    207
           :region "Ship"
           :condition (or boost-climb
                          (and spin-double
                               (items "Wall Run")))
           :card-id 7
           :coords '(14 23))
 (location "Card 08: Toucade"    208
           :region "Past First Puzzle" ; requires getting here without solving the puzzle
           :condition (items "Spin Dodge")
           :card-id 8
           :coords '(19 18))
 (location "Card 09: Shaifi"     209
           :region "Beach"
           :card-id 9
           :coords '(2 13))
 (location "Card 10: Pengrunt"   210
           :region "Griger's Base (Powerless Room)"
           :card-id 10
           :coords '(16 11.5))
 (location "Card 11: Cottospark" 211
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical)
           :card-id 12
           :tracker-group "Cotto Cards"
           :coords '(5 17))
 (location "Card 12: Cottocache" 212
           :region "Above Orb A"
           :condition (and (items "Speed Boost")
                           any-vertical)
           :card-id 13
           :tracker-group "Cotto Cards")
 (location "Card 13: Drilbas"    213
           :region "Left of Ship"
           :condition both-vertical
           :card-id 14
           :coords '(9 24))
 (location "Card 14: Jinvell"    214
           :region "Beach"
           :condition (items "Speed Boost"
                             "Wall Run"
                             "Spin Dodge")
           :card-id 15
           :coords '(3 19))
 (location "Card 15: Royalrose"  215
           :region "Upper Floatlands"
           :card-id 16
           :coords '(11 30))
 (location "Card 16: Rupo"       216
           :region "Orb B"
           :condition boost-climb
           :card-id 17
           :coords '(9 28))
 (location "Card 17: Froesburn"  217
           :region "Mountain Fall"
           :condition larva-mode
           :card-id 18
           :coords '(30 16))
 (location "Card 18: Ghostily"   218
           :region "Underwater"
           :condition larva-mode
           :card-id 19
           :tracker-group "Ghostily Chase")
 (location "Card 19: Sherivice"  219
           :region "Right Floatlands"
           :card-id 20
           :coords '(14 30))
 (location "Card 20: Griger"     220
           :region "Griger"
           :condition (and any-vertical
                           (items "Energy Claw")
                           (or (option 'RequireBossCards false)
                               (items "Card: Griger")))
           :card-id 21
           :tracker-group "Griger Fight")
 (location "Card 21: Solatia"    221
           :region "Solatia"
           :card-id 22
           :coords '(14 28))
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
           :card-id 23
           :tracker-group "Save Point Wall"
           :coords '(25 30))
 (location "Card 23: Oracle"     223
           :region "Orb D"
           :card-id 24
           :tracker-group "Orb D")
 (location "Card 24: Oracle-L"   224
           :region "Ship"
           :condition larva-mode
           :card-id 25
           :coords '(11 20))
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
           :health-upgrade-id "HU0"
           :coords '(20 19))
 (location "Pre-Spin Dodge Health Upgrade" 401
           :region "Pre-Spin Dodge"
           :condition charge-wall
           :include-option "add_physical"
           :health-upgrade-id "HU1"
           :coords '(23 14))
 (location "Floatlands Health Upgrade" 402
           :region "Upper Floatlands"
           :include-option "add_physical"
           :health-upgrade-id "HU2"
           :coords '(9 30))
 (location "Warehouse Entry Health Upgrade" 403
           :region "Warehouse"
           :include-option "add_physical"
           :health-upgrade-id "HU3"
           :coords '(31 8))
 (location "Phase Upgrade Left of Ship" 404
           :region "Left of Ship"
           :include-option "add_physical"
           :phase-upgrade-id "PU0"
           :coords '(7 21))
 (location "Phase Upgrade Outside Griger's Base" 405
           :region "Griger's Base (Left)"
           :condition any-vertical
           :include-option "add_physical"
           :phase-upgrade-id "PU1"
           :coords '(9 14))
 (location "Lower Mountain Phase Upgrade" 406
           :region "Mountain Fall"
           :include-option "add_physical"
           :phase-upgrade-id "PU2"
           :coords '(29 22))
 (location "Upper Mountain Phase Upgrade" 407
           :region "Upper Mountain"
           :include-option "add_physical"
           :phase-upgrade-id "PU3"
           :tracker-group "Save Point Wall")
 (location "Orb A" 408
           :region "Orb A"
           :condition (or (items "Spin Dodge")
                          boost-climb)
           :include-option "add_physical"
           :orb-id "ORB0"
           :coords '(6.5 10.5))
 (location "Orb B" 409
           :region "Orb B"
           :condition (or (items "Spin Dodge")
                          (entrance? "Upper Floatlands" "Orb B")
                          boost-climb)
           :include-option "add_physical"
           :orb-id "ORB1"
           :coords '(10.5 28.5))
 (location "Orb C" 410
           :region "Orb C"
           :condition (or (items "Wall Run")
                          spin-double
                          twister-jump)
           :include-option "add_physical"
           :orb-id "ORB2"
           :coords '(26.5 22.5))
 (location "Orb D" 411
           :region "Orb D"
           :include-option "add_physical"
           :orb-id "ORB3"
           :tracker-group "Orb D"
           :coords '(32.5 12.5))
 (event "Defeat Salesman" "Victory"
        :region "Mountaintop"
        :condition (or (option 'RequireBossCards false)
                       (items "Card: Salesman"))
        :coords '(24 36)))
