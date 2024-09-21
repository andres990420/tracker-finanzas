import logging as log

log.basicConfig(level=log.DEBUG,format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
        datefmt='%I:%M:%S %p',
        handlers=[
            log.FileHandler('../log/user_data.log'),
            log.StreamHandler()
        ]
        )




if __name__ == "__main__":
    pass