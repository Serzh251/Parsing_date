BOT_NAME = 'superjob'

SPIDER_MODULES = ['superjob.spiders']
NEWSPIDER_MODULE = 'superjob.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

ITEM_PIPELINES = {
   'superjob.pipelines.SuperjobPipeline': 1,
   'superjob.pipelines.LeroyPhotosPipeline': 2,
   'superjob.pipelines.DataBasePipeline': 3,
   'superjob.pipelines.CSVPipeline': 4,
}
FILES_STORE = r'downloaded'

DOWNLOAD_DELAY = 2

