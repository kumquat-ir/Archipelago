;; helper macros for logic

(set* 'charge-wall
      (or (item "Charge Shot")
          (item "Energy Claw"
                "Vile Claw")))

(set* 'boostable-claw-wall
      (or (item "Energy Claw")
          (item "Speed Boost"
                "Piercing Speed"))
      'fast-boostable-claw-wall
      (or (item "Energy Claw")
          (item "Speed Boost"
                "Piercing Speed"
                "Engine Tune"))
      'nonboostable-claw-wall
      (item "Energy Claw"))

(set* 'boost-wall
      (item "Speed Boost")
      'fast-boost-wall
      (item "Speed Boost"
            "Engine Tune"))

(set 'boost-climb
     (item "Speed Boost"
           "Wall Run"))

(set 'any-vertical
     (any-item "Wall Run"
               "Spin Dodge"))

(set 'both-vertical
     (item "Wall Run"
           "Spin Dodge"))

(set 'hot-water
     (item "Heat Resist"))

(set* 'virus
      (item "d#Z 5~qn. P")
      'antivirus
      (item "Virus Wipe"))

(set 'larva-mode
     (item "Strip Suit"))

(set 'power-on
     (region? "Power Area"))

(set 'spin-double
     (item "Spin Dodge"
           "Spin Double"))

(set 'here-be-cottosparks
     (and (item "Spin Dodge")
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
 :goal (item "Victory"))
