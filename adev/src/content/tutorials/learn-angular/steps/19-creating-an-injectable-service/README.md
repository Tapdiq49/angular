# İnyeksiya edilə bilən (injectable) servisin yaradılması

Angular-da aslılıqların inyeksiyası (Dependency Injection - DI) freymvorkun ən güclü xüsusiyyətlərindən biridir. Dependency Injection-ı Angular-ın tətbiqiniz üçün lazım olan resursları icra zamanı (runtime) _təmin etmək_ abilitəsi kimi düşünün. Aslılıq bir servis və ya digər resurslar ola bilər.

QEYD: [Essentials bələdçisində aslılıqların inyeksiyası (DI)](/essentials/dependency-injection) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz `injectable` (inyeksiya edilə bilən) servisi necə yaradacağınızı öyrənəcəksiniz.

<hr>

Bir servisi istifadə etməyin bir yolu, verilənlər və API-lərlə qarşılıqlı əlaqə vasitəsi kimi çıxış etməkdir. Servisi təkrar istifadə edilə bilən etmək üçün məntiqi servisdə saxlamalı və ehtiyac olduqda onu tətbiq boyu paylaşmalısınız.

Bir servisin DI sistemi tərəfindən inyeksiya edilməyə uyğun olması üçün `@Injectable` dekoratorundan istifadə edin. Məsələn:

```ts {highlight:[1,2,3]}
@Injectable({
  providedIn: 'root',
})
class UserService {
  // məlumatları əldə etmək və qaytarmaq üçün metodlar
}
```

`@Injectable` dekoratoru DI sisteminə `UserService`-in bir class daxilində sorğu edilə biləcəyini bildirir. `providedIn` bu resursun hansı sahədə (scope) əlçatan olduğunu müəyyən edir. Hələlik `providedIn: 'root'` ifadəsinin `UserService`-in bütün tətbiq üçün əlçatan olduğu mənasına gəldiyini bilmək kifayətdir.

Yaxşı, indi siz sınayın:

<docs-workflow>

<docs-step title="`@Injectable` dekoratorunu əlavə edin">
`car.service.ts` faylındakı kodu `@Injectable` dekoratorunu əlavə edərək yeniləyin.
</docs-step>

<docs-step title="Dekoratoru konfiqurasiya edin">
Dekoratora ötürülən obyektin içindəki dəyərlər dekorator üçün konfiqurasiya sayılır.
<br>
`car.service.ts` faylındakı `@Injectable` dekoratorunu `providedIn: 'root'` konfiqurasiyasını daxil edəcək şəkildə yeniləyin.

İPUCU: Düzgün sintaksisi tapmaq üçün yuxarıdakı nümunədən istifadə edin.

</docs-step>

</docs-workflow>

Əla 👍 artıq bu servis `injectable`-dır və bu əyləncədə iştirak edə bilər. Servis artıq `injectable` olduğuna görə, gəlin onu bir komponentə inyeksiya etməyə çalışaq 👉
