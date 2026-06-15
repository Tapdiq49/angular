# Komponentin template-inə interpolation əlavə edin

Bu təlimat dərsi template-də dinamik məlumatları göstərmək üçün Angular template-lərinə interpolation əlavə etməyi nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/eM3zi_n7lNs?si=IFAly3Ss8dwqFx8N&amp;start=338"/>

## Nə öyrənəcəksiniz

- Tətbiqiniz `HousingLocation` template-ində interpolyasiya olunmuş (interpolated) dəyərləri göstərəcək.
- Tətbiqiniz brauzerdə yaşayış yeri məlumatlarını render edəcək.

## Interpolation (İnterpolyasiya) haqqında konseptual baxış

Bu addımda siz interpolation istifadə edərək template-də `input` property-lərindən oxunan dəyərləri göstərəcəksiniz.

Angular template-lərində `{{ expression }}` istifadə edərək property-lərdən, `inputs`-dan və etibarlı JavaScript ifadələrindən gələn dəyərləri render edə bilərsiniz.

Daha ətraflı izah üçün zəhmət olmasa [İnterpolyasiya ilə dəyərlərin göstərilməsi](guide/templates/binding#render-dynamic-text-with-text-interpolation) bələdçisinə müraciət edin.

<docs-workflow>

<docs-step title="İnterpolyasiya olunmuş dəyərləri daxil etmək üçün `HousingLocation` template-ini yeniləyin">
Bu addım `HousingLocation` template-inə yeni HTML strukturu və interpolyasiya olunmuş dəyərlər əlavə edir.

Kod redaktorunda:

1.  `src/app/housing-location/housing-location.ts` ünvanına keçin.
1.  `@Component` dekoratorunun template property-sində mövcud HTML strukturunu aşağıdakı kodla əvəz edin:

    <docs-code language="angular-ts"  header="housing-location.ts daxilində HousingLocation template-ini yeniləyin" path="adev/src/content/tutorials/first-app/steps/08-ngFor/src/app/housing-location/housing-location.ts" visibleLines="[6,17]"/>

Bu yenilənmiş template kodunda siz `housingLocation.photo`-nu `src` attribute-una bağlamaq üçün property binding-dən istifadə etdiniz. `alt` attribute-u şəklin alt mətninə daha çox kontekst vermək üçün interpolation-dan istifadə edir.

`housingLocation` property-sinin `name`, `city` və `state` dəyərlərini daxil etmək üçün interpolation-dan istifadə edirsiniz.

</docs-step>

<docs-step title="Dəyişikliklərin brauzerdə render olunduğunu təsdiqləyin">
1.  Bütün dəyişiklikləri yadda saxlayın.
1.  Brauzeri açın və tətbiqin foto, şəhər və ştat nümunə məlumatlarını render etdiyini təsdiqləyin.
    <img alt="homes-app-ın logo, filtr mətn giriş qutusu, axtarış düyməsi və eyni yaşayış yeri UI kartını göstərən brauzer pəncərəsi" src="assets/images/tutorials/first-app/homes-app-lesson-07-step-2.png">
</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz yeni HTML strukturu əlavə etdiniz və `HousingLocation` template-ində dəyərləri render etmək üçün Angular template sintaksisindən istifadə etdiniz.

İndi sizin iki vacib bacarığınız var:

- komponentlərə məlumat ötürmək
- template-ə dəyərləri interpolyasiya etmək

Bu bacarıqlarla tətbiqiniz artıq məlumat paylaşa və brauzerdə dinamik dəyərləri göstərə bilər. İndiyə qədərki işiniz əladır.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/templates" title="Template sintaksisi"/>
  <docs-pill href="guide/templates/binding#render-dynamic-text-with-text-interpolation" title="İnterpolyasiya ilə dəyərlərin göstərilməsi"/>
</docs-pill-row>
