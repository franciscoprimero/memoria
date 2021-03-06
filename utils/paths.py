raw_path = 'raw_data'
data_path = 'data'
scores_path = 'scores'
times_path = 'tiempos'
models_path = 'models'
graficos_path = 'graficos'

datasets = ['amazon', 'twitter']

pruebas = ['baseline', 'msda', 'gfk', 'pca', 'sda']

dataframe_columns = ['Adaptacion',
                     'Tarea',
                     'Fuente',
                     'Objetivo',
                     'Baseline error',
                     'Transfer error',
                     'Transfer loss']


dataframe_time_columns = ['Adaptacion', 'Tiempo']

raw_folders = {
    'amazon': 'multi-domain/processed_acl',
    'twitter': 'twitter',
}

dimensions = {
 'amazon': 3000,
 'twitter': 2000,
}
