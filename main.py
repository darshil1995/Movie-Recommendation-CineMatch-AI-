import extract,transform,load_model
import time

if __name__ == "__main__":
    start = time.time()
    extract.run_extraction()
    transform.run_transformation()
    load_model.run_modeling()
    print(f"✅ Full ETL Pipeline finished in {round(time.time()-start, 2)} seconds.")