# Xüsusi (custom) pipe yaradın

Məlumat çevirmə ehtiyaclarınıza uyğun olaraq Angular-da xüsusi pipe-lar yarada bilərsiniz.

QEYD: [Ətraflı bələdçidə xüsusi pipe-ların yaradılması](/guide/templates/pipes#creating-custom-pipes) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz xüsusi bir pipe yaradacaq və ondan template-inizdə istifadə edəcəksiniz.

<hr>

Pipe, `@Pipe` dekoratoruna malik TypeScript class-ıdır. Budur bir nümunə:

```ts
import {Pipe, PipeTransform} from '@angular/core';

@Pipe({
  name: 'star',
})
export class StarPipe implements PipeTransform {
  transform(value: string): string {
    return `⭐️ ${value} ⭐️`;
  }
}
```

`StarPipe` bir string dəyəri qəbul edir və həmin string-i ulduzlarla əhatə olunmuş şəkildə qaytarır. Qeyd edin ki:

- `@Pipe` dekorator konfiqurasiyasındakı `name` template-də istifadə olunacaq addır
- `transform` funksiyası məntiqinizi yerləşdirdiyiniz yerdir

Yaxşı, növbə sizindir — `ReversePipe` (tərs çevirmə pipe-ı) yaradacaqsınız:

<docs-workflow>

<docs-step title="`ReversePipe` yaradın">

`reverse.pipe.ts` faylında `ReversePipe` class-ına `@Pipe` dekoratorunu əlavə edin və aşağıdakı konfiqurasiyanı təmin edin:

```ts
@Pipe({
  name: 'reverse'
})
```

</docs-step>

<docs-step title="`transform` funksiyasını implementasiya edin">

İndi `ReversePipe` class-ı bir pipe-dır. Tərs çevirmə məntiqini əlavə etmək üçün `transform` funksiyasını yeniləyin:

```ts {highlight:[3,4,5,6,7,8,9]}
export class ReversePipe implements PipeTransform {
  transform(value: string): string {
    let reverse = '';

    for (let i = value.length - 1; i >= 0; i--) {
      reverse += value[i];
    }

    return reverse;
  }
}
```

</docs-step>

<docs-step title="Template-də `ReversePipe` istifadə edin"></docs-step>
Pipe məntiqi implementasiya edildikdən sonra son addım ondan template-də istifadə etməkdir. `app.ts` faylında pipe-ı template-ə daxil edin və onu komponent import-larına əlavə edin:

```angular-ts {highlight:[3,4]}
@Component({
  ...
  template: `Reverse Machine: {{ word | reverse }}`
  imports: [ReversePipe]
})
```

</docs-workflow>

Və bununla da siz bacardınız. Bu fəaliyyəti tamamladığınız üçün sizi təbrik edirik. Artıq pipe-lardan necə istifadə edəcəyinizi və hətta öz xüsusi pipe-larınızı necə implementasiya edəcəyinizi bilirsiniz.
