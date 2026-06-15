# Angular servisləri

Bu təlimat dərsi bir Angular servisinin necə yaradılacağını və onu tətbiqinizə daxil etmək üçün aslılıq inyeksiyasından (dependency injection) necə istifadə olunacağını nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/-jRxG84AzCI?si=rieGfJawp9xJ00Sz"/>

## Nə öyrənəcəksiniz

Tətbiqinizin məlumatları tətbiqə ötürmək üçün bir servisi olacaq.
Bu dərsin sonunda servis məlumatları yerli, statik məlumatlardan oxuyacaq.
Sonrakı dərsdə siz servisi bir veb servisdən məlumat alacaq şəkildə yeniləyəcəksiniz.

## Servislərə konseptual baxış

Bu təlimat Angular servisləri və aslılıq inyeksiyasını (dependency injection - DI) təqdim edir.

### Angular servisləri

_Angular servisləri_ sizin Angular tətbiq məlumatlarını və tətbiqinizdəki bir neçə komponent tərəfindən istifadə edilə bilən funksiyaları ayırmaq üçün bir yol təqdim edir.
Birdən çox komponent tərəfindən istifadə olunmaq üçün bir servis _inyeksiya edilə bilən_ (injectable) edilməlidir.
İnyeksiya edilə bilən və bir komponent tərəfindən istifadə olunan servislər həmin komponentin aslılıqlarına (dependencies) çevrilir.
Komponent həmin servislərdən asılıdır və onlar olmadan fəaliyyət göstərə bilmir.

### Aslılıq inyeksiyası (Dependency injection)

_Aslılıq inyeksiyası_ tətbiq komponentlərinin aslılıqlarını və digər komponentlərin istifadə edə biləcəyi servisləri idarə edən mexanizmdir.

<docs-workflow>

<docs-step title="Tətbiqiniz üçün yeni bir servis yaradın">
Bu addım tətbiqiniz üçün inyeksiya edilə bilən bir servis yaradır.

IDE-nizin **Terminal** bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.
1. `first-app` qovluğunda yeni servisi yaratmaq üçün bu əmri işlədin:

   ```shell
   ng generate service housing --skip-tests
   ```

1. Tətbiqi qurmaq və `http://localhost:4200` ünvanında işə salmaq üçün `ng serve` işlədin.
1. Tətbiqin xətasız qurulduğunu təsdiqləyin.
   Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
   </docs-step>

<docs-step title="Yeni servisə statik məlumatlar əlavə edin">
Bu addım yeni servisinizə bəzi nümunə məlumatlar əlavə edir.
Sonrakı dərsdə siz statik məlumatları real tətbiqlərdə olduğu kimi məlumat almaq üçün bir veb interfeyslə əvəz edəcəksiniz.
Hələlik tətbiqinizin yeni servisi indiyə qədər `Home` komponentində yerli olaraq yaradılmış məlumatlardan istifadə edir.

IDE-nizin **Edit** (Redaktə) bölməsində:

1. `src/app/home/home.ts` faylında `Home` komponentindən `housingLocationList` dəyişənini və onun massiv dəyərini kopyalayın.
1. `src/app/housing.service.ts` faylında:
   1. `HousingService` class-ının daxilində, əvvəlki addımda `Home` komponentindən kopyaladığınız dəyişəni yapışdırın.
   1. `HousingService` class-ının daxilində, indicə kopyaladığınız məlumatlardan sonra bu funksiyaları yapışdırın.
      Bu funksiyalar aslılıqlara servisin məlumatlarına daxil olmağa imkan verir.

      <docs-code header="src/app/housing.service.ts daxilində servis funksiyaları" path="adev/src/content/tutorials/first-app/steps/10-routing/src/app/housing.service.ts" visibleLines="[112,118]"/>

      Gələcək dərsdə bu funksiyalara ehtiyacınız olacaq. Hələlik bu funksiyaların id-yə görə spesifik bir `HousingLocation` və ya bütün siyahını qaytardığını başa düşmək kifayətdir.

   1. `HousingLocation` üçün fayl səviyyəsində import əlavə edin.

      <docs-code header="src/app/housing.service.ts daxilində HousingLocation tipini import edin" path="adev/src/content/tutorials/first-app/steps/10-routing/src/app/housing.service.ts" visibleLines="[2]"/>

1. Tətbiqin xətasız qurulduğunu təsdiqləyin.
   Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
   </docs-step>

<docs-step title="Yeni servisi `Home` komponentinə inyeksiya edin">
Bu addım yeni servisi tətbiqinizin `Home` komponentinə inyeksiya edir ki, o tətbiqin məlumatlarını bir servisdən oxuya bilsin.
Sonrakı dərsdə siz statik məlumatları real tətbiqlərdə olduğu kimi canlı məlumat mənbəyi ilə əvəz edəcəksiniz.

IDE-nizin **Edit** (Redaktə) bölməsində, `src/app/home/home.ts` faylında:

1.  `src/app/home/home.ts` faylının yuxarı hissəsində `@angular/core`-dan import edilən elementlərə `inject`-i əlavə edin. Bu, `inject` funksiyasını `Home` class-ına import edəcək.

       <docs-code language="angular-ts" header="src/app/home/home.ts üçün yeniləmə" path="adev/src/content/tutorials/first-app/steps/10-routing/src/app/home/home.ts" visibleLines="[1]"/>

1.  `HousingService` üçün yeni bir fayl səviyyəsində import əlavə edin:

       <docs-code language="angular-ts" header="src/app/home/home.ts faylına import əlavə edin" path="adev/src/content/tutorials/first-app/steps/10-routing/src/app/home/home.ts" visibleLines="[4]"/>

1.  `Home` komponentindən `housingLocationList` massiv girişlərini silin və `housingLocationList`-ə boş massiv (`[]`) dəyərini təyin edin. Bir neçə addımdan sonra məlumatları `HousingService`-dən çəkmək üçün kodu yeniləyəcəksiniz.

1.  `Home` komponentində yeni servisi inyeksiya etmək və tətbiq üçün məlumatları başlanğıc vəziyyətinə gətirmək üçün aşağıdakı kodu əlavə edin. `constructor` bu komponent yaradıldıqda işləyən ilk funksiyadır. `constructor`-dakı kod `housingLocationList`-ə `getAllHousingLocations` çağırışından qaytarılan dəyəri təyin edəcək.

       <docs-code language="angular-ts" header="src/app/home/home.ts daxilində servisdən məlumatları inisializasiya edin" path="adev/src/content/tutorials/first-app/steps/10-routing/src/app/home/home.ts" visibleLines="[23,30]"/>

1.  `src/app/home/home.ts` faylına etdiyiniz dəyişiklikləri yadda saxlayın və tətbiqinizin xətasız qurulduğunu təsdiqləyin.
    Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
    </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqinizə bir Angular servisi əlavə etdiniz və onu `Home` class-ına inyeksiya etdiniz.
Bu, tətbiqinizin məlumatlarını necə əldə etdiyini hissələrə ayırır.
Hələlik yeni servis məlumatlarını statik məlumat massivindən alır.
Sonrakı dərsdə siz servisi məlumatlarını bir API endpoint-indən alacaq şəkildə refaktor edəcəksiniz.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/di/creating-and-using-services" title="İnyeksiya edilə bilən servisin yaradılması"/>
  <docs-pill href="guide/di" title="Angular-da aslılıq inyeksiyası"/>
  <docs-pill href="cli/generate/service" title="ng generate service"/>
  <docs-pill href="cli/generate" title="ng generate"/>
</docs-pill-row>
