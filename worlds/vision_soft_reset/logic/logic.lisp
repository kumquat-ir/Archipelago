;; helper macros for logic

(set* 'charge-wall
      (or (items "Charge Shot")
          (items "Energy Claw"
                 "Vile Claw")))

(set* 'boostable-claw-wall
      (or (items "Energy Claw")
          (items "Speed Boost"
                 "Piercing Speed"))
      'fast-boostable-claw-wall
      (or (items "Energy Claw")
          (items "Speed Boost"
                 "Piercing Speed"
                 "Engine Tune"))
      'nonboostable-claw-wall
      (items "Energy Claw"))

(set* 'boost-wall
      (items "Speed Boost")
      'fast-boost-wall
      (items "Speed Boost"
             "Engine Tune"))

(set 'boost-climb
     (items "Speed Boost"
            "Wall Run"))

(set 'any-vertical
     (any-item "Wall Run"
               "Spin Dodge"))

(set 'both-vertical
     (items "Wall Run"
            "Spin Dodge"))

(set 'hot-water
     (items "Heat Resist"))

(set* 'virus
      (items "d#Z 5~qn. P")
      'antivirus
      (items "Virus Wipe"))

(set 'larva-mode
     (items "Strip Suit"))

(set 'power-on
     (region? "Power Area"))

(set 'spin-double
     (items "Spin Dodge"
            "Spin Double"))

(set 'here-be-cottosparks
     (and (items "Spin Dodge")
          charge-wall))

(set 'block-puzzle-solve
     (and charge-wall
          any-vertical))

;; every entrance to griger's base except the one involving power
(set 'grigers-base-unpowered
     (or (entrance? "After Griger" "Griger")
         (entrance? "Claw Bounce Area" "Griger's Base (Bottom Right)")
         (entrance? "Griger's Base (Left)" "Griger's Base (Central)")
         (entrance? "Above Wall Run" "Griger's Base (Bottom Right)")
         (and (entrance? "Past First Puzzle" "Griger's Base (Top)")
              (or boostable-claw-wall
                  spin-double))))

(set 'can-escape-warehouse
     (and (entrance? "Warehouse" "Hot Water Area")
          (entrance? "Hot Water Area" "Endoplanetary Shield")
          (entrance? "Endoplanetary Shield" "Past First Puzzle")))

(logic-data
 :regions (require "regions")
 :locations (require "locations")
 :goal (items "Victory"))
