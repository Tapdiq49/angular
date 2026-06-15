# Tətbiqin HousingLocation komponentini yaradın

Bu təlimat dərsi Angular tətbiqinizə `HousingLocation` komponentini necə əlavə edəcəyinizi nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/R0nRX8jD2D0?si=U4ONEbPvtptdUHTt&amp;start=440"/>

## Nə öyrənəcəksiniz

- Tətbiqinizin yeni bir komponenti var: `HousingLocation` və o, komponentin tətbiqinizə əlavə olunduğunu təsdiqləyən bir mesaj göstərir.

<docs-workflow>

<docs-step title="`HousingLocation` komponentini yaradın">
Bu addımda tətbiqiniz üçün yeni bir komponent yaradırsınız.

IDE-nizin **Terminal** bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.

1. Yeni bir `HousingLocation` komponenti yaratmaq üçün bu əmri işlədin:

   ```shell
   ng generate component housingLocation
   ```

1. Tətbiqinizi qurmaq və serverdə işə salmaq üçün bu əmri işlədin.

   ```shell
   ng serve
   ```

   QEYD: Bu addım yalnız yerli mühitiniz üçündür!

1. Tətbiqi tapmaq üçün brauzeri açın və `http://localhost:4200` ünvanına keçin.
1. Tətbiqin xətasız qurulduğunu təsdiqləyin.

   FAYDALI: O, əvvəlki dərsdəki kimi render olunmalıdır, çünki yeni komponent əlavə etsəniz də, hələ ki onu tətbiqin template-lərindən hər hansı birinə daxil etməmisiniz.

1. Növbəti addımları tamamlayarkən `ng serve` əmrini işlək vəziyyətdə saxlayın.
   </docs-step>

<docs-step title="Yeni komponenti tətbiqinizin düzümünə əlavə edin">
Bu addımda siz yeni `HousingLocation` komponentini tətbiqinizin `Home` komponentinə əlavə edirsiniz ki, o tətbiqinizin düzümündə görünsün.

IDE-nizin **Edit** (Redaktə) bölməsində:

1.  Redaktorda `home.ts` faylını açın.
1.  `home.ts` daxilində fayl səviyyəsindəki import-lara bu sətri əlavə edərək `HousingLocation` komponentini import edin.

       <docs-code header="src/app/home/home.ts daxilində HousingLocation-ı import edin" path="adev/src/content/tutorials/first-app/steps/04-interfaces/src/app/home/home.ts" visibleLines="[2]"/>

1.  Növbəti olaraq `@Component` metadata-sındakı `imports` property-sini massivə `HousingLocation` əlavə edərək yeniləyin.

       <docs-code  header="src/app/home/home.ts daxilində imports massivinə HousingLocation əlavə edin" path="adev/src/content/tutorials/first-app/steps/04-interfaces/src/app/home/home.ts" visibleLines="[6]"/>

1.  İndi komponent `Home` komponentinin template-ində istifadə üçün hazırdır. `@Component` metadata-sındakı `template` property-sini `<app-housing-location>` teqinə istinadı daxil edəcək şəkildə yeniləyin.

       <docs-code language="angular-ts" header="src/app/home/home.ts daxilində komponent template-inə housing location əlavə edin" path="adev/src/content/tutorials/first-app/steps/04-interfaces/src/app/home/home.ts" visibleLines="[7,17]"/>

</docs-step>

<docs-step title="Komponent üçün üslubları (styles) əlavə edin">
Bu addımda, tətbiqin düzgün render olunması üçün `HousingLocation` komponenti üçün əvvəlcədən yazılmış üslubları tətbiqinizə köçürəcəksiniz.

1. `src/app/housing-location/housing-location.css` faylını açın və aşağıdakı üslubları fayla yapışdırın:

   QEYD: Brauzerdə bunlar `src/app/housing-location/housing-location.ts` faylında `styles` massivinə yerləşdirilə bilər.

   <docs-code header="src/app/housing-location/housing-location.css daxilində komponentə CSS üslubları əlavə edin" path="adev/src/content/tutorials/first-app/steps/04-interfaces/src/app/housing-location/housing-location.css"/>

1. Kodunuzu yadda saxlayın, brauzerə qayıdın və tətbiqin xətasız qurulduğunu təsdiqləyin. Ekranda "housing-location works!" mesajının render olunduğunu görməlisiniz. Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.

   <img alt="homes-app-ın logo, filtr mətn giriş qutusu, axtarış düyməsi və 'housing-location works!' mesajını göstərən brauzer pəncərəsi" src="assets/images/tutorials/first-app/homes-app-lesson-03-step-2.png">

</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqiniz üçün yeni bir komponent yaratdınız və onu tətbiqin düzümünə əlavə etdiniz.
