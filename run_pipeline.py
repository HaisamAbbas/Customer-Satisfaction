from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__=="__main__":
    
    print(Client().active_stack.experiment_tracker.get_tracking_uri())

    
    train_pipeline(data_path="E:\Customer Satisfaction\data\olist_customers_dataset.csv")


# mlflow ui --backend-store-uri "file:C:\Users\Tanassar Hussain\AppData\Roaming\zenml\local_stores\8d73f2fc-43a6-40ab-b00e-02631d519e13\mlruns"