# Resource API vasitəsilə siqnallarla asinxron məlumatları idarə etmək

Artıq [bağlı siqnallar (linked signals) ilə vəziyyəti necə törədəcəyinizi](/tutorials/signals/3-deriving-state-with-linked-signals) öyrəndiniz, gəlin Resource API vasitəsilə asinxron məlumatları necə idarə edəcəyimizi araşdıraq. Resource API daxili yükləmə vəziyyətləri (loading states), xəta emalı və sorğu idarəetməsi ilə siqnallardan istifadə edərək asinxron əməliyyatları idarə etmək üçün güclü bir yol təqdim edir.

Bu fəaliyyətdə siz məlumatları asinxron şəkildə yükləmək üçün `resource()` funksiyasından necə istifadə edəcəyinizi və Resource API-ni iş başında nümayiş etdirən istifadəçi profili yükləyicisi quraraq asinxron əməliyyatların müxtəlif vəziyyətlərini necə idarə edəcəyinizi öyrənəcəksiniz.

<hr />

<docs-workflow>

<docs-step title="Resource funksiyasını və API-ni import edin">
Mövcud import-larınıza `resource` əlavə edin və saxta (mock) API funksiyasını import edin.

```ts
// Mövcud import-lara resource əlavə edin
import {Component, signal, computed, resource, ChangeDetectionStrategy} from '@angular/core';
// Mock API funksiyasını import edin
import {getUserData} from './user-api';
```

</docs-step>

<docs-step title="İstifadəçi məlumatları üçün bir resurs yaradın">
Komponent class-ına istifadəçi ID siqnalına əsasən istifadəçi məlumatlarını yükləyən bir resurs yaradan property əlavə edin.

```ts
userId = signal(1);

userResource = resource({
  params: () => ({id: this.userId()}),
  loader: (params) => getUserData(params.params.id),
});
```

</docs-step>

<docs-step title="Resursla qarşılıqlı əlaqə qurmaq üçün metodlar əlavə edin">
İstifadəçi ID-sini dəyişən və resursu yenidən yükləyən metodlar əlavə edin.

```ts
loadUser(id: number) {
  this.userId.set(id);
}

reloadUser() {
  this.userResource.reload();
}
```

Parametr siqnalını (params signal) dəyişdirmək avtomatik olaraq yenidən yükləməni tətikləyir, yaxud `reload()` ilə əllə yenidən yükləyə bilərsiniz.
</docs-step>

<docs-step title="Resurs vəziyyətləri üçün computed siqnallar yaradın">
Resursun müxtəlif vəziyyətlərinə daxil olmaq üçün computed siqnallar əlavə edin.

```ts
isLoading = computed(() => this.userResource.status() === 'loading');
hasError = computed(() => this.userResource.status() === 'error');
```

Resurslar 'loading', 'success' və ya 'error' ola bilən `status()` siqnalı, yüklənmiş məlumat üçün `value()` siqnalı və məlumatın əlçatan olub-olmadığını təhlükəsiz şəkildə yoxlayan `hasValue()` metodu təmin edir.
</docs-step>

<docs-step title="Düymələri qoşun və resurs vəziyyətlərini göstərin">
Template strukturu artıq təmin edilib. İndi hər şeyi birləşdirin:

Hissə 1. **Düymələrə klikləmə emalçılarını (click handlers) əlavə edin:**

```html
<button (click)="loadUser(1)">İstifadəçi 1-i yüklə</button>
<button (click)="loadUser(2)">İstifadəçi 2-ni yüklə</button>
<button (click)="loadUser(999)">Yanlış istifadəçini yüklə</button>
<button (click)="reloadUser()">Yenidən yüklə</button>
```

Hissə 2. **Yer tutucanı (placeholder) resurs vəziyyəti emalı ilə əvəz edin:**

```angular-html
@if (isLoading()) {
  <p>İstifadəçi yüklənir...</p>
} @else if (hasError()) {
  <p class="error">Xəta: {{ userResource.error()?.message }}</p>
} @else if (userResource.hasValue()) {
  <div class="user-info">
    <h3>{{ userResource.value().name }}</h3>
    <p>{{ userResource.value().email }}</p>
  </div>
}
```

Resurs onun vəziyyətini yoxlamaq üçün fərqli metodlar təqdim edir:

- `isLoading()` - məlumatlar çəkilərkən true olur
- `hasError()` - xəta baş verdikdə true olur
- `userResource.hasValue()` - məlumat əlçatan olduqda true olur
- `userResource.value()` - yüklənmiş məlumatlara müraciət edir
- `userResource.error()` - xəta məlumatlarına müraciət edir

</docs-step>

</docs-workflow>

Mükəmməl! Siz artıq siqnallarla Resource API-dən necə istifadə edəcəyinizi öyrəndiniz. Yadda saxlanmalı əsas konsepsiyalar:

- **Resurslar reaktivdir**: Parametrlər dəyişdikdə onlar avtomatik olaraq yenidən yüklənirlər
- **Daxili vəziyyət idarəetməsi**: Resurslar `status()`, `value()` və `error()` siqnalları təmin edir
- **Avtomatik təmizləmə**: Resurslar sorğunun ləğvini və təmizlənməsini avtomatik idarə edir
- **Əllə idarəetmə**: Lazım olduqda sorğuları əllə yenidən yükləyə və ya dayandıra bilərsiniz

Növbəti dərsdə, [input siqnalları vasitəsilə komponentlərə məlumat ötürməyi](/tutorials/signals/5-component-communication-with-signals) öyrənəcəksiniz!
