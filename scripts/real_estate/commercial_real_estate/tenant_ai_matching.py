from sklearn.cluster import KMeans
import numpy as np

def match_tenants_to_properties(tenant_features, property_features):
    """Matches commercial tenants to properties using AI clustering."""
    model = KMeans(n_clusters=3)
    model.fit(np.vstack([tenant_features, property_features]))
    return model.labels_

# Example usage
if __name__ == "__main__":
    tenants = np.array([[2000, 5], [1500, 3], [3000, 7]])  # Monthly budget, employees
    properties = np.array([[1800, 4], [2200, 6], [2500, 5]])
    matches = match_tenants_to_properties(tenants, properties)
    print(f"✅ Tenant-Property Matches: {matches}")
