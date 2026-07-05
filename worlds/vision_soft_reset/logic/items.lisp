(item-list
 ;; filler items
 (item "Phase Refill (25%)"  0 'filler
       :weight 50)
 (item "Phase Refill (50%)"  1 'filler
       :weight 25)
 (item "Phase Refill (75%)"  2 'filler
       :weight 15)
 (item "Phase Refill (100%)" 3 'filler
       :weight 10)

 ;; decryptors
 (item "Charge Shot"     100 'progression)
 (item "Charge Magnet"   101 'useful)
 (item "Altered Shot"    102 'useful)
 (item "Charge Grip"     103 'useful)
 (item "Wall Run"        104 'progression)
 (item "Spin Dodge"      105 'progression)
 (item "Heat Resist"     106 'progression)
 (item "Mental Recovery" 107 'useful)
 (item "Energy Claw"     108 'progression)
 (item "Strip Suit"      109 'progression)
 (item "Shell Escape"    110 'useful)
 (item "Speed Boost"     111 'progression)
 (item "Vile Claw"       112 'progression)
 (item "Piercing Speed"  113 'progression)
 (item "Golden View"     114 'filler ; shows which decryptor pickups are important in vanilla
       :trimmable true)
 (item "d#Z 5~qn. P"     115 'progression)
 (item "Virus Wipe"      116 'filler)
 (item "Double Shot"     117 'useful)

 ;; extra decryptors, not normally obtainable
 (item "Spin Double"       118 'progression
       :pool-option "extra_decryptors")
 (item "Twister Jump"      119 'progression
       :pool-option "extra_decryptors")
 (item "Chamber Focus"     120 'useful
       :pool-option "extra_decryptors")
 (item "Engine Tune"       121 'progression
       :pool-option "extra_decryptors")

 ;; cards
 (item "Card: Magoom"     201 'useful)
 (item "Card: Ciurivy"    202 'useful)
 (item "Card: Smosey"     203 'useful)
 (item "Card: Wavemoth"   204 'useful)
 (item "Card: Midow"      205 'useful)
 (item "Card: Prittle"    206 'useful)
 (item "Card: Sealime"    207 'useful)
 (item "Card: Toucade"    208 'useful)
 (item "Card: Shaifi"     209 'filler ; can't attack these little fish
       :trimmable true)
 (item "Card: Pengrunt"   210 'useful)
 (item "Card: Cottospark" 211 'useful)
 (item "Card: Cottocache" 212 'useful)
 (item "Card: Drilbas"    213 'useful)
 (item "Card: Jinvell"    214 'useful)
 (item "Card: Royalrose"  215 'useful)
 (item "Card: Rupo"       216 'useful)
 (item "Card: Froesburn"  217 'useful)
 (item "Card: Ghostily"   218 'useful)
 (item "Card: Sherivice"  219 'useful)
 (item "Card: Griger"     220 'useful)
 (item "Card: Solatia"    221 'useful)
 (item "Card: Salesman"   222 'useful)
 (item "Card: Oracle"     223 'filler ; you can't fight yourself
       :trimmable true)
 (item "Card: Oracle-L"   224 'filler
       :trimmable true))
