from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R=Path(__file__).resolve().parents[1]
out=R/'store-assets';out.mkdir(exist_ok=True)
def font(size,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'segoeui.ttf'),size)
def icon(size):
    im=Image.new('RGB',(size,size),'#7054dc');d=ImageDraw.Draw(im)
    d.ellipse((size*.54,-size*.25,size*1.3,size*.51),fill='#7c62df')
    d.polygon([(size*.54,size*.18),(size*.27,size*.55),(size*.47,size*.55),(size*.42,size*.83),(size*.75,size*.41),(size*.54,size*.41)],fill='#d3f4e5')
    return im
icon(512).save(out/'play-icon-512.png');icon(1024).save(out/'app-icon-1024.png');icon(192).save(R/'web/icon.png')
for name,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    folder=R/'android/res'/('mipmap-'+name);folder.mkdir(parents=True,exist_ok=True);icon(size).save(folder/'ic_launcher.png')
folder=R/'android/res/drawable';folder.mkdir(parents=True,exist_ok=True)
(folder/'ic_foreground.xml').write_text('''<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108"><path android:fillColor="#D3F4E5" android:pathData="M59,27 L36,57 L52,57 L48,81 L75,45 L59,45 Z"/></vector>''')
folder=R/'android/res/values';folder.mkdir(parents=True,exist_ok=True)
(folder/'colors.xml').write_text('<resources><color name="icon_background">#7054DC</color></resources>')
folder=R/'android/res/mipmap-anydpi-v26';folder.mkdir(parents=True,exist_ok=True)
(folder/'ic_launcher.xml').write_text('<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android"><background android:drawable="@color/icon_background"/><foreground android:drawable="@drawable/ic_foreground"/></adaptive-icon>')
im=Image.new('RGB',(1024,500),'#26243f');d=ImageDraw.Draw(im)
d.ellipse((670,-180,1220,370),outline='#393451',width=70);d.ellipse((780,200,1110,530),fill='#393451')
im.paste(icon(76),(66,59));d.text((159,67),'FitFlow',font=font(43,True),fill='white')
d.text((66,179),'Find your rhythm.',font=font(57,True),fill='white');d.text((66,252),'Feel your best.',font=font(57,True),fill='#c8b4ff')
d.text((69,363),'MOVE  /  NOURISH  /  GROW',font=font(21,True),fill='#d3f4e5')
im.save(out/'feature-graphic-1024x500.png')
print('Created icons, adaptive resources, and feature graphic.')
