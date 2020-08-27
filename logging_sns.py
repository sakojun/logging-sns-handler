import logging
import logging.handlers
import boto3
import os

sns_topic = os.environ["sns_topic"]


class SNSHandler(logging.Handler):
    # TODO: topic,subjectをどこで設定するのが良いか
    def __init__(self, topic=sns_topic, subject="test"):
        logging.Handler.__init__(self)

        self.sns_topic = boto3.resource('sns').Topic(topic)
        self.subject = subject

    def emit(self, record):
        self.sns_topic.publish(Message=record.msg, Subject=self.subject)


if __name__ == '__main__':
    logger = logging.getLogger('myapp')
    logger.addHandler(SNSHandler())
    logger.setLevel(logging.ERROR)
    logger.error("AAA")
    logger.info("BBB")

