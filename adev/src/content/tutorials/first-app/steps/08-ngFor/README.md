# Komponentdə obyektləri siyahıya almaq üçün @for istifadə edin

Bu təlimat dərsi template-də dinamik şəkildə təkrarlanan məlumatları göstərmək üçün Angular template-lərində `@for` blokundan necə istifadə olunacağını nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/eM3zi_n7lNs?si=MIl5NcRxvcLjYt5f&amp;start=477"/>

QEYD: Bu video köhnə sintaksisi əks etdirir, lakin əsas anlayışlar qüvvədə qalır.

## Nə öyrənəcəksiniz

- Tətbiqə bir məlumat dəsti (data set) əlavə etmiş olacaqsınız.
- Tətbiqiniz `@for` istifadə edərək yeni məlumat dəstindən elementlərin siyahısını göstərəcək.

## `@for` haqqında konseptual baxış

Angular-da `@for`, template-də məlumatları dinamik şəkildə təkrarlamaq üçün istifadə olunan xüsusi bir [control flow blokudur](/guide/templates/control-flow). Sadə JavaScript-də siz for dövründən istifadə edərdiniz - `@for` Angular template-ləri üçün oxşar funksionallıq təmin edir.

Siz massivlər və hətta asinxron dəyərlər üzərində iterasiya etmək üçün `@for`-dan istifadə edə bilərsiniz. Bu dərsdə siz üzərində iterasiya aparmaq üçün yeni bir məlumat massivi əlavə edəcəksiniz.

Daha ətraflı izah üçün zəhmət olmasa [control flow](guide/templates/control-flow#repeat-content-with-the-for-block) bələdçisinə müraciət edin.

<docs-workflow>

<docs-step title="`Home` komponentinə yaşayış yeri məlumatlarını əlavə edin">

`Home` komponentində yalnız bir yaşayış yeri var. Bu addımda siz `HousingLocation` girişlərindən ibarət bir massiv əlavə edəcəksiniz.

1. `src/app/home/home.ts` faylından `housingLocation` property-sini `Home` class-ından silin.
1. `Home` class-ını `housingLocationList` adlı property-yə sahib olacaq şəkildə yeniləyin. Kodunuzu aşağıdakı koda uyğunlaşdırın:
   <docs-code language="angular-ts"  header="home.ts daxilində housingLocationList property-sini əlavə edin" path="adev/src/content/tutorials/first-app/steps/09-services/src/app/home/home.ts" visibleLines="26-131"/>

   VACİB: `@Component` dekoratorunu silməyin, növbəti addımda həmin kodu yeniləyəcəksiniz.

</docs-step>

<docs-step title="`@for` istifadə etmək üçün `Home` template-ini yeniləyin">
İndi tətbiqin `@for` blokundan istifadə edərək brauzerdə girişləri göstərmək üçün istifadə edə biləcəyiniz bir məlumat dəsti (dataset) var.

1. Template kodunda `<app-housing-location>` teqini bu şəkildə yeniləyin:
   <docs-code language="angular-ts"  header="home.ts daxilində Home template-inə @for əlavə edin" path="adev/src/content/tutorials/first-app/steps/09-services/src/app/home/home.ts" visibleLines="[15,19]"/>

   Nəzərə alın ki, `[housingLocation] = "housingLocation"` kodunda `housingLocation` dəyəri indi `@for` blokunda istifadə olunan dəyişənə müraciət edir. Bu dəyişiklikdən əvvəl o, `Home` class-ındakı property-yə müraciət edirdi.

1. Bütün dəyişiklikləri yadda saxlayın.

1. Brauzeri yeniləyin və tətbiqin indi yaşayış yerlərindən ibarət bir şəbəkə (grid) render etdiyini təsdiqləyin.

<section class="lightbox">
<img alt="homes-app-ın logo, filtr mətn giriş qutusu, axtarış düyməsi və yaşayış yeri kartlarından ibarət şəbəkəni göstərən brauzer pəncərəsi" src="assets/images/tutorials/first-app/homes-app-lesson-08-step-2.png">
</section>

</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz Angular template-lərində məlumatları dinamik şəkildə təkrarlamaq üçün `@for` blokundan istifadə etdiniz. Həmçinin Angular tətbiqində istifadə olunacaq yeni bir məlumat massivi əlavə etdiniz. Tətbiq indi brauzerdə yaşayış yerlərinin siyahısını dinamik şəkildə render edir.

Tətbiq formalaşmağa başlayır, əla işdir.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/templates/control-flow" title="Control flow blokları"/>
  <docs-pill href="guide/templates/control-flow#repeat-content-with-the-for-block" title="@for bələdçisi"/>
  <docs-pill href="/api/core/@for" title="@for"/>
</docs-pill-row>
