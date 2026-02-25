# Komponentin template-inə property binding əlavə edin

Bu təlimat dərsi template-ə property binding əlavə etməyi və ondan komponentlərə dinamik məlumat ötürmək üçün necə istifadə etməyi nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/eM3zi_n7lNs?si=AsiczpWnMz5HhJqB&amp;start=599"/>

## Nə öyrənəcəksiniz

- Tətbiqinizin `Home` template-ində məlumat binding-ləri var.
- Tətbiqiniz `Home` komponentindən `HousingLocation` komponentinə məlumat göndərir.

## Girişlərə (Inputs) konseptual baxış

Bu dərsdə siz template-də property binding-dən istifadə edərək məlumatları valideyn komponentdən övlad komponentə paylaşmaq prosesini davam etdirəcəksiniz.

Property binding dəyişəni Angular template-indəki `Input`-a qoşmağa imkan verir. Məlumatlar daha sonra dinamik olaraq `Input`-a bağlanır (bound).

Daha ətraflı izah üçün zəhmət olmasa [Property binding](/guide/templates/binding#css-class-and-style-property-bindings) bələdçisinə müraciət edin.

<docs-workflow>

<docs-step title="`Home` template-ini yeniləyin">
Bu addım `<app-housing-location>` teqinə property binding əlavə edir.

Kod redaktorunda:

1.  `src/app/home/home.ts` ünvanına keçin.
1.  `@Component` dekoratorunun template property-sində kodu aşağıdakı koda uyğun yeniləyin:
    <docs-code language="angular-ts" header="housingLocation property binding-i əlavə edin" path="adev/src/content/tutorials/first-app/steps/07-dynamic-template-values/src/app/home/home.ts" visibleLines="[15,17]"/>

    Komponent teqinə property binding əlavə edərkən biz Angular-a təyin edilmiş dəyərin string dəyəri deyil, komponent class-ından olan bir property kimi qəbul edilməli olduğunu bildirmək üçün `[attribute] = "value"` sintaksisindən istifadə edirik.

    Sağ tərəfdəki dəyər `Home` komponentindəki property-nin adıdır.

</docs-step>

<docs-step title="Kodun hələ də işlədiyini təsdiqləyin">
1.  Dəyişikliklərinizi yadda saxlayın və tətbiqdə xəta olmadığını təsdiqləyin.
1.  Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
</docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz yeni bir property binding əlavə etdiniz və class property-sinə müraciət ötürdünüz. İndi `HousingLocation` komponenti komponentin görünüşünü fərdiləşdirmək üçün istifadə edə biləcəyi məlumatlara daxil ola bilir.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="/guide/templates/binding#css-class-and-style-property-bindings" title="Property binding"/>
</docs-pill-row>
