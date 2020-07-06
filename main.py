import boto3
import argparse
import sys

# Let's use Amazon S3
s3 = boto3.resource('s3')

region = 'us-west-1'

parser = argparse.ArgumentParser(
    description="Lists url for aws buckets given filter")


def cli(args=sys.argv[1:]):
    parser.add_argument("-f",
                        "--filter",
                        help="filter files by substring ex) ",
                        default='',
                        dest="filter")
    options = parser.parse_args(args)
    return options


def main():
    options = cli()
    substring = options.filter
    for bucket in s3.buckets.all():
        print(f'\nBucket: {bucket.name}')
        for obj in bucket.objects.all():
            url = f'https://{bucket.name}.s3-{region}.amazonaws.com/{obj.key}'
            if substring == '':
                print(url)
            elif substring in obj.key:
                print(url)

main()
