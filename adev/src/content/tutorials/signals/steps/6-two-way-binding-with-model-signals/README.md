# Model siqnalları ilə iki tərəfli binding (two-way binding)

Artıq [input siqnalları vasitəsilə komponentlərə məlumat ötürməyi](/tutorials/signals/5-component-communication-with-signals) öyrəndiniz, gəlin Angular-ın iki tərəfli binding (iki tərəfli əlaqələndirmə) üçün `model()` API-sini araşdıraq. Model siqnalları checkbox-lar, slider-lər və ya komponentin həm bir dəyəri qəbul etməli, həm də onu yeniləməli olduğu xüsusi forma idarəetmə elementləri üçün mükəmməldir.

Bu fəaliyyətdə siz valideyn komponenti sinxron saxlayaraq öz vəziyyətini idarə edən xüsusi checkbox komponenti yaradacaqsınız.

<hr />

<docs-workflow>

<docs-step title="Xüsusi checkbox-u model siqnalı ilə quraşdırın">
`custom-checkbox` komponentində həm valideynin dəyərini qəbul edə bilən, həm də onu yeniləyə bilən bir model siqnalı yaradın.

```ts
// Model siqnalları üçün import-lar əlavə edin
import {Component, model, input, ChangeDetectionStrategy} from '@angular/core';

// İki tərəfli binding üçün model siqnalı
checked = model.required<boolean>();

// Etiket (label) üçün seçimli input
label = input<string>('');
```

Yalnız oxunabilən `input()` siqnallarından fərqli olaraq, `model()` siqnalları həm oxuna, həm də yazıla bilər.
</docs-step>

<docs-step title="Checkbox template-ini yaradın">
Kliklərə cavab verən və öz modelini yeniləyən checkbox template-ini qurun.

```html
<label class="custom-checkbox">
  <input type="checkbox" [checked]="checked()" (change)="toggle()" />
  <span class="checkmark"></span>
  {{ label() }}
</label>
```

Komponent öz model siqnalından oxuyur və onu yeniləmək üçün bir metoda malikdir.
</docs-step>

<docs-step title="Keçid (toggle) metodunu əlavə edin">
Checkbox klikləndikdə model siqnalını yeniləyən keçid metodunu implementasiya edin.

```ts
toggle() {
  // Bu həm komponentin vəziyyətini, həm də valideynin modelini yeniləyir!
  this.checked.set(!this.checked());
}
```

Övlad komponent `this.checked.set()` çağırdıqda, o avtomatik olaraq dəyişikliyi valideynə ötürür. Bu, `input()` siqnallarından əsas fərqdir.
</docs-step>

<docs-step title="Valideyn komponentdə iki tərəfli binding-i quraşdırın">
Əvvəlcə `app.ts` faylındakı model siqnalı property-lərini və metodlarını şərhdən (comment) çıxarın:

```ts
// Valideyn siqnal modelləri
agreedToTerms = model(false);
enableNotifications = model(true);

// İki tərəfli binding-i test etmək üçün metodlar
toggleTermsFromParent() {
  this.agreedToTerms.set(!this.agreedToTerms());
}

resetAll() {
  this.agreedToTerms.set(false);
  this.enableNotifications.set(false);
}
```

Sonra template-i yeniləyin:

Hissə 1. **Checkbox-ları şərhdən çıxarın və iki tərəfli binding əlavə edin:**

- Birinci checkbox üçün `___ADD_TWO_WAY_BINDING___` yazısını `[(checked)]="agreedToTerms"` ilə əvəz edin
- İkinci üçün `___ADD_TWO_WAY_BINDING___` yazısını `[(checked)]="enableNotifications"` ilə əvəz edin

Hissə 2. **`???` yer tutucularını @if blokları ilə əvəz edin:**

```angular-html
@if (agreedToTerms()) {
  Bəli
} @else {
  Xeyr
}

@if (enableNotifications()) {
  Bəli
} @else {
  Xeyr
}
```

Hissə 3. **Düymələrə klikləmə emalçılarını əlavə edin:**

```html
<button (click)="toggleTermsFromParent()">Valideyndən şərtləri dəyiş</button>
<button (click)="resetAll()">Hamısını sıfırla</button>
```

`[(checked)]` sintaksisi iki tərəfli binding yaradır - məlumatlar komponentə aşağı axır VƏ dəyişikliklər siqnalın özünə müraciət edən və siqnal getter-ini birbaşa çağırmayan (event vasitəsilə) geri valideynə ötürülür.
</docs-step>

<docs-step title="İki tərəfli binding-i test edin">
İki tərəfli binding-in işlədiyini görmək üçün tətbiqlə qarşılıqlı əlaqədə olun:

1. **Checkbox-ları klikləyin** - Komponent öz vəziyyətini yeniləyir və valideyni xəbərdar edir
2. **"Valideyndən şərtləri dəyiş" klikləyin** - Valideyn yeniləmələri komponentə aşağı ötürülür
3. **"Hamısını sıfırla" klikləyin** - Valideyn hər iki modeli sıfırlayır və komponentlər avtomatik yenilənir

Həm valideyn, həm də övlad paylaşılan vəziyyəti yeniləyə bilər və hər ikisi avtomatik olaraq sinxron qalır!
</docs-step>

</docs-workflow>

Mükəmməl! Siz model siqnallarının iki tərəfli binding-i necə təmin etdiyini öyrəndiniz:

- **Model siqnalları** - Həm oxuna, həm də yazıla bilən dəyərlər üçün `model()` və `model.required()` istifadə edin
- **İki tərəfli binding** - Valideyn siqnallarını övlad modellərinə bağlamaq üçün `[(property)]` sintaksisindən istifadə edin
- **UI komponentləri üçün mükəmməldir** - Checkbox-lar, forma idarəetmə elementləri və öz vəziyyətini idarə etməli olan vidjetlər
- **Avtomatik sinxronizasiya** - Valideyn və övlad əllə hadisə işlənməsi (event handling) olmadan sinxron qalır

**Nə vaxt `model()` yoxsa `input()` istifadə etməli:**

- Məlumatların yalnız aşağı axdığı hallar üçün `input()` istifadə edin (göstərilən məlumatlar, konfiqurasiya)
- Öz dəyərini yeniləməli olan UI komponentləri üçün `model()` istifadə edin (forma idarəetmə elementləri, keçid düymələri və s.)

Növbəti dərsdə, [servislərlə siqnallardan istifadə etməyi](/tutorials/signals/7-using-signals-with-services) öyrənəcəksiniz!
