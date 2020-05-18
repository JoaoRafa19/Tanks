import cx_Freeze

executables = [cx_Freeze.Executable("main.py", base = "Win32GUI")]

cx_Freeze.setup(
    name="Tanks",
    options={"build_exe": {"packages": ["pygame"],
                          "include_files": ["muro.png","Explosion.wav","shoot.wav","tanklaranja.png","tanklaranjabaixo.png",
                                            "tanklaranjadireita.png","tanklaranjaesquerda.png","tankverde.png","tankverdebaixo.png",
                                            "tankverdedireita.png","tankverdeesquerda.png","tiro.png"]}},
    description="A Tanks Hero copy",

    executables = executables
    )