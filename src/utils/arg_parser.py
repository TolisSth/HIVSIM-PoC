# Author: Apostolos Chalis 2026 | cs05414@uowm.gr
import argparse 

def get_args(): 
    parser = argparse.ArgumentParser(description="Modeling the infection of CD4+ T4 cells from HIV virions in a petri dish | Apostolos Chalis 2026 <cs05414@uowm.gr> ")

    # Agent polulation parameters 
    parser.add_argument("--initial_cd4_cells", type=int, default=100, help="Initial number of CD4+ T4 cells in the petri dish")
    parser.add_argument("--initial_hiv_virions", type=int, default=10, help="Initial number of HIV virions in the petri dish")

    return parser.parse_args()
