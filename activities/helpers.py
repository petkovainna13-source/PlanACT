def filter_activities(activities,cleaned_data):

    max_budget = cleaned_data['max_budget']
    distance = cleaned_data['distance']
    pet_friendly =cleaned_data['pet_friendly']
    environment = cleaned_data['environment']

    if max_budget is not None:
        activities = activities.filter(budget__lte=max_budget)

    if distance is not None:
        activities = activities.filter(distance__lte=distance)

    if pet_friendly == "yes":

        activities = activities.filter(pet_friendly=True)
    elif pet_friendly == "no":
        activities = activities.filter(pet_friendly=False)

    if environment:
        activities = activities.filter(environment=environment)

    return activities