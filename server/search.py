import click

from modules.cameras import parse_csv_cameras_to_json


@click.command()
@click.option('--name', default='')
@click.option('--latitude', default='')
@click.option('--longitude', default='')
@click.option('--number', default='')
def get_filtered_cameras(name, latitude, longitude, number):
    cameras = parse_csv_cameras_to_json('data/cameras-defb.csv')

    if name:
        cameras = [camera for camera in cameras if name.lower() in camera['Camera'].lower()]
    if latitude:
        cameras = [camera for camera in cameras if latitude == camera['Latitude']]
    if longitude:
        cameras = [camera for camera in cameras if longitude == camera['Longitude']]
    if number:
        cameras = [camera for camera in cameras if number == camera['number']]

    print_cameras(cameras)


def print_cameras(cameras):
    for camera in cameras:
        print(
            '{} | {} | {} | {}'.format(camera['number'], camera['Camera'], camera['Latitude'], camera['Longitude']))


if __name__ == '__main__':
    get_filtered_cameras()
