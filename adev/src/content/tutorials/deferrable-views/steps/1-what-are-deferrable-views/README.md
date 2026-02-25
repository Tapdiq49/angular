# Deferrable views (təxirə salına bilən görünüşlər) nədir?

Tam render olunmuş bir Angular səhifəsi bir çox fərqli komponent, direktiv və payp-dan (pipe) ibarət ola bilər. Səhifənin müəyyən hissələri istifadəçiyə dərhal göstərilməli olsa da, bəzi hissələrin göstərilməsi daha sonraya qədər gözləyə bilər.
Angular-ın _deferrable views_ (təxirə salına bilən görünüşlər) xüsusiyyəti, `@defer` sintaksisindən istifadə edərək, Angular-a səhifənin dərhal göstərilməsi lazım olmayan hissələri üçün JavaScript-i yükləməyi təxirə salmağı tapşıraraq tətbiqinizi sürətləndirməyə kömək edə bilər.

Bu fəaliyyətdə siz komponent template-inizin bir hissəsinin yüklənməsini təxirə salmaq üçün deferrable views-dan necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="Template-in bir hissəsinə `@defer` bloku əlavə edin">
`app.ts` faylınızda, `article-comments` komponentini yüklənməsini təxirə salmaq üçün onu `@defer` bloku daxilinə alın.

```angular-html
@defer {
  <article-comments />
}
```

Susmaya görə (default), `@defer` brauzer boş (idle) olduqda `article-comments` komponentini yükləyir.

Brauzerinizin proqramçı konsolunda (developer console) `article-comments-component` lazy chunk faylının ayrıca yükləndiyini görə bilərsiniz (spesifik fayl adları hər işəsalmada dəyişə bilər):

```markdown
Initial chunk files | Names | Raw size
chunk-NNSQHFIE.js | - | 769.00 kB |
main.js | main | 229.25 kB |

Lazy chunk files | Names | Raw size
chunk-T5UYXUSI.js | article-comments-component | 1.84 kB |
```

</docs-step>
</docs-workflow>

Əla iş! Siz deferrable views-un əsaslarını öyrəndiniz.
