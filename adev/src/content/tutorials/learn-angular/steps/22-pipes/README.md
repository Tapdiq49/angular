# Pipe-lar

Pipe-lar template-lərdə məlumatları çevirmək üçün istifadə olunan funksiyalardır. Ümumiyyətlə, pipe-lar yan təsirlərə (side effects) səbəb olmayan "pure" (saf) funksiyalardır. Angular, komponentlərinizdə import edib istifadə edə biləcəyiniz bir sıra faydalı daxili pipe-lara malikdir. Siz həmçinin xüsusi (custom) pipe da yarada bilərsiniz.

QEYD: [Ətraflı bələdçidə pipe-lar](/guide/templates/pipes) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz bir pipe-ı import edib template-də istifadə edəcəksiniz.

<hr>

Template-də pipe istifadə etmək üçün onu interpolation ifadəsinə daxil edin. Bu nümunəyə baxın:

```angular-ts {highlight:[1,5,6]}
import {UpperCasePipe} from '@angular/common';

@Component({
  ...
  template: `{{ loudMessage | uppercase }}`,
  imports: [UpperCasePipe],
})
export class App {
  loudMessage = 'we think you are doing great!'
}
```

İndi isə sizin növbənizdir:

<docs-workflow>

<docs-step title="`LowerCase` pipe-ını import edin">
İlk olaraq, `@angular/common` paketindən `LowerCasePipe` üçün fayl səviyyəsində import əlavə edərək `app.ts` faylını yeniləyin.

```ts
import {LowerCasePipe} from '@angular/common';
```

</docs-step>

<docs-step title="Pipe-ı template import-larına əlavə edin">
Növbəti addım olaraq, `@Component()` dekoratorunun `imports` massivinə `LowerCasePipe`-ı əlavə edin.

```ts {highlight:[3]}
@Component({
  ...
  imports: [LowerCasePipe]
})
```

</docs-step>

<docs-step title="Pipe-ı template-ə əlavə edin">
Nəhayət, `app.ts` faylında template-i `lowercase` pipe-ını daxil edəcək şəkildə yeniləyin:

```angular-html
template: `{{ username | lowercase }}`
```

</docs-step>

</docs-workflow>

Pipe-lar həmçinin çıxışı konfiqurasiya etmək üçün istifadə olunan parametrləri qəbul edə bilər. Növbəti fəaliyyətdə daha çox məlumat əldə edin.

P.S. Əla gedirsiniz ⭐️
