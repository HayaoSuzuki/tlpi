import grp
import pwd


def user_name_from_id(uid: int) -> str:
    try:
        name = pwd.getpwuid(uid)[0]
    except KeyError:
        print(f"uid {uid} is not found.")
    else:
        return name


def user_id_from_name(name: str) -> int:
    try:
        uid = pwd.getpwnam(name)[2]
    except KeyError:
        print(f"username {name} is not found.")
    else:
        return uid


def group_name_from_id(gid: int) -> str:
    try:
        name = grp.getgrgid(gid)[0]
    except KeyError:
        print(f"gid {gid} is not found.")
    else:
        return name


def group_id_from_name(name: str) -> int:
    try:
        gid = grp.getgrnam(name)[2]
    except KeyError:
        print(f"username {name} is not found.")
    else:
        return gid


if __name__ == "__main__":
    uid = user_id_from_name("root")
    uname = user_name_from_id(uid)
    gname = group_name_from_id(0)
    gid = group_id_from_name(gname)

    print(f"{uname}({uid})")
    print(f"{gname}({gid})")
