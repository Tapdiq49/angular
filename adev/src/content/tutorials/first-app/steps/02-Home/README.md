# Home komponentini yaradın

Bu təlimat dərsi Angular tətbiqiniz üçün yeni bir [komponenti](guide/components) necə yaradacağınızı nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/R0nRX8jD2D0?si=OMVaw71EIa44yIOJ"/>

## Nə öyrənəcəksiniz

Tətbiqinizin yeni bir komponenti var: `Home`.

## Angular komponentlərinə konseptual baxış

Angular tətbiqləri Angular-ın quruluş blokları olan komponentlər ətrafında qurulur.
Komponentlər tətbiqdəki bir elementin funksiyasını və görünüşünü təmin edən kodu, HTML strukturunu və CSS üslub məlumatlarını ehtiva edir.
Angular-da komponentlər digər komponentləri ehtiva edə bilər. Bir tətbiqin funksiyaları və görünüşü komponentlərə bölünə və hissələrə ayrıla bilər.

Angular-da komponentlər onların xüsusiyyətlərini təyin edən metadatalara malikdir.
`Home` komponentini yaratdıqda bu xüsusiyyətlərdən istifadə edirsiniz:

- `selector`: Angular-ın template-lərdə komponentə necə müraciət etdiyini təsvir etmək üçün.
- `standalone`: komponentin `NgModule` tələb edib-etmədiyini təsvir etmək üçün.
- `imports`: komponentin aslılıqlarını təsvir etmək üçün.
- `template`: komponentin HTML strukturunu və düzümünü təsvir etmək üçün.
- `styleUrls`: komponentin istifadə etdiyi CSS fayllarının URL-lərini massivdə siyahıya almaq üçün.

<docs-pill-row>
  <docs-pill href="api/core/Component" title="Komponentlər haqqında daha çox öyrənin"/>
</docs-pill-row>

<docs-workflow>

<docs-step title="`Home` komponentini yaradın">
Bu addımda tətbiqiniz üçün yeni bir komponent yaradırsınız.

IDE-nizin **Terminal** bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.
1. Yeni bir `Home` komponenti yaratmaq üçün bu əmri işlədin:

   ```shell
   ng generate component home
   ```

1. Tətbiqinizi qurmaq və serverdə işə salmaq üçün bu əmri işlədin.

   QEYD: Bu addım yalnız yerli mühitiniz üçündür!

   ```shell
   ng serve
   ```

1. Tətbiqi tapmaq üçün brauzeri açın və `http://localhost:4200` ünvanına keçin.

1. Tətbiqin xətasız qurulduğunu təsdiqləyin.

   FAYDALI: O, əvvəlki dərsdəki kimi render olunmalıdır, çünki yeni komponent əlavə etsəniz də, hələ ki onu tətbiqin template-lərindən hər hansı birinə daxil etməmisiniz.

1. Növbəti addımları tamamlayarkən `ng serve` əmrini işlək vəziyyətdə saxlayın.
   </docs-step>

<docs-step title="Yeni komponenti tətbiqinizin düzümünə əlavə edin">
Bu addımda siz yeni `Home` komponentini tətbiqinizin kök komponenti olan `App`-ə əlavə edirsiniz ki, o tətbiqinizin düzümündə (layout) görünsün.

IDE-nizin **Edit** (Redaktə) bölməsində:

1.  Redaktorda `app.ts` faylını açın.
1.  `app.ts` daxilində fayl səviyyəsindəki import-lara bu sətri əlavə edərək `Home` komponentini import edin.

       <docs-code header="src/app/app.ts daxilində Home-u import edin" path="adev/src/content/tutorials/first-app/steps/03-HousingLocation/src/app/app.ts" visibleLines="[2]"/>

1.  `app.ts` faylındakı `@Component` daxilində `imports` massivini yeniləyin və `Home` əlavə edin.

       <docs-code header="src/app/app.ts daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/03-HousingLocation/src/app/app.ts" visibleLines="[6]"/>

1.  `app.ts` faylındakı `@Component` daxilində `template` property-sini aşağıdakı HTML kodunu daxil edəcək şəkildə yeniləyin.

       <docs-code language="angular-ts" header="src/app/app.ts daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/03-HousingLocation/src/app/app.ts" visibleLines="[7,16]"/>

1.  `app.ts` faylına etdiyiniz dəyişiklikləri yadda saxlayın.
1.  Əgər `ng serve` işləyirsə, tətbiq yenilənməlidir.
    Əgər `ng serve` işləmirsə, onu yenidən başladın.
    Tətbiqinizdəki _Hello world_ yazısı `Home` komponentindən gələn _home works!_ yazısına dəyişməlidir.
1.  Brauzerdə işləyən tətbiqi yoxlayın və tətbiqin yeniləndiyini təsdiqləyin.

   <img alt="brauzer pəncərəsində 'home works!' mətnini göstərən səhifə" src="assets/images/tutorials/first-app/homes-app-lesson-02-step-2.png">

</docs-step>

<docs-step title="`Home` komponentinə xüsusiyyətlər əlavə edin">

Bu addımda siz `Home` komponentinə xüsusiyyətlər əlavə edirsiniz.

Əvvəlki addımda siz standart `Home` komponentini tətbiqinizin template-inə əlavə etdiniz və onun standart HTML-i tətbiqdə göründü.
Bu addımda siz sonrakı dərsdə istifadə olunacaq axtarış filtri və düymə əlavə edirsiniz.
Hələlik `Home` komponentində olanlar bunlardır.
Nəzərə alın ki, bu addım sadəcə axtarış elementlərini düzümə əlavə edir, hələlik heç bir funksionallıq yoxdur.

Əgər başlanğıc layihəni yükləmək əvəzinə yeni bir Angular layihəsindən başlamısınızsa
(ng new): axtarış düyməsinin və giriş sərhədinin görünən olması üçün bu qlobal üslubları `src/styles.css` faylına əlavə edin:

```
:root {
  --primary-color: #605DC8;
  --secondary-color: #8B89E6;
  --accent-color: #e8e7fa;
  --shadow-color: #E8E8E8;
}

button.primary {
  padding: 10px;
  border: solid 1px var(--primary-color);
  background: var(--primary-color);
  color: white;
  border-radius: 8px;
}
```

IDE-nizin **Edit** (Redaktə) bölməsində:

1.  `first-app` qovluğunda redaktorda `home.ts` faylını açın.
1.  `home.ts` faylında `@Component` daxilində `template` property-sini bu kodla yeniləyin.

       <docs-code language="angular-ts" header="src/app/home/home.ts daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/03-HousingLocation/src/app/home/home.ts" visibleLines="[5,12]"/>

1.  Sonra redaktorda `home.css` faylını açın və məzmunu bu üslublarla yeniləyin.

    QEYD: Brauzerdə bunlar `src/app/home/home.ts` faylında `styles` massivinə yerləşdirilə bilər.

       <docs-code header="src/app/home/home.css daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/03-HousingLocation/src/app/home/home.css"/>

1.  Tətbiqin xətasız qurulduğunu təsdiqləyin. Tətbiqinizdə filtr sorğusu qutusu və düyməni tapmalısınız və onlar üslublanmış olmalıdır. Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.

   <img alt="homes-app-ın logo, filtr mətn giriş qutusu və axtarış düyməsini göstərən brauzer pəncərəsi" src="assets/images/tutorials/first-app/homes-app-lesson-02-step-3.png">
</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqiniz üçün yeni bir komponent yaratdınız və ona filtr redaktə kontrolu və düymə verdiniz.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="cli/generate/component" title="`ng generate component`"/>
  <docs-pill href="api/core/Component" title="`Component` arayışı"/>
  <docs-pill href="guide/components" title="Angular komponentlərinə ümumi baxış"/>
</docs-pill-row>
