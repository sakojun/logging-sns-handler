import logging
import boto3
import os

sns_topic = os.environ["sns_topic_arn"]


class SNSHandler(logging.Handler):
    def __init__(self, topic_arn, subject):
        logging.Handler.__init__(self)

        self.sns_topic = boto3.resource('sns').Topic(topic_arn)
        self.subject = subject

    def emit(self, record):
        self.sns_topic.publish(Message=record.msg, Subject=self.subject)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    sns_hdl = SNSHandler(sns_topic, "test")
    sns_hdl.setLevel(logging.ERROR)
    logger.addHandler(sns_hdl)

    std_hdl = logging.StreamHandler()
    std_hdl.setLevel(logging.INFO)
    logger.addHandler(std_hdl)

    logger.error("AAA")
    logger.info("BBB")
