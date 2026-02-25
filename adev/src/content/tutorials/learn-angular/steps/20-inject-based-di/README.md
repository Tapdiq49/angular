# İnyeksiya əsaslı aslılıq inyeksiyası (Inject-based DI)

İnyeksiya edilə bilən (injectable) servisin yaradılması Angular-da aslılıq inyeksiyası (DI) sisteminin birinci hissəsidir. Bəs bir servisi komponentə necə inyeksiya edirsiniz? Angular-ın uyğun kontekstdə istifadə edilə bilən `inject()` adlı rahat bir funksiyası var.

QEYD: İnyeksiya kontekstləri bu təlimatın əhatə dairəsindən kənardır, lakin siz [aslılıq inyeksiyası (DI) essentials bələdçisində](/essentials/dependency-injection) və [DI kontekst bələdçisində](guide/di/dependency-injection-context) daha çox öyrənə bilərsiniz.

Bu fəaliyyətdə siz servisi necə inyeksiya edəcəyinizi və ondan komponentdə necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

Class property-lərini DI sistemi tərəfindən təmin edilən dəyərlərlə inisializasiya etmək tez-tez faydalı olur. Budur bir nümunə:

```ts {highlight:[3]}
@Component({...})
class PetCareDashboard {
  petRosterService = inject(PetRosterService);
}
```

<docs-workflow>

<docs-step title="`CarService`-i inyeksiya edin">

`app.ts` faylında `inject()` funksiyasından istifadə edərək `CarService`-i inyeksiya edin və onu `carService` adlı property-yə təyin edin.

QEYD: `carService` property-si ilə `CarService` class-ı arasındakı fərqə diqqət yetirin.

</docs-step>

<docs-step title="`carService` instansiyasından (instance) istifadə edin">

`inject(CarService)` çağırmaq sizə `carService` property-sində saxlanılan və tətbiqinizdə istifadə edə biləcəyiniz `CarService` instansiyasını verdi.

`display` property-sini aşağıdakı implementasiya ilə inisializasiya edin:

```ts
display = this.carService.getCars().join(' ⭐️ ');
```

</docs-step>

<docs-step title="`App` template-ini yeniləyin">

`app.ts` faylındakı komponent template-ini aşağıdakı kodla yeniləyin:

```ts
template: `<p>Avtomobil Siyahısı: {{ display }}</p>`,
```

</docs-step>

</docs-workflow>

Siz indicə komponentə ilk servisinizi inyeksiya etdiniz - fantastik nəticədir.
