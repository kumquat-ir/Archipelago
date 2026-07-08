(region-list
 (region "Ship"
         (-> "First Puzzle Solution"
             charge-wall)
         (-> "Past First Puzzle" nil)
         (-> "Left of Ship"
             any-vertical)
         (-> "Power Area"
             charge-wall)
         (-> "Above First Puzzle"
             (or charge-wall
                 (items "Wall Run")))
         (-> "After Griger"
             larva-mode)
         (-> "Mountain Water Run"
             boost-climb))
 (region "First Puzzle Solution" ; going through here backwards?
         (-> "Spin Dodge Area"
             (and (true) ; coerce the option to a rule
                  (option 'HardLogic true))))
 (region "Past First Puzzle"
         (-> "Pre-Spin Dodge"
             (or power-on
                 any-vertical))
         (-> "Griger's Base (Top)"
             (or (and power-on
                      (items "Spin Dodge"))
                 boostable-claw-wall
                 spin-double))
         (-> "Above Wall Run"
             boostable-claw-wall)
         (-> "Endoplanetary Shield"
             charge-wall))
 (region "Above First Puzzle"
         (-> "Mountain Chamber"
             (or both-vertical
                 boost-climb)))
 (region "Power Area"
         (-> "Under Beach"
             any-vertical)
         (-> "After Griger"
             fast-boostable-claw-wall))
 (region "Pre-Spin Dodge"
         (-> "Spin Dodge Area" nil))
 (region "Spin Dodge Area"
         (-> "Pre-Spin Dodge"
             (items "Spin Dodge"))
         (-> "First Puzzle Solution"
             (items "Spin Dodge")))
 (region "Griger"
         (-> "After Griger"
             fast-boostable-claw-wall)
         (-> "Griger's Base (Top)" nil))
 (region "After Griger"
         (-> "Power Area"
             boostable-claw-wall)
         (-> "Griger"
             nonboostable-claw-wall))
 (region "Claw Bounce Area"
         (-> "Orb A"
             (items "Spin Dodge"
                    "Energy Claw"))
         (-> "Griger's Base (Bottom Right)"
             (and any-vertical
                  (items "Energy Claw")))
         (-> "Wall Run Area"
             ;; charge wall here is 3 minute obsidian vines
             ;; not all routes here will be fast enough, but you should be able to get here fast enough no matter what if this entrance is in logic
             ;; you can get here with nothing but claw and spin dodge in ~1:30, via the first puzzle and griger's front door
             ;; or a bit slower via the gap above charge shot instead of the puzzle, if i decide to rando that
             ;; and the vine might fail to spawn for some reason??? jank
             (and charge-wall
                  any-vertical)))
 (region "Wall Run Area"
         (-> "Claw Bounce Area"
             both-vertical)
         (-> "Above Wall Run"
             both-vertical))
 (region "Above Wall Run"
         (-> "Past First Puzzle"
             boostable-claw-wall)
         (-> "Wall Run Area"
             (or both-vertical
                 spin-double))
         (-> "Griger's Base (Bottom Right)"
             (and (or both-vertical
                      spin-double)
                  boost-wall)))
 (region "Griger's Base (Top)"
         (-> "Griger's Base (Central)" nil)
         (-> "Griger"
             any-vertical))
 (region "Griger's Base (Central)"
         (-> "Griger's Base (Top)"
             (items "Spin Dodge"))
         (-> "Griger's Base (Right)"
             (or block-puzzle-solve
                 fast-boostable-claw-wall))
         (-> "Griger's Base (Left)"
             (and (or (items "Spin Dodge")
                      (and (items "Wall Run")
                           nonboostable-claw-wall))
                  boostable-claw-wall))
         (-> "Griger's Base (Bottom Right)"
             (and any-vertical
                  (or block-puzzle-solve
                      boostable-claw-wall)))
         (-> "Griger's Base (Bottom Left)"
             (or fast-boostable-claw-wall
                 (and block-puzzle-solve
                      here-be-cottosparks))))
 (region "Griger's Base (Right)")
 (region "Griger's Base (Left)"
         (-> "Griger's Base (Central)"
             (and any-vertical
                  nonboostable-claw-wall))
         (-> "Above Orb A"
             (and (items "Energy Claw")
                  (or both-vertical
                      spin-double))))
 (region "Griger's Base (Bottom Right)"
         (-> "Claw Bounce Area"
             (items "Energy Claw"
                    "Spin Dodge"))
         (-> "Griger's Base (Central)"
             (and (items "Wall Run")
                  nonboostable-claw-wall))
         (-> "Griger's Base (Powerless Room)"
             (and any-vertical
                  grigers-base-unpowered)))
 (region "Griger's Base (Bottom Left)"
         (-> "Griger's Base (Central)"
             (and (items "Wall Run")
                  nonboostable-claw-wall))
         (-> "Griger's Base (Powerless Room)"
             (and any-vertical
                  grigers-base-unpowered)))
 (region "Griger's Base (Powerless Room)"
         (-> "Griger's Base (Bottom Left)"
             fast-boostable-claw-wall)
         (-> "Griger's Base (Bottom Right)"
             any-vertical))
 (region "Left of Ship"
         (-> "Floatlands Entry"
             both-vertical)
         (-> "Beach"
             fast-boostable-claw-wall))
 (region "Under Beach"
         (-> "Beach"
             (items "Spin Dodge"))
         (-> "Power Area" nil)
         (-> "Above Orb A"
             fast-boost-wall))
 (region "Beach"
         (-> "Underwater"
             ;; charge wall here is 3 minute obsidian vines
             ;; don't think this one is a problem, all logical routes here are fast enough
             (or (and (or (items "Spin Dodge")
                          boost-climb)
                      charge-wall)
                 larva-mode)))
 (region "Underwater"
         (-> "Beach"
             larva-mode)
         (-> "Orb A"
             any-vertical))
 (region "Orb A"
         (-> "Underwater"
             any-vertical)
         (-> "Claw Bounce Area"
             (items "Spin Dodge"
                    "Energy Claw"))
         (-> "Above Orb A"
             both-vertical))
 (region "Above Orb A"
         (-> "Orb A" nil)
         (-> "Griger's Base (Left)"
             (items "Wall Run"))
         (-> "Under Beach"
             boost-climb))
 (region "Endoplanetary Shield"
         (-> "Hot Water Area"
             (and (items "Wall Run")
                  (any-item "Spin Dodge"
                            "Speed Boost")
                  (or (items "Heat Reisist"
                             "Spin Dodge")
                      spin-double)))
         (-> "Past First Puzzle"
             (and boost-climb
                  charge-wall)))
 (region "Hot Water Area"
         (-> "Warehouse"
             (and boost-climb
                  (or (items "Heat Resist"
                             "Spin Dodge")
                      spin-double)))
         (-> "Endoplanetary Shield"
             (items "Wall Run")))
 (region "Warehouse"
         (-> "Orb D"
             larva-mode)
         (-> "Hot Water Area"
             boost-wall))
 (region "Orb D")
 (region "Floatlands Entry"
         (-> "Upper Floatlands"
             (and both-vertical
                  (or power-on
                      spin-double)))
         (-> "Lower Floatlands"
             (items "Spin Dodge"))
         (-> "Orb B"
             both-vertical))
 (region "Upper Floatlands"
         (-> "Orb B" nil)
         (-> "Floatlands Entry" nil)
         (-> "Right Floatlands"
             (and (items "Spin Dodge")
                  (any-item "Energy Claw"
                            "Spin Double"
                            "Twister Jump"))))
 (region "Lower Floatlands"
         (-> "Orb B"
             both-vertical))
 (region "Orb B"
         (-> "Lower Floatlands" nil)
         (-> "Upper Floatlands"
             (and both-vertical
                  (or spin-double
                      boost-climb)))
         (-> "Floatlands Ambush" nil)
         (-> "Floatlands Entry"
             (items "Spin Dodge")))
 (region "Floatlands Ambush"
         (-> "Right Floatlands"
             (items "Wall Run"))
         (-> "Orb B"
             (and (items "Wall Run")
                  (any-item "Spin Dodge"
                            "Speed Boost")))
         (-> "Lower Floatlands"
             (any-item "Spin Dodge"
                       "Speed Boost"))
         (-> "Floatlands Entry"
             (items "Spin Dodge"))
         (-> "Solatia Run"
             boost-wall))
 (region "Right Floatlands"
         (-> "Floatlands Ambush" nil)
         (-> "Upper Floatlands"
             (any-item "Energy Claw"
                       "Spin Dodge"))
         (-> "Solatia"
             (and (or (and (region? "Upper Floatlands")
                           (region? "Lower Floatlands")
                           (region? "Floatlands Entry")
                           power-on)
                      boost-wall)
                  both-vertical
                  (or (option 'RequireBossCards false)
                      (items "Card: Solatia")))))
 (region "Solatia"
         (-> "Solatia Run" nil))
 (region "Solatia Run"
         (-> "Floatlands Ambush"
             boost-wall)
         (-> "Upper Mountain"
             boost-climb))
 (region "Upper Mountain"
         (-> "Solatia Run"
             boost-wall)
         (-> "Mountain Chamber" nil)
         (-> "Mountain Fall" nil)
         (-> "Mountaintop"
             (and both-vertical
                  can-escape-warehouse
                  (region? "Orb A")
                  (region? "Orb B")
                  (region? "Orb C")
                  (region? "Orb D"))))
 (region "Mountain Chamber"
         (-> "Upper Mountain"
             both-vertical)
         (-> "Mountain Water Run" nil)
         (-> "Above First Puzzle" nil)
         (-> "Orb C"
             (or larva-mode
                 (and (option 'HardLogic true)
                      both-vertical
                      spin-double))))
 (region "Mountain Water Run"
         (-> "Mountain Chamber"
             (or both-vertical
                 boost-climb)))
 (region "Orb C"
         (-> "Mountain Water Run"
             (items "Wall Run"))
         (-> "Mountain Fall"
             any-vertical))
 (region "Mountain Fall"
         (-> "Warehouse"
             larva-mode)
         (-> "Orb C" nil)
         (-> "Upper Mountain"
             both-vertical))
 (region "Mountaintop"))
