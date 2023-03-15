from db.models import MovieSession
from django.db.models import QuerySet

import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )

    return new_movie_session


def get_movies_sessions(
        movie_show_time: str = None
) -> QuerySet:
    query_set = MovieSession.objects.filter()
    if movie_show_time:
        movie_show_time = movie_show_time.split("-")
        query_set = query_set.filter(
            show_time__year=movie_show_time[0],
            show_time__month=movie_show_time[1],
            show_time__day=movie_show_time[2]
        )

    return query_set


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> int:
    return MovieSession.objects.filter(id=session_id).delete()
