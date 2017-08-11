import os
import json
import facebook

if __name__ == '__main__':
    token='EAAGzloQVBVcBAHvKau5NSaVLhBhYo70acmpiz9fP3mUDPZACCT8PGWTKL9GdUojNEZArctNSZBkHClKlZBHHE8URGeaBHgTsMdzj6ZCmxehVdjyc1QlSo8tTkISUhEZAowfSfNtlVHckRNvtAzkWZBFasijYkLcfEwZD'

    graph=facebook.GraphAPI(token)
    profile=graph.get_object('100000425733994',fields='name,location')

    print(json.dumps(profile,indent=4))