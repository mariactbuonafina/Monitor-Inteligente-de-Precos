from services.tratamento import transformar_feriados
from services.persistencia import salvar_csv
from services.analise import gerar_relatorio
from services.graficos import gerar_grafico_tipos
from utils.logger import logger


class Pipeline:

    def executar(self, dados):

        logger.info("Pipeline iniciado.")

        df = transformar_feriados(dados)

        salvar_csv(df)

        gerar_relatorio(df)

        gerar_grafico_tipos(df)

        logger.info(f"{len(df)} registros processados.")

        logger.info("Pipeline finalizado.")

        return df