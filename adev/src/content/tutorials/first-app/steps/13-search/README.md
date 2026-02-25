# Tətbiqinizə axtarış xüsusiyyətini əlavə edin

Bu təlimat dərsi Angular tətbiqinizə axtarış funksionallığını necə əlavə edəcəyinizi nümayiş etdirir.

Tətbiq istifadəçilərə tətbiq tərəfindən təqdim olunan məlumatlar arasında axtarış aparmağa və yalnız daxil edilmiş terminə uyğun gələn nəticələri göstərməyə imkan verəcək.

<docs-video src="https://www.youtube.com/embed/5K10oYJ5Y-E?si=TiuNKx_teR9baO7k&amp;start=457"/>

VACİB: Təlimatın bu addımı üçün yerli mühitinizdən istifadə etməyi tövsiyə edirik.

## Nə öyrənəcəksiniz

- Tətbiqiniz uyğun yaşayış yerlərini axtarmaq üçün formadan gələn məlumatları istifadə edəcək
- Tətbiqiniz yalnız uyğun gələn yaşayış yerlərini göstərəcək

<docs-workflow>

<docs-step title="Home komponentinin xüsusiyyətlərini (properties) yeniləyin">
Bu addımda, filtrləmə üçün istifadə edəcəyiniz yeni bir massiv property-sində məlumatları saxlamaq üçün `Home` class-ını yeniləyəcəksiniz.

1. `src/app/home/home.ts` faylında class-a `filteredLocationList` adlı yeni property əlavə edin.

   <docs-code header="home.ts daxilində filteredLocationList property-sini əlavə edin" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[27]"/>

   `filteredLocationList` istifadəçi tərəfindən daxil edilən axtarış meyarlarına uyğun gələn dəyərləri saxlayacaq.

1. Səhifə yüklənərkən `filteredLocationList` standart olaraq bütün yaşayış yerlərinin dəyərlərini ehtiva etməlidir. Dəyəri təyin etmək üçün `Home` komponentinin `constructor`-ını yeniləyin.

<docs-code header="filteredLocationList-in dəyərini təyin edin" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[29,32]"/>

</docs-step>

<docs-step title="Home komponentinin template-ini yeniləyin">
`Home` komponentində artıq istifadəçidən girişi tutmaq üçün istifadə edəcəyiniz giriş sahəsi var. Həmin string mətn nəticələri filtrləmək üçün istifadə olunacak.

1. `Home` template-ində `input` elementinə `#filter` adlı bir template dəyişəni daxil etmək üçün yeniləyin.

<docs-code language="angular-ts" header="home.ts daxilində input HTML elementinə template dəyişəni əlavə edin" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[12]"/>
Bu nümunə `input` elementinə daxil olmaq üçün bir [template müraciət dəyişənindən (template reference variable)](guide/templates) istifadə edir.

1. Növbəti olaraq, "Search" düyməsinə bir event handler bağlamaq üçün komponent template-ini yeniləyin.

   <docs-code language="angular-ts" header="home.ts daxilində düymə klik eventini bir metoda bağlayın" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[13]"/>

   `button` elementində `click` event-inə binding etməklə siz `filterResults` funksiyasını çağıra bilirsiniz. Funksiyanın arqumenti `filter` template dəyişəninin `value` property-sidir. Xüsusilə, `input` HTML elementindən gələn `.value` property-si.

1. Sonuncu template yeniləməsi `@for` direktivinədir. `filteredLocationList` massivindəki dəyərlər üzərində iterasiya aparmaq üçün `@for`-u yeniləyin.

<docs-code header="home.ts daxilində @for template direktivini yeniləyin" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[17,19]" language="html"/>

</docs-step>

<docs-step title="Event handler funksiyasını implementasiya edin">
Template `filterResults` funksiyasını `click` event-inə bağlamaq üçün yeniləndi. Növbəti tapşırığınız `Home` class-ında `filterResults` funksiyasını implementasiya etməkdir.

1.  `Home` class-ına `filterResults` funksiyasının implementasiyasını daxil etmək üçün yeniləyin.

     <docs-code header="filterResults funksiya implementasiyasını əlavə edin" path="adev/src/content/tutorials/first-app/steps/14-http/src/app/home/home.ts" visibleLines="[34,43]"/>

    Bu funksiya `text` parametrinin dəyərini `housingLocation.city` property-si ilə müqayisə etmək üçün `String` `filter` funksiyasından istifadə edir. Maraqlı bir məşq kimi siz bu funksiyanı hər hansı bir property və ya bir neçə property ilə yoxlamaq üçün yeniləyə bilərsiniz.

1.  Kodunuzu yadda saxlayın.

1.  Brauzeri yeniləyin və mətn daxil etdikdən sonra "Search" düyməsini kliklədikdə yaşayış yeri məlumatlarını şəhərə görə axtara bildiyinizi təsdiqləyin.

      <img alt="istifadəçi girişinə əsaslanan filtrlənmiş axtarış nəticələri" src="assets/images/tutorials/first-app/homes-app-lesson-13-step-3.png">

    </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqinizi template dəyərləri ilə qarşılıqlı əlaqədə olmaq üçün template dəyişənlərindən istifadə etmək və event binding və massiv funksiyalarından istifadə edərək axtarış funksionallığı əlavə etmək üçün yenilədiniz.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/templates" title="Template Dəyişənləri"/>
  <docs-pill href="guide/templates/event-listeners" title="Event Handling"/>
</docs-pill-row>
