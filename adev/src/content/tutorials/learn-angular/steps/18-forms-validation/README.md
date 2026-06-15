# Formaların validasiyası (doğrulanması)

Formalarla işləyərkən digər geniş yayılmış ssenari düzgün məlumatların göndərilməsini təmin etmək üçün girişləri yoxlamaq (validasiya etmək) ehtiyacıdır.

QEYD: [Ətraflı bələdçidə form girişinin validasiyası](/guide/forms/reactive-forms#validating-form-input) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz reaktiv formalarla formaları necə validasiya edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="Validator-ları import edin">

Angular bir sıra validasiya alətləri təqdim edir. Onlardan istifadə etmək üçün əvvəlcə komponenti `@angular/forms` kitabxanasından `Validators` import edəcək şəkildə yeniləyin.

```ts {highlight:[1]}
import {ReactiveFormsModule, Validators} from '@angular/forms';

@Component({...})
export class App {}
```

</docs-step>

<docs-step title="Formaya validasiya əlavə edin">

Hər bir `FormControl`-a həmin kontrolun dəyərlərini validasiya etmək üçün istifadə etmək istədiyiniz `Validators` ötürülə bilər. Məsələn, `profileForm`-dakı `name` sahəsini məcburi (required) etmək istəyirsinizsə, `Validators.required` istifadə edin.

Angular formamızdakı `email` sahəsi üçün onun boş qalmamasını və düzgün email ünvanı strukturuna uyğun olmasını təmin etmək istəyirik. Biz buna `Validators.required` və `Validators.email` validator-larını bir massivdə birləşdirərək nail ola bilərik.
`name` və `email` `FormControl`-larını yeniləyin:

```ts
profileForm = new FormGroup({
  name: new FormControl('', Validators.required),
  email: new FormControl('', [Validators.required, Validators.email]),
});
```

</docs-step>

<docs-step title="Template-də form validasiyasını yoxlayın">

Formanın etibarlı (valid) olub-olmadığını müəyyən etmək üçün `FormGroup` class-ının `valid` property-si var.
Siz bu property-dən attribute-ları dinamik şəkildə bağlamaq üçün istifadə edə bilərsiniz. Göndərmə (submit) düyməsini formanın etibarlılığına əsasən aktivləşdirilməsi (və ya deaktiv edilməsi) üçün yeniləyin.

```angular-html
<button type="submit" [disabled]="!profileForm.valid">Göndər</button>
```

</docs-step>

</docs-workflow>

İndi artıq reaktiv formalarla validasiyanın necə işlədiyinə dair əsasları bilirsiniz.

Angular-da formalarla işləməyin bu əsas anlayışlarını öyrəndiyiniz üçün əla iş gördünüz. Daha çox öyrənmək istəyirsinizsə, [Angular formaları sənədlərinə](guide/forms/form-validation) müraciət etdiyinizdən əmin olun.
