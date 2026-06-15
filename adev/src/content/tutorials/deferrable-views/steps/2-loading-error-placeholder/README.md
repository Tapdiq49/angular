# @loading, @error və @placeholder blokları

Deferrable views (təxirə salına bilən görünüşlər) müxtəlif yükləmə vəziyyətlərində göstəriləcək məzmunu təyin etməyə imkan verir.

<div class="docs-table docs-scroll-track-transparent">
  <table>
    <tr>
      <td><code>@placeholder</code></td>
      <td>
        Susmaya görə, təxirə salınmış (defer) bloklar tətiklənməmişdən (trigger) əvvəl heç bir məzmun render etmir. <code>@placeholder</code>, təxirə salınmış məzmun yüklənməmişdən əvvəl göstəriləcək məzmunu elan edən seçimli (optional) bir blokdur. Angular yükləmə başa çatdıqdan sonra placeholder-i təxirə salınmış məzmunla əvəz edir. Bu blok seçimli olsa da, Angular komandası həmişə placeholder daxil etməyi tövsiyə edir.
        <a href="https://angular.dev/guide/templates/defer#triggers" target="_blank">
          Tam deferrable views sənədlərində daha çox öyrənin
        </a>
      </td>
    </tr>
    <tr>
      <td><code>@loading</code></td>
      <td>
        Bu seçimli blok hər hansı aslılıqların (dependencies) yüklənməsi zamanı göstəriləcək məzmunu elan etməyə imkan verir.
      </td>
    </tr>
    <tr>
      <td><code>@error</code></td>
      <td>
        Bu blok təxirə salınmış yükləmə uğursuz olduqda göstərilən məzmunu elan etməyə imkan verir.
      </td>
    </tr>
  </table>
</div>

Yuxarıdakı bütün alt blokların məzmunu dərhal (eagerly) yüklənir. Bundan əlavə, bəzi xüsusiyyətlər `@placeholder` blokunu tələb edir.

Bu fəaliyyətdə siz deferrable views vəziyyətlərini idarə etmək üçün `@loading`, `@error` və `@placeholder` bloklarından necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="`@placeholder` bloku əlavə edin">
`app.ts` faylınızda `@defer` blokuna bir `@placeholder` bloku əlavə edin.

```angular-html {highlight:[3,4,5]}
@defer {
  <article-comments />
} @placeholder {
  <p>Şərhlər üçün placeholder</p>
}
```

</docs-step>

<docs-step title="`@placeholder` blokunu konfiqurasiya edin">
`@placeholder` bloku bu placeholder-in göstərilməli olduğu `minimum` vaxtı müəyyən etmək üçün seçimli bir parametr qəbul edir. Bu `minimum` parametri millisaniyə (ms) və ya saniyə (s) vahidləri ilə göstərilir. Bu parametr təxirə salınmış aslılıqların tez bir zamanda çəkildiyi (fetch) halda placeholder məzmununun sürətli titrəməsinin (fast flickering) qarşısını almaq üçün mövcuddur.

```angular-html {highlight:[3,4,5]}
@defer {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
}
```

</docs-step>

<docs-step title="`@loading` bloku əlavə edin">
Növbəti olaraq komponent template-inə bir `@loading` bloku əlavə edin.

`@loading` bloku iki seçimli parametr qəbul edir:

- `minimum`: bu blokun göstərilməli olduğu vaxt
- `after`: yükləmə başladıqdan sonra yükləmə template-ini göstərmək üçün gözlənilməli olan vaxt

Hər iki parametr millisaniyə (ms) və ya saniyə (s) vahidləri ilə göstərilir.

`app.ts` faylını yeniləyərək minimum parametri `1s` və after parametri `500ms` olan bir `@loading` bloku daxil edin.

```angular-html {highlight:[5,6,7]}
@defer {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
} @loading (minimum 1s; after 500ms) {
  <p>Şərhlər yüklənir...</p>
}
```

QEYD: Bu nümunə `;` simvolu ilə ayrılmış iki parametrdən istifadə edir.

</docs-step>

<docs-step title="`@error` bloku əlavə edin">
Sonda `@defer` blokuna bir `@error` bloku əlavə edin.

```angular-html {highlight:[7,8,9]}
@defer {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
} @loading (minimum 1s; after 500ms) {
  <p>Şərhlər yüklənir...</p>
} @error {
  <p>Şərhləri yükləmək mümkün olmadı</p>
}
```

</docs-step>
</docs-workflow>

Təbriklər! Bu nöqtədə sizin deferrable views haqqında yaxşı təsəvvürünüz var. Əla işə davam edin və növbəti addımda tətikləyicilər (triggers) haqqında öyrənək.
