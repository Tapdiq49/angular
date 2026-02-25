# Computed siqnallarla vəziyyəti (state) törətmək

Artıq [siqnalları necə yaradacağınızı və yeniləyəcəyinizi](/tutorials/signals/1-creating-your-first-signal) öyrəndiyinizə görə, gəlin computed siqnalları haqqında öyrənək. Computed siqnallar aslılıqları dəyişdikdə avtomatik olaraq yenilənən törəmə dəyərlərdir. Onlar digər siqnallara əsaslanan reaktiv hesablamalar yaratmaq üçün mükəmməldir.

Bu fəaliyyətdə siz əsas siqnallar dəyişdikdə avtomatik olaraq yenilənən törəmə vəziyyət yaratmaq üçün `computed()` funksiyasından necə istifadə edəcəyinizi öyrənəcəksiniz.

Gəlin istifadəçi statusu siqnalımızdan məlumat əldə edən computed dəyərlər əlavə edərək istifadəçi statusu sistemimizi təkmilləşdirək. Başlanğıc kodu indi üç status seçimini daxil edir: `'online'`, `'away'` və `'offline'`.

<hr />

<docs-workflow>

<docs-step title="Computed funksiyasını import edin">
Mövcud import-larınıza `computed` əlavə edin.

```ts
// Mövcud import-lara computed əlavə edin
import {Component, signal, computed, ChangeDetectionStrategy} from '@angular/core';
```

</docs-step>

<docs-step title="Bildirişlər üçün bir computed siqnal yaradın">
İstifadəçi statusuna əsasən bildirişlərin aktiv edilib-edilməməsini müəyyən edən bir computed siqnal əlavə edin.

```ts
notificationsEnabled = computed(() => this.userStatus() === 'online');
```

Bu computed siqnal `userStatus` siqnalı dəyişdikdə avtomatik olaraq yenidən hesablanacaq. Siqnalın dəyərini oxumaq üçün computed funksiyasının daxilində `this.userStatus()` necə çağırdığımıza diqqət yetirin.
</docs-step>

<docs-step title="Təsviri mesaj üçün bir computed siqnal yaradın">
İstifadəçi statusuna əsasən təsviri mesaj yaradan bir computed siqnal əlavə edin.

```ts
statusMessage = computed(() => {
  const status = this.userStatus();
  switch (status) {
    case 'online':
      return 'Görüşlər və mesajlar üçün əlçatandır';
    case 'away':
      return 'Müvəqqəti olaraq uzaqdadır, tezliklə cavab verəcək';
    case 'offline':
      return 'Əlçatan deyil, sonra yenidən yoxlayın';
    default:
      return 'Status naməlumdur';
  }
});
```

Bu, computed siqnalların switch operatorları və string transformasiyaları ilə daha mürəkkəb məntiqi necə idarə edə bildiyini göstərir.
</docs-step>

<docs-step title="İş saatları əlçatanlığını hesablayan bir computed siqnal yaradın">
İstifadəçinin iş saatları daxilində olub-olmadığını hesablayan bir computed siqnal əlavə edin.

```ts
isWithinWorkingHours = computed(() => {
  const now = new Date();
  const hour = now.getHours();
  const isWeekday = now.getDay() > 0 && now.getDay() < 6;
  return isWeekday && hour >= 9 && hour < 17 && this.userStatus() !== 'offline';
});
```

Bu, computed siqnalların hesablamalar apara bildiyini və birdən çox məlumat mənbəyini birləşdirə bildiyini nümayiş etdirir. `userStatus` dəyişdikdə dəyər avtomatik yenilənir.
</docs-step>

<docs-step title="Computed dəyərləri template-də göstərin">
Template-də artıq "Yüklənir..." göstərən yer tutucular (placeholders) var. Onları öz computed siqnallarınızla əvəz edin:

1. Bildirişlər üçün, `Yüklənir...` yazısını `@if` bloku ilə əvəz edin:

   ```angular-html
   @if (notificationsEnabled()) {
     Aktivdir
   } @else {
     Deaktivdir
   }
   ```

1. Mesaj üçün, `Yüklənir...` yazısını bununla əvəz edin:

   ```angular-html
   {{ statusMessage() }}
   ```

1. İş saatları üçün, `Yüklənir...` yazısını `@if` bloku ilə əvəz edin:

   ```angular-html
   @if (isWithinWorkingHours()) {
     Bəli
   } @else {
     Xeyr
   }
   ```

Computed siqnalların da normal siqnallar kimi - mötərizə ilə çağırıldığını unutmayın!
</docs-step>

</docs-workflow>

Mükəmməl! Siz artıq computed siqnalları necə yaradacağınızı öyrəndiniz.

Budur yadda saxlanmalı bəzi əsas məqamlar:

- **Computed siqnallar reaktivdir**: Onların aslılıqları dəyişdikdə onlar avtomatik yenilənirlər
- **Onlar yalnız oxunandır (read-only)**: Siz computed dəyərləri birbaşa təyin edə bilməzsiniz, onlar digər siqnallardan törədilir
- **Onlar mürəkkəb məntiq ehtiva edə bilər**: Hesablamalar, transformasiyalar və törəmə vəziyyətlər üçün onlardan istifadə edin
- **Onlar dinamik vəziyyətə əsaslanan performanslı hesablamalar aparmaq imkanı verir**: Angular onları yalnız aslılıqları həqiqətən dəyişdikdə yenidən hesablayır

Növbəti dərsdə, [linkedSignals ilə vəziyyəti törətməyin fərqli yolunu](/tutorials/signals/3-deriving-state-with-linked-signals) öyrənəcəksiniz!
