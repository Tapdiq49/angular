# Linked signals (bağlı siqnallar) ilə vəziyyəti törətmək

Artıq [computed siqnallar ilə vəziyyəti necə törədəcəyinizi](/tutorials/signals/2-deriving-state-with-computed-signals) öyrəndiniz, burada istifadəçi statusunuzu avtomatik izləyən `notificationsEnabled` üçün bir computed siqnal yaratdınız. Bəs istifadəçilər onlayn olduqda belə bildirişləri əllə (manually) deaktiv etmək istəsələr necə? Məhz burada bağlı siqnallar köməyə çatır.

Linked signals (bağlı siqnallar) mənbə siqnalları ilə reaktiv əlaqəni saxlayan yazıla bilən (writable) siqnallardır. Onlar normalda bir hesablama nəticəsini izləyən, lakin lazım olduqda üstündən yazıla bilən (overridden) vəziyyət yaratmaq üçün mükəmməldir.

Bu fəaliyyətdə siz əvvəlki istifadəçi statusu sisteminin computed `notificationsEnabled` dəyərini yazıla bilən bir linked siqnalına çevirərək `linkedSignal()` funksiyasının `computed()` funksiyasından nə ilə fərqləndiyini öyrənəcəksiniz.

<hr />

<docs-workflow>

<docs-step title="linkedSignal funksiyasını import edin">
Mövcud import-larınıza `linkedSignal` əlavə edin.

```ts
// Mövcud import-lara linkedSignal əlavə edin
import {Component, signal, computed, linkedSignal, ChangeDetectionStrategy} from '@angular/core';
```

</docs-step>

<docs-step title="Eyni ifadə ilə computed-u linkedSignal-a çevirin">
Computed `notificationsEnabled` dəyərini tamamilə eyni ifadədən istifadə edərək bir linkedSignal ilə əvəz edin:

```ts
// Əvvəllər (2-ci dərsdən):
// notificationsEnabled = computed(() => this.userStatus() === 'online');

// İndi linkedSignal ilə - eyni ifadə, lakin yazıla bilən:
notificationsEnabled = linkedSignal(() => this.userStatus() === 'online');
```

İfadə eynidir, lakin linkedSignal yazıla bilən bir siqnal yaradır. O, `userStatus` dəyişdikdə hələ də avtomatik yenilənəcək, lakin siz onu əllə də təyin edə bilərsiniz.
</docs-step>

<docs-step title="Bildirişləri əllə dəyişmək üçün bir metod əlavə edin">
Bağlı siqnalların üzərinə birbaşa yazıla bildiyini nümayiş etdirmək üçün bir metod əlavə edin:

```ts
toggleNotifications() {
  // Bu, linkedSignal ilə işləyir, lakin computed ilə xəta verərdi!
  this.notificationsEnabled.set(!this.notificationsEnabled());
}
```

Əsas fərq budur: computed siqnallar yalnız oxunandır, lakin bağlı siqnallar reaktiv əlaqələrini qoruyaraq əllə yenilənə bilər.
</docs-step>

<docs-step title="Əllə bildiriş idarəetməsini əlavə etmək üçün template-i yeniləyin">
Bildirişlər üçün keçid (toggle) düyməsi əlavə etmək üçün template-i yeniləyin:

```angular-html
<div class="status-info">
  <div class="notifications">
    <strong>Bildirişlər:</strong>
    @if (notificationsEnabled()) {
      Aktivdir
    } @else {
      Deaktivdir
    }
    <button (click)="toggleNotifications()" class="override-btn">
      @if (notificationsEnabled()) {
        Deaktiv et
      } @else {
        Aktiv et
      }
    </button>
  </div>
  <!-- mövcud mesaj və iş saatları div-ləri qalır -->
</div>
```

</docs-step>

<docs-step title="Reaktiv davranışı müşahidə edin">
İndi davranışı test edin:

1. İstifadəçi statusunu dəyişin - `notificationsEnabled` dəyərinin avtomatik necə yeniləndiyinə diqqət yetirin
2. Bildirişləri əllə dəyişin - bu, hesablanmış dəyərin üstündən yazır
3. Statusu yenidən dəyişin - bağlı siqnal öz hesablaması ilə yenidən sinxronlaşır

Bu, bağlı siqnalların hətta əllə təyin edildikdən sonra da reaktiv əlaqələrini saxladığını nümayiş etdirir!
</docs-step>

</docs-workflow>

Mükəmməl! Siz computed və linked siqnallar arasındakı əsas fərqləri öyrəndiniz:

- **Computed siqnallar**: Yalnız oxunandır, həmişə digər siqnallardan törədilir
- **Linked siqnallar**: Yazıla biləndir, həm törədilə bilər, həm də əllə yenilənə bilər
- **Nə vaxt computed istifadə etməli**: Dəyər həmişə hesablanmalıdır
- **Nə vaxt linkedSignal istifadə etməli**: Üstündən yazıla bilən standart bir hesablamaya ehtiyacınız olduqda

Növbəti dərsdə, [siqnallarla asinxron məlumatları necə idarə etməyi](/tutorials/signals/4-managing-async-data-with-signals) öyrənəcəksiniz!
