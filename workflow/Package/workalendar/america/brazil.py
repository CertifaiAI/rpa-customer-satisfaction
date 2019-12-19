# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import timedelta, date

from ..core import WesternCalendar, ChristianMixin
from ..core import MON, SAT, SUN
from ..registry_tools import iso_register


@iso_register('BR')
class Brazil(WesternCalendar, ChristianMixin):
    "Brazil"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (4, 21, "Tiradentes' Day"),
        (5, 1, "Labour Day"),
        (9, 7, "Independence Day"),
        (10, 12, "Our Lady of Aparecida"),
        (11, 2, "All Souls' Day"),
        (11, 15, "Republic Day"),
    )
    include_sao_jose = False
    sao_jose_label = "São José"
    include_sao_pedro = False
    sao_pedro_label = "São Pedro"
    include_sao_joao = False
    sao_joao_label = "São João"
    include_servidor_publico = False
    servidor_publico_label = "Dia do Servidor Público"
    # Consciência Negra day
    include_consciencia_negra = True
    # There are two dates for the Consciência Negra day
    # The most common is November, 20th
    consciencia_negra_day = (11, 20)
    consciencia_negra_label = "Consciência Negra"
    include_nossa_senhora_conceicao = False
    include_easter_sunday = True

    def get_carnaval(self, year):
        """
        Return the third day of Carnaval (Tuesday)

        This day is shared holidays by several Brazil states.
        """
        return self.get_easter_sunday(year) - timedelta(days=47)

    def get_variable_days(self, year):
        days = super(Brazil, self).get_variable_days(year)
        if self.include_sao_jose:
            days.append((date(year, 3, 19), self.sao_jose_label))
        if self.include_sao_pedro:
            days.append((date(year, 6, 29), self.sao_pedro_label))
        if self.include_sao_joao:
            days.append((date(year, 6, 24), self.sao_joao_label))
        if self.include_servidor_publico:
            days.append((date(year, 10, 28), self.servidor_publico_label))
        if self.include_consciencia_negra:
            month, day = self.consciencia_negra_day
            days.append(
                (date(year, month, day), self.consciencia_negra_label)
            )
        if self.include_nossa_senhora_conceicao:
            days.append(
                (date(year, 12, 8), "Dia de Nossa Senhora da Conceição")
            )
        return days


@iso_register('BR-AC')
class BrazilAcre(Brazil):
    "Brazil Acre State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 23, "Dia do evangélico"),
        (6, 15, "Aniversário do Acre"),
        (9, 5, "Dia da Amazônia"),
        (11, 17, "Assinatura do Tratado de Petrópolis"),
        (8, 6, "Início da Revolução Acreana"),
    )


@iso_register('BR-AL')
class BrazilAlagoas(Brazil):
    "Brazil Alagoas State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (9, 16, "Emancipação política de Alagoas"),
    )
    include_sao_pedro = True
    include_sao_joao = True
    include_consciencia_negra = True


@iso_register('BR-AP')
class BrazilAmapa(Brazil):
    "Brazil Amapá State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 25, "São Tiago"),
        (10, 5, "Criação do estado"),
        (9, 13, "Aniversário da Amapá"),
    )
    include_sao_jose = True
    sao_jose_label = "Dia de São José"
    include_consciencia_negra = True


@iso_register('BR-AM')
class BrazilAmazonas(Brazil):
    "Brazil Amazonas State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (9, 5, "Elevação do Amazonas á categoria de província"),
    )
    include_consciencia_negra = True
    include_nossa_senhora_conceicao = True


@iso_register('BR-BA')
class BrazilBahia(Brazil):
    "Brazil Bahia State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 2, "Independência da Bahia"),
    )


@iso_register('BR-CE')
class BrazilCeara(Brazil):
    "Brazil Ceará State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (3, 23, "Data Manga do Ceará"),
        (3, 25, "Aniversário do Ceará"),
    )
    include_sao_jose = True


@iso_register('BR-DF')
class BrazilDistritoFederal(Brazil):
    "Brazil Distrito Federal State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 21, "Fundação de Brasília"),
        (11, 30, "Dia do Evangélico"),
    )


@iso_register('BR-ES')
class BrazilEspiritoSanto(Brazil):
    "Brazil Espírito Santo State"
    include_servidor_publico = True


@iso_register('BR-GO')
class BrazilGoias(Brazil):
    "Brazil Goiás State"
    include_servidor_publico = True


@iso_register('BR-MA')
class BrazilMaranhao(Brazil):
    "Brazil Maranhão State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 28, "Adesão do Maranhão á independência do Brasil"),
    )
    include_nossa_senhora_conceicao = True


@iso_register('BR-MG')
class BrazilMinasGerais(Brazil):
    "Brasil Minas Gerais State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 21, "Aniversário de Minas Gerais"),
    )


@iso_register('BR-MT')
class BrazilMatoGrosso(Brazil):
    "Brazil Mato Grosso State"
    include_consciencia_negra = True
    consciencia_negra_day = (11, 29)


@iso_register('BR-MS')
class BrazilMatoGrossoDoSul(Brazil):
    "Brazil Mato Grosso do Sul State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 11, "Criação do estado"),
    )


@iso_register('BR-PA')
class BrazilPara(Brazil):
    "Brazil Pará State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 15, "Adesão do Grão-Pará á independência do Brasil"),
    )
    include_nossa_senhora_conceicao = True


@iso_register('BR-PB')
class BrazilParaiba(Brazil):
    "Brazil Paraíba State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 5, "Fundação do Estado"),
        (7, 26, "Homenagem à memória do ex-presidente João Pessoa"),
    )


@iso_register('BR-PE')
class BrazilPernambuco(Brazil):
    "Brazil Pernambuco State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (6, 3, "Revolução Pernambucana de 1817"),
    )
    include_sao_joao = True


@iso_register('BR-PI')
class BrazilPiaui(Brazil):
    "Brazil Piauí State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (3, 13, "Dia da Batalha do Jenipapo"),
        (10, 19, "Dia do Piauí"),
    )


@iso_register('BR-PR')
class BrazilParana(Brazil):
    "Brazil Paraná State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (12, 19, "Aniversário do Paraná"),
    )


@iso_register('BR-RJ')
class BrazilRioDeJaneiro(Brazil):
    "Brazil Rio de Janeiro State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (4, 23, "Dia de São Jorge"),
        (3, 1, "Aniversário da Cidade do Rio de Janeiro"),
    )
    include_servidor_publico = True
    servidor_publico_label = "Dia do Funcionário Público"
    include_consciencia_negra = True
    consciencia_negra_label = "Dia da Consciência Negra"
    include_nossa_senhora_conceicao = True

    def get_dia_do_comercio(self, year):
        """
        Return Dia do Comércio variable date

        It happens on the 3rd Monday of october.
        """
        return BrazilRioDeJaneiro.get_nth_weekday_in_month(year, 10, MON, 3)

    def get_variable_days(self, year):
        days = super(BrazilRioDeJaneiro, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        days.append((self.get_dia_do_comercio(year), "Dia do Comércio"))
        return days


@iso_register('BR-RN')
class BrazilRioGrandeDoNorte(Brazil):
    "Brazil Rio Grande do Norte State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 3, "Mártires de Cunhaú e Uruaçuu"),
    )
    include_sao_pedro = True
    sao_pedro_label = "Dua de São Pedro"


@iso_register('BR-RS')
class BrazilRioGrandeDoSul(Brazil):
    "Brazil Rio Grande do Sul State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (9, 20, "Revolução Farroupilha"),
    )


@iso_register('BR-RO')
class BrazilRondonia(Brazil):
    "Brazil Rondônia State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 4, "Criação do estado"),
        (6, 18, "Dia do Evangélico"),
    )


@iso_register('BR-RR')
class BrazilRoraima(Brazil):
    "Brazil Roraima State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (10, 5, "Criação de Roraima"),
    )


@iso_register('BR-SC')
class BrazilSantaCatarina(Brazil):
    "Brazil Santa Catarina State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (8, 11, "Criação da capitania, separando-se de SP"),
        (11, 25, "Dia de Santa Catarina de Alexandria"),
    )


@iso_register('BR-SP')
class BrazilSaoPauloState(Brazil):
    "Brazil São Paulo State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 9, "Constitutional Revolution of 1932"),
    )


class BrazilSaoPauloCity(BrazilSaoPauloState):
    "Brazil São Paulo City"
    FIXED_HOLIDAYS = BrazilSaoPauloState.FIXED_HOLIDAYS + (
        (1, 25, "Anniversary of the city of São Paulo"),
    )
    include_easter_sunday = True
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Sexta-feira da Paixão"
    include_consciencia_negra = True
    consciencia_negra_label = "Dia da Consciência Negra"

    def get_variable_days(self, year):
        days = super(BrazilSaoPauloCity, self).get_variable_days(year)
        days.append((self.get_carnaval(year), "Carnaval"))
        return days


@iso_register('BR-SE')
class BrazilSergipe(Brazil):
    "Brazil Sergipe State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (7, 8, "Autonomia política de Sergipe"),
    )


@iso_register('BR-TO')
class BrazilTocantins(Brazil):
    "Brazil Tocantins State"
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (1, 1, "Instalação de Tocantins"),
        (9, 8, "Nossa Senhora da Natividade"),
        (10, 5, "Criação de Tocantins"),
        (3, 18, "Autonomia do estado de Tocantins"),
    )


class BrazilVitoriaCity(BrazilEspiritoSanto):
    "Brazil Vitória City"
    FIXED_HOLIDAYS = BrazilEspiritoSanto.FIXED_HOLIDAYS + (
        (4, 24, "Nossa Senhora da Penha"),  # Our Lady of Pain?
        (9, 8, "Nossa Senhora da Vitória"),  # Our Lady of Vitória
        (9, 8, "Aniversário de Vitória"),
    )
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Paixão do Cristo"


class BrazilVilaVelhaCity(BrazilEspiritoSanto):
    "Brazil Vila Velha City"
    FIXED_HOLIDAYS = BrazilEspiritoSanto.FIXED_HOLIDAYS + (
        (5, 23, "Colonização do Solo Espírito-santense"),
    )


class BrazilCariacicaCity(BrazilEspiritoSanto):
    "Brazil Cariacica City"
    FIXED_HOLIDAYS = BrazilEspiritoSanto.FIXED_HOLIDAYS + (
        (4, 13, "Nossa Senhora da Penha"),
    )
    include_corpus_christi = True
    include_good_friday = True
    good_friday_label = "Paixão do Cristo"
    include_sao_joao = True
    sao_joao_label = "São João Batista / Aniversãrio de Cariacica"


class BrazilGuarapariCity(BrazilEspiritoSanto):
    "Brazil Guarapari City"
    FIXED_HOLIDAYS = BrazilEspiritoSanto.FIXED_HOLIDAYS + (
        (9, 19, "Emancipação de Guarapari"),
    )
    include_sao_pedro = True
    include_consciencia_negra = True
    consciencia_negra_day = (11, 29)
    include_nossa_senhora_conceicao = True


class BrazilSerraCity(BrazilEspiritoSanto):
    "Brazil Serra City"
    FIXED_HOLIDAYS = BrazilEspiritoSanto.FIXED_HOLIDAYS + (
        (12, 26, "Dia do Serrano"),
    )
    include_ash_wednesday = True
    ash_wednesday_label = "Quarta-feira de cinzas"
    include_good_friday = True
    good_friday_label = "Paixão do Cristo"
    include_sao_pedro = True
    include_nossa_senhora_conceicao = True

    def get_variable_days(self, year):
        days = super(BrazilSerraCity, self).get_variable_days(year)
        carnaval_tuesday = self.get_carnaval(year)
        days.append((carnaval_tuesday - timedelta(days=1), "Carnaval Monday"))
        days.append((carnaval_tuesday, "Carnaval"))
        return days


class BrazilRioBrancoCity(BrazilAcre):
    "Brazil Rio Branco City"
    FIXED_HOLIDAYS = BrazilAcre.FIXED_HOLIDAYS + (
        (12, 28, "Aniversário de Rio Branco"),
    )


class BrazilMaceioCity(BrazilAlagoas):
    "Brazil Maceió City"
    FIXED_HOLIDAYS = BrazilAlagoas.FIXED_HOLIDAYS + (
        (12, 5, "Aniversário de Maceió"),
    )


class BrazilManausCity(BrazilAmazonas):
    "Brazil Manaus City"
    FIXED_HOLIDAYS = BrazilAmazonas.FIXED_HOLIDAYS + (
        (10, 24, "Aniversário de Manaus"),
    )


class BrazilMacapaCity(BrazilAmapa):
    "Brazil Macapá City"
    FIXED_HOLIDAYS = BrazilAmapa.FIXED_HOLIDAYS + (
        (2, 4, "Aniversário de Macapá"),
    )


class BrazilSalvadorCity(BrazilBahia):
    "Brazil Salvador City"
    FIXED_HOLIDAYS = BrazilBahia.FIXED_HOLIDAYS + (
        (3, 29, "Aniversário de Salvador"),
    )


class BrazilFortalezaCity(BrazilCeara):
    "Brazil Fortaleza City"
    FIXED_HOLIDAYS = BrazilCeara.FIXED_HOLIDAYS + (
        (4, 13, "Aniversário de Fortaleza"),
    )


class BrazilGoianiaCity(BrazilGoias):
    "Brazil Goiânia City"
    FIXED_HOLIDAYS = BrazilGoias.FIXED_HOLIDAYS + (
        (10, 24, "Aniversário de Goiânia"),
    )


class BrazilBeloHorizonteCity(BrazilMinasGerais):
    "Brazil Belo Horizonte City"
    FIXED_HOLIDAYS = BrazilMinasGerais.FIXED_HOLIDAYS + (
        (12, 12, "Aniversário de Belo Horizonte"),
    )


class BrazilCampoGrandeCity(BrazilMatoGrossoDoSul):
    "Brazil Campo Grande City"
    FIXED_HOLIDAYS = BrazilMatoGrossoDoSul.FIXED_HOLIDAYS + (
        (8, 26, "Aniversário de Campo Grande"),
    )


class BrazilCuiabaCity(BrazilMatoGrosso):
    "Brazil Cuiabá City"
    FIXED_HOLIDAYS = BrazilMatoGrosso.FIXED_HOLIDAYS + (
        (4, 8, "Aniversário de Cuiabá"),
    )


class BrazilBelemCity(BrazilPara):
    "Brazil Belém City"
    FIXED_HOLIDAYS = BrazilPara.FIXED_HOLIDAYS + (
        (1, 12, "Aniversário de Belém"),
    )


class BrazilJoaoPessoaCity(BrazilParaiba):
    "Brazil João Pessoa City"
    FIXED_HOLIDAYS = BrazilParaiba.FIXED_HOLIDAYS + (
        (8, 5, "Aniversário de João Pessoa"),
    )


class BrazilRecifeCity(BrazilPernambuco):
    "Brazil Recife City"
    FIXED_HOLIDAYS = BrazilPernambuco.FIXED_HOLIDAYS + (
        (3, 12, "Aniversário de Recife"),
    )


class BrazilTeresinaCity(BrazilPiaui):
    "Brazil Teresina City"
    FIXED_HOLIDAYS = BrazilPiaui.FIXED_HOLIDAYS + (
        (8, 16, "Aniversário de Teresina"),
    )


class BrazilCuritibaCity(BrazilParana):
    "Brazil Curitiba City"
    FIXED_HOLIDAYS = BrazilParana.FIXED_HOLIDAYS + (
        (3, 29, "Aniversário de Curitiba"),
    )


class BrazilNatalCity(BrazilRioGrandeDoNorte):
    "Brazil Natal City"
    FIXED_HOLIDAYS = BrazilRioGrandeDoNorte.FIXED_HOLIDAYS + (
        (12, 25, "Aniversário de Natal"),
    )


class BrazilPortoVelhoCity(BrazilRondonia):
    "Brazil Porto Velho City"
    FIXED_HOLIDAYS = BrazilRondonia.FIXED_HOLIDAYS + (
        (10, 2, "Aniversário de Porto Velho"),
    )


class BrazilBoaVistaCity(BrazilRoraima):
    "Brazil Boa Vista City"
    FIXED_HOLIDAYS = BrazilRoraima.FIXED_HOLIDAYS + (
        (6, 9, "Aniversário de Boa Vista"),
    )


class BrazilPortoAlegreCity(BrazilRioGrandeDoSul):
    "Brazil Porto Alegre City"
    FIXED_HOLIDAYS = BrazilRioGrandeDoSul.FIXED_HOLIDAYS + (
        (3, 26, "Aniversário de Porto Alegre"),
    )


class BrazilChapecoCity(BrazilSantaCatarina):
    "Brazil Chapecó City"
    FIXED_HOLIDAYS = BrazilSantaCatarina.FIXED_HOLIDAYS + (
        (8, 25, "Aniversário de Chapecó"),
    )


class BrazilFlorianopolisCity(BrazilSantaCatarina):
    "Brazil Florianópolis City"
    FIXED_HOLIDAYS = BrazilSantaCatarina.FIXED_HOLIDAYS + (
        (3, 23, "Aniversário de Florianópolis"),
    )


class BrazilJoinvilleCity(BrazilSantaCatarina):
    "Brazil Joinville City"
    FIXED_HOLIDAYS = BrazilSantaCatarina.FIXED_HOLIDAYS + (
        (3, 9, "Aniversário de Joinville"),
    )


class BrazilAracajuCity(BrazilSergipe):
    "Brazil Aracaju City"
    FIXED_HOLIDAYS = BrazilSergipe.FIXED_HOLIDAYS + (
        (3, 17, "Aniversário de Aracaju"),
    )


class BrazilSorocabaCity(BrazilSaoPauloState):
    "Brazil Sorocaba City"
    FIXED_HOLIDAYS = BrazilSaoPauloState.FIXED_HOLIDAYS + (
        (8, 15, "Aniversário de Sorocaba"),
    )


class BrazilPalmasCity(BrazilTocantins):
    "Brazil Palmas City"
    FIXED_HOLIDAYS = BrazilTocantins.FIXED_HOLIDAYS + (
        (5, 20, "Aniversário de Palmas"),
    )


class BrazilBankCalendar(Brazil):
    """
    Calendar that considers only working days for bank transactions
    for companies and the general public
    """
    FIXED_HOLIDAYS = Brazil.FIXED_HOLIDAYS + (
        (12, 25, "Christmas Day"),
    )

    def get_last_day_of_year_for_only_internal_bank_trans(self, year):
        """
        The last day of year isn't a working day for public bank
        transactions in Brazil. More details can be read in
        http://www.bcb.gov.br/pre/bc_atende/port/servicos4.asp
        """
        last_day = date(year, 12, 31)

        if last_day.weekday() == SAT:
            return last_day - timedelta(days=1)
        elif last_day.weekday() == SUN:
            return last_day - timedelta(days=2)

        return last_day

    def get_variable_days(self, year):
        """
        Define the brazilian variable holidays and the last
        day for only internal bank transactions
        """
        tuesday_carnaval = self.get_carnaval(year)
        monday_carnaval = tuesday_carnaval - timedelta(days=1)
        good_friday = self.get_good_friday(year)
        corpus_christi = self.get_corpus_christi(year)
        ash_wednesday = self.get_ash_wednesday(year)

        non_fixed_holidays = [
            (monday_carnaval, "Monday carnaval"),
            (tuesday_carnaval, "Tuesday carnaval"),
            (good_friday, "Good friday"),
            (corpus_christi, "Corpus Christi"),
            (ash_wednesday, "Ash Wednesday"),
        ]

        non_working_days = [
            (
                self.get_last_day_of_year_for_only_internal_bank_trans(year),
                "Last day of year for only internal bank transactions"
            )
        ]

        return non_fixed_holidays + non_working_days

    def find_following_working_day(self, day):
        """
        Find for the next working day by ignoring weekends,
        fixed and non fixed holidays and the last working
        day for only internal bank transactions in Brazil
        """
        while not self.is_working_day(day):
            day = day + timedelta(days=1)
        return day


IBGE_TUPLE = (
    ('BR-IBGE-12', BrazilAcre),
    ('BR-IBGE-27', BrazilAlagoas),
    ('BR-IBGE-16', BrazilAmapa),
    ('BR-IBGE-13', BrazilAmazonas),
    ('BR-IBGE-29', BrazilBahia),
    ('BR-IBGE-23', BrazilCeara),
    ('BR-IBGE-53', BrazilDistritoFederal),
    ('BR-IBGE-32', BrazilEspiritoSanto),
    ('BR-IBGE-52', BrazilGoias),
    ('BR-IBGE-21', BrazilMaranhao),
    ('BR-IBGE-31', BrazilMinasGerais),
    ('BR-IBGE-51', BrazilMatoGrosso),
    ('BR-IBGE-50', BrazilMatoGrossoDoSul),
    ('BR-IBGE-15', BrazilPara),
    ('BR-IBGE-25', BrazilParaiba),
    ('BR-IBGE-26', BrazilPernambuco),
    ('BR-IBGE-22', BrazilPiaui),
    ('BR-IBGE-41', BrazilParana),
    ('BR-IBGE-33', BrazilRioDeJaneiro),
    ('BR-IBGE-24', BrazilRioGrandeDoNorte),
    ('BR-IBGE-43', BrazilRioGrandeDoSul),
    ('BR-IBGE-11', BrazilRondonia),
    ('BR-IBGE-14', BrazilRoraima),
    ('BR-IBGE-42', BrazilSantaCatarina),
    ('BR-IBGE-35', BrazilSaoPauloState),
    ('BR-IBGE-3550308', BrazilSaoPauloCity),
    ('BR-IBGE-28', BrazilSergipe),
    ('BR-IBGE-17', BrazilTocantins),
    ('BR-IBGE-3205309', BrazilVitoriaCity),
    ('BR-IBGE-3205200', BrazilVilaVelhaCity),
    ('BR-IBGE-3201308', BrazilCariacicaCity),
    ('BR-IBGE-3202405', BrazilGuarapariCity),
    ('BR-IBGE-3205002', BrazilSerraCity),
    ('BR-IBGE-1200401', BrazilRioBrancoCity),
    ('BR-IBGE-2704302', BrazilMaceioCity),
    ('BR-IBGE-1302603', BrazilManausCity),
    ('BR-IBGE-1600303', BrazilMacapaCity),
    ('BR-IBGE-2927408', BrazilSalvadorCity),
    ('BR-IBGE-2304400', BrazilFortalezaCity),
    ('BR-IBGE-5208707', BrazilGoianiaCity),
    ('BR-IBGE-3106200', BrazilBeloHorizonteCity),
    ('BR-IBGE-5002704', BrazilCampoGrandeCity),
    ('BR-IBGE-5103403', BrazilCuiabaCity),
    ('BR-IBGE-1501402', BrazilBelemCity),
    ('BR-IBGE-2507507', BrazilJoaoPessoaCity),
    ('BR-IBGE-2611606', BrazilRecifeCity),
    ('BR-IBGE-2211001', BrazilTeresinaCity),
    ('BR-IBGE-4106902', BrazilCuritibaCity),
    ('BR-IBGE-2408102', BrazilNatalCity),
    ('BR-IBGE-1100205', BrazilPortoVelhoCity),
    ('BR-IBGE-1400100', BrazilBoaVistaCity),
    ('BR-IBGE-4314902', BrazilPortoAlegreCity),
    ('BR-IBGE-4204202', BrazilChapecoCity),
    ('BR-IBGE-4205407', BrazilFlorianopolisCity),
    ('BR-IBGE-4209102', BrazilJoinvilleCity),
    ('BR-IBGE-2800308', BrazilAracajuCity),
    ('BR-IBGE-3552205', BrazilSorocabaCity),
    ('BR-IBGE-1721000', BrazilPalmasCity),
)
IBGE_REGISTER = dict(IBGE_TUPLE)
