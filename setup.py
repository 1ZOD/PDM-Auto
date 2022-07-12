from distutils.core import setup
import py2exe

setup(windows=[{"script":"app.py","icon_resources":[(1,"brand_adidas_icon_159015.ico")]}])


#python setup.py py2exe