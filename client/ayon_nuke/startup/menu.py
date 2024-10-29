# 1 start mnm
try:
    from ayon_core.pipeline import install_host
    from ayon_nuke.api import NukeHost

    host = NukeHost()
    install_host(host)
except Exception as error:
    print(error)
# 1 end mnm

