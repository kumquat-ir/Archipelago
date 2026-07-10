from Options import PerGameCommonOptions, Toggle, OptionGroup, DefaultOnToggle
import dataclasses

class HardLogic(Toggle):
    """
    Add some more difficult/inconsistent tricks to logic.
    """

    display_name="Hard Logic"

class ExtraDecryptors(Toggle):
    """
    Add 4 extra decryptors that aren't obtainable in vanilla.
    """

    display_name="Extra Decryptors"

class RequireBossCards(DefaultOnToggle):
    """
    Require obtaining the card for a boss before you are expected to fight it.
    """

    display_name="Require Boss Cards"

class AddAmbushes(Toggle):
    """
    Adds locations for clearing each of the 10 ambushes for the first time.
    """

    display_name="Ambushes"

class AddPhysical(Toggle):
    """
    Adds 12 locations for collecting each of the physical upgrades (health, phase, orbs) for the first time.
    """

    display_name="Physical Upgrades"

@dataclasses.dataclass
class VisionSoftResetOptions(PerGameCommonOptions):
    hard_logic: HardLogic
    extra_decryptors: ExtraDecryptors
    require_boss_cards: RequireBossCards
    add_ambushes: AddAmbushes
    add_physical: AddPhysical

option_groups = [
    OptionGroup(
        "Locations",
        [AddAmbushes, AddPhysical]
    )
]
