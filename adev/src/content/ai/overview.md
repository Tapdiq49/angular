<!-- TODO: need an Angular + AI logo -->

<docs-decorative-header title="AI ilə Qurun (Build with AI)" imgSrc="adev/src/assets/images/what_is_angular.svg"> <!-- markdownlint-disable-line -->
AI dəstəkli tətbiqlər qurun. AI ilə daha sürətli inkişaf edin.
</docs-decorative-header>

HELPFUL: Sevdiyiniz AI dəstəkli IDE-də qurmağa başlamaq istəyirsiniz? <br>Bizim [sorğu (prompt) qaydalarımıza və ən yaxşı təcrübələrimizə](/ai/develop-with-ai) baxın.

Böyük dil modelləri (LLM) ilə generativ AI (GenAI), fərdiləşdirilmiş məzmun, ağıllı tövsiyələr, media yaratma və anlama, məlumatların ümumiləşdirilməsi və dinamik funksionallıq daxil olmaqla mürəkkəb və cəlbedici tətbiq təcrübələrinin yaradılmasına imkan verir.

Bu kimi xüsusiyyətlər əvvəllər dərin sahə ekspertizası və əhəmiyyətli mühəndislik səyi tələb edirdi. Lakin yeni məhsullar və SDK-lar giriş maneəsini aşağı salır. Angular-ın aşağıdakılara görə veb tətbiqinizə AI inteqrasiyası üçün çox uyğundur:

- Angular-ın güclü şablon (templating) API-ləri, yaradılan məzmundan ibarət dinamik, təmiz şəkildə mürəkkəb arayüzlərin (UI) yaradılmasına imkan verir
- Məlumat və vəziyyəti dinamik şəkildə idarə etmək üçün nəzərdə tutulmuş siqnal-əsaslı (signal-based) güclü arxitektura
- Angular, AI SDK-ları və API-ləri ilə problemsiz inteqrasiya edir

Bu bələdçi, Angular tətbiqlərinizi bu gün AI ilə zənginləşdirmək üçün [Genkit](/ai#build-ai-powered-applications-with-genkit-and-angular), [Firebase AI Logic](/ai#build-ai-powered-applications-with-firebase-ai-logic-and-angular) və [Gemini API](/ai#build-ai-powered-applications-with-gemini-api-and-angular)-dən necə istifadə edə biləcəyinizi nümayiş etdirir. Bu bələdçi, AI-nin Angular tətbiqlərinə inteqrasiyasına necə başlayacağınızı izah edərək AI dəstəkli veb tətbiq inkişafı səfərinizə başlamanıza kömək edəcək. Bu bələdçi həmçinin sürətlə ayağa qalxmaq üçün istifadə edə biləcəyiniz başlangıc dəstlər (starter kits), nümunə kodlar və ümumi iş axınları üçün reseptlər kimi resursları da paylaşır.

Başlamaq üçün Angular haqqında əsas anlayışa sahib olmalısınız. Angular-a yeni başlayırsınız? [Əsaslar bələdçimizi](/essentials) və ya [başlanğıc dərsliklərini (tutorials)](/tutorials) sınayın.

QEYD: Bu səhifə Google AI məhsulları ilə inteqrasiyaları və nümunələri özündə cəmləşdirsə də, Genkit kimi alətlər model-agnostikdir (model-agnostic) və öz modelinizi seçməyə imkan verir. Bir çox halda, nümunələr və kod nümunələri digər üçüncü tərəf həllərə də tətbiq oluna bilər.

## Başlamaq

AI dəstəkli tətbiqlər qurmaq yeni və sürətlə inkişaf edən bir sahədir. Haradan başlayacağınıza və hansı texnologiyaları seçəcəyinizə qərar vermək çətin ola bilər. Aşağıdakı bölmə seçmək üçün üç variant təqdim edir:

1. _Genkit_, tam stack tətbiqlər qurmaq üçün [dəstəklənən model və interfeysi vahid API ilə](https://genkit.dev) seçmə imkanı verir. Fərdiləşdirilmiş tövsiyələr kimi mürəkkəb arxa plan (back-end) AI məntiqi tələb edən tətbiqlər üçün idealdır.

1. _Firebase AI Logic_, brauzerda birbaşa AI xüsusiyyətləri üçün ən uyğun olan yalnız müştəri tərəfli (client-side) tətbiqlər və ya mobil tətbiqlər qurmaq üçün Google-un modellərinə təhlükəsiz müştəri tərəfli API təqdim edir. Real vaxtlı mətn təhlili və ya əsas chatbotlar kimi brauzerda birbaşa interaktiv AI xüsusiyyətləri üçün ən yaxşısıdır.

1. _Gemini API_, tam stack tətbiqlər üçün ən uyğun olan API səthi vasitəsilə açıq metodlar və funksionallıqdan birbaşa istifadə edən bir tətbiq qurmağa imkan verir. Xüsusi şəkil yaratma və ya dərin məlumat emalı kimi AI modelləri üzərində birbaşa nəzarət tələb edən tətbiqlər üçün uyğundur.

### Build AI-powered applications with Genkit and Angular

[Genkit](https://genkit.dev), veb və mobil tətbiqlərdə AI dəstəkli xüsusiyyətlər qurmağa kömək etmək üçün nəzərdə tutulmuş açıq mənbəli (open-source) bir alət dəstidir. Google, OpenAI, Anthropic, Ollama və daha çoxundan AI modellarini inteqrasiya etmək üçün vahid bir interfeys təklif edir, buna görə ehtiyaclarınız üçün ən yaxşı modelləri araşdırıb seçə bilərsiniz. Server tərəfli (server-side) bir həll olaraq, veb tətbiqlərinizin Genkit ilə inteqrasiya üçün node-əsaslı server kimi dəstəklənən bir server mühitinə ehtiyacı var. Məsələn, Angular SSR istifadə edərək tam stack tətbiq qurmaq sizə başlanğıc server tərəfli kodu verir.

Budur Genkit və Angular ilə necə quracağınızın nümunələri:

- [Genkit və Angular başlangıc dəsti ilə Agentik Tətbiqlər](https://github.com/angular/examples/tree/main/genkit-angular-starter-kit) — AI ilə qurmağa yeni başlayırsınız? Agentik iş axınını özündə cəmləşdirən əsas bir tətbiqlə buradan başlayın. İlk AI quruculuq təcrübəniz üçün mükəmməl bir yer.

- [Angular tətbiqində Genkit istifadəsi](https://genkit.dev/docs/frameworks/angular/) — Genkit Flows, Angular və Gemini 2.5 Flash istifadə edərək əsas bir tətbiq qurun. Bu addım-addım izahat, AI xüsusiyyətləri olan tam stack Angular tətbiqi yaratmağınızda sizə rəhbərlik edir.

- [Dinamik Hekayə Generatoru tətbiqi](https://github.com/angular/examples/tree/main/genkit-angular-story-generator) — Genkit, Gemini və Imagen 3 ilə işləyən, istifadəçi interaksiyasına əsaslanaraq dinamik olaraq baş verən hadisələri müşayiət edən gözəl şəkil panelləri ilə bir hekayə yaradan agentik Angular tətbiqi qurmağı öyrənin. Daha qabaqcıl bir istifadə halı sınamaq istəyirsinizsə buradan başlayın.

  Bu nümunənin həmçinin funksionallığın ətraflı video izahatı var:
  - ["Angular və Genkit ilə Agentik Tətbiqlər qurmaq canlı!" izlə](https://youtube.com/live/mx7yZoIa2n4?feature=share)
  - ["Angular və Genkit ilə Agentik Tətbiqlər qurmaq canlı! 2-ci hissə" izlə](https://youtube.com/live/YR6LN5_o3B0?feature=share)

- [Firebase və Google Cloud ilə Agentik tətbiqlər qurmaq (Barista Nümunəsi)](https://developers.google.com/solutions/learn/agentic-barista) - Firebase və Google Cloud ilə agentik bir qəhvə sifariş tətbiqi necə quracağınızı öyrənin. Bu nümunə həm Firebase AI Logic həm də Genkit istifadə edir.

- [Dinamik, Server Tərəfindən İdarə Olunan Arayüzlər (SDUI) Yaratmaq](https://github.com/angular/examples/tree/main/dynamic-sdui-app) - İstifadəçi girişinə əsaslanaraq icra zamanında (runtime) yaradılan UI baxışları olan Agentik Angular tətbiqləri qurmağı öyrənin.

  Bu nümunənin həmçinin funksionallığın ətraflı video izahatı var:
  - ["Veb tətbiqlərin gələcəyini araşdırmaq" izlə](https://www.youtube.com/live/4qargCqOu70?feature=share)

### Build AI-powered applications with Firebase AI Logic and Angular

[Firebase AI Logic](https://firebase.google.com/products/vertex-ai-in-firebase), veb və mobil tətbiqlərinizdən birbaşa Vertex AI Gemini API və ya Imagen API ilə əlaqə qurmaq üçün təhlükəsiz bir yol təqdim edir. Bu, Angular tətbiqləri ya tam stack, ya da yalnız müştəri tərəfli (client-side) ola biləcəyi üçün Angular tərtibatçıları üçün cəlbedicidir. Yalnız müştəri tərəfli bir tətbiq hazırlayırsınızsa, Firebase AI Logic veb tətbiqlərinizə AI daxil etmək üçün yaxşı bir seçimdir.

Budur Firebase AI Logic və Angular ilə necə quracağınızın nümunəsi:

- [Firebase AI Logic x Angular Başlangıc Dəsti](https://github.com/angular/examples/tree/main/vertex-ai-firebase-angular-example) - Tapşırıqları yerinə yetirə bilən bir söhbət agenti olan elektron ticarət (e-commerce) tətbiqi qurmaq üçün bu başlangıc dəstindən istifadə edin. Firebase AI Logic və Angular ilə qurmaq təcrübəniz yoxdursa buradan başlayın.

  Bu nümunə funksionallığı izah edən və yeni xüsusiyyətlərin necə əlavə ediləcəyini nümayiş etdirən [ətraflı video izahatı](https://youtube.com/live/4vfDz2al_BI) ehtiva edir.

### Build AI-powered applications with Gemini API and Angular

[Gemini API](https://ai.google.dev/gemini-api/docs), audio, şəkil, video və mətn girişini dəstəkləyən Google-un ən son modellərinə giriş imkanı verir. Xüsusi istifadə halları üçün optimallaşdırılmış bu modellər haqqında [Gemini API sənədləşmə saytında daha ətraflı məlumat əldə edin](https://ai.google.dev/gemini-api/docs/models).

- [AI Mətn Redaktoru Angular tətbiq şablonu](https://github.com/FirebaseExtended/firebase-framework-tools/tree/main/starters/angular/ai-text-editor) - Mətni incəltmə, genişləndirmə və rəsmiləşdirmə kimi AI dəstəkli xüsusiyyətlərə malik tam işlək mətn redaktoru ilə başlamaq üçün bu şablondan istifadə edin. Gemini API-ni HTTP vasitəsilə çağırma təcrübəsi qazanmaq üçün yaxşı bir başlanğıc nöqtəsidir.

- [AI Chatbot tətbiq şablonu](https://github.com/FirebaseExtended/firebase-framework-tools/tree/main/starters/angular/ai-chatbot) - Bu şablon HTTP vasitəsilə Gemini API ilə əlaqə quran bir chatbot istifadəçi arayüzündən başlayır.

## Ən Yaxşı Təcrübələr

### Model təminatçılarına qoşulmaq və API Etimadnaməlerinizi Təhlükəsiz Saxlamaq

Model təminatçılarına qoşularkən API sirrlərinizi təhlükəsiz saxlamaq vacibdir. _API açarınızı heç vaxt `environments.ts` kimi müştəriyə göndərilən bir faylda yerləşdirməyin_.

Tətbiqinizin arxitekturası hansı AI API-lərini və alətlərini seçəcəyinizi müəyyən edir. Xüsusi olaraq, tətbiqinizin müştəri tərəfli (client-side) olub-olmadığına görə seçin. Firebase AI Logic kimi alətlər, müştəri tərəfli kod üçün model API-lərinə təhlükəsiz bir bağlantı təmin edir. Firebase AI Logic-dən fərqli bir API istifadə etmək və ya fərqli model təminatçısına üstünlük verirmisinizə, API açarlarınızı ifşa etməmək üçün bir proksi-server (proxy-server) və ya hətta [Firebase üçün Cloud Functions](https://firebase.google.com/docs/functions) yaratmağı düşünün.

Müştəri tərəfli tətbiq istifadə edərək qoşulma nümunəsi üçün koda baxın: [Firebase AI Logic Angular nümunə deposu](https://github.com/angular/examples/tree/main/vertex-ai-firebase-angular-example).

API açarları tələb edən model API-lərinə server tərəfli bağlantılar üçün `environments.ts` deyil, sirr meneceri (secrets manager) və ya mühit dəyişənindən (environment variable) istifadəni üstün tutun. API açarlarını və etimadnamələrini qorumaq üçün standart ən yaxşı təcrübələrə əməl etməlisiniz. Firebase indi Firebase App Hosting-in ən son yenilikləri ilə yeni bir sirr meneceri təqdim edir. Ətraflı məlumat üçün [rəsmi sənədlərə baxın](https://firebase.google.com/docs/app-hosting/configure).

Tam stack tətbiqdə server tərəfli bağlantı nümunəsi üçün koda baxın: [Angular AI Nümunəsi (Genkit və Angular Hekayə Generatoru) deposu](https://github.com/angular/examples/tree/main/genkit-angular-story-generator).

### Tətbiqləri təkmilləşdirmək üçün Alət Çağırışından (Tool Calling) istifadə edin

Agentlərin sorğulara (prompts) əsaslanaraq problemləri həll etmək üçün hərəkət edə bildiyi və alətlər istifadə edə bildiyi agentik iş axınları (agentic workflows) qurmaq istəyirsinizsə, "alət çağırışı" istifadə edin. Funksiya çağırışı (function calling) olaraq da bilinən alət çağırışı, LLM-lərə onu çağıran tətbiqə geri sorğu göndərmə imkanı verməyin bir yoludur. Bir tərtibatçı olaraq hansı alətlərin mövcud olduğunu müəyyən edirsiniz və alətlərin necə və nə zaman çağrılacağına siz nəzarət edirsiniz.

Alət çağırışı, AI inteqrasiyanızı sual-cavab üslublu chatbotun ötəsinə genişlədərək veb tətbiqlərinizi daha da inkişaf etdirir. Əslində, model təminatçınızın funksiya çağırışı API-sini istifadə edərək modelinizi funksiya çağırışları tələb etməklə gücləndirə bilərsiniz. Mövcud alətlər, tətbiqinizin kontekstindəki daha mürəkkəb hərəkətləri yerinə yetirmək üçün istifadə edilə bilər.

[Angular nümunələri deposunun](https://github.com/angular/examples) [elektron ticarət nümunəsindəki](https://github.com/angular/examples/blob/main/vertex-ai-firebase-angular-example/src/app/ai.service.ts#L88) LLM, mağazadakı bir qrup əşyanın nə qədər tutacağını hesablamaq kimi daha mürəkkəb tapşırıqları yerinə yetirmək üçün lazımi konteksti əldə etmək məqsədiylə inventar üçün funksiyalara çağırışlar etməyi tələb edir. Mövcud API-nin əhatə dairəsi LLM-in tələb etdiyi bir funksiyanı çağırıb-çağırmamaq kimi, sizin bir tərtibatçı olaraq sizə aiddır. İcranın axınına nəzarəti sizdə qalır. Məsələn, bir xidmətin bütün funksiyalarını deyil, xüsusi funksiyalarını açıq edə bilərsiniz.

### Qeyri-deterministik cavabların idarə edilməsi (Handling non-deterministic responses)

Modellər qeyri-deterministik nəticələr qaytara biləcəyi üçün tətbiqləriniz bunu nəzərə alaraq hazırlanmalıdır. Tətbiq icrası zamanı istifadə edə biləcəyiniz bir neçə strategiya var:

- Daha deterministik və ya daha az deterministik cavablar üçün sorğuları (prompts) və model parametrlərini (məsələn, [temperatur](https://ai.google.dev/gemini-api/docs/prompting-strategies)) tənzimləyin. [ai.google.dev](https://ai.google.dev/)-in [sorğu strategiyaları bölməsindən](https://ai.google.dev/gemini-api/docs/prompting-strategies) daha ətraflı məlumat ala bilərsiniz.
- Bir iş axınında davam etmədən əvvəl insan çıxışları yoxladığında "dövrədə insan" (human in the loop) strategiyasından istifadə edin. Çıxışları yoxlamaq və əsas qərarları təsdiqləmək üçün operatorlara (insanlar və ya digər modellər) imkan verəcək şəkildə tətbiq iş axınları qurun.
- Model cavablarını əvvəlcədən müəyyən edilmiş formatlara yönəltmək və məhdudlaşdırmaq, cavab proqnozlaşdırılmasını artırmaq üçün alət (və ya funksiya) çağırışından və sxem məhdudiyyətlərindən (schema constraints) istifadə edin.

Bu strategiya və texnikaları nəzərə alsaq belə, tətbiq dizaynınıza ağlabatan alternativ variantlar (fallbacks) daxil edilməlidir. Tətbiqin dayanıqlıq (resiliency) üzrə mövcud standartları izləyin. Məsələn, bir resurs və ya API mövcud olmadıqda tətbiqin çöküşü qəbuledilməzdir. Bu ssenaridə istifadəçiyə bir xəta mesajı göstərilir və əgər mümkündürsə, növbəti addımlar üçün seçimlər də göstərilir. AI dəstəkli tətbiqlər qurmaq eyni diqqəti tələb edir. Cavabın gözlənilən çıxışla uyğun olduğunu təsdiqləyin və [zərif deqradasiya (graceful degradation)](https://developer.mozilla.org/en-US/docs/Glossary/Graceful_degradation) yolu ilə uyğun olmadığı halda "təhlükəsiz eniş" təmin edin. Bu, LLM təminatçıları üçün API fasilələrinə də aiddir.

Bu nümunəni nəzərdən keçirin: LLM təminatçısı cavab vermir. Fasiləni idarə etmək üçün potensial strategiya:

- Yenidən cəhd ssenarisindən (indi və ya daha sonra) istifadə etmək üçün istifadəçinin cavabını saxlayın
- Həssas məlumatları ifşa etməyən uyğun bir mesajla istifadəçiyə fasilə barədə xəbər verin
- Xidmətlər yenidən mövcud olduqdan sonra söhbəti daha sonra davam etdirin.

## Növbəti addımlar

LLM sorğuları (prompts) və AI IDE quraşdırması haqqında öyrənmək üçün aşağıdakı bələdçilərə baxın:

<docs-pill-row>
  <docs-pill href="ai/develop-with-ai" title="LLM sorğuları (prompts) və IDE quraşdırması"/>
</docs-pill-row>
