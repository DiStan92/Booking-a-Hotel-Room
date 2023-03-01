# Booking-a-Hottel-Room platform Back-End

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/DiStan92/Booking-a-Hotel-Room.git
$ cd BookingHottelRoom
```

Clone `.env.dev` file, rename it to `.env` and fill it with your data.

Once `pip` has finished downloading the dependencies, run `PostgreSQL` docker container localy:

```sh
$ docker run --name db -p 5432:5432 --env-file ./.env -d postgres:14
```

And run docker-compose.yml:

```sh
$ docker-compose run -d

```

Navigate to `http://127.0.0.1:8000`.
