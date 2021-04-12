import os


def mk_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def mk_starter(project_folder, child_folders):
    mk_folder(project_folder)
    for folder in child_folders:
        mk_folder((os.path.join(project_folder, folder)))


if __name__ == '__main__':
    project_fold = 'my_project'
    children_flds = ('settings', 'mainapp', 'adminapp', 'authapp')
    mk_starter(project_fold, children_flds)
    for root, dirs, files in os.walk(project_fold):
        print(root, dirs, files)
