import requests
import json

base_url = "https://www.udemy.com/api-2.0"

def get_course_data(course_id):

    headers = {
                'user-agent': 'PostmanRuntime/7.28.1',
                'Content-Type': 'application/json;charset=utf-8',
                'Accept': 'application/json, text/plain, */*'
              }

    uri = '/courses/' + course_id + '/public-curriculum-items' +'?page_size=10000'

    url = base_url + uri

    res = requests.get(url = url, headers = headers, verify = False)

    data = json.loads(res.text)

    results = data['results']

    lectures = []
    chapter = ''
    for result in results:
        _class = result['_class']
        if _class == 'chapter':
            chapter = result['title']
        else:
            lecture = chapter + ' : ' + result['title']
            lectures.append(lecture)
    return lectures


lectures = get_course_data('2459618')
i = 1
for lecture in lectures:
    print(i, lecture)
    i += 1

