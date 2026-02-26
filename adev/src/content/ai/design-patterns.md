# AI SDK-ları və signal API-ləri üçün dizayn nümunələri (Design Patterns)

AI və Böyük Dil Modeli (Large Language Model - LLM) API-ləri ilə əlaqə qurmaq asinxron əməliyyatları idarə etmək, axın (streaming) məlumatlarını emal etmək və potensial olaraq yavaş və ya etibarsız şəbəkə sorğuları üçün cavab verən bir istifadəçi təcrübəsi dizayn etmək kimi unikal problemlər yaradır. Angular [signals](guide/signals) və [`resource`](guide/signals/resource) API-si bu problemləri zərif şəkildə həll etmək üçün güclü alətlər təqdim edir.

## Siqnallarla (Signals) Sorğuları Tetiklemek

İstifadəçi tərəfindən verilən sorğularla işləyərkən ümumi bir nümunə, istifadəçinin canlı girişini API çağırışını təkikləyən göndərilmiş dəyərdən ayırmaqdır.

1. İstifadəçinin yazarkən xam girişini bir siqnalda saxlayın
2. İstifadəçi göndərdikdə (məs., bir düyməni tıkladıqda), ikinci siqnalı birinci siqnalin məzmunu ilə yeniləyin.
3. `resource`-nuzun **`params`** sahəsində ikinci siqnaldan istifadə edin.

Bu quraşdırma, `resource`-un **`loader`** funksiyasının yalnız istifadəçi sorğusunu açıq şəkildə göndərdikdə işləməsini təmin edir, hər düymə basımında deyil. `loader` sahəsindəki `sessionId` və ya `userId` kimi əlavə siqnal parametrlərindən istifadə edə bilərsiniz (bu, davamlı LLM sessiyaları yaratmaq üçün faydalı ola bilər). Bu şəkildə, sorğu həmişə bu parametrlərin cari dəyərlərindən istifadə edir, `loader` sahəsindəki asinxron funksiyanı yenidən tetiklemeden.

Bir çox AI SDK, API çağırışları üçün köməkçi metodlar təqdim edir. Məsələn, Genkit müştəri kitabxanası Genkit axınlarını (flows) çağırmaq üçün bir `runFlow` metodu açır və siz onu `resource`-un `loader`-indən çağıra bilərsiniz. Digər API-lər üçün [`httpResource`](guide/signals/resource#reactive-data-fetching-with-httpresource)-dan istifadə edə bilərsiniz.

Aşağıdakı nümunə, AI tərəfindən yaradılan hekayənin hissələrini gətirən bir `resource` göstərir. `loader` yalnız `storyInput` siqnalı dəyişdikdə tetiklenir.

```ts
// AI tərəfindən yaradılan hekayənin üç hissəsini gətirən resource
storyResource = resource({
  // İlk sorğudan əvvəl və ya xəta zamanı istifadə ediləcək standart dəyər
  defaultValue: DEFAULT_STORY,
  // Bu siqnal dəyişdikdə loader yenidən tetiklenir
  params: () => this.storyInput(),
  // Məlumatları gətirmək üçün asinxron funksiya
  loader: ({params}): Promise<StoryData> => {
    // params dəyəri storyInput siqnalının cari dəyəridir
    const url = this.endpoint();
    return runFlow({
      url,
      input: {
        userInput: params,
        sessionId: this.storyService.sessionId(), // Başqa siqnaldan oxuyun
      },
    });
  },
});
```

## LLM Məlumatlarını Şablonlar üçün Hazırlamaq

LLM API-lərini strukturlu məlumat qaytarmaq üçün konfiqurasiya edə bilərsiniz. `resource`-unuzu LLM-dən gözlənilən çıxışa uyğun olaraq güclü şəkildə tipləşdirmək daha yaxşı tip təhlükəsizliyi (type safety) və redaktor avtotamamlanması (autocompletion) təmin edir.

`resource`-dan əldə edilən vəziyyəti idarə etmək üçün `computed` siqnal və ya `linkedSignal` istifadə edin. `linkedSignal` [əvvəlki dəyərlərə giriş imkanı verdiyi](guide/signals/linked-signal) üçün, o, aşağıdakılar daxil olmaqla bir sıra AI-yə aid istifadə hallarına xidmət edə bilər:

- söhbət tarixçəsi (chat history) qurmaq
- LLM-lər məzmun yaradarkən şablonların göstərdiyi məlumatları qorumaq və ya fərdiləşdirmək

Aşağıdakı nümunədə, `storyParts` elə bir `linkedSignal`-dır ki, `storyResource`-dan qaytarılan ən son hekayə hissələrini mövcud hekayə hissələri massivine əlavə edir.

```ts
storyParts = linkedSignal<string[], string[]>({
  // Hesablamanı tetikleyen mənbə siqnal
  source: () => this.storyResource.value().storyParts,
  // Hesablama funksiyası
  computation: (newStoryParts, previous) => {
    // Bu linkedSignal-ın əvvəlki dəyərini alın və ya boş massiv
    const existingStoryParts = previous?.value || [];
    // Köhnə və yeni hissələrlə yeni massiv qaytarın
    return [...existingStoryParts, ...newStoryParts];
  },
});
```

## Performans və İstifadəçi Təcrübəsi

LLM API-ləri adi, deterministik API-lərə nisbətən daha yavaş və xətaya daha meyilli ola bilər. Performanslı ve istifadəçi dostu bir arayüz qurmaq üçün bir neçə Angular xüsusiyyətindən istifadə edə bilərsiniz.

- **Məhdudlaşdırılmış Yükləmə (Scoped Loading):** `resource`-u birbaşa məlumatlardan istifadə edən komponentdə yerləşdirin. Bu, dəyişiklik aşkarlama dövrlərini (change detection cycles) məhdudlaşdırmağa kömək edir (xüsusilə zonasız (zoneless) tətbiqlərdə) və tətbiqinizin digər hissələrinin bloklanmasının qarşısını alır. Məlumatların bir neçə komponent arasında paylaşılması lazım olduqda, `resource`-u bir xidmətdən (service) təmin edin.
- **SSR və Hidratasiya (Hydration):** İlkin səhifə məzmununu tez render etmək üçün artan hidratasiya ilə Server Tərəfli Render-dən (SSR) istifadə edin. AI tərəfindən yaradılan məzmun üçün bir yer saxlayıcı (placeholder) göstərə bilər və komponent müştəridə hidrate olana qədər məlumatların gətirilməsini təxirə sala bilərsiniz.
- **Yükləmə Vəziyyəti (State):** Sorğu davam edərkən fırlan (spinner) kimi bir göstərici göstərmək üçün `resource`-un `LOADING` [statusundan](guide/signals/resource#resource-status) istifadə edin. Bu status həm ilk yükləmələri, həm də yenidən yükləmələri əhatə edir.
- **Xəta Emalı (Error Handling) və Yenidən Cəhdlər (Retries):** İstifadəçilərin uğursuz sorğuları yenidən cəhd etmələri üçün sadə bir yol kimi `resource`-un [**`reload()`**](guide/signals/resource#reloading) metodundan istifadə edin; bu, AI tərəfindən yaradılan məzmuna etibar edərkən daha çox yayılmış ola bilər.

Aşağıdakı nümunə, yükləmə və yenidən cəhd funksionallığı ilə AI tərəfindən yaradılan şəkli dinamik olaraq göstərmək üçün cavab verən bir arayüz (UI) yaratmağı nümayiş etdirir.

```angular-html
<!-- LLM şəkli yaradarkən yükləmə fırlanı göstər -->
@if (imgResource.isLoading()) {
  <div class="img-placeholder">
    <mat-spinner [diameter]="50" />
  </div>
  <!-- Yaradılan şəkil URL-i ilə src atributunu dinamik doldurur -->
} @else if (imgResource.hasValue()) {
  <img [src]="imgResource.value()" />
  <!-- Sorğu uğursuz olarsa yenidən cəhd seçimi təqdim edir  -->
} @else {
  <div class="img-placeholder" (click)="imgResource.reload()">
    <mat-icon fontIcon="refresh" />
    <p>Şəkil yüklənmədi. Yenidən cəhd etmək üçün tıklayın.</p>
  </div>
}
```

## Tətbiqdə AI nümunələri: Axın (Streaming) söhbət cavabları

Arayüzlər çox vaxt cavab məlumatları gəldikcə LLM-yə əsaslanan API-lərdən qismən nəticələri tədricən göstərir. Angular-ın resource API-si bu tip nümunəni dəstəkləmək üçün cavabları axın şəklində ötürmə imkanı təqdim edir. `resource`-un `stream` xüsusiyyəti, zamanla bir siqnal dəyərini yeniləmək üçün istifadə edə biləcəyiniz asinxron bir funksiya qəbul edir. Yenilənən siqnal axın edilən məlumatları təmsil edir.

```ts
characters = resource({
  stream: async () => {
    const data = signal<ResourceStreamItem<string>>({value: ''});
    // Genkit müştəri SDK-sı tərəfindən açılan streamFlow metodu
    // vasitəsilə Genkit axın axını çağırır
    const response = streamFlow({
      url: '/streamCharacters',
      input: 10,
    });

    (async () => {
      for await (const chunk of response.stream) {
        data.update((prev) => {
          if ('value' in prev) {
            return {value: `${prev.value} ${chunk}`};
          } else {
            return {error: chunk as unknown as Error};
          }
        });
      }
    })();

    return data;
  },
});
```

`characters` üzvü asinxron olaraq yenilənir və şablonda göstərilə bilər.

```angular-html
@if (characters.isLoading()) {
  <p>Yüklənir...</p>
} @else if (characters.hasValue()) {
  <p>{{ characters.value() }}</p>
} @else {
  <p>{{ characters.error() }}</p>
}
```

Server tərəfində, məsələn `server.ts`-də, müəyyən edilmiş son nöqtə (endpoint) axın ediləcək məlumatları müştəriyə göndərir. Aşağıdakı kod Genkit çərçivəsi (framework) ilə Gemini-dən istifadə edir, lakin bu texnika LLM-lərdən axın cavablarını dəstəkləyən digər API-lərə də tətbiq olunur:

```ts
import {startFlowServer} from '@genkit-ai/express';
import {genkit} from 'genkit/beta';
import {googleAI, gemini20Flash} from '@genkit-ai/googleai';

const ai = genkit({plugins: [googleAI()]});

export const streamCharacters = ai.defineFlow(
  {
    name: 'streamCharacters',
    inputSchema: z.number(),
    outputSchema: z.string(),
    streamSchema: z.string(),
  },
  async (count, {sendChunk}) => {
    const {response, stream} = ai.generateStream({
      model: gemini20Flash,
      config: {
        temperature: 1,
      },
      prompt: `${count} fərqli RPG oyun xarakteri yarat.`,
    });

    (async () => {
      for await (const chunk of stream) {
        sendChunk(chunk.content[0].text!);
      }
    })();

    return (await response).text;
  },
);

startFlowServer({
  flows: [streamCharacters],
});
```
