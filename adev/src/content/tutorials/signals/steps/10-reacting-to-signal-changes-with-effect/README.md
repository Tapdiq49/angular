# effect ilə siqnal dəyişikliklərinə reaksiya vermək

Artıq [siqnal sorğuları ilə övlad elementləri sorğulamağı](/tutorials/signals/9-query-child-elements-with-signal-queries) öyrəndiniz, gəlin effektlərlə (effects) siqnal dəyişikliklərinə necə reaksiya veriləcəyini araşdıraq. Effektlər aslılıqları dəyişdikdə avtomatik işləyən funksiyalardır, bu da onları loqlama (logging), DOM manipulyasiyası və ya API çağırışları kimi yan təsirlər (side effects) üçün mükəmməl edir.

**Vacib: Effektlər müraciət edəcəyiniz ən son API olmalıdır.** Törəmə dəyərlər üçün həmişə `computed()`, həm törədilə bilən, həm də əllə təyin edilə bilən dəyərlər üçün isə `linkedSignal()` funksiyasına üstünlük verin. Əgər bir effektlə məlumatları bir siqnaldan digərinə kopyalayırsınızsa, bu, həqiqət mənbəyini (source-of-truth) daha yuxarı səviyyəyə köçürməli və bunun əvəzinə `computed()` və ya `linkedSignal()` istifadə etməli olduğunuzu göstərən bir işarədir. Effektlər siqnal vəziyyətini imperativ, qeyri-siqnal API-ləri ilə sinxronlaşdırmaq üçün ən yaxşısıdır.

Bu fəaliyyətdə siz siqnal dəyişikliklərinə cavab verən legitim yan təsirlər üçün `effect()` funksiyasından necə düzgün istifadə edəcəyinizi öyrənəcəksiniz.

<hr />

Artıq siqnalları qurulmuş mövzu meneceri (theme manager) tətbiqiniz var. İndi siqnal dəyişikliklərinə avtomatik reaksiya vermək üçün effektlər əlavə edəcəksiniz.

<docs-workflow>

<docs-step title="effect funksiyasını import edin">
Mövcud import-larınıza `effect` əlavə edin.

```ts
// Mövcud import-lara effect əlavə edin
import {Component, signal, computed, effect, ChangeDetectionStrategy} from '@angular/core';
```

`effect` funksiyası oxuduğu hər hansı bir siqnal dəyişdikdə avtomatik olaraq işləyən reaktiv bir yan təsir yaradır.
</docs-step>

<docs-step title="Local storage üçün effekt yaradın">
Mövzu (theme) dəyişdikdə onu avtomatik olaraq local storage-ə saxlayan bir effekt əlavə edin.

```ts
constructor() {
  // Mövzu dəyişdikdə onu localStorage-də yadda saxlayın
  effect(() => {
    localStorage.setItem('theme', this.theme());
    console.log('Mövzu localStorage-ə saxlanıldı:', this.theme());
  });
}
```

Bu effekt mövzu siqnalı dəyişdikdə işləyir və istifadəçinin seçimini avtomatik olaraq qalıcı edir.
</docs-step>

<docs-step title="İstifadəçi fəaliyyətini loqlamaq üçün effekt yaradın">
İstifadəçi daxil olduqda və ya çıxdıqda loq qeydi aparan bir effekt əlavə edin.

```ts
constructor() {
  // ... əvvəlki effekt

  // İstifadəçi fəaliyyəti dəyişikliklərini loqlayın
  effect(() => {
    const status = this.isLoggedIn() ? 'daxil oldu' : 'çıxış etdi';
    const user = this.username();
    console.log(`İstifadəçi ${user} ${status}`);
  });
}
```

Bu effekt efektlərin birdən çox siqnalı necə oxuya bildiyini və onlardan hər hansı birindəki dəyişikliklərə necə reaksiya verə bildiyini nümayiş etdirir.
</docs-step>

<docs-step title="Təmizləmə (cleanup) funksiyası olan effekt yaradın">
Taymer quran və komponent məhv edildikdə (destroy) təmizləmə aparan bir effekt əlavə edin.

```ts
constructor() {
  // ... əvvəlki effektlər

  // Təmizləmə (cleanup) funksiyası olan taymer effekti
  effect((onCleanup) => {
    const interval = setInterval(() => {
      console.log('Taymer döyüntüsü - Cari mövzu:', this.theme());
    }, 5000);

    // Effekt məhv edildikdə taymeri təmizləyin
    onCleanup(() => {
      clearInterval(interval);
      console.log('Taymer təmizləndi');
    });
  });
}
```

Bu effekt effektlər məhv edildikdə və ya yenidən işlədikdə resursların necə təmizlənməsini nümayiş etdirir.
</docs-step>

<docs-step title="Effektləri test edin">
Brauzer konsolunu açın və tətbiqlə qarşılıqlı əlaqədə olun:

- **Mövzunu dəyişin (Toggle Theme)** - localStorage yadda saxlamalarını və taymer loqlarını görün
- **Daxil olun/Çıxın (Login/Logout)** - İstifadəçi fəaliyyəti loqlarını görün
- **Taymeri izləyin** - Hər 5 saniyədən bir mövzu loqlarını görün

Effektlər izlədikləri siqnallar dəyişdikdə avtomatik işləyir!
</docs-step>

</docs-workflow>

Mükəmməl! Siz artıq siqnallarla effektlərdən necə istifadə edəcəyinizi öyrəndiniz. Yadda saxlanmalı əsas konsepsiyalar:

- **Effektlər reaktivdir**: Oxuduqları hər hansı bir siqnal dəyişdikdə onlar avtomatik işləyirlər
- **Yalnız yan təsirlər (side effects)**: Loqlama, DOM manipulyasiyası, API çağırışları və imperativ API-lərlə sinxronizasiya üçün mükəmməldir
- **Təmizləmə (Cleanup)**: Taymerlər və ya abunəliklər (subscriptions) kimi resursları təmizləmək üçün `onCleanup` callback-indən istifadə edin
- **Avtomatik izləmə**: Effektlər hansı siqnalları oxuduqlarını avtomatik izləyir və həmin siqnallar dəyişdikdə yenidən işləyir

**Unutmayın: Effektlərdən qənaətlə istifadə edin!** Bu dərsdəki nümunələr (localStorage sinxronizasiyası, loqlama, taymerlər) uyğun istifadə hallaridir. Aşağıdakılar üçün effektlərdən qaçının:

- Digər siqnallardan dəyər törətmək - bunun əvəzinə `computed()` istifadə edin
- Yazıla bilən törəmə vəziyyət yaratmaq - bunun əvəzinə `linkedSignal()` istifadə edin
- Siqnallar arasında məlumat kopyalamaq - ortaq bir həqiqət mənbəyi istifadə etmək üçün strukturu dəyişin

Effektlər güclüdür, lakin `computed()` və `linkedSignal()` sizin probleminizi həll edə bilmədikdə ən son çarə olmalıdır.
