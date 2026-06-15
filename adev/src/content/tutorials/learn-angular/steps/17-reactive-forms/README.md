# Reaktiv Formalar (Reactive Forms)

Formalarınızı tamamilə template-ə etibar etmək əvəzinə proqramlı şəkildə idarə etmək istədikdə, reaktiv formalar bu sualın cavabıdır.

QEYD: [Ətraflı bələdçidə reaktiv formalar](/guide/forms/reactive-forms) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz reaktiv formaları necə quracağınızı öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="`ReactiveForms` modulunu import edin">

`app.ts` faylında `@angular/forms` kitabxanasından `ReactiveFormsModule`-u import edin və komponentin `imports` massivinə əlavə edin.

```angular-ts
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  template: `
    <form>
      <label>Ad
        <input type="text" />
      </label>
      <label>Email
        <input type="email" />
      </label>
      <button type="submit">Göndər</button>
    </form>
  `,
  imports: [ReactiveFormsModule],
})
```

</docs-step>

<docs-step title="FormControls ilə `FormGroup` obyekti yaradın">

Reaktiv formalar form kontrollarını (məsələn, girişləri) təmsil etmək üçün `FormControl` class-ından istifadə edir. Angular, form kontrollarını faydalı bir obyekt şəklində qruplaşdırmaq üçün `FormGroup` class-ını təqdim edir ki, bu da böyük formaların idarə edilməsini proqramçılar üçün daha rahat edir.

`@angular/forms`-dan `FormControl` və `FormGroup`-u import edin ki, hər bir form üçün `name` və `email` xüsusiyyətlərini `FormControls` kimi daxil edən bir `FormGroup` yarada biləsiniz.

```ts
import {ReactiveFormsModule, FormControl, FormGroup } from '@angular/forms';
...
export class App {
  profileForm = new FormGroup({
    name: new FormControl(''),
    email: new FormControl(''),
  });
}
```

</docs-step>

<docs-step title="FormGroup və FormControls-u formaya bağlayın">

Hər bir `FormGroup`, `[formGroup]` direktivindən istifadə edərək bir formaya əlavə edilməlidir.

Bundan əlavə, hər bir `FormControl`, `formControlName` direktivi ilə əlavə edilə və müvafiq property-yə təyin edilə bilər. Template-i aşağıdakı formada olan kodla yeniləyin:

```angular-html
<form [formGroup]="profileForm">
  <label>
    Ad
    <input type="text" formControlName="name" />
  </label>
  <label>
    Email
    <input type="email" formControlName="email" />
  </label>
  <button type="submit">Göndər</button>
</form>
```

</docs-step>

<docs-step title="Formanın yenilənməsini idarə edin">

`FormGroup`-dan məlumatlara daxil olmaq istədiyinizdə, bunu `FormGroup`-un `value` xüsusiyyətinə müraciət etməklə edə bilərsiniz. Form dəyərlərini göstərmək üçün `template`-i yeniləyin:

```angular-html
...
<h2>Profil Formu</h2>
<p>Ad: {{ profileForm.value.name }}</p>
<p>Email: {{ profileForm.value.email }}</p>
```

</docs-step>

<docs-step title="FormGroup dəyərlərinə daxil olun">

Komponent class-ına formanın göndərilməsini idarə etmək üçün istifadə edəcəyiniz `handleSubmit` adlı yeni bir metod əlavə edin. Bu metod formadakı dəyərləri göstərəcək; siz bu dəyərlərə `FormGroup` vasitəsilə daxil ola bilərsiniz.

Komponent class-ında, formanın göndərilməsini (submission) idarə etmək üçün `handleSubmit()` metodunu əlavə edin.

```ts
handleSubmit() {
  alert(
    this.profileForm.value.name + ' | ' + this.profileForm.value.email
  );
}
```

</docs-step>

<docs-step title="Formaya `ngSubmit` əlavə edin">

Form dəyərlərinə daxil ola bilirsiniz, indi isə göndərmə event-ini idarə etmək və `handleSubmit` metodunu istifadə etmək vaxtıdır. Angular-ın bu xüsusi məqsəd üçün `ngSubmit` adlı bir event handler-i var. Form elementini yeniləyərək form göndərildikdə `handleSubmit` metodunun çağırılmasını təmin edin.

```angular-html {highlight:[3]}
<form [formGroup]="profileForm" (ngSubmit)="handleSubmit()"></form>
```

</docs-step>

</docs-workflow>

Və budur, artıq Angular-da reaktiv formalarla necə işləyəcəyinizi bilirsiniz.

Bu fəaliyyətdə göstərdiyiniz möhtəşəm nəticəyə görə afərin. Forma validasiyası (doğrulanması) haqqında öyrənmək üçün davam edin.
