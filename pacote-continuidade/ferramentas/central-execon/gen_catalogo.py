# Gera dossie-grupo-execon/31-catalogo.md a partir dos dados abaixo e confere limites e termos.
import re, sys

D = "/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/dossie-grupo-execon/"
ENV = open(D + "20-envelope.md", encoding="utf-8").read()
PUB_IDS = set(re.findall(r"^- \[(fact\.[a-z_]+\.\d{3})\]", ENV, re.M))

N = "A Execon Engenharia e Construção"
WA = "(11) 98454-5681"
AREA = "a capital, a Grande São Paulo, o interior e o litoral paulista"
CONDOS_2 = "Ninho Verde II (Pardinho) e Riviera de Santa Cristina XIII"

items = []

# ------------------------------------------------------------------ p547877
items.append(dict(
    key="p547877", kind="cad",
    card="Construção de casa de alto padrão",
    url="/construcao-de-casa-alto-padrao",
    h1="Construção de casa de alto padrão em São Paulo (SP)",
    title="Construção de casa de alto padrão em São Paulo (SP) | Execon",
    meta=f"{N} desenvolve projetos e executa obras de casas de alto padrão na capital, na Grande SP, no interior e no litoral paulista.",
    meta_ids=["fact.name.001", "fact.service.008", "fact.service.001", "fact.positioning.001", "fact.service_area.001"],
    intro=(f"{N} é uma construtora de São Paulo (SP) que desenvolve projetos e executa obras para quem quer construir uma casa de alto padrão.",
           ["fact.name.001", "fact.category.001", "fact.city.001", "fact.service.008", "fact.service.001", "fact.positioning.001"]),
    bullets=[
        (f"{N} também faz a gestão e o acompanhamento de obras.", ["fact.service.002"]),
        (f"{N} constrói áreas de lazer residenciais, com piscina, churrasqueira e área gourmet.", ["fact.service.005"]),
        (f"{N} constrói pergolados de madeira, alumínio ou ferro.", ["fact.service.006"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
        (f"No interior, a Execon Engenharia e Construção atende obras em condomínios como {CONDOS_2}.", ["fact.service_area.002"]),
    ],
    serve="quem quer construir uma casa de alto padrão",
    cta=(f"Para falar sobre a sua casa, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe a cidade ou o condomínio do terreno e se já tem projeto.",
         ["fact.phone.001", "fact.channel.001"]),
    faq=[
        ("Em quais regiões a Execon Engenharia e Construção constrói casas?",
         f"{N} atende {AREA}.",
         ["fact.service_area.001", "fact.service.001"]),
        ("A Execon Engenharia e Construção atende obra em condomínio do interior?",
         f"Sim. {N} atende obras em condomínios do interior paulista, como {CONDOS_2}.",
         ["fact.service_area.002"]),
    ],
    links="/gerenciamento-de-obras · /obras-condominios-interior-sp · /area-de-lazer · /pergolado · /reforma-de-casa",
    pend=("Forma de contratação (administração × empreitada/preço fechado), como é feito o orçamento, se há visita técnica e garantia "
          "pós-obra: são as perguntas que a pauta do nicho mais faz e nenhuma tem fato — cliente. Lista de obras entregues com "
          "condomínio, ano e foto, e o número de casas com data de corte e método (C02) — cliente. Ano de início da atuação (C01) — "
          "cliente. Com PC1: \"responsável técnico registrado no CREA-SP\", sem nome — nós + cliente. Custo por m² fica fora (B29)."),
    nota_atual=("O item se chama \"Construtora Especializada\": descreve a empresa, não um produto, e repete em lista cinco serviços que já "
                "têm item próprio, sobrepondo-se ao catálogo inteiro. Tem de bom a única menção a \"construção de casas de alto padrão\", "
                "o posicionamento que o CS confirmou, e por isso vira a página do produto principal. Tem de errado o \"9 anos\" congelado (B02), "
                "\"projetos arquitetônicos\" sem CAU (B10), \"compromisso com prazos e orçamentos\" e \"construtora referência em São Paulo\" (B11) "
                "e \"sustentabilidade\" sem evidência (B28)."),
))

# ------------------------------------------------------------------ p547879
items.append(dict(
    key="p547879", kind="cad",
    card="Gerenciamento de obras",
    url="/gerenciamento-de-obras",
    h1="Gerenciamento e acompanhamento de obras em São Paulo (SP)",
    title="Gerenciamento e acompanhamento de obra em São Paulo | Execon",
    meta=f"{N} faz gestão e acompanhamento de obras com foco em casas de alto padrão na capital, na Grande SP, no interior e no litoral.",
    meta_ids=["fact.name.001", "fact.service.002", "fact.positioning.001", "fact.service_area.001"],
    intro=(f"{N} faz o gerenciamento e o acompanhamento de obras em São Paulo (SP), com foco em casas de alto padrão.",
           ["fact.name.001", "fact.city.001", "fact.service.002", "fact.positioning.001"]),
    bullets=[
        (f"{N} faz a gestão e a administração de obras.", ["fact.service.002"]),
        (f"{N} também executa obras e constrói casas de alto padrão.", ["fact.service.008", "fact.service.001"]),
        (f"{N} atende obras na capital, na Grande São Paulo, no interior e no litoral paulista.", ["fact.service_area.001"]),
        (f"No interior, a Execon Engenharia e Construção atende obras em condomínios como {CONDOS_2}.", ["fact.service_area.002"]),
        ("O atendimento da Execon Engenharia e Construção é feito pelo WhatsApp e também online.", ["fact.channel.001"]),
    ],
    serve="com foco em casas de alto padrão",
    cta=(f"Para falar sobre o gerenciamento da sua obra, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe onde fica a obra e em que etapa ela está.",
         ["fact.phone.001", "fact.channel.001", "fact.service.002"]),
    faq=[
        ("A Execon Engenharia e Construção só gerencia ou também constrói?",
         f"{N} faz as duas coisas: constrói casas de alto padrão e faz a gestão e o acompanhamento de obras.",
         ["fact.service.001", "fact.service.002"]),
        ("A Execon Engenharia e Construção acompanha obra no interior e no litoral?",
         f"Sim. {N} atende {AREA}.",
         ["fact.service_area.001", "fact.service.002"]),
    ],
    links="/construcao-de-casa-alto-padrao · /obras-condominios-interior-sp · /reforma-de-casa · /obras-comerciais",
    pend=("Como funciona o acompanhamento: frequência, formato e canal dos relatórios e se há visita à obra — cliente; int.process.001 "
          "(cronograma, custos, relatórios) só vira texto com isso, e é a resposta à pergunta da pauta \"como acompanhar a obra à distância\". "
          "Se \"administração de obra\" é a modalidade de contrato (custo + taxa) ou só o nome do serviço, e se gerencia obra tocada por "
          "outra construtora — cliente. Com PC1: responsável técnico registrado no CREA-SP, sem nome — nós + cliente."),
    nota_atual=("Markup do tradutor automático com \"canto de obras\" (canteiro) e \"seja contínuo com competência\". Promete "
                "\"acompanhamento em tempo real\" sem ferramenta identificada (B27), \"redução de riscos\" e obra \"dentro do orçamento\" (B11), "
                "e repete o \"9 anos\" (B02). Tem de bom a lista de atividades (cronograma, custos, fornecedores, relatórios), que volta ao "
                "texto quando o cliente disser como funciona."),
))

# ------------------------------------------------------------------ p547870 (fundir)
items.append(dict(
    key="p547870", kind="fundir", destino="p547879",
    card="— (sai do catálogo)",
    url="/acompanhamento-de-obra → 301 para /gerenciamento-de-obras",
    motivo=("O envelope registra gerenciamento e acompanhamento como um único fato (fact.service.002, três fontes convergentes), e nenhum "
            "fato diz o que o acompanhamento entrega que o gerenciamento não entrega. O que os dois produtos listam — cronograma, custos, "
            "relatórios — é o mesmo e está interno (int.process.001). Duas páginas para \"acompanhamento de obra\" e \"gerenciamento de obras\" "
            "disputam a mesma busca e canibalizam; a página que fica (p547879) leva os dois termos no H1, no title e na meta. Fica o 547879 "
            "porque \"gestão de obras\" é o termo do banner e do site próprio."),
    volta_se=("Volta a ser página própria só se o cliente descrever um serviço de acompanhamento vendido separado — por exemplo, fiscalização "
              "de obra de outra construtora, com visitas e relatório definidos — cliente."),
    nota_atual=("Markup do tradutor automático com \"canto de obras\" e \"Gerenciamento de Custódia\" (era \"de custos\"). Promete obra \"com a "
                "máxima qualidade e dentro do prazo, sem surpresas\" e \"conformidade técnica\" (B11), cita \"equipe de engenheiros\" (B09) e o "
                "\"9 anos\" (B02). Repete quase item a item o 547879."),
))

# ------------------------------------------------------------------ s-condominios
items.append(dict(
    key="s-condominios-interior", kind="pronto",
    card="Obras em condomínios do interior",
    url="/obras-condominios-interior-sp",
    h1="Construtora para condomínios do interior de SP: Ninho Verde e Riviera de Santa Cristina",
    title="Obras no Ninho Verde e na Riviera de Santa Cristina | Execon",
    meta=f"{N} atende obras em condomínios do interior paulista, como {CONDOS_2}.",
    meta_ids=["fact.name.001", "fact.service_area.002"],
    intro=(f"{N} atende obras em condomínios do interior paulista, como {CONDOS_2}.",
           ["fact.name.001", "fact.service_area.002"]),
    bullets=[
        ("Os condomínios do interior atendidos pela Execon Engenharia e Construção incluem Ninho Verde I, Ninho Verde II e Riviera de Santa Cristina II, III e XIII.",
         ["fact.service_area.002"]),
        (f"{N} constrói casas de alto padrão.", ["fact.service.001", "fact.positioning.001"]),
        (f"{N} também faz a gestão e o acompanhamento de obras.", ["fact.service.002"]),
        (f"{N} constrói áreas de lazer residenciais e pergolados.", ["fact.service.005", "fact.service.006"]),
        (f"{N} é uma construtora de São Paulo (SP) que atende também a Grande São Paulo, o interior e o litoral paulista.",
         ["fact.city.001", "fact.category.001", "fact.service_area.001"]),
    ],
    serve="condomínios do interior paulista",
    cta=(f"Para falar sobre a obra no condomínio, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe o nome do condomínio e o que pretende construir.",
         ["fact.phone.001", "fact.channel.001", "fact.service_area.002"]),
    faq=[
        ("Em quais condomínios do interior a Execon Engenharia e Construção atende obras?",
         f"{N} atende obras em condomínios do interior paulista como Ninho Verde I, Ninho Verde II (Pardinho) e Riviera de Santa Cristina II, III e XIII.",
         ["fact.service_area.002"]),
        ("A Execon Engenharia e Construção é de São Paulo ou do interior?",
         f"{N} é uma construtora de São Paulo (SP) que também atende o interior e o litoral paulista.",
         ["fact.city.001", "fact.category.001", "fact.service_area.001"]),
    ],
    links="/construcao-de-casa-alto-padrao · /gerenciamento-de-obras · /area-de-lazer · /pergolado",
    pend=("C09 primeiro: a página duplicada 23064979 (\"… em Riviera de Santa Cristina XIII\") disputa exatamente esta busca; consolidar com 301 "
          "ou alinhar antes de publicar — nós. Lista de obras nesses condomínios com ano e foto: hoje o envelope NÃO prova obra entregue, por "
          "isso o texto diz \"atende obras\" e nunca \"já construiu\" — cliente. Se a Execon cuida da aprovação do projeto na associação do "
          "condomínio (pergunta da pauta; se for ato técnico, PC1/PC3) — cliente. Municípios das Rivieras II, III e XIII e o que é \"Águas de "
          "Santa Bárbara\" — nós/cliente. Se o (14) 99120-9697 atende a região e tem WhatsApp (C08); se tiver, entra no CTA desta página — "
          "cliente. Nunca citar a loteadora (B06) nem \"parceira/credenciada\"."),
    nota_atual=("Não há item no catálogo atual. O fato vem da 2ª página Solutudo (23064979) e do título de obrasexecon.com.br; aquela página "
                "associa a Execon à loteadora (B06), põe \"CREA-SP\" com número no título (B08) e traz números de portfólio divergentes (C02)."),
))

# ------------------------------------------------------------------ s-reforma
items.append(dict(
    key="s-reforma", kind="pronto",
    card="Reforma de casa",
    url="/reforma-de-casa",
    h1="Reforma de casa em São Paulo (SP)",
    title="Empresa de reforma de casa em São Paulo (SP) | Execon",
    meta=f"{N} faz reforma residencial na capital, na Grande SP, no interior e no litoral paulista. WhatsApp {WA}.",
    meta_ids=["fact.name.001", "fact.service.003", "fact.service_area.001", "fact.phone.001"],
    intro=(f"{N} faz reforma residencial em São Paulo (SP), além de construir casas de alto padrão.",
           ["fact.name.001", "fact.city.001", "fact.service.003", "fact.service.001"]),
    bullets=[
        (f"{N} também faz reforma comercial de lojas, escritórios e restaurantes.", ["fact.service.003", "fact.service.004"]),
        (f"{N} constrói áreas de lazer residenciais, com piscina, churrasqueira e área gourmet.", ["fact.service.005"]),
        (f"{N} faz instalações elétricas residenciais e manutenção elétrica.", ["fact.service.007"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
    ],
    serve="reforma residencial",
    cta=(f"Para falar sobre a reforma, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe a cidade, o tipo de imóvel e o que quer reformar.",
         ["fact.phone.001", "fact.channel.001", "fact.service.003"]),
    faq=[
        ("A Execon Engenharia e Construção faz reforma ou só construção?",
         f"{N} faz as duas coisas: reforma residencial e comercial e construção de casas de alto padrão.",
         ["fact.service.003", "fact.service.001"]),
    ],
    links="/construcao-de-casa-alto-padrao · /obras-comerciais · /area-de-lazer · /instalacao-eletrica",
    pend=("Que reformas a Execon aceita (completa, ampliação, cozinha e banheiro, apartamento, reforma em condomínio) e se a reforma segue o "
          "foco em alto padrão (C03) — cliente. Reforma com mudança estrutural, ampliação com alvará e regularização dependem de PC1/PC3. "
          "Fotos de antes e depois com local e ano — cliente."),
    nota_atual=("Não existe item de reforma no catálogo atual: a reforma aparece só dentro do 547876 (comercial) e nos canais próprios de fora da "
                "Solutudo — Facebook, execonobras e o título de execoneng.com.br (\"Projetos, Construção e Reforma\"). É o serviço com mais fontes "
                "independentes do texto da Solutudo e o único sem página."),
))

# ------------------------------------------------------------------ p547881
items.append(dict(
    key="p547881", kind="cad",
    card="Área de lazer",
    url="/area-de-lazer",
    h1="Área de lazer com piscina, churrasqueira e área gourmet em São Paulo (SP)",
    title="Área de lazer com piscina e área gourmet em SP | Execon",
    meta=f"{N} constrói áreas de lazer residenciais em São Paulo (SP), com piscina, churrasqueira, área gourmet, varanda e paisagismo.",
    meta_ids=["fact.name.001", "fact.city.001", "fact.service.005"],
    intro=(f"{N} constrói áreas de lazer residenciais em São Paulo (SP), com piscina, churrasqueira e área gourmet.",
           ["fact.name.001", "fact.city.001", "fact.service.005"]),
    bullets=[
        (f"{N} também faz varandas, paisagismo e iluminação externa.", ["fact.service.005"]),
        (f"{N} constrói pergolados de madeira, alumínio ou ferro, com cobertura de policarbonato ou vegetal.", ["fact.service.006"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
        (f"No interior, a Execon Engenharia e Construção atende obras em condomínios como {CONDOS_2}.", ["fact.service_area.002"]),
    ],
    serve="áreas de lazer residenciais",
    cta=(f"Para falar sobre a sua área de lazer, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe a cidade e o que quer incluir, como piscina ou pergolado.",
         ["fact.phone.001", "fact.channel.001", "fact.service.005", "fact.service.006"]),
    faq=[
        ("O que a Execon Engenharia e Construção faz em área de lazer?",
         f"{N} faz piscinas, churrasqueiras, áreas gourmet, varandas, paisagismo e iluminação externa em residências.",
         ["fact.service.005"]),
    ],
    links="/pergolado · /construcao-de-casa-alto-padrao · /obras-condominios-interior-sp · /reforma-de-casa",
    pend=("Se faz área de lazer em casa já pronta ou só dentro da obra nova, e se atende condomínio ou comércio (o fato é residencial) — "
          "cliente. Tipo de piscina (alvenaria, vinil, fibra) — cliente. Paisagismo entra como execução; \"projeto paisagístico\" depende de "
          "PC2. Fotos com legenda de obra (tarefa 8 do cadastro) — cliente."),
    nota_atual=("Sem markup de tradutor e com a lista concreta de itens — piscina, churrasqueira, área gourmet, varanda, paisagismo, iluminação "
                "externa —, que é o fato que sustenta a página. Erra em \"especialista\", \"já entregou diversos projetos… garantindo a satisfação "
                "total\" (B11) e no \"9 anos\" (B02); o nome diz \"Projeto\" quando o fato é a construção, e \"condomínio ou projeto comercial\" "
                "não tem fato (a área de lazer do envelope é residencial)."),
))

# ------------------------------------------------------------------ p547873
items.append(dict(
    key="p547873", kind="cad",
    card="Pergolado",
    url="/pergolado",
    h1="Pergolado de madeira, alumínio ou ferro em São Paulo (SP)",
    title="Pergolado de madeira, alumínio ou ferro em SP | Execon",
    meta=f"{N} constrói pergolados de madeira, alumínio ou ferro, com cobertura de policarbonato ou vegetal, em São Paulo (SP).",
    meta_ids=["fact.name.001", "fact.service.006", "fact.city.001"],
    intro=(f"{N} constrói pergolados para a área externa em São Paulo (SP).",
           ["fact.name.001", "fact.city.001", "fact.service.006"]),
    bullets=[
        ("O pergolado da Execon Engenharia e Construção pode ser de madeira, de alumínio ou de ferro.", ["fact.service.006"]),
        ("A cobertura do pergolado da Execon Engenharia e Construção pode ser de policarbonato ou vegetal.", ["fact.service.006"]),
        (f"{N} também constrói áreas de lazer residenciais, com piscina, churrasqueira e área gourmet.", ["fact.service.005"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
    ],
    serve="área externa",
    cta=(f"Para pedir o pergolado, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe a cidade, a medida aproximada do espaço, o material e o tipo de cobertura.",
         ["fact.phone.001", "fact.channel.001", "fact.service.006"]),
    faq=[
        ("De que material a Execon Engenharia e Construção faz pergolado?",
         f"{N} faz pergolados de madeira, de alumínio ou de ferro.",
         ["fact.service.006"]),
        ("Que cobertura a Execon Engenharia e Construção usa no pergolado?",
         f"{N} cobre o pergolado com policarbonato ou com cobertura vegetal.",
         ["fact.service.006"]),
    ],
    links="/area-de-lazer · /construcao-de-casa-alto-padrao · /reforma-de-casa",
    pend=("Se faz pergolado avulso, em casa pronta, ou só dentro de obra — cliente. Fotos de pergolados feitos, com material e local — "
          "cliente. Pergolado para comércio: não há fato."),
    nota_atual=("Sem markup de tradutor, é o único item com imagem marcada como padrão e o mais concreto do catálogo: materiais (madeira, "
                "alumínio, ferro) e coberturas (policarbonato, vegetal) viram fato e perguntas da página. Erra no \"9 anos\" (B02) e em "
                "\"execução impecável\", \"materiais de qualidade superior\" e \"solução perfeita\" (B11)."),
))

# ------------------------------------------------------------------ p547876
items.append(dict(
    key="p547876", kind="cad",
    card="Obras comerciais",
    url="/obras-comerciais",
    h1="Construção e reforma de lojas, escritórios e restaurantes em São Paulo (SP)",
    title="Construção e reforma de lojas e escritórios em SP | Execon",
    meta=f"{N} constrói e reforma lojas, escritórios e restaurantes na capital, na Grande São Paulo, no interior e no litoral paulista.",
    meta_ids=["fact.name.001", "fact.service.004", "fact.service_area.001"],
    intro=(f"{N} faz obras comerciais em São Paulo (SP): constrói e reforma lojas, escritórios e restaurantes.",
           ["fact.name.001", "fact.city.001", "fact.service.004"]),
    bullets=[
        (f"{N} faz instalações elétricas comerciais e manutenção elétrica.", ["fact.service.007"]),
        (f"{N} também faz a gestão e o acompanhamento de obras.", ["fact.service.002"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
        ("O atendimento da Execon Engenharia e Construção é feito pelo WhatsApp e também online.", ["fact.channel.001"]),
    ],
    serve="lojas, escritórios e restaurantes",
    cta=(f"Para falar sobre a obra do seu negócio, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe o tipo de espaço, a cidade e se é construção ou reforma.",
         ["fact.phone.001", "fact.channel.001", "fact.service.004"]),
    faq=[
        ("A Execon Engenharia e Construção reforma restaurante?",
         f"Sim. {N} constrói e reforma restaurantes, lojas e escritórios.",
         ["fact.service.004"]),
        ("A Execon Engenharia e Construção faz a parte elétrica da loja?",
         f"{N} faz instalações elétricas comerciais e manutenção elétrica.",
         ["fact.service.007"]),
    ],
    links="/instalacao-eletrica · /gerenciamento-de-obras · /reforma-de-casa",
    pend=("Obras para indústrias (int.service.002) só entram com confirmação do cliente. \"Projeto comercial\", aprovação em órgãos e "
          "acessibilidade são atos técnicos: esperam PC1/PC3 (e PC2 para projeto de arquitetura ou layout). Lista de obras comerciais com "
          "tipo de espaço, cidade e ano — cliente."),
    nota_atual=("Markup do tradutor automático com \"instalações possíveis\". O nome \"Projeto Comercial\" e a \"aprovação de projetos junto aos "
                "órgãos competentes\" são atos técnicos que esperam PC1/PC3; \"indústrias\" está interno (int.service.002), e \"dentro do prazo, "
                "do orçamento\" (B11) e o \"9 anos\" (B02) caem. Tem de bom os tipos de espaço — lojas, escritórios e restaurantes —, que viram o H1."),
))

# ------------------------------------------------------------------ p547883
items.append(dict(
    key="p547883", kind="cad",
    card="Instalações elétricas",
    url="/instalacao-eletrica",
    h1="Instalação e manutenção elétrica residencial e comercial em São Paulo (SP)",
    title="Instalação e manutenção elétrica em São Paulo (SP) | Execon",
    meta=f"{N} faz instalações elétricas residenciais e comerciais e manutenção elétrica em São Paulo (SP). WhatsApp {WA}.",
    meta_ids=["fact.name.001", "fact.service.007", "fact.city.001", "fact.phone.001"],
    intro=(f"{N} faz instalações elétricas residenciais e comerciais em São Paulo (SP).",
           ["fact.name.001", "fact.city.001", "fact.service.007"]),
    bullets=[
        (f"{N} também faz manutenção elétrica.", ["fact.service.007"]),
        (f"{N} constrói casas de alto padrão e faz obras comerciais.", ["fact.service.001", "fact.service.004"]),
        (f"{N} atende {AREA}.", ["fact.service_area.001"]),
        ("O atendimento da Execon Engenharia e Construção é feito pelo WhatsApp e também online.", ["fact.channel.001"]),
    ],
    serve="residenciais e comerciais",
    cta=(f"Para pedir o serviço, chame a Execon Engenharia e Construção no WhatsApp {WA} e informe se é instalação ou manutenção, se o imóvel é residencial ou comercial e a cidade.",
         ["fact.phone.001", "fact.channel.001", "fact.service.007"]),
    faq=[
        ("A Execon Engenharia e Construção faz manutenção elétrica?",
         f"Sim. {N} faz manutenção elétrica, além de instalações elétricas residenciais e comerciais.",
         ["fact.service.007"]),
    ],
    links="/obras-comerciais · /construcao-de-casa-alto-padrao · /reforma-de-casa",
    pend=("\"Projeto elétrico\" e dimensionamento são atos técnicos: esperam PC1/PC3. Hidráulica e automação (int.service.001) só com "
          "confirmação do cliente. Se atende chamado avulso de manutenção, fora de obra própria, e em que região — cliente. Nenhuma menção a "
          "norma técnica ou segurança sem PC1 (B11)."),
    nota_atual=("Markup do tradutor automático com \"conectores, interruptores, tomadas e interruptores\" repetido e \"excelência elétrica\". "
                "Promete \"conformidade com normas de segurança (NBR)\", \"entrega pontual\" e \"tecnologia de ponta\" (B11) e oferece \"projetos "
                "elétricos\" e \"dimensionamento\", atos técnicos que esperam PC3. Tem de bom a separação residencial × comercial × manutenção, "
                "que é exatamente o fato publicável (fact.service.007)."),
))

# ------------------------------------------------------------------ p547874 (cond)
items.append(dict(
    key="p547874", kind="cond",
    card="Projeto arquitetônico (reservado)",
    url="/projeto-arquitetonico (reservada)",
    h1="Projeto arquitetônico residencial em São Paulo (SP)",
    title="Projeto arquitetônico residencial em São Paulo (SP) | Execon",
    meta=f"{N} faz projeto arquitetônico residencial em São Paulo (SP), com arquiteto(a) registrado(a) no CAU, e executa a obra da casa.",
    meta_note="rascunho reservado: só vale depois de PC2, e a redação muda se o registro for de parceiro (\"com arquiteto(a) parceiro(a) registrado(a) no CAU\")",
    serve="projeto arquitetônico residencial",
    cond=("PC2: arquiteto(a) com registro ativo no CAU — próprio ou parceiro, citado pelo título e sem nome — ou registro de pessoa jurídica "
          "no CAU, com RRT dos projetos; mais o escopo que o cliente confirma (casa? comercial? interiores?) — cliente entrega, nós conferimos "
          "na consulta pública do CAU. Com isso chegam os fatos novos que viram intro, bullets e perguntas."),
    enquanto=("Tirar o item 547874 do ar nas duas vitrines agora (afirma arquitetura sem CAU: B09, B10). A categoria \"Arquitetura\" fica em "
              "revisão. O nível seguro — \"desenvolve projetos e executa obras residenciais\" (fact.service.008) — já está na página p547877; "
              "reescrever o 547874 nesse nível criaria uma segunda página para a mesma busca."),
    pend="Registro no CAU e escopo — cliente. Conferência na consulta pública do CAU — nós. Categoria \"Arquitetura\" (tarefa 6 do cadastro) — nós.",
    nota_atual=("Markup do tradutor automático com \"projeto atualizado\". Afirma \"equipe de arquitetos e engenheiros\" (B09) sem CAU achado "
                "(B10, PC2), \"integração de sustentabilidade\" com energia solar e água da chuva sem evidência (B28), \"tecnologia de ponta\" "
                "(B11) e o \"9 anos\" (B02). É o único item na categoria \"Arquitetura\", que hoje não tem sustentação."),
))

# ------------------------------------------------------------------ p547871 (cond)
items.append(dict(
    key="p547871", kind="cond",
    card="Projeto e aprovação de obra (reservado)",
    url="/projeto-e-aprovacao-de-obra (reservada)",
    h1="Projeto estrutural e aprovação de obra na prefeitura em São Paulo (SP)",
    title="Projeto estrutural e aprovação de obra em São Paulo | Execon",
    meta=None,
    meta_note="não redigida: depende de quais atos técnicos o cliente confirmar",
    serve="projeto estrutural e aprovação de obra",
    cond=("PC1 (CREA-SP: registro de pessoa jurídica do CNPJ com responsável técnico ativo e o título dele) + PC3 (quais atos técnicos a "
          "Execon assina com ART: projeto estrutural? alvará e aprovação na prefeitura? aprovação no condomínio? regularização?) — cliente "
          "entrega, nós conferimos na consulta pública do CREA-SP. Se o cliente não confirmar nenhum ato técnico próprio, o 547871 é excluído "
          "de vez: o nível seguro já está em p547877."),
    enquanto=("Tirar o item 547871 do ar nas duas vitrines agora (projeto estrutural, licenciamento e aprovação sem PC1/PC3). O que ele tem de "
              "seguro — planejamento e execução de obra (fact.service.008) — está em p547877, e o acompanhamento que ele lista está em p547879; "
              "reescrevê-lo nesse nível criaria uma terceira página para a busca de construção."),
    pend="Certidão de registro PJ no CREA-SP e lista dos atos técnicos com ART — cliente. Consulta pública do CREA-SP (situação do 5070683298) — nós.",
    nota_atual=("Markup do tradutor automático com \"projeto atualizado\" e \"licenças permitidas\". Oferece \"projeto de estrutura\" com "
                "\"cálculos precisos\" e \"licenciamento e regularização\", atos técnicos que esperam PC1/PC3, promete prazos, orçamentos e "
                "segurança (B11) e cita \"arquitetura\" (PC2). O resto — planejamento, execução e acompanhamento — repete o 547877 e o 547879."),
))

# ------------------------------------------------------------------ s-eua (cond, só ficha)
items.append(dict(
    key="s-eua", kind="cond", ficha_only=True,
    card="Estados Unidos (reservado)",
    url="/estados-unidos (reservada)",
    ja_pode=("Só fora do catálogo, na descrição da empresa, uma vez, fora de title, meta, Google e da frase de abertura, com validade até "
             "31/12/2026: \"A Execon Engenharia e Construção está em expansão para os Estados Unidos. | [fact.expansion.001]\""),
    cond=("PC4 inteiro: (a) confirmação ESCRITA do cliente para a frase; (b) estado e cidade; (c) entidade legal americana (LLC ou Inc.) com "
          "registro na Secretaria de Estado; (d) licença estadual de contractor, com estado emissor, classe e número verificável no órgão "
          "estadual; (e) tipo de serviço — execução própria com licença, gestão ou consultoria de obra para brasileiros, ou parceria com "
          "builder local licenciado; (f) desde quando; (g) obra concluída ou em andamento; (h) seguros exigidos, se executar a obra. H1, "
          "title, meta e texto só são redigidos com (b) e (e), que definem a busca da página."),
    perguntas=("Perguntas da pauta que a página responderá, se os fatos chegarem (são perguntas do público, não fatos): o construtor é "
               "licenciado no meu estado? · que serviço a Execon presta nos Estados Unidos? · em que estado e cidade? · como fica o "
               "acompanhamento da obra para quem mora no Brasil?"),
    pend=("Confirmação escrita e itens (b)–(h) — cliente. Conferir o registro da entidade e a licença nos órgãos estaduais — nós. Corrigir o "
          "banner \"expansão no EUA\" para \"expansão para os Estados Unidos\" (tarefa 9 do cadastro) — nós. Nunca \"atua / constrói / "
          "atende nos EUA\" (B07)."),
    nota_atual=("Não há item nem frase sobre os Estados Unidos no catálogo. A única menção é a descrição do banner \"[Solusite]\" de "
                "28/09/2026, \"com atual expansão no EUA\", com erro de preposição e que não é fonte independente da declaração do CS."),
))

# ================================================================== checks
BANNED = [r"\banos?\b", r"m²", r"\d{2,}\s*(casas|resid)", r"garant", r"qualidade", r"excel", r"refer[êe]ncia", r"exclusiv",
          r"\bs[óo] \b(?!constru|gerencia)", r"somente", r"Momentum", r"tempo real", r"\bNBR\b", r"seguran", r"no prazo", r"prazo",
          r"orçamento", r"líder", r"especialis", r"sustent", r"parceir", r"credenciad", r"Estados Unidos", r"\bEUA\b",
          r"arquitet", r"estrutural", r"licen", r"aprova", r"CREA", r"CAU", r"Grupo", r"Av(enida|\.) Paulista", r"Bela Vista", r"equipe",
          r"sonho", r"ideal", r"perfeit", r"sempre", r"24 horas", r"(13) 98191", r"(14) 99120"]
errors, report = [], []

def sentences(txt):
    return [s for s in re.split(r"(?<=[.?!])\s+", txt.strip()) if s]

def check_ids(ids, where):
    for i in ids:
        if i not in PUB_IDS:
            errors.append(f"{where}: id {i} não é fato PUB do envelope")

def scan(txt, where, allow=()):
    for b in BANNED:
        if b in allow:
            continue
        if re.search(b, txt, re.I):
            errors.append(f"{where}: termo barrado /{b}/ em: {txt[:90]}")

for it in items:
    k = it["key"]
    if it["kind"] in ("cad", "pronto"):
        tl, ml = len(it["title"]), len(it["meta"])
        if tl > 60: errors.append(f"{k}: title {tl} > 60")
        if ml > 155: errors.append(f"{k}: meta {ml} > 155")
        texts = [it["intro"][0]] + [b[0] for b in it["bullets"]]
        if not (3 <= len(it["bullets"]) <= 5): errors.append(f"{k}: {len(it['bullets'])} bullets")
        if not re.search(re.escape(it["serve"]), " ".join(texts)):
            errors.append(f"{k}: serve '{it['serve']}' não aparece em intro/bullets")
        if WA not in it["cta"][0]: errors.append(f"{k}: CTA sem WhatsApp")
        if "Execon" not in it["intro"][0]: errors.append(f"{k}: intro sem Execon")
        check_ids(it["intro"][1], k + " intro"); check_ids(it["meta_ids"], k + " meta")
        for b in it["bullets"]: check_ids(b[1], k + " bullet")
        check_ids(it["cta"][1], k + " cta")
        for q in it["faq"]:
            check_ids(q[2], k + " faq")
            if "Execon" not in q[1]: errors.append(f"{k}: resposta de FAQ sem o nome")
        public = [it["h1"], it["title"], it["meta"], it["intro"][0], it["cta"][0]] + [b[0] for b in it["bullets"]] + [x for q in it["faq"] for x in q[:2]]
        for t in public:
            scan(t, k)
        allsent = []
        for t in [it["intro"][0], it["cta"][0]] + [b[0] for b in it["bullets"]] + [x for q in it["faq"] for x in q[:2]]:
            allsent += sentences(t)
        wc = [len(s.split()) for s in allsent]
        it["_wc"] = (round(sum(wc) / len(wc), 1), max(wc), len(allsent))
        report.append(f"{k}: title {tl}/60 · meta {ml}/155 · frases {len(allsent)} · média {it['_wc'][0]} palavras · maior {it['_wc'][1]}")
    elif it["kind"] == "cond" and not it.get("ficha_only"):
        tl = len(it["title"])
        if tl > 60: errors.append(f"{k}: title {tl} > 60")
        if it.get("meta") and len(it["meta"]) > 155: errors.append(f"{k}: meta > 155")
        report.append(f"{k}: title reservado {tl}/60" + (f" · meta reservada {len(it['meta'])}/155" if it.get("meta") else ""))

print("\n".join(report))
if errors:
    print("\nERROS:"); print("\n".join(errors)); sys.exit(1)

# ================================================================== render
def f(s, ids): return f"{s} | [{', '.join(ids)}]"

KIND = {"cad": "cad (cadastrado e publicável)", "pronto": "pronto (sugerido e publicável)",
        "cond": "cond (espera condição)", "fundir": "fundir"}
out = []
out.append("# 31 · Catálogo como páginas — Grupo Execon (Execon Engenharia e Construção)\n")
out.append("**Redator:** agente redator-3-0 (catálogo), sem internet · **data:** 30/09/2026 · **única fonte de fatos:** `20-envelope.md` "
           "(ids `fact.*` PUB; nada de `int.*`, B01–B29 respeitados, C01–C11 fora do texto, PC1–PC7 aplicadas) · **textos atuais:** "
           "`02-textos-atuais.md` §PRODUTOS · **perguntas:** pauta do nicho em `10-descoberta-reputacao-conteudo.md` (só perguntas, nunca fatos).\n")
out.append("**Regra de base** (`solusite-padrao.md` §3): um item do catálogo é uma página do site, com o mesmo texto — e vice-versa. "
           "Item `cond` não sobe em nenhuma das duas vitrines até a condição chegar; item `fundir` sai do catálogo e a URL antiga redireciona (301).\n")
out.append("**Nome:** a prosa usa sempre \"Execon Engenharia e Construção\" (fact.name.001); \"Execon\" aparece só no fim do title, como nome curto (alternateName no JSON-LD); \"Grupo Execon\" fica só como nome da página (fact.name.002, C10).\n")
out.append("**Formato:** frases publicáveis em `frase | [ids]`; FAQ em `pergunta | resposta | [ids]`. Contagens de title e meta feitas com "
           "python3 (`len()` sobre a string exata). `serve` é a expressão literal do texto que diz para que ou para quem a página serve "
           "(vai virar regex de conferência; o gerador confirmou que cada uma aparece na intro ou nos bullets).\n")
out.append("**Setor regulado:** engenharia e arquitetura — `needs_human_review = SIM` (PC7). Nenhuma página promete prazo, orçamento, "
           "segurança ou norma técnica; nenhuma cita número de anos, casas ou m²; nenhuma cita registro em conselho, pessoa física, "
           "endereço de rua, horário ou a loteadora dos condomínios. Gate §8: o site inteiro só publica depois de C09 (página duplicada "
           "23064979) resolvido (PC6).\n")
out.append("**Resumo:** 6 `cad` · 2 `pronto` · 3 `cond` (547874, 547871, s-eua) · 1 `fundir` (547870 → 547879). Catálogo publicado: 8 itens = 8 páginas.\n")
out.append("---\n")

for it in items:
    k = it["key"]
    out.append(f"## {k} · {it['card']}\n")
    out.append(f"- **key:** {k}")
    if it["kind"] == "fundir":
        out.append(f"- **kind:** fundir → {it['destino']}")
        out.append(f"- **card:** {it['card']}")
        out.append(f"- **url:** {it['url']}")
        out.append(f"- **motivo:** {it['motivo']}")
        out.append(f"- **volta se:** {it['volta_se']}")
        out.append(f"- **nota_atual:** {it['nota_atual']}\n")
        continue
    out.append(f"- **kind:** {KIND[it['kind']]}")
    out.append(f"- **card:** {it['card']}")
    out.append(f"- **url:** {it['url']}")
    if it["kind"] == "cond":
        if it.get("ficha_only"):
            out.append("- **h1 · title · meta · intro · bullets · cta · faq:** não redigidos — ficha de condição apenas.")
            out.append(f"- **o que já pode ir ao ar (fora do catálogo):** {it['ja_pode']}")
            out.append(f"- **cond:** {it['cond']}")
            out.append(f"- **perguntas da página futura:** {it['perguntas']}")
        else:
            out.append(f"- **h1 (reservado):** {it['h1']}")
            out.append(f"- **title ({len(it['title'])}/60, reservado):** {it['title']}")
            if it.get("meta"):
                out.append(f"- **meta ({len(it['meta'])}/155, reservado):** {it['meta']} — {it['meta_note']}")
            else:
                out.append(f"- **meta:** {it['meta_note']}")
            out.append("- **intro · bullets · cta · faq:** não redigidos — nenhuma frase desta página tem fato publicável no envelope hoje.")
            out.append(f"- **serve (reservado):** `{it['serve']}`")
            out.append(f"- **cond:** {it['cond']}")
            out.append(f"- **enquanto isso:** {it['enquanto']}")
        out.append(f"- **pend:** {it['pend']}")
        out.append(f"- **nota_atual:** {it['nota_atual']}\n")
        continue
    out.append(f"- **h1:** {it['h1']}")
    out.append(f"- **title ({len(it['title'])}/60):** {it['title']}")
    out.append(f"- **meta ({len(it['meta'])}/155):** {f(it['meta'], it['meta_ids'])}")
    out.append(f"- **intro:** {f(*it['intro'])}")
    out.append("- **bullets:**")
    for b in it["bullets"]:
        out.append(f"  - {f(*b)}")
    out.append(f"- **serve:** `{it['serve']}`")
    out.append(f"- **cta:** {f(*it['cta'])}")
    if it["faq"]:
        out.append("- **faq:**")
        for q in it["faq"]:
            out.append(f"  - {q[0]} | {q[1]} | [{', '.join(q[2])}]")
    else:
        out.append("- **faq:** —")
    out.append(f"- **links internos:** {it['links']}")
    out.append(f"- **frases:** {it['_wc'][2]} · média {it['_wc'][0]} palavras · maior {it['_wc'][1]}")
    out.append(f"- **pend:** {it['pend']}")
    out.append(f"- **nota_atual:** {it['nota_atual']}\n")

out.append("---\n")
out.append("## Ordem recomendada do catálogo\n")
order = [
    ("1", "p547877", "Construção de casa de alto padrão", "É o produto principal: o posicionamento que o CS confirmou e o banner de 28/09/2026 (fact.service.001, fact.positioning.001). Abre o catálogo e recebe links de todas as outras páginas."),
    ("2", "p547879", "Gerenciamento de obras", "Segundo serviço do banner (\"projetos completos de gestão de obras\") e o de mais fontes depois da construção (três, fact.service.002). Absorve o 547870."),
    ("3", "s-condominios-interior", "Obras em condomínios do interior", "É o fato mais próprio da Execon (unicidade na rubrica) e fala com o cliente de casa de campo; sobe logo depois dos dois serviços que ele contrata ali. Só publica com C09 resolvido."),
    ("4", "s-reforma", "Reforma de casa", "Serviço com quatro canais independentes do texto da Solutudo (fact.service.003) e que hoje não tem item."),
    ("5", "p547881", "Área de lazer", "Complemento da casa: piscina, churrasqueira e área gourmet (fact.service.005)."),
    ("6", "p547873", "Pergolado", "Complemento da área de lazer, com fatos concretos de material e cobertura (fact.service.006)."),
    ("7", "p547876", "Obras comerciais", "Público diferente (negócio, não casa); fica depois da jornada residencial, que é o foco declarado."),
    ("8", "p547883", "Instalações elétricas", "Serviço de apoio, com a fonte mais fraca (produto + pista de CNAE) e com os limites de PC3."),
]
out.append("| # | Item | Card | Por quê |\n|---|---|---|---|")
for o in order:
    out.append(f"| {o[0]} | {o[1]} | {o[2]} | {o[3]} |")
out.append("\nA lógica é a jornada de quem vai construir uma casa de alto padrão — construir, gerenciar, onde, reformar, complementar — e só "
           "depois os públicos e serviços de apoio. Fora da vitrine: p547874 e p547871 (cond, PC2 e PC1/PC3), s-eua (cond, PC4) e p547870 "
           "(fundido no p547879).\n")
out.append("**Enumeração de serviços (a mesma em todos os canais):** construção de casas de alto padrão · gestão e acompanhamento de obras · "
           "reforma residencial e comercial · obras comerciais (lojas, escritórios, restaurantes) · áreas de lazer residenciais · pergolados · "
           "instalações e manutenção elétrica. A descrição da empresa, o Google e o Solusite devem listar exatamente estes sete, sem "
           "\"projetos arquitetônicos\", \"projeto estrutural\", \"licenciamento\", \"hidráulica\" ou \"automação\".\n")

out.append("## Catálogo = páginas\n")
table = [
    ("p547877", "cad", "Construção de casa de alto padrão", "/construcao-de-casa-alto-padrao", "Renomear o item (era \"Construtora Especializada\") e trocar o texto."),
    ("p547879", "cad", "Gerenciamento de obras", "/gerenciamento-de-obras", "Trocar o texto (tira o markup do tradutor); recebe o 547870."),
    ("p547870", "fundir", "—", "/acompanhamento-de-obra → 301 /gerenciamento-de-obras", "Excluir o item do catálogo."),
    ("s-condominios-interior", "pronto", "Obras em condomínios do interior", "/obras-condominios-interior-sp", "Criar o item (depois de C09)."),
    ("s-reforma", "pronto", "Reforma de casa", "/reforma-de-casa", "Criar o item."),
    ("p547881", "cad", "Área de lazer", "/area-de-lazer", "Renomear (tira \"Projeto\") e trocar o texto."),
    ("p547873", "cad", "Pergolado", "/pergolado", "Trocar o texto; manter a imagem padrão."),
    ("p547876", "cad", "Obras comerciais", "/obras-comerciais", "Renomear (era \"Projeto Comercial\") e trocar o texto (tira o markup do tradutor)."),
    ("p547883", "cad", "Instalações elétricas", "/instalacao-eletrica", "Renomear (era \"Elétrica em Geral\") e trocar o texto (tira o markup do tradutor)."),
    ("p547874", "cond", "Projeto arquitetônico (reservado)", "/projeto-arquitetonico (reservada, sem página)", "Tirar do ar agora; volta com PC2."),
    ("p547871", "cond", "Projeto e aprovação de obra (reservado)", "/projeto-e-aprovacao-de-obra (reservada, sem página)", "Tirar do ar agora; volta com PC1 + PC3, ou é excluído."),
    ("s-eua", "cond", "Estados Unidos (reservado)", "/estados-unidos (reservada, sem página)", "Não criar; só com PC4."),
]
out.append("| Item | kind | Card na Solutudo | URL no Solusite | Ação no cadastro |\n|---|---|---|---|---|")
for t in table:
    out.append(f"| {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} |")
out.append("\n**Conferências feitas pelo gerador** (`gen_catalogo.py`, no scratchpad): title ≤ 60 e meta ≤ 155 em todas as páginas publicáveis; "
           "todo id citado existe no envelope como `fact.*` PUB; a expressão `serve` aparece literalmente na intro ou nos bullets; o CTA traz "
           "o WhatsApp (11) 98454-5681; toda resposta de FAQ repete o nome; nenhuma frase publicável contém anos, m², garantia, qualidade, "
           "prazo, orçamento, segurança, NBR, \"tempo real\", referência, exclusividade, especialista, sustentabilidade, parceria, a loteadora, "
           "Estados Unidos, arquitetura, estrutural, licença, aprovação, CREA, CAU, \"Grupo\", rua, bairro, equipe, \"sempre\" nem os telefones "
           "(13) e (14).\n")

open(D + "31-catalogo.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\nOK: gravado 31-catalogo.md")
