"""This is a quick-and-simple script to glean a high level view of Datadog metrics. To use this
script, navigate to your Datadog landing page, choose 'metrics' from the left sidebar, then choose 'Summary' from the resulting menu. There is a button reading 'export as .csv', click this button and then replace the filename at line 10 with whatever you choose to name the exported .csv. 

I have manually deleted the first line of the .csv, which is the title of a column and not relevant."""

from pprint import pprint

def build_metrics_glossary():  
    glossary_dict = {}
    with open('datadog_all_metrics.csv', 'r') as all_metrics:
        for each_line in all_metrics:
            split_line = each_line.split('.')
            first_term = split_line[0]
            if first_term in glossary_dict:
                glossary_dict[first_term] += 1
            else:
                glossary_dict[first_term] = 1

    return glossary_dict

def calculate_metrics_total(all_metrics):
    """takes a dictionary using metric names as the key and the number
    of instances of that metric as the key's value. Returns the total sum of metrics"""

    return sum(all_metrics.values())


glossary = build_metrics_glossary()
print("a glossary of {} has been generated".format(len(glossary)))
pprint(glossary)

print(f"the total number of metrics is {calculate_metrics_total(glossary)}")
