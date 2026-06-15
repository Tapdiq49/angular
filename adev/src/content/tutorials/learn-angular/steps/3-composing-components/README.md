# Komponentlərin Birləşdirilməsi (Composition)

Siz komponent template-ini, məntiqini və üslublarını yeniləməyi öyrəndiniz, bəs bir komponenti tətbiqinizdə necə istifadə edirsiniz?

Komponent konfiqurasiyasının `selector` property-si sizə həmin komponentə başqa bir template-də müraciət etmək üçün ad verir. Siz `selector`-dan HTML teqi kimi istifadə edirsiniz, məsələn, `app-user` template-də `<app-user />` şəklində olacaqdır.

QEYD: [Essentials bələdçisində komponentlərin istifadəsi](/essentials/components#komponentləri-istifadə-etmək) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz komponentləri necə birləşdirməyi öyrənəcəksiniz.

<hr/>

Bu nümunədə iki komponent var: `User` və `App`.

<docs-workflow>

<docs-step title="`User` komponentinə istinad əlavə edin">
`App` template-ini yeniləyərək `app-user` selector-undan istifadə edən `User` komponentinə istinad əlavə edin. `User` komponentini `App`-in `imports` massivinə əlavə etməyi unutmayın; bu, onu `App` template-ində istifadə üçün əlçatan edir.

```angular-html
template: `<app-user />`, imports: [User]
```

İndi komponent `Username: youngTech` mesajını göstərir. Daha çox markup əlavə etmək üçün template kodunu yeniləyə bilərsiniz.
</docs-step>

<docs-step title="Daha çox markup əlavə edin">
Template-də istədiyiniz hər hansı bir HTML markup-dan istifadə edə bildiyiniz üçün, `App` template-ini daha çox HTML elementi daxil edəcək şəkildə yeniləməyə çalışın. Bu nümunədə `<app-user>` elementinin valideyni kimi bir `<section>` elementi əlavə ediləcək.

```angular-html
template: `
<section><app-user /></section>
`,
```

</docs-step>

</docs-workflow>

Tətbiq ideyanızı reallığa çevirmək üçün lazım olduğu qədər HTML markup və komponentdən istifadə edə bilərsiniz. Hətta eyni səhifədə komponentinizin bir neçə nüsxəsini yerləşdirə bilərsiniz.

Bu, yaxşı bir keçiddir — bəs məlumatlara əsasən bir komponenti şərtli olaraq necə göstərmək olar? Öyrənmək üçün növbəti bölməyə keçin.
