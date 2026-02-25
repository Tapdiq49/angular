# İlk Angular tətbiqinizi qurun

Bu təlimat Angular-da kod yazmağa başlamaq üçün bilməli olduğunuz Angular konsepsiyalarını təqdim edən dərslərdən ibarətdir.

İstədiyiniz qədər və ya az dərs edə bilərsiniz və onları hər hansı bir ardıcıllıqla yerinə yetirə bilərsiniz.

FAYDALI: Videoya üstünlük verirsiniz? Bu təlimat üçün tam [YouTube kursumuz](https://youtube.com/playlist?list=PL1w1q3fL4pmj9k1FrJ3Pe91EPub2_h4jF&si=1q9889ulHp8VZ0e7) da var!

<docs-video src="https://www.youtube.com/embed/xAT0lHYhHMY?si=cKUW_MGn3MesFT7o"/>

## Başlamazdan əvvəl

Bu təlimatdan ən yaxşı təcrübəni əldə etmək üçün, uğurlu olmaq üçün lazım olan her şeyə sahib olduğunuzdan əmin olmaq üçün bu tələbləri nəzərdən keçirin.

### Təcrübəniz

Bu təlimatdakı dərslər aşağıdakılar üzrə təcrübənizin olduğunu fərz edir:

1. HTML-i birbaşa redaktə etməklə HTML veb səhifəsi yaratmaq.
1. JavaScript-də veb sayt məzmununu proqramlaşdırmaq.
1. Cascading Style Sheet (CSS) məzmununu oxumaq və selektorların necə istifadə edildiyini başa düşmək.
1. Kompüterinizdə tapşırıqları yerinə yetirmək üçün əmr satırı (command-line) təlimatlarından istifadə etmək.

### Avadanlığınız

Bu dərslər Angular alətlərinin yerli quraşdırılması və ya quraşdırılmış redaktorumuz vasitəsilə tamamlana bilər. Yerli Angular inkişafı Windows, MacOS və ya Linux əsaslı sistemlərdə həyata keçirilə bilər.

QEYD: Yalnız yerli redaktorunuz üçün ola biləcək addımları göstərən bu kimi xəbərdarlıqlara diqqət yetirin.

## İlk Angular tətbiqinizin konseptual ön baxışı

Bu təlimatdakı dərslər icarəyə verilən evlərin siyahısını göstərən və hər bir evin təfərrüatlarını əks etdirən Angular tətbiqi yaradır.
Bu tətbiq bir çox Angular tətbiqləri üçün ümumi olan xüsusiyyətlərdən istifadə edir.

<img alt="Evlərin ana səhifəsinin çıxışı" src="assets/images/tutorials/first-app/homes-app-landing-page.png">

## Yerli inkişaf mühiti

QEYD: Bu addım yalnız yerli mühitiniz üçündür!

Bu addımları bu təlimat üçün istifadə etmək istədiyiniz kompüterdə əmr satırı alətində yerinə yetirin.

<docs-workflow>

<docs-step title="Angular-ın tələb etdiyi `node.js` versiyasını müəyyənləşdirin">
Angular Node-un aktiv LTS və ya texniki xidmət (maintenance) LTS versiyasını tələb edir. Gəlin `node.js` versiyanızı təsdiqləyək. Xüsusi versiya tələbləri haqqında məlumat üçün [package.json faylındakı](https://unpkg.com/browse/@angular/core@15.1.5/package.json) engines property-sinə baxın.

**Terminal** pəncərəsindən:

1. Aşağıdakı əmri işlədin: `node --version`
1. Göstərilən versiya nömrəsinin tələblərə cavab verdiyini təsdiqləyin.
   </docs-step>

<docs-step title="Angular üçün düzgün `node.js` versiyasını quraşdırın">
Əgər `node.js` versiyanız quraşdırılmayıbsa, zəhmət olmasa [nodejs.org ünvanındakı quraşdırma təlimatlarını](https://nodejs.org/en/download/) izləyin.
</docs-step>

<docs-step title="Angular-ın ən son versiyasını quraşdırın">
`node.js` və `npm` quraşdırıldıqdan sonra növbəti addım effektiv Angular inkişafı üçün alətlər təqdim edən [Angular CLI](tools/cli)-ni quraşdırmaqdır.

**Terminal** pəncərəsindən aşağıdakı əmri işlədin: `npm install -g @angular/cli`.
</docs-step>

<docs-step title="İnteqrasiya olunmuş inkişaf mühitini (IDE) quraşdırın">
Angular ilə tətbiqlər qurmaq üçün üstünlük verdiyiniz hər hansı alətdən istifadə etməkdə sərbəstsiniz. Aşağıdakıları tövsiyə edirik:

1. [Visual Studio Code](https://code.visualstudio.com/)
2. Könüllü, lakin tövsiyə olunan bir addım olaraq [Angular Language Service](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template) quraşdıraraq proqramçı təcrübənizi daha da artıra bilərsiniz.
3. [WebStorm](https://www.jetbrains.com/webstorm/)
   </docs-step>

<docs-step title="Könüllü: AI dəstəkli IDE-nizi quraşdırın">

Əgər bu təlimatı üstünlük verdiyiniz AI dəstəkli IDE-də izləyirsinizsə, [Angular prompt qaydaları və ən yaxşı təcrübələrə baxın](/ai/develop-with-ai).

</docs-step>

</docs-workflow>

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="/overview" title="Angular nədir"/>
  <docs-pill href="/tools/cli/setup-local" title="Yerli mühitin və iş sahəsinin qurulması"/>
  <docs-pill href="/cli" title="Angular CLI Arayışı"/>
</docs-pill-row>
