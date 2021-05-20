from django.http import HttpResponse
from django.utils.timezone import now


posts = [
    {
        'name': 'Marvin Ramirez',
        'user': 'mRamirez',
        'timestamp': str(now()),
    }
] * 3


def list_posts(request):
    content = (
        """
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        """.format(**post)
        for post in posts
    )

    return HttpResponse('<br>'.join(content))
