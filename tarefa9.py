from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Importe sua função ou script aqui
from tarefa9 import minha_funcao

# Defina seus argumentos de DAG
default_args = {
    'owner': 'seu_nome',
    'start_date': datetime(2023, 9, 7),
    # Adicione outros argumentos, como horário de início, agenda, etc.
}

# Crie um objeto DAG
dag = DAG(
    'nome_do_dag',  # Nome do seu DAG
    default_args=default_args,
    schedule_interval='@daily',  # Frequência de execução
    catchup=False,  # Se você deseja pegar o backlog de datas
)

# Defina uma tarefa no DAG que executa sua função ou script
executar_script = PythonOperator(
    task_id='executar_script',
    python_callable=minha_funcao,  # Substitua pela sua função
    dag=dag,
)

# Você pode definir dependências entre tarefas se necessário
# executar_script >> outra_tarefa

if __name__ == "__main__":
    dag.cli()
