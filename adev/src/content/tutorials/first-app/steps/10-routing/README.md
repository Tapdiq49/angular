# Tətbiqə marşrutlar (routes) əlavə edin

Bu təlimat dərsi tətbiqinizə marşrutları necə əlavə edəcəyinizi nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/r5DEBMuStPw?si=H6Bx6nLJoMLaMxkx" />

VACİB: Marşrutlaşdırmanı (routing) öyrənmək üçün yerli mühitinizdən istifadə etməyi tövsiyə edirik.

## Nə öyrənəcəksiniz

Bu dərsin sonunda tətbiqiniz marşrutlaşdırma dəstəyinə sahib olacaq.

## Marşrutlaşdırmaya (routing) konseptual baxış

Bu təlimat Angular-da marşrutlaşdırmanı təqdim edir. Marşrutlaşdırma tətbiqdəki bir komponentdən digərinə naviqasiya etmək qabiliyyətidir. [Təksəhifəli tətbiqlərdə (SPA)](guide/routing) istifadəçi üçün tələb olunan görünüşü təmsil etmək üçün səhifənin yalnız hissələri yenilənir.

[Angular Router](guide/routing) istifadəçilərə marşrutları elan etməyə və həmin marşrut tətbiq tərəfindən tələb edildikdə ekranda hansı komponentin göstərilməli olduğunu müəyyən etməyə imkan verir.

Bu dərsdə siz təfərrüat (details) səhifəsinə naviqasiya etmək üçün tətbiqinizdə marşrutlaşdırmanı aktivləşdirəcəksiniz.

<docs-workflow>

<docs-step title="Standart details komponenti yaradın">
1. Terminaldan `Details` komponentini yaratmaq üçün aşağıdakı əmri daxil edin:

    ```shell
    ng generate component details
    ```

    Bu komponent verilmiş yaşayış yeri haqqında daha çox məlumat verən təfərrüat səhifəsini təmsil edəcək.

</docs-step>

<docs-step title="Tətbiqə marşrutlaşdırma əlavə edin">
1.  `src/app` qovluğunda `routes.ts` adlı fayl yaradın. Bu fayl tətbiqdəki marşrutları müəyyən edəcəyimiz yerdir.

2.  `main.ts` faylında tətbiqdə marşrutlaşdırmanı aktivləşdirmək üçün aşağıdakı yeniləmələri edin:
    1.  Marşrutlar faylını və `provideRouter` funksiyasını import edin:

          <docs-code header="src/main.ts daxilində marşrutlaşdırma təfərrüatlarını import edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/main.ts" visibleLines="[7,8]"/>

    1.  Marşrutlaşdırma konfiqurasiyasını daxil etmək üçün `bootstrapApplication` çağırışını yeniləyin:

          <docs-code header="src/main.ts daxilində router konfiqurasiyasını əlavə edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/main.ts" visibleLines="[10,17]"/>

3.  `src/app/app.ts` faylında marşrutlaşdırmanı istifadə etmək üçün komponenti yeniləyin:
    1.  `RouterOutlet` və `RouterLink` router direktivləri üçün fayl səviyyəsində importlar əlavə edin:

          <docs-code language="angular-ts" header="src/app/app.ts daxilində router direktivlərini import edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/app/app.ts" visibleLines="[3]"/>

    1.  `RouterOutlet` və `RouterLink`-i `@Component` metadata importlarına əlavə edin.

          <docs-code language="angular-ts" header="src/app/app.ts daxilində komponent importlarına router direktivlərini əlavə edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/app/app.ts" visibleLines="[6]"/>

    1.  `template` property-sində `<app-home />` teqini `<router-outlet>` direktivi ilə əvəz edin və ana səhifəyə geri qayıtmaq üçün link əlavə edin. Kodunuz bu koda uyğun olmalıdır:

          <docs-code language="angular-ts" header="src/app/app.ts daxilində router-outlet əlavə edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/app/app.ts" visibleLines="[7,18]"/>

</docs-step>

<docs-step title="Yeni komponentə marşrut əlavə edin">
Əvvəlki addımda template-dəki `<app-home>` komponentinə olan müraciəti sildiniz. Bu addımda həmin komponent üçün yeni bir marşrut əlavə edəcəksiniz.

1. `routes.ts` faylında marşrut yaratmaq üçün aşağıdakı yeniləmələri yerinə yetirin.
   1. `Home`, `Details` komponentləri və marşrut təriflərində istifadə edəcəyiniz `Routes` tipi üçün fayl səviyyəsində importlar əlavə edin.

      <docs-code header="Komponentləri və Routes tipini import edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/app/routes.ts" visibleLines="[1,3]"/>

   1. `Routes` tipində `routeConfig` adlı bir dəyişən təyin edin və tətbiq üçün iki marşrut müəyyən edin:
      <docs-code header="Tətbiqə marşrutlar əlavə edin" path="adev/src/content/tutorials/first-app/steps/11-details-page/src/app/routes.ts" visibleLines="[5,18]"/>

      `routeConfig` massivindəki girişlər tətbiqdəki marşrutları təmsil edir. Birinci giriş URL `''` ilə uyğunlaşdıqda `Home` komponentinə naviqasiya edir. İkinci giriş gələcək dərsdə yenidən baxılacaq xüsusi bir formatdan istifadə edir.

1. Bütün dəyişiklikləri yadda saxlayın və tətbiqin brauzerdə işlədiyini təsdiqləyin. Tətbiq hələ də yaşayış yerlərinin siyahısını göstərməlidir.
   </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqinizdə marşrutlaşdırmanı aktivləşdirdiniz, həmçinin yeni marşrutlar təyin etdiniz. İndi tətbiqiniz görünüşlər arasında naviqasiyanı dəstəkləyə bilər. Növbəti dərsdə verilmiş yaşayış yeri üçün "details" (təfərrüat) səhifəsinə necə keçəcəyinizi öyrənəcəksiniz.

Tətbiqinizlə bağlı böyük irəliləyiş əldə edirsiniz, afərin.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/routing" title="Angular-da Marşrutlaşdırmaya Ümumi Baxış"/>
  <docs-pill href="guide/routing/common-router-tasks" title="Ümumi Marşrutlaşdırma Tapşırıqları"/>
</docs-pill-row>
