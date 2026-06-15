# Təxirə salına bilən görünüşlər (Deferrable Views)

Bəzən tətbiq inkişafı zamanı tətbiqinizdə istinad etməli olduğunuz bir çox komponentlərlə qarşılaşırsınız, lakin müxtəlif səbəblərdən onların bəzilərinin dərhal yüklənməsinə ehtiyac qalmır.

Bəlkə onlar görünən hissədən (viewport) aşağıdadırlar və ya sonraya qədər qarşılıqlı əlaqədə olunmayan ağır komponentlərdirlər. Bu halda, həmin resursların bəzilərini təxirə salına bilən görünüşlər vasitəsilə daha sonra yükləyə bilərik.

QEYD: [Ətraflı bələdçidə @defer ilə təxirə salınmış yükləmə](/guide/templates/defer) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz komponent template-inizin bir hissəsinin yüklənməsini təxirə salmaq üçün təxirə salına bilən görünüşlərdən necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="Şərhlər komponenti ətrafına bir `@defer` bloku əlavə edin">

Tətbiqinizdə bloq yazısı səhifəsində yazı təfərrüatlarından sonra şərh komponenti var.

Şərh komponentini təxirə salınmış şəkildə yükləmək üçün onu bir `@defer` bloku ilə əhatə edin.

```angular-html
@defer {
  <comments />
}
```

Yuxarıdakı kod əsas `@defer` blokunun necə istifadə olunacağına bir nümunədir. Defolt olaraq `@defer`, brauzer boş (idle) qaldıqda `comments` komponentini yükləyəcək.

</docs-step>

<docs-step title="Bir placeholder əlavə edin">

`@defer` blokuna bir `@placeholder` bloku əlavə edin. `@placeholder` bloku təxirə salınmış yükləmə başlamazdan əvvəl göstəriləcək HTML-i yerləşdirdiyiniz yerdir. `@placeholder` bloklarındakı məzmun dərhal (eagerly) yüklənir.

```angular-html {highlight:[3,4,5]}
@defer {
  <comments />
} @placeholder {
  <p>Gələcək şərhlər</p>
}
```

</docs-step>

<docs-step title="Bir yükləmə (loading) bloku əlavə edin">

`@defer` blokuna bir `@loading` bloku əlavə edin. `@loading` bloku təxirə salınmış məzmun aktiv şəkildə gətirilərkən (amma hələ bitmədikdə) göstəriləcək HTML-i yerləşdirdiyiniz yerdir. `@loading` bloklarındakı məzmun dərhal (eagerly) yüklənir.

```angular-html {highlight:[5,6,7]}
@defer {
  <comments />
} @placeholder {
  <p>Gələcək şərhlər</p>
} @loading {
  <p>Şərhlər yüklənir...</p>
}
```

</docs-step>

<docs-step title="Minimum müddət əlavə edin">

Həm `@placeholder`, həm də `@loading` bölmələrinin yükləmə tez baş verdikdə titrəmənin (flickering) qarşısını almaq üçün könüllü parametrləri var. `@placeholder` üçün `minimum`, `@loading` üçün isə `minimum` və `after` parametrləri mövcuddur. `@loading` blokuna `minimum` müddət əlavə edin ki, o, ən azı 2 saniyə ərzində render olunsun.

```angular-html {highlight:[5]}
@defer {
  <comments />
} @placeholder {
  <p>Gələcək şərhlər</p>
} @loading (minimum 2s) {
  <p>Şərhlər yüklənir...</p>
}
```

</docs-step>

<docs-step title="Bir viewport triggeri əlavə edin">

Təxirə salına bilən görünüşlərin bir sıra trigger seçimləri var. Bir viewport triggeri əlavə edin ki, məzmun görünüş sahəsinə (viewport) daxil olduqdan sonra təxirə salınmış şəkildə yüklənsin.

```angular-html {highlight:[1]}
@defer (on viewport) {
  <comments />
}
```

</docs-step>

<docs-step title="Məzmun əlavə edin">

Viewport triggeri ən yaxşı o zaman istifadə olunur ki, siz səhifənin kifayət qədər aşağısında olan və görünməsi üçün skrol edilməsi lazım olan məzmunu təxirə salırsınız. Beləliklə, bloq yazımıza bir az məzmun əlavə edək. Özünüz yazıya bilərsiniz və ya aşağıdakı məzmunu kopyalayıb `<article>` elementinin daxilinə yerləşdirə bilərsiniz.

```html {highlight:[1]}
<article>
  <p>
    Angular mənim sevimli freymvorkumdur və səbəbi budur. Angular, təxirə salınmış yükləməni mümkün
    qədər asan və erqonomik edən ən möhtəşəm təxirə salına bilən görünüş xüsusiyyətinə malikdir.
    Angular icması həmçinin yüksək keyfiyyətli məzmun yaradan möhtəşəm töhfəçilər və ekspertlərlə
    doludur. İcma qarşılayan və mehribandır və o, həqiqətən də mövcud olan ən yaxşı icmadır.
  </p>
  <p>
    Angular ilə işləməkdən nə qədər zövq aldığımı kifayət qədər ifadə edə bilmirəm. O, mənim indiyə
    qədər yaşadığım ən yaxşı developer təcrübəsini təklif edir. Mən sevirəm ki, Angular komandası öz
    proqramçılarını ön plana çəkir və bizi çox xoşbəxt etmək üçün qayğı göstərir. Onlar həqiqətən
    Angular-ın ola biləcəyi ən yaxşı freymvork olmasını istəyirlər və bu işdə çox möhtəşəm bir iş
    görürlər. Bu bəyanat ürəyimdən gəlir və heç də kopyalanıb yapışdırılmayıb. Əslində, düşünürəm
    ki, eyni şeyləri bir neçə dəfə də deyəcəyəm.
  </p>
  <p>
    Angular mənim sevimli freymvorkumdur və səbəbi budur. Angular, təxirə salınmış yükləməni mümkün
    qədər asan və erqonomik edən ən möhtəşəm təxirə salına bilən görünüş xüsusiyyətinə malikdir.
    Angular icması həmçinin yüksək keyfiyyətli məzmun yaradan möhtəşəm töhfəçilər və ekspertlərlə
    doludur. İcma qarşılayan və mehribandır və o, həqiqətən də mövcud olan ən yaxşı icmadır.
  </p>
  <p>
    Angular ilə işləməkdən nə qədər zövq aldığımı kifayət qədər ifadə edə bilmirəm. O, mənim indiyə
    qədər yaşadığım ən yaxşı developer təcrübəsini təklif edir. Mən sevirəm ki, Angular komandası öz
    proqramçılarını ön plana çəkir və bizi çox xoşbəxt etmək üçün qayğı göstərir. Onlar həqiqətən
    Angular-ın ola biləcəyi ən yaxşı freymvork olmasını istəyirlər və bu işdə çox möhtəşəm bir iş
    görürlər. Bu bəyanat ürəyimdən gəlir və heç də kopyalanıb yapışdırılmayıb. Əslində, düşünürəm
    ki, eyni şeyləri bir neçə dəfə də deyəcəyəm.
  </p>
  <p>
    Angular mənim sevimli freymvorkumdur və səbəbi budur. Angular, təxirə salınmış yükləməni mümkün
    qədər asan və erqonomik edən ən möhtəşəm təxirə salına bilən görünüş xüsusiyyətinə malikdir.
    Angular icması həmçinin yüksək keyfiyyətli məzmun yaradan möhtəşəm töhfəçilər və ekspertlərlə
    doludur. İcma qarşılayan və mehribandır və o, həqiqətən də mövcud olan ən yaxşı icmadır.
  </p>
  <p>
    Angular ilə işləməkdən nə qədər zövq aldığımı kifayət qədər ifadə edə bilmirəm. O, mənim indiyə
    qədər yaşadığım ən yaxşı developer təcrübəsini təklif edir. Mən sevirəm ki, Angular komandası öz
    proqramçılarını ön plana çəkir və bizi çox xoşbəxt etmək üçün qayğı göstərir. Onlar həqiqətən
    Angular-ın ola biləcəyi ən yaxşı freymvork olmasını istəyirlər və bu işdə çox möhtəşəm bir iş
    görürlər. Bu bəyanat ürəyimdən gəlir və heç də kopyalanıb yapışdırılmayıb.
  </p>
</article>
```

Bu kodu əlavə etdikdən sonra, təxirə salınmış məzmunun görünüş sahəsinə daxil olduqda yükləndiyini görmək üçün aşağı skrol edin.

</docs-step>

</docs-workflow>

Fəaliyyətdə siz tətbiqlərinizdə təxirə salına bilən görünüşlərdən necə istifadə edəcəyinizi öyrəndiniz. Əla iş. 🙌

Onlarla edə biləcəyiniz daha çox şey var, məsələn, müxtəlif triggerlər, prefetching və `@error` blokları.

Daha çox öyrənmək istəyirsinizsə, [Təxirə salına bilən görünüşlər üçün sənədlərə](/guide/templates/defer) baxın.
