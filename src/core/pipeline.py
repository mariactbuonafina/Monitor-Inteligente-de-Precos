from services.persistencia import salvar_csv
from services.analise import gerar_relatorio
from services.graficos import gerar_graficos
from services.dashboard import gerar_dashboard


class Pipeline:

    def executar(self, df):

        salvar_csv(df)

        gerar_relatorio(df)

        gerar_graficos(df)

        gerar_dashboard(df)

        return df