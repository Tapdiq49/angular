# Angular tətbiqinizə forma əlavə etmək

Bu təlimat dərsi Angular tətbiqinə istifadəçi məlumatlarını toplayan bir formanın necə əlavə ediləcəyini nümayiş etdirir.
Bu dərs funksional bir Angular tətbiqi ilə başlayır və ona formanın necə əlavə olunacağını göstərir.

Formanın topladığı məlumatlar yalnız tətbiqin servisinə göndərilir və servis onu brauzerin konsoluna yazır.
Formanın məlumatlarını göndərmək və qəbul etmək üçün REST API istifadəsi bu dərsdə əhatə olunmur.

<docs-video src="https://www.youtube.com/embed/kWbk-dOJaNQ?si=FYMXGdUiT-qh321h"/>

VACİB: Təlimatın bu addımı üçün yerli mühitinizdən istifadə etməyi tövsiyə edirik.

## Nə öyrənəcəksiniz

- Tətbiqinizin bir forması var ki, orada istifadəçilər tətbiqinizin servisinə göndərilən məlumatları daxil edə bilərlər.
- Servis formadan gələn məlumatları brauzerin konsol loquna yazır.

<docs-workflow>

<docs-step title="Form məlumatlarını göndərmək üçün bir metod əlavə edin">
Bu addım tətbiqinizin servisinə form məlumatlarını qəbul edən və onları məlumatın təyinat yerinə göndərən bir metod əlavə edir.
Bu nümunədə metod formadan gələn məlumatları brauzerin konsol loquna yazır.

IDE-nizin **Edit** (Redaktə) bölməsində:

1.  `src/app/housing.service.ts` faylında `HousingService` class-ının daxilində aşağıdakı metodu class tərifinin sonuna yapışdırın.

       <docs-code header="src/app/housing.service.ts daxilində submit metodu" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/housing.service.ts" visibleLines="[120,124]"/>

1.  Tətbiqin xətasız qurulduğunu təsdiqləyin.
    Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
    </docs-step>

<docs-step title="Təfərrüat səhifəsinə forma funksiyalarını əlavə edin">
Bu addım təfərrüat səhifəsinə formanın qarşılıqlı əlaqələrini idarə edən kodu əlavə edir.

IDE-nizin **Edit** (Redaktə) bölməsində, `src/app/details/details.ts` faylında:

1.  Faylın yuxarı hissəsindəki `import` bəyanatlarından sonra Angular forma class-larını import etmək üçün aşağıdakı kodu əlavə edin.

       <docs-code header="src/app/details/details.ts daxilində forma import-ları" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/details/details.ts" visibleLines="[5]"/>

1.  `Details` dekorator metadata-sında `imports` property-sini aşağıdakı kodla yeniləyin:

       <docs-code header="src/app/details/details.ts daxilində imports direktivi" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/details/details.ts" visibleLines="[9]"/>

1.  `Details` class-ında, `constructor()` metodundan əvvəl form obyektini yaratmaq üçün aşağıdakı kodu əlavə edin.

       <docs-code header="src/app/details/details.ts daxilində template direktivi" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/details/details.ts" visibleLines="[52,56]"/>

    Angular-da `FormGroup` və `FormControl` forma qurmağa imkan verən tiplərdir. `FormControl` tipi standart dəyər təmin edə və forma məlumatlarını formalaşdıra bilər. Bu nümunədə `firstName` bir `string`-dir və standart dəyəri boş string-dir.

1.  `Details` class-ında, `constructor()` metodundan sonra **Apply now** düyməsinin kliklənməsini idarə etmək üçün aşağıdakı kodu əlavə edin.

       <docs-code header="src/app/details/details.ts daxilində template direktivi" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/details/details.ts" visibleLines="[62,68]"/>

    Bu düymə hələ mövcud deyil - onu növbəti addımda əlavə edəcəksiniz. Yuxarıdakı kodda `FormControl`-lar `null` qaytara bilər. Bu kod, əgər dəyər `null` olarsa, boş string-ə keçmək üçün nullish coalescing operatorundan istifadə edir.

1.  Tətbiqin xətasız qurulduğunu təsdiqləyin.
    Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
    </docs-step>

<docs-step title="Təfərrüat səhifəsinə formanın strukturunu əlavə edin">
Bu addım təfərrüat səhifəsinə formanı göstərən strukturu əlavə edir.

IDE-nizin **Edit** (Redaktə) bölməsində, `src/app/details/details.ts` faylında:

1. `Details` dekorator metadata-sında formanın strukturunu əlavə etmək üçün `template` HTML-i aşağıdakı koda uyğun yeniləyin.

   <docs-code language="angular-ts" header="src/app/details/details.ts daxilində template direktivi" path="adev/src/content/tutorials/first-app/steps/13-search/src/app/details/details.ts" visibleLines="[10,45]"/>

   Template indi `(submit)="submitApplication()"` adlı bir event handler daxil edir. Angular template kodunda event-ləri müəyyən etmək üçün event adının ətrafında mötərizə sintaksisindən istifadə edir. Bərabərlik işarəsinin sağ tərəfindəki kod bu event tətikləndikdə (trigger) icra edilməli olan koddur. Siz brauzer event-lərinə və xüsusi (custom) event-lərə bağlana bilərsiniz.

1. Tətbiqin xətasız qurulduğunu təsdiqləyin.
   Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.

   <img alt="bu məkanda yaşamaq üçün müraciət forması olan təfərrüat səhifəsi" src="assets/images/tutorials/first-app/homes-app-lesson-12-step-3.png">

</docs-step>

<docs-step title="Tətbiqinizin yeni formasını test edin">
Bu addım yeni formanın məlumatları tətbiqə göndərildikdə konsol loqunda göründüyünü yoxlamaq üçün test edir.

1. IDE-nizin **Terminal** bölməsində, əgər artıq işləmirsə, `ng serve` işlədin.
1. Brauzerinizdə tətbiqinizi `http://localhost:4200` ünvanında açın.
1. Brauzerdə tətbiqin üzərində sağ klikləyin və kontekst menyusundan **Inspect** (Yoxla) seçin.
1. Proqramçı alətləri (developer tools) pəncərəsində **Console** nişanını seçin.
   Növbəti addımlar üçün proqramçı alətləri pəncərəsinin görünən olduğundan əmin olun.
1. Tətbiqinizdə:
   1. Bir yaşayış yeri seçin və ev haqqında detalları görmək üçün **Learn more** klikləyin.
   2. Evin təfərrüat səhifəsində yeni formanı tapmaq üçün aşağı skrol edin.
   3. Formanın sahələrinə məlumat daxil edin - hər hansı məlumat olar.
   4. Məlumatları göndərmək üçün **Apply now** seçin.
1. Proqramçı alətləri pəncərəsində forma məlumatlarınızı tapmaq üçün loq çıxışını nəzərdən keçirin.
   </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz Angular-ın formalar xüsusiyyətindən istifadə edərək tətbiqinizə forma əlavə etmək üçün tətbiqinizi yenilədiniz və formada tutulan məlumatları bir event handler vasitəsilə komponentə bağladınız.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/forms" title="Angular Formaları"/>
  <docs-pill href="guide/templates/event-listeners" title="Event Handling"/>
</docs-pill-row>
