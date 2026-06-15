# İlk siqnalınızı (signal) yaratmaq və yeniləmək

Angular siqnalları təlimatına xoş gəlmisiniz! [Siqnallar](/essentials/signals) vəziyyəti (state) idarə etmək və həmin vəziyyət dəyişdikdə UI-nı avtomatik olaraq yeniləmək üçün Angular-ın reaktiv primitividir.

Bu fəaliyyətdə siz aşağıdakıları öyrənəcəksiniz:

- `signal()` funksiyasından istifadə edərək ilk siqnalınızı yaratmaq
- Onun dəyərini template-də göstərmək
- `set()` və `update()` metodlarından istifadə edərək siqnalın dəyərini yeniləmək

Gəlin siqnallarla interaktiv user status (istifadəçi statusu) sistemi quraq!

<hr />

<docs-workflow>

<docs-step title="Siqnal funksiyasını import edin">
Komponent faylınızın yuxarı hissəsində `@angular/core`-dan `signal` funksiyasını import edin.

```ts
import {Component, signal, ChangeDetectionStrategy} from '@angular/core';
```

</docs-step>

<docs-step title="Komponentinizdə siqnal yaradın">
Komponent class-ınıza `'offline'` dəyəri ilə inisializasiya edilmiş `userStatus` siqnalını əlavə edin.

```ts
@Component({
  /* Konfiqurasiya buraxılıb */
})
export class App {
  userStatus = signal<'online' | 'offline'>('offline');
}
```

</docs-step>

<docs-step title="Template-də siqnalın dəyərini göstərin">
Cari istifadəçi statusunu göstərmək üçün status göstəricisini yeniləyin:
1. `[class]="userStatus()"` ilə siqnalı class atributuna bağlayın (binding)
2. `???` işarəsini `{{ userStatus() }}` ilə əvəz edərək status mətnini göstərin

```angular-html
<!-- Buradan yeniləyin: -->
<div class="status-indicator offline">
  <span class="status-dot"></span>
  Status: ???
</div>

<!-- Bura: -->
<div class="status-indicator" [class]="userStatus()">
  <span class="status-dot"></span>
  Status: {{ userStatus() }}
</div>
```

Siqnalın dəyərini oxumaq üçün onu necə mötərizə ilə `userStatus()` çağırdığımıza diqqət yetirin.
</docs-step>

<docs-step title="Siqnalı yeniləmək üçün metodlar əlavə edin">
Komponentinizə `set()` metodundan istifadə edərək istifadəçi statusunu dəyişən metodlar əlavə edin.

```ts
goOnline() {
  this.userStatus.set('online');
}

goOffline() {
  this.userStatus.set('offline');
}
```

`set()` metodu siqnalın dəyərini tamamilə yeni bir dəyərlə əvəz edir.

</docs-step>

<docs-step title="İdarəetmə düymələrini qoşun">
Düymələr artıq template-dədir. İndi aşağıdakıları əlavə edərək onları metodlarınıza qoşun:
1. `(click)` ilə klikləmə emalçıları (handlers)
2. Artıq həmin statusda olduqda `[disabled]` ilə qeyri-aktiv vəziyyətlər

```html
<!-- Mövcud düymələrə binding-ləri əlavə edin: -->
<button (click)="goOnline()" [disabled]="userStatus() === 'online'">Onlayn ol</button>
<button (click)="goOffline()" [disabled]="userStatus() === 'offline'">Offlayn ol</button>
```

</docs-step>

<docs-step title="update() istifadə edərək keçid (toggle) metodu əlavə edin">
`update()` metodundan istifadə edərək onlayn və offlayn arasında keçid edən `toggleStatus()` metodu əlavə edin.

```ts
toggleStatus() {
  this.userStatus.update(current => current === 'online' ? 'offline' : 'online');
}
```

`update()` metodu cari dəyəri qəbul edən və yeni dəyəri qaytaran bir funksiya qəbul edir. Bu, mövcud dəyəri onun cari vəziyyətinə əsasən dəyişdirmək lazım olduqda faydalıdır.

</docs-step>

<docs-step title="Keçid düyməsi emalçısını əlavə edin">
Keçid (toggle) düyməsi artıq template-dədir. Onu `toggleStatus()` metodunuza qoşun:

```html
<button (click)="toggleStatus()" class="toggle-btn">Statusu dəyiş</button>
```

</docs-step>

</docs-workflow>

Təbriklər! Siz ilk siqnalınızı yaratdınız və həm `set()`, həm də `update()` metodlarından istifadə edərək onu necə yeniləyəcəyinizi öyrəndiniz. `signal()` funksiyası Angular-ın izlədiyi reaktiv bir dəyər yaradır və siz onu yenilədikdə, UI-nız dəyişiklikləri avtomatik əks etdirir.

Növbəti addımda [computed istifadə edərək siqnallardan vəziyyəti necə törətməyi](/tutorials/signals/2-deriving-state-with-computed-signals) öyrənəcəksiniz!

<docs-callout helpful title="ChangeDetectionStrategy.OnPush haqqında">

Bu təlimat boyu komponent dekoratorunda `ChangeDetectionStrategy.OnPush` görə bilərsiniz. Bu, siqnallardan istifadə edən Angular komponentləri üçün performans optimallaşdırılmasıdır. Hələlik buna əhəmiyyət verməməyiniz mümkündür — sadəcə bilin ki, bu, siqnallardan istifadə edərkən tətbiqinizin daha sürətli işləməsinə kömək edir! [Change detection strategies API sənədlərində](/api/core/ChangeDetectionStrategy) daha çox öyrənə bilərsiniz.

</docs-callout>
