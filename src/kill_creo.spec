# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Data\\Development\\PycharmProjects\\KillCreo\\src\\kill_creo.py'],
             pathex=['c:\\ProgLib\\Devel\\Python35-64\\Lib\\site-packages\\PyQt5\\Qt\\bin','C:\\Data\\Development\\PycharmProjects\\KillCreo\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='kill_creo',
          debug=False,
          strip=False,
          upx=True,
          console=False )
