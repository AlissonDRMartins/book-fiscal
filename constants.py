from typing import Dict, List, Tuple

LIMITS = [180000, 360000, 720000, 1800000, 3600000, 4800000]

TAX_RATES: Dict[int, List[Tuple[float, int]]] = {
    1: [
        (4.0, 0),
        (7.3, 5940),
        (9.5, 13860),
        (10.7, 22500),
        (14.3, 87300),
        (19.0, 378000),
    ],
    2: [
        (4.5, 0),
        (7.8, 5940),
        (10.0, 13860),
        (11.2, 22500),
        (14.7, 85500),
        (30.0, 720000),
    ],
    3: [
        (6.0, 0),
        (11.2, 9360),
        (13.5, 17640),
        (16.0, 35640),
        (21.0, 125640),
        (33.0, 648000),
    ],
    4: [
        (4.5, 0),
        (9.0, 8100),
        (10.2, 12420),
        (14.0, 39780),
        (22.0, 183780),
        (33.0, 828000),
    ],
    5: [
        (15.5, 0),
        (18.0, 4500),
        (19.5, 9900),
        (20.5, 17100),
        (23.0, 62100),
        (30.5, 540000),
    ],
}

MAP_ANEXO: Dict[int, List[int]] = {
    0: [1],  # Comércio -> Anexo 1
    1: [2],  # Indústria -> Anexo 2
    2: [3, 4, 5],  # Outros -> Anexos 3, 4, 5
    3: [1, 2, 3, 4, 5],  # Todos os Anexos
}

MESES_PTBR = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

CATEGORIES = {0: "Comércio", 1: "Indústria", 2: "Outros", 3: "Todos os Anexos"}
