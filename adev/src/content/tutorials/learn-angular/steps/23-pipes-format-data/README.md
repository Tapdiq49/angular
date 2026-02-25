# Pipe-lar vasitəsilə məlumatların formatlanması

Pipe-ların çıxışını konfiqurasiya etməklə onlardan istifadəni daha da irəli apara bilərsiniz. Pipe-lara seçimlər (options) ötürməklə onları konfiqurasiya etmək mümkündür.

QEYD: [Ətraflı bələdçidə pipe-lar vasitəsilə məlumatların formatlanması](/guide/templates/pipes) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz bəzi pipe-lar və pipe parametrləri ilə işləyəcəksiniz.

<hr>

Pipe-a parametrlər ötürmək üçün `:` sintaksisindən və ardından parametr dəyərindən istifadə edin. Budur bir nümunə:

```angular-html
template: `{{ date | date: 'medium' }}`;
```

Çıxış belə olacaq: `Jun 15, 2015, 9:43:11 PM`.

Bəzi pipe çıxışlarını fərdiləşdirmək vaxtıdır:

<docs-workflow>

<docs-step title="`DecimalPipe` ilə rəqəmi formatlayın">

`app.ts` faylında `decimal` pipe-ı üçün parametr daxil etmək məqsədilə template-i yeniləyin.

```angular-html {highlight:[3]}
template: ` ...
<li>Number with "decimal" {{ num | number: '3.2-2' }}</li>
`
```

QEYD: Bu hansı formatdır? `DecimalPipe` üçün parametr `digitsInfo` adlanır və bu parametr bu formatdan istifadə edir: `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`

</docs-step>

<docs-step title="`DatePipe` ilə tarixi formatlayın">

İndi isə `date` pipe-ından istifadə etmək üçün template-i yeniləyin.

```angular-html {highlight:[3]}
template: ` ...
<li>Date with "date" {{ birthday | date: 'medium' }}</li>
`
```

Əlavə əyləncə üçün `date` üçün müxtəlif parametrləri sınayın. Daha çox məlumatı [Angular sənədlərində](guide/templates/pipes) tapa bilərsiniz.

</docs-step>

<docs-step title="`CurrencyPipe` ilə valyutanı formatlayın">

Sonuncu tapşırığınız üçün `currency` pipe-ından istifadə etmək məqsədilə template-i yeniləyin.

```angular-html {highlight:[3]}
template: ` ...
<li>Currency with "currency" {{ cost | currency }}</li>
`
```

Siz həmçinin `currency` üçün müxtəlif parametrləri sınaya bilərsiniz. Daha çox məlumatı [Angular sənədlərində](guide/templates/pipes) tapa bilərsiniz.

</docs-step>

</docs-workflow>

Pipe-larla bağlı əla iş gördünüz. İndiyə qədər böyük irəliləyiş əldə etmisiniz.

Tətbiqlərinizdə istifadə edə biləcəyiniz daha çox daxili pipe-lar var. Siyahını [Angular sənədlərində](guide/templates/pipes) tapa bilərsiniz.

Daxili pipe-ların ehtiyaclarınızı qarşılamadığı təqdirdə, öz xüsusi pipe-ınızı da yarada bilərsiniz. Daha çox məlumat üçün növbəti dərsə baxın.
