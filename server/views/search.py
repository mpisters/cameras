import click

from server.modules.cameras import parse_csv_cameras_to_json


@click.command()
@click.option('--name', default='')
@click.option('--latitude', default='')
@click.option('--longitude', default='')
@click.option('--row_number', default='')
def get_cameras_by_name(name, latitude, longitude, row_number):
    cameras = parse_csv_cameras_to_json('../data/cameras-defb.csv')
    cameras_filtered = []

    if name:
        cameras_filtered = [camera for camera in cameras if name.lower() in camera['Camera'].lower()]
    if latitude:
        cameras_filtered = [camera for camera in cameras_filtered if latitude == camera['Latitude']]
    if longitude:
        cameras_filtered = [camera for camera in cameras_filtered if longitude == camera['Longitude']]
    if row_number:
        cameras_filtered = [camera for camera in cameras_filtered if row_number == str(camera['row_number'])]
    cameras_filtered = cameras_filtered if cameras_filtered else cameras

    print_cameras(cameras_filtered)


def print_cameras(cameras):
    for camera in cameras:
        print(
            '{} | {} | {} | {}'.format(camera['row_number'], camera['Camera'], camera['Latitude'], camera['Longitude']))


if __name__ == '__main__':
    get_cameras_by_name()
