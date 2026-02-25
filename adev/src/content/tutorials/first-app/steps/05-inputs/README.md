# Komponentə bir giriş (input) parametri əlavə edin

Bu təlimat dərsi bir komponentin `input`-unu necə yaradacağınızı və ondan fərdiləşdirmə üçün komponentə məlumat ötürmək məqsədilə necə istifadə edəcəyinizi nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/eM3zi_n7lNs?si=WvRGFSkW_7_zDIFD&amp;start=241"/>

QEYD: Bu video köhnə sintaksisi əks etdirir, lakin əsas anlayışlar qüvvədə qalır.

## Nə öyrənəcəksiniz

Tətbiqinizin `HousingLocation` template-ində girişi (input) qəbul etmək üçün bir `HousingLocation` property-si var.

## Girişlərə (Inputs) konseptual baxış

[Girişlər (Inputs)](api/core/input) komponentlərə valideyn komponentdən ötürülə bilən məlumatları müəyyən etməyə imkan verir.

Bu dərsdə siz `HousingLocation` komponentində komponentdə göstərilən məlumatları fərdiləşdirməyə imkan verən bir `input` property-si təyin edəcəksiniz.

[Giriş property-ləri ilə məlumatların qəbul edilməsi](guide/components/inputs) və [Çıxışlar (outputs) ilə xüsusi event-lər](guide/components/outputs) bələdçilərindən daha çox məlumat əldə edin.

<docs-workflow>

<docs-step title="input() funksiyasını import edin">
Kod redaktorunda `@angular/core`-dan `input` köməkçi metodunu `HousingLocation` komponentinə import edin.

<docs-code header="housing-location.ts daxilində input-u import edin" path="adev/src/content/tutorials/first-app/steps/06-property-binding/src/app/housing-location/housing-location.ts" visibleLines="[1]"/>

</docs-step>

<docs-step title="Giriş (Input) property-sini əlavə edin">
`housingLocation` adlı məcburi bir property əlavə edin və onu `HousingLocationInfo` tipi ilə `input.required()` istifadə edərək başlanğıc vəziyyətinə gətirin.

  <docs-code header="housing-location.ts daxilində input property-sini elan edin" path="adev/src/content/tutorials/first-app/steps/06-property-binding/src/app/housing-location/housing-location.ts" visibleLines="[12]"/>

Valideyn komponentin bir dəyər təmin etməli olduğunu bildirmək üçün `input` üzərində `required` metodunu çağırmalısınız. Nümunə tətbiqimizdə biz bu dəyərin həmişə ötürüləcəyini bilirik — bu, dizaynla belədir. `.required()` çağırışı TypeScript kompilyatorunun bunu tələb etməsini və bu komponent template-də istifadə edildikdə property-yə nullable olmayan (non-nullable) kimi yanaşmasını təmin edir.

</docs-step>

<docs-step title="Girişə məlumat ötürün">
`housingLocation` dəyərini `Home` komponentindən `HousingLocation` komponentinin `housingLocation` property-sinə göndərin.

<docs-code language="angular-ts" header="home.ts daxilində HousingLocation üçün input property-sini elan edin" path="adev/src/content/tutorials/first-app/steps/06-property-binding/src/app/home/home.ts" visibleLines="[16]"/>

</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz yeni bir `input` property-si yaratdınız. Sinyal (signal) dəyərinin həmişə təyin olunduğuna əmin olmaq üçün `.required` metodundan da istifadə etdiniz.

<docs-pill-row>
  <docs-pill href="guide/components/inputs" title="Giriş property-ləri ilə məlumatların qəbul edilməsi"/>
  <docs-pill href="guide/components/outputs" title="Çıxışlar (outputs) ilə xüsusi event-lər"/>
</docs-pill-row>
