(item-list
 ;; filler items
 (item "Phase Refill (25%)"  1 'filler
       :phase-amount 20
       :weight 50)
 (item "Phase Refill (50%)"  2 'filler
       :phase-amount 40
       :weight 25)
 (item "Phase Refill (75%)"  3 'filler
       :phase-amount 60
       :weight 15)
 (item "Phase Refill (100%)" 4 'filler
       :phase-amount 80
       :weight 10)

 ;; decryptors
 (item "Charge Shot"     100 'progression
       :decryptor-id "CHARGE_SHOT")
 (item "Charge Magnet"   101 'useful
       :decryptor-id "CHARGE_MAGNET")
 (item "Altered Shot"    102 'useful
       :decryptor-id "ALTERED_SHOT")
 (item "Charge Grip"     103 'useful
       :decryptor-id "CHARGE_GRIP")
 (item "Wall Run"        104 'progression
       :decryptor-id "WALL_RUN")
 (item "Spin Dodge"      105 'progression
       :decryptor-id "SPIN_DODGE")
 (item "Heat Resist"     106 'progression
       :decryptor-id "HEAT_RESIST")
 (item "Mental Recovery" 107 'useful
       :decryptor-id "MENTAL_RECOVERY")
 (item "Energy Claw"     108 'progression
       :decryptor-id "ENERGY_CLAW")
 (item "Strip Suit"      109 'progression
       :decryptor-id "STRIP_SUIT")
 (item "Shell Escape"    110 'useful
       :decryptor-id "NO_OBJECTIONS")
 (item "Speed Boost"     111 'progression
       :decryptor-id "SPEED_BOOST")
 (item "Vile Claw"       112 'progression
       :decryptor-id "CLAW_BREAKS_CHARGE_SHOT")
 (item "Piercing Speed"  113 'progression
       :decryptor-id "SPEED_BOOST_BREAKS_CLAW")
 (item "Golden View"     114 'filler ; shows which decryptor pickups are important in vanilla
       :decryptor-id "SHOW_IMPORTANT")
 (item "d#Z 5~qn. P"     115 'progression
       :decryptor-id "VIRUS")
 (item "Virus Wipe"      116 'filler ; doesn't actually do anything as all random virus squares have been removed
       :decryptor-id "VIRUS_WIPE")
 (item "Double Shot"     117 'useful
       :decryptor-id "DOUBLE_SHOT")

 ;; extra decryptors, not normally obtainable
 (item "Spin Double"       118 'progression
       :pool-option "extra_decryptors"
       :decryptor-id "SPIN_DOUBLE")
 (item "Twister Jump"      119 'filler
       :pool-option false
       :decryptor-id "SPIN_DODGE_JUMP")
 (item "Chamber Focus"     120 'useful
       :pool-option "extra_decryptors"
       :decryptor-id "CHAMBER_FOCUS")
 (item "Engine Tune"       121 'progression
       :pool-option "extra_decryptors"
       :decryptor-id "SPEED_BOOST_EARLIER")

 ;; cards
 (item "Card: Magoom"     201 'useful
       :card-id 1)
 (item "Card: Ciurivy"    202 'useful
       :card-id 2)
 (item "Card: Smosey"     203 'useful
       :card-id 3)
 (item "Card: Wavemoth"   204 'useful
       :card-id 4)
 (item "Card: Midow"      205 'useful
       :card-id 5)
 (item "Card: Prittle"    206 'useful
       :card-id 6)
 (item "Card: Sealime"    207 'useful
       :card-id 7)
 (item "Card: Toucade"    208 'useful
       :card-id 8)
 (item "Card: Shaifi"     209 'filler ; can't attack these little fish
       :trimmable true
       :card-id 9)
 (item "Card: Pengrunt"   210 'useful
       :card-id 10)
 (item "Card: Cottospark" 211 'useful
       :card-id 12)
 (item "Card: Cottocache" 212 'useful
       :card-id 13)
 (item "Card: Drilbas"    213 'filler ; more of a stage hazard than an enemy
       :trimmable true
       :card-id 14)
 (item "Card: Jinvell"    214 'useful
       :card-id 15)
 (item "Card: Royalrose"  215 'useful
       :card-id 16)
 (item "Card: Rupo"       216 'useful
       :card-id 17)
 (item "Card: Froesburn"  217 'useful
       :card-id 18)
 (item "Card: Ghostily"   218 'filler ; another stage hazard
       :card-id 19)
 (item "Card: Sherivice"  219 'filler ; technically a boss but is really just the tutorial
       :card-id 20)
 (item "Card: Griger"     220 (if-option "require_boss_cards" 'progression 'useful)
       :card-id 21)
 (item "Card: Solatia"    221 (if-option "require_boss_cards" 'progression 'useful)
       :card-id 22)
 (item "Card: Salesman"   222 (if-option "require_boss_cards" 'progression 'useful)
       :card-id 23)
 (item "Card: Oracle"     223 'filler ; you can't fight yourself
       :trimmable true
       :card-id 24)
 (item "Card: Oracle-L"   224 'filler
       :trimmable true
       :card-id 25))
