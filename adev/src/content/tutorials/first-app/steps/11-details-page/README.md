# Təfərrüat səhifəsini tətbiqə inteqrasiya edin

Bu təlimat dərsi təfərrüat (details) səhifəsini tətbiqinizə necə bağlayacağınızı nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/-jRxG84AzCI?si=CbqIpmRpwp5ZZDnu&amp;start=345"/>

VACİB: Marşrutlaşdırmanı öyrənmək üçün yerli mühitinizdən istifadə etməyi tövsiyə edirik.

## Nə öyrənəcəksiniz

Bu dərsin sonunda tətbiqiniz təfərrüat səhifəsinə marşrutlaşdırma dəstəyinə sahib olacaq.

## Marşrut parametrləri ilə marşrutlaşdırmaya konseptual baxış

Hər bir yaşayış yerinin istifadəçi həmin element üçün təfərrüat səhifəsinə keçdikdə göstərilməli olan xüsusi detalları var. Bu məqsədə nazil olmaq üçün marşrut parametrlərindən istifadə etməli olacaqsınız.

Marşrut parametrləri marşrut URL-inizin tərkib hissəsi kimi dinamik məlumatları daxil etməyə imkan verir. İstifadəçinin hansı yaşayış yerinə kliklədiyini müəyyən etmək üçün `HousingLocation` tipinin `id` property-sindən istifadə edəcəksiniz.

<docs-workflow>

<docs-step title="Dinamik naviqasiya üçün `routerLink` istifadəsi">
10-cu dərsdə siz `src/app/routes.ts` faylına marşrut parametrini, yəni `id`-ni müəyyən edən xüsusi seqmenti daxil edən ikinci bir marşrut əlavə etdiniz:

```
'details/:id'
```

Bu halda, `:id` dinamikdir və marşrutun kod tərəfindən necə tələb olunduğuna əsasən dəyişəcək.

1.  `src/app/housing-location/housing-location.ts` faylında `section` elementinə bir anchor teqi əlavə edin və `routerLink` direktivini daxil edin:

    <docs-code language="angular-ts" header="housing-location.ts daxilində routerLink direktivi ilə bir anchor əlavə edin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/housing-location/housing-location.ts" visibleLines="[18]"/>

    `routerLink` direktivi Angular-ın router-inə tətbiqdə dinamik linklər yaratmağa imkan verir. `routerLink`-ə təyin edilən dəyər iki girişli bir massivdir: yolun statik hissəsi və dinamik məlumat.

    `routerLink`-in template-də işləməsi üçün '@angular/router'-dan `RouterLink` və `RouterOutlet` üçün fayl səviyyəsində import əlavə edin, sonra hər ikisini daxil etmək üçün komponentin `imports` massivini yeniləyin.

1.  Bu nöqtədə marşrutlaşdırmanın tətbiqinizdə işlədiyini təsdiqləyə bilərsiniz. Brauzerdə ana səhifəni yeniləyin və yaşayış yeri üçün "Learn More" düyməsini klikləyin.

      <img alt="'details works!' mətnini göstərən təfərrüat səhifəsi" src="assets/images/tutorials/first-app/homes-app-lesson-11-step-1.png">

</docs-step>

<docs-step title="Marşrut parametrlərini əldə edin">
Bu addımda siz `Details` komponentində marşrut parametrini əldə edəcəksiniz. Hazırda tətbiq `details works!` göstərir. Sonra marşrut parametrləri vasitəsilə ötürülən `id` dəyərini göstərmək üçün kodu yeniləyəcəksiniz.

1.  `src/app/details/details.ts` faylında `Details` komponentində istifadə etməli olacağınız funksiyaları, class-ları və servisləri import etmək üçün template-i yeniləyin:

       <docs-code header="Fayl səviyyəsində importları yeniləyin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/details/details.ts" visibleLines="[1,4]"/>

1.  `housingLocationId` dəyərini göstərmək üçün `@Component` dekoratorunun `template` property-sini yeniləyin:

          ```angular-ts
          template: `<p>details works! {{ housingLocationId }}</p>`,
          ```

1.  `Details` class-ının gövdəsini aşağıdakı kodla yeniləyin:

          ```ts
          export class Details {
             route: ActivatedRoute = inject(ActivatedRoute);
             housingLocationId = -1;
             constructor() {
             this.housingLocationId = Number(this.route.snapshot.params['id']);
             }
          }
          ```

    Bu kod `Details` komponentinə cari marşrut haqqında məlumatlara daxil olmağa imkan verən `ActivatedRoute` router xüsusiyyətinə çıxış verir. `constructor`-da kod marşrutdan əldə edilən `id` parametrini string-dən rəqəmə (number) çevirir.

1.  Bütün dəyişiklikləri yadda saxlayın.

1.  Brauzerdə yaşayış yerlərindən birinin "Learn More" linkinə klikləyin və səhifədə göstərilən rəqəmsal dəyərin həmin yer üçün məlumatlardakı `id` property-si ilə uyğun gəldiyini təsdiqləyin.
    </docs-step>

<docs-step title="`Details` komponentini fərdiləşdirin">
Artıq marşrutlaşdırma tətbiqdə düzgün işlədiyindən, bu `Details` komponentinin template-ini marşrut parametri üçün yaşayış yerini təmsil edən xüsusi məlumatları göstərmək üçün yeniləmək üçün əla vaxtdır.

Məlumatlara daxil olmaq üçün `HousingService` çağırışı əlavə edəcəksiniz.

1. Template kodunu aşağıdakı koda uyğun yeniləyin:

   <docs-code language="angular-ts" header="src/app/details/details.ts daxilində Details template-ini yeniləyin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/details/details.ts" visibleLines="[8,29]"/>

   Nəzərə alın ki, `housingLocation` xüsusiyyətlərinə `?` optional chaining operatoru ilə müraciət edilir. Bu, `housingLocation` dəyərinin null və ya undefined olduğu halda tətbiqin çökməməsini təmin edir.

1. `Details` class-ının gövdəsini aşağıdakı koda uyğun yeniləyin:

   <docs-code language="angular-ts" header="src/app/details/details.ts daxilində Details class-ını yeniləyin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/details/details.ts" visibleLines="[32,41]"/>

   İndi komponent seçilmiş yaşayış yerinə əsasən düzgün məlumatları göstərmək üçün koda sahibdir. `constructor` indi marşrut parametrini `getHousingLocationById` servis funksiyasına arqument kimi ötürmək üçün `HousingService` çağırışını daxil edir.

1. Aşağıdakı üslubları `src/app/details/details.css` faylına kopyalayın:

   <docs-code header="Details üçün üslublar əlavə edin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/details/details.css" visibleLines="[1,71]"/>

   və dəyişikliklərinizi yadda saxlayın

1. `Details` komponentində üslublar üçün mənbə kimi indicə yaradılmış `details.css` faylını istifadə edin:
   <docs-code language="angular-ts" header="Yaradılmış css faylını istifadə etmək üçün details.ts-i yeniləyin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/details/details.ts" visibleLines="[30]"/>

1. Brauzerdə səhifəni yeniləyin və hər hansı bir yaşayış yeri üçün "Learn More" linkinə kliklədikdə təfərrüat səhifəsinin həmin seçilmiş element üçün məlumatlara əsasən düzgün informasiyanı göstərdiyini təsdiqləyin.

<img alt="Ev məlumatlarını siyahıya alan təfərrüat səhifəsi" src="assets/images/tutorials/first-app/homes-app-lesson-11-step-3.png">

</docs-step>

<docs-step title="`Home` komponentində naviqasiyanı yoxlayın">
Əvvəlki dərsdə siz `App` template-ini `routerLink` daxil edəcək şəkildə yenilədiniz. Bu kodun əlavə edilməsi loqo klikləndikdə tətbiqinizin `Home` komponentinə geri naviqasiyasını aktivləşdirdi.

1.  Kodunuzun aşağıdakı ilə uyğun gəldiyini təsdiqləyin:

      <docs-code language="angular-ts" header="app.ts daxilində routerLink-i təsdiqləyin" path="adev/src/content/tutorials/first-app/steps/12-forms/src/app/app.ts" visibleLines="[8,19]"/>

    Kodunuz artıq yenilənmiş olmalıdır, lakin əmin olmaq üçün təsdiqləyin.

    </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz təfərrüat səhifələrini göstərmək üçün marşrutlaşdırma əlavə etdiniz.

İndi siz aşağıdakıları bilirsiniz:

- marşruta məlumat ötürmək üçün marşrut parametrlərini istifadə etmək
- marşrut yaratmaq üçün dinamik məlumatları istifadə etmək məqsədilə `routerLink` direktivini istifadə etmək
- spesifik yaşayış yeri məlumatlarını göstərmək üçün `HousingService`-dən məlumatları əldə etmək üçün marşrut parametrini istifadə etmək.

İndiyə qədər həqiqətən əla iş görmüsünüz.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/routing/read-route-state#get-information-about-the-current-route-with-activatedroute" title="Marşrut Parametrləri"/>
  <docs-pill href="guide/routing" title="Angular-da Marşrutlaşdırmaya Ümumi Baxış"/>
  <docs-pill href="guide/routing/common-router-tasks" title="Ümumi Marşrutlaşdırma Tapşırıqları"/>
  <docs-pill href="https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/Optional_chaining" title="Optional Chaining Operatoru"/>
</docs-pill-row>
