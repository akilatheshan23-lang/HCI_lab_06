"""Reproducible release APK using the installed official Android SDK (no Gradle download).
Set ANDROID_HOME and JAVA_HOME if they are not installed in the standard Windows paths.
Creates a private local release key once. Never commit .private/ or share its password.
"""
import os, pathlib, subprocess, zipfile, shutil, secrets, json, hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
SDK=pathlib.Path(os.environ.get('ANDROID_HOME',str(pathlib.Path.home()/'AppData/Local/Android/Sdk')))
JAVA=pathlib.Path(os.environ.get('JAVA_HOME',r'C:\Program Files\Android\Android Studio\jbr'))/'bin'
TOOLS=SDK/'build-tools/36.1.0'
ANDROID=SDK/'platforms/android-36/android.jar'
BUILD=ROOT/'build/android'; BUILD.mkdir(parents=True,exist_ok=True)
PRIVATE=ROOT/'.private'; PRIVATE.mkdir(exist_ok=True)
OUT=ROOT/'releases'; OUT.mkdir(exist_ok=True)
def run(*args):
    subprocess.run([str(a) for a in args],check=True,cwd=ROOT)
for tool in [JAVA/'java.exe',JAVA/'javac.exe',JAVA/'keytool.exe',TOOLS/'aapt2.exe',ANDROID]:
    if not tool.exists():raise SystemExit(f'Required SDK tool missing: {tool}')
classes=BUILD/'classes'; classes.mkdir(exist_ok=True)
assets=BUILD/'assets/web'; assets.mkdir(parents=True,exist_ok=True)
for path in (ROOT/'web').glob('*'):
    if path.is_file():shutil.copy2(path,assets/path.name)
run(TOOLS/'aapt2.exe','compile','--dir',ROOT/'android/res','-o',BUILD/'resources.zip')
run(TOOLS/'aapt2.exe','link','-o',BUILD/'unsigned.apk','-I',ANDROID,'--manifest',ROOT/'android/AndroidManifest.xml','-A',BUILD/'assets','--min-sdk-version','26','--target-sdk-version','36',BUILD/'resources.zip')
sources=list((ROOT/'android/src').rglob('*.java'))
run(JAVA/'javac.exe','-source','8','-target','8','-classpath',ANDROID,'-d',classes,*sources)
run(JAVA/'java.exe','-cp',TOOLS/'lib/d8.jar','com.android.tools.r8.R8','--release','--min-api','26','--lib',ANDROID,'--pg-conf',ROOT/'android/proguard-rules.pro','--pg-map-output',BUILD/'mapping.txt','--output',BUILD,*classes.rglob('*.class'))
with zipfile.ZipFile(BUILD/'unsigned.apk','a',zipfile.ZIP_DEFLATED,compresslevel=9) as z:z.write(BUILD/'classes.dex','classes.dex')
run(TOOLS/'zipalign.exe','-f','-p','4',BUILD/'unsigned.apk',BUILD/'aligned.apk')
key=PRIVATE/'fitflow-release.jks'; pwfile=PRIVATE/'signing-password.txt'
if not key.exists():
    if not pwfile.exists():pwfile.write_text(secrets.token_urlsafe(36),encoding='ascii')
    run(JAVA/'keytool.exe','-genkeypair','-keystore',key,'-storetype','JKS','-storepass:file',pwfile,'-keypass:file',pwfile,'-alias','fitflow-release','-keyalg','RSA','-keysize','3072','-validity','10000','-dname','CN=FitFlow Lab Release, OU=IT23379442, O=Student Project, C=LK','-noprompt')
apk=OUT/'FitFlow-1.1.0-release.apk'
run(JAVA/'java.exe','-jar',TOOLS/'lib/apksigner.jar','sign','--ks',key,'--ks-key-alias','fitflow-release','--ks-pass','file:'+str(pwfile),'--out',apk,BUILD/'aligned.apk')
verification=subprocess.check_output([str(JAVA/'java.exe'),'-jar',str(TOOLS/'lib/apksigner.jar'),'verify','--verbose','--print-certs',str(apk)],text=True)
run(TOOLS/'zipalign.exe','-c','-v','4',apk)
(OUT/'signature-verification.txt').write_text(verification,encoding='utf-8')
metadata={'applicationId':'lk.fitflow.it23379442','versionName':'1.1.0','versionCode':2,'minSdk':26,'targetSdk':36,'bytes':apk.stat().st_size,'sha256':hashlib.sha256(apk.read_bytes()).hexdigest(),'artifact':apk.name,'buildTools':'36.1.0','signing':'Local private release key; excluded from Git','optimization':'R8 release shrinking/optimization/obfuscation, ZIP deflate assets, zipalign. No third-party Java dependencies.'}
(OUT/'build-info.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
print(verification);print(json.dumps(metadata,indent=2))
