#%%
import requests
import json
import pathlib


#%%
aa_base_url = 'https://cov-spectrum.ethz.ch/gisaid/api/v1/sample/aa-mutations'
count_base_url = 'https://cov-spectrum.ethz.ch/gisaid/api/v1/sample/aggregated'
THRESHOLD = 0.005

clusters = {
    '21A.Delta': ['11514.','4181.','6402.','27752T','28461G','22995A'],
    '21J.Delta': ['4181T','6402T','27752T','28461G','22995A'],
    '21I.Delta': ['5584G', '11514T', '22227T','27752T','28461G','22995A'],
    'AY.4.2': ['21995C','22227T','4181T','6402T','27752T','28461G','22995A'],
    'AY.9': ['1729A', '14030A', '18086T','5584G'],
}

def build_url(base_url,cluster,threshold):
    url = f"{base_url}?nucMutations={','.join(cluster)}"
    if threshold is not None:
        url += f"&minProportion={threshold:f}"
    return url
#%%

if __name__ == '__main__':
    for cluster_name, cluster_muts in clusters.items():
        aa_request_url = build_url(aa_base_url,cluster_muts,THRESHOLD)
        count_request_url = build_url(count_base_url,cluster_muts,None)
        print(aa_request_url)
        print(count_request_url)
        aa_request = requests.get(aa_request_url)
        count_request = requests.get(count_request_url)
        aa = json.loads(aa_request.content)
        count = json.loads(count_request.content)
        mutations = []
        for mutation in aa['data']:
            mutations.append({'mut': mutation['mutation'], 'count': mutation['proportion']})

        out_json = {
            "total": count['data'][0]['count'],
            "counts": mutations
        }
        
        path = pathlib.Path(f"output/{cluster_name}.json")
        path.parent.mkdir(parents=True, exist_ok=True) 
        
        with open(path,'w') as f:
            json.dump(out_json,f)


# %%
