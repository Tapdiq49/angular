# Formalara (Forms) Baxış

Formalar bir çox tətbiqlərin vacib hissəsidir, çünki onlar tətbiqinizə istifadəçi daxiletməsini qəbul etməyə imkan verir. Gəlin Angular-da formaların necə idarə olunduğunu öyrənək.

Angular-da formaların iki növü var: template-driven (template əsaslı) və reactive (reaktiv). Növbəti bir neçə fəaliyyətdə hər ikisini öyrənəcəksiniz.

QEYD: [Ətraflı bələdçidə Angular-da formalar](/guide/forms) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz template-driven yanaşmasından istifadə edərək formanı necə quracağınızı öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="Giriş (input) sahəsi yaradın">

`user.ts` faylında `id` attribute-u `framework`, tipi isə `text` olaraq təyin edilmiş bir mətn girişi əlavə edərək template-i yeniləyin.

```angular-html
<label for="framework">
  Sevimli Framework:
  <input id="framework" type="text" />
</label>
```

</docs-step>

<docs-step title="`FormsModule` import edin">

Bu formanın formalara data bağlamağa (data binding) imkan verən Angular xüsusiyyətlərindən istifadə etməsi üçün `FormsModule`-u import etməlisiniz.

`@angular/forms` paketindən `FormsModule`-u import edin və `User` komponentinin `imports` massivinə əlavə edin.

```ts {highlight:[2,6]}
import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms';

@Component({
...
imports: [FormsModule],
})
export class User {}
```

</docs-step>

<docs-step title="Giriş dəyərinə binding əlavə edin">

`FormsModule` daxilində giriş dəyərini class-ınızdakı bir property-yə bağlayan `ngModel` adlı bir direktiv var.

Property-ni `favoriteFramework` property-sinə bağlamaq üçün `ngModel` direktivindən istifadə edin, xüsusən də `[(ngModel)]="favoriteFramework"` sintaksisi ilə girişi (input) yeniləyin.

```html {highlight:[3]}
<label for="framework">
  Sevimli Framework:
  <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
</label>
```

Dəyişiklikləri etdikdən sonra giriş sahəsinə (input field) bir dəyər daxil etməyə çalışın. Onun ekranda necə yeniləndiyinə diqqət yetirin (bəli, çox maraqlıdır).

QEYD: `[()]` sintaksisi "banana in a box" kimi tanınır, lakin o, ikitərəfli bağlamanı (two-way binding) təmsil edir: property binding və event binding. [Angular sənədlərində ikitərəfli data binding](guide/templates/two-way-binding) haqqında daha çox öyrənin.

</docs-step>

</docs-workflow>

Siz artıq Angular ilə formalar qurmaq istiqamətində mühüm bir addım atdınız.

Yaxşı işdir. Gəlin sürəti davam etdirək!
