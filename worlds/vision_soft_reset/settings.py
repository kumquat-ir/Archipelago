from typing import Union
import settings

class VisionSoftResetSettings(settings.Group):
    class UTPackPath(settings.FilePath):
        required = False
        ut_dialog_name = "Select Poptracker Pack"

    ut_pack_path: Union[UTPackPath, str] = UTPackPath()
