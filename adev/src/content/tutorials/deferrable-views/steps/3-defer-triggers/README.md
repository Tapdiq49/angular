# Defer triggers (Təxirə salınma tətikləyiciləri)

`@defer` üçün susmaya görə (default) seçimlər komponentlərinizin hissələrini lazy loading (təmbəl yükləmə) etmək üçün böyük imkanlar təqdim etsə də, təxirə salınmış yükləmə təcrübəsini daha da fərdiləşdirmək istəyi hələ də yarana bilər.

Susmaya görə, təxirə salınmış məzmun brauzer boş (idle) olduqda yüklənir. Bununla belə, siz bir **trigger** (tətikləyici) müəyyən edərək bu yükləmənin nə vaxt baş verəcəyini fərdiləşdirə bilərsiniz. Bu, komponentinizə ən uyğun yükləmə davranışını seçməyə imkan verir.

Deferrable views (təxirə salına bilən görünüşlər) iki növ yükləmə tətikləyicisi təklif edir:

<div class="docs-table docs-scroll-track-transparent">
  <table>
    <tr>
      <td><code>on</code></td>
      <td>
        Daxili tətikləyicilər siyahısından bir tətikləyicini istifadə edən tətiklənmə şərti.<br/>
        Məsələn: <code>@defer (on viewport)</code>
      </td>
    </tr>
    <tr>
      <td><code>when</code></td>
      <td>
        Doğruluğu (truthiness) qiymətləndirilən bir ifadə şəklində şərt. İfade doğru (truthy) olduqda, placeholder lazy loading ilə yüklənmiş məzmunla əvəz olunur.<br/>
        Məsələn: <code>@defer (when customizedCondition)</code>
      </td>
    </tr>
  </table>
</div>

Əgər `when` şərti `false` olaraq qiymətləndirilərsə, `defer` bloku yenidən placeholder-ə qaytarılmır. Əvəzetmə birdəfəlik əməliyyatdır.

Siz eyni anda birdən çox hadisə tətikləyicisi təyin edə bilərsiniz, bu tətikləyicilər "OR" (VƏ YA) şərtləri kimi qiymətləndiriləcək.

- Məs: `@defer (on viewport; on timer(2s))`
- Məs: `@defer (on viewport; when customizedCondition)`

Bu fəaliyyətdə siz deferrable views-un yüklənmə şərtini müəyyən etmək üçün tətikləyicilərdən necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="`on hover` tətikləyicisi əlavə edin">
`app.ts` faylınızda `@defer` blokuna bir `on hover` tətikləyicisi əlavə edin.

```angular-html {highlight:[1]}
@defer (on hover) {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
} @loading (minimum 1s; after 500ms) {
  <p>Şərhlər yüklənir...</p>
} @error {
  <p>Şərhləri yükləmək mümkün olmadı</p>
}
```

İndi səhifə, siz onun placeholder-inin üzərinə gəlməyincə (hover) şərhlər bölməsini render etməyəcək.
</docs-step>

<docs-step title="'Show all comments' düyməsi əlavə edin">
Növbəti olaraq template-i "Show all comments" yazısı olan bir düymə daxil edəcək şəkildə yeniləyin. Düyməyə `#showComments` adlı bir template dəyişəni daxil edin.

```angular-html {highlight:[1]}
<button type="button" #showComments>Hamısını göstər</button>

@defer (on hover) {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
} @loading (minimum 1s; after 500ms) {
  <p>Şərhlər yüklənir...</p>
} @error {
  <p>Şərhləri yükləmək mümkün olmadı</p>
}
```

QEYD: [template dəyişənləri haqqında daha çox məlumat üçün sənədlərə baxın](/guide/templates/variables#declaring-a-template-reference-variable).

</docs-step>

<docs-step title="`on interaction` tətikləyicisi əlavə edin">
Template-dəki `@defer` blokunu `on interaction` tətikləyicisini istifadə edəcək şəkildə yeniləyin. `showComments` template dəyişənini `interaction` üçün parametr kimi təqdim edin.

```angular-html {highlight:[3]}
<button type="button" #showComments>Hamısını göstər</button>

@defer (on hover; on interaction(showComments)) {
  <article-comments />
} @placeholder (minimum 1s) {
  <p>Şərhlər üçün placeholder</p>
} @loading (minimum 1s; after 500ms) {
  <p>Şərhlər yüklənir...</p>
} @error {
  <p>Şərhləri yükləmək mümkün olmadı</p>
}
```

Bu dəyişikliklərlə səhifə şərhlər bölməsini render etməmişdən əvvəl aşağıdakı şərtlərdən birini gözləyəcək:

- İstifadəçi şərhlər bölməsinin placeholder-inin üzərinə gəlir (hover)
- İstifadəçi “Hamısını göstər" düyməsini klikləyir

Şərhlər bölməsini render etmək üçün fərqli tətikləyiciləri sınamaq məqsədilə səhifəni yeniləyə bilərsiniz.
</docs-step>
</docs-workflow>

Daha çox öyrənmək istəyirsinizsə, [Deferrable View](/guide/templates/defer) sənədlərinə baxın.
Angular-ın digər möhtəşəm xüsusiyyətlərini kəşf etmək üçün öyrənməyə davam edin.
