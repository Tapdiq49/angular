# Form kontrol dəyərinin əldə edilməsi

Formalarınız artıq Angular ilə quraşdırıldığına görə, növbəti addım form kontrollarından (form controls) dəyərləri əldə etməkdir.

QEYD: [Ətraflı bələdçidə əsas form kontrolunun əlavə edilməsi](/guide/forms/reactive-forms#adding-a-basic-form-control) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz form girişindən (input) dəyəri necə əldə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="Giriş sahəsinin dəyərini template-də göstərin">

Giriş dəyərini template-də göstərmək üçün, komponentin hər hansı digər class property-si kimi `{{}}` interpolation sintaksisindən istifadə edə bilərsiniz:

```angular-ts {highlight:[5]}
@Component({
  selector: 'app-user',
  template: `
    ...
    <p>Framework: {{ favoriteFramework }}</p>
    <label for="framework">
      Sevimli Framework:
      <input id="framework" type="text" [(ngModel)]="favoriteFramework" />
    </label>
  `,
})
export class User {
  favoriteFramework = '';
}
```

</docs-step>

<docs-step title="Giriş sahəsinin dəyərini əldə edin">

Giriş sahəsinin (input field) dəyərinə komponent class-ı daxilində müraciət etmək lazım olduqda, bunu `this` sintaksisi vasitəsilə class property-sinə müraciət edərək edə bilərsiniz.

```angular-ts {highlight:[15]}
...
@Component({
  selector: 'app-user',
  template: `
    ...
    <button (click)="showFramework()">Framework-ü göstər</button>
  `,
  ...
})
export class User {
  favoriteFramework = '';
  ...

  showFramework() {
    alert(this.favoriteFramework);
  }
}
```

</docs-step>

</docs-workflow>

Giriş dəyərlərini template-inizdə göstərməyi və onlara proqramlı şəkildə daxil olmağı öyrəndiyiniz üçün əla iş gördünüz.

Angular ilə formaları idarə etməyin növbəti üsuluna keçmək vaxtıdır: reaktiv formalar (reactive forms). Template-driven formalar haqqında daha çox öyrənmək istəyirsinizsə, [Angular formaları sənədlərinə](guide/forms/template-driven-forms) baxın.
