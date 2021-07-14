# -*- mode: python ; coding: utf-8 -*-
add_files = [('resources\\images\\*.thumb','images'),
             ('resources\\icons\\*.ico','icons'),
             ]

block_cipher = None


a = Analysis(['cy.py'],
             pathex=['C:\\Users\\Admin\\Work-Space\\pyInstaller-Projects\\SEFA\\Sefa_v3'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Sefa',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='resources\\icons\\logo_dark.ico')
