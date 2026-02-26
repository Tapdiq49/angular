# Angular CLI MCP Server quraşdırması

Angular CLI, geliştirme mühitinizdəki AI köməkçilərinin Angular CLI ilə əlaqə qurmasına imkan verən eksperimental bir [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/) ehtiva edir. CLI dəstəkli kod yaratma, paket əlavə etmə və daha çox üçün dəstək daxil etmişik.

## Available Tools

Angular CLI MCP server, inkişaf iş axınınızda sizə kömək etmək üçün bir neçə alət təqdim edir. Standart olaraq aşağıdakı alətlər aktivdir:

| Ad                          | Açıqlama                                                                                                                                                                                                                                                                 | `local-only` | `read-only` |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------: | :---------: |
| `ai_tutor`                  | İnteraktiv AI dəstəkli Angular müəllimini işə salır. v20 və ya daha sonrakı versiyadan istifadə edərək yeni bir Angular layihəsindən işə salmaq tövsiyə olunur. [Ətraflı öyrənin](ai/ai-tutor).                                                                          |      ✅      |     ✅      |
| `find_examples`             | **Müasir, yeni və yaxın zamanda yenilənmiş** Angular xüsusiyyətlərinə diqqət yetirərək, seçilmiş rəsmi, ən yaxşı təcrübə nümunələrinin verilənlər bazasından nüfuzlu kod nümunələri tapır.                                                                               |      ✅      |     ✅      |
| `get_best_practices`        | Angular Ən Yaxşı Təcrübələr Bələdçisini əldə edir. Bu bələdçi, bütün kodun müstəqil komponentlər (standalone components), tipli formlar (typed forms) və müasir nəzarət axını (control flow) daxil olmaqla müasir standartlara uyğun olmasını təmin etmək üçün vacibdir. |      ✅      |     ✅      |
| `list_projects`             | Angular iş sahəsindəki (workspace) bütün tətbiq və kitabxanaların adlarını sadalayır. Layihələri müəyyən etmək üçün `angular.json` konfiqurasiya faylını oxuyur.                                                                                                         |      ✅      |     ✅      |
| `onpush_zoneless_migration` | Angular kodunu təhlil edir və onu zonasız (zoneless) tətbiq üçün ön şərt olan `OnPush` dəyişiklik aşkarlamasına (change detection) miqrasiya etmək üçün addım-addım, iterativ bir plan təqdim edir.                                                                      |      ✅      |     ✅      |
| `search_documentation`      | <https://angular.dev> ünvanında rəsmi Angular sənədlərini axtarır. Bu alət, API-lər, dərsliklər (tutorials) və ən yaxşı təcrübələr kimi Angular haqqında istənilən suala cavab vermək üçün istifadə edilməlidir.                                                         |      ❌      |     ✅      |

### Eksperimental Alətlər

Bəzi alətlər yeni olduqları və ya tam sınaqdan keçirilmədikləri üçün eksperimental/önizləmə statusunda təqdim edilir. Bunları [`--experimental-tool`](#əmr-seçimləri) seçimi ilə ayrı-ayrılıqda aktivləşdirin və ehtiyatla istifadə edin.

| Ad                         | Açıqlama                                                                                                                                                                                                                                                                            | `local-only` | `read-only` |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------: | :---------: |
| `build`                    | `ng build` istifadə edərək bir dəfəlik, izlənməyən (non-watched) bir yığım (build) həyata keçirir.                                                                                                                                                                                  |      ✅      |     ❌      |
| `devserver.start`          | `ng serve`-i işlətməyə bənzər, dəyişikliklər üçün iş sahəsini izləyən bir inkişaf serverini asinxron olaraq başladır. Bu asinxron olduğundan dərhal geri dönür. Nəticəde oluşan serveri idarə etmək üçün `devserver.stop` və `devserver.wait_for_build` alətlərindən istifadə edin. |      ✅      |     ✅      |
| `devserver.stop`           | `devserver.start` tərəfindən başladılmış inkişaf serverini dayandırır.                                                                                                                                                                                                              |      ✅      |     ✅      |
| `devserver.wait_for_build` | `devserver.start` tərəfindən başladılmış işləyən inkişaf serverindəki ən son yığımın (build) çıxış jurnallarını qaytarır. Hal hazırda bir yığım davam edirsə, əvvəlcə həmin yığımın tamamlanmasını gözləyəcək, sonra jurnalları qaytaracaq.                                         |      ✅      |     ✅      |
| `e2e`                      | Layihədə konfiqurasiya edilmiş uçdan-uca (end-to-end) testləri icra edir.                                                                                                                                                                                                           |      ✅      |     ✅      |
| `modernize`                | Kod miqrasiyaları həyata keçirir və Angular kodunu ən son ən yaxşı təcrübə və sintaksisə uyğunlaşdırmaq üçün necə modernizasiya edəcəyiniz barədə əlavə təlimatlar verir. [Ətraflı öyrənin](https://angular.dev/reference/migrations)                                               |      ✅      |     ❌      |
| `test`                     | Layihənin vahid testlərini (unit tests) icra edir.                                                                                                                                                                                                                                  |      ✅      |     ✅      |

## Get Started

Başlamaq üçün terminalınızda aşağıdakı əmri işlədin:

```bash
ng mcp
```

İnteraktiv bir terminaldan işə salındıqda, bu əmr MCP serverindən istifadə etmək üçün host mühitinin necə konfiqurasiya ediləcəyinə dair təlimatları göstərir. Aşağıdakı bölmələr bir neçə populyar redaktor və alət üçün nümunə konfiqurasiyalar təqdim edir.

### Cursor

Layihənizin kökündə `.cursor/mcp.json` adlı bir fayl yaradın və aşağıdakı konfiqurasiyanı əlavə edin. Bunu qlobal olaraq `~/.cursor/mcp.json`-da da konfiqurasiya edə bilərsiniz.

```json
{
  "mcpServers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

### Firebase Studio

Layihənizin kökündə `.idx/mcp.json` adlı bir fayl yaradın və aşağıdakı konfiqurasiyanı əlavə edin:

```json
{
  "mcpServers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

### Gemini CLI

Layihənizin kökündə `.gemini/settings.json` adlı bir fayl yaradın və aşağıdakı konfiqurasiyanı əlavə edin:

```json
{
  "mcpServers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

### JetBrains IDE-ləri

JetBrains IDE-lərində (IntelliJ IDEA və ya WebStorm kimi), JetBrains AI Assistant plaginini quraşdırdıqdan sonra `Settings | Tools | AI Assistant | Model Context Protocol (MCP)` bölməsinə keçin. Yeni server (`+`) əlavə edin və `As JSON` seçin. Sonra aşağıdakı konfiqurasiyanı yapışdırın:

```json
{
  "mcpServers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

MCP serverlərinin konfiqurasiyasına dair ən son təlimat üçün lütfən JetBrains sənədlərini nəzərdən keçirin: [MCP serverinə qoşulun](https://www.jetbrains.com/help/ai-assistant/mcp.html#connect-to-an-mcp-server).

### VS Code

Layihənizin kökündə `.vscode/mcp.json` adlı bir fayl yaradın və aşağıdakı konfiqurasiyanı əlavə edin. `servers` xüsusiyyətinin istifadəsinə diqqət yetirin.

```json
{
  "servers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

### Digər IDE-lər

Digər IDE-lər üçün MCP konfiqurasiya faylının düzgün yerini (çox vaxt `mcp.json`) tapmaq üçün IDE-nizin sənədlərini nəzərdən keçirin. Konfigurasiya aşağıdakı parçanı ehtiva etməlidir.

```json
{
  "mcpServers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp"]
    }
  }
}
```

## Əmr Seçimləri

`mcp` əmri, IDE-nizin MCP konfiqurasiyasında arqument kimi ötürülən aşağıdakı seçimlərlə konfiqurasiya edilə bilər:

| Seçim                         | Növ       | Açıqlama                                                                                                                                                                                  | Standart |
| :---------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| `--read-only`                 | `boolean` | Yalnız layihəyə dəyişiklik etməyən alətləri qeydiyyatdan keçirin. Redaktorunuz və ya kodlaşdırma agentiniz yenə də redaktə edə bilər.                                                     | `false`  |
| `--local-only`                | `boolean` | Yalnız internet bağlantısı tələb etməyən alətləri qeydiyyatdan keçirin. Redaktorunuz və ya kodlaşdırma agentiniz yenə də şəbəkə üzərindən məlumat göndərə bilər.                          | `false`  |
| `--experimental-tool`<br>`-E` | `string`  | [Eksperimental alət](#eksperimental-alətlər) aktivləşdirin. Bir neçə seçimi boşluqlarla ayırın, məs. `-E tool_a tool_b`. Bütün `devserver.x` alətlərini `-E devserver` ilə aktivləşdirin. |          |

Məsələn, VS Code-da serveri yalnız oxuma (read-only) rejimində işlətmək üçün `mcp.json`-unuzu belə yeniləyərdiniz:

```json
{
  "servers": {
    "angular-cli": {
      "command": "npx",
      "args": ["-y", "@angular/cli", "mcp", "--read-only"]
    }
  }
}
```

## Rəy və Yeni İdeyalar

Angular komandası mövcud MCP imkanları haqqında rəyinizi və yeni alətlər və ya xüsusiyyətlər üçün hər hansı bir ideyanızı məmnuniyyətlə qəbul edir. Lütfən [angular/angular GitHub deposunda](https://github.com/angular/angular/issues) bir problem açaraq düşüncələrinizi paylaşın.
