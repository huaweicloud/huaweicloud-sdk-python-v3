# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeInstanceReportNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'endpoint': 'str',
        'topic': 'str',
        'topic_urn': 'str',
        'bucket_name': 'str',
        'level': 'str',
        'service_uri': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'topic': 'topic',
        'topic_urn': 'topic_urn',
        'bucket_name': 'bucket_name',
        'level': 'level',
        'service_uri': 'service_uri'
    }

    def __init__(self, protocol=None, endpoint=None, topic=None, topic_urn=None, bucket_name=None, level=None, service_uri=None):
        r"""SubscribeInstanceReportNewRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 协议
        :type protocol: str
        :param endpoint: 地址
        :type endpoint: str
        :param topic: 主题
        :type topic: str
        :param topic_urn: 主题地址
        :type topic_urn: str
        :param bucket_name: 桶名
        :type bucket_name: str
        :param level: 风险等级
        :type level: str
        :param service_uri: 服务URI
        :type service_uri: str
        """
        
        

        self._protocol = None
        self._endpoint = None
        self._topic = None
        self._topic_urn = None
        self._bucket_name = None
        self._level = None
        self._service_uri = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint
        self.topic = topic
        self.topic_urn = topic_urn
        if bucket_name is not None:
            self.bucket_name = bucket_name
        self.level = level
        self.service_uri = service_uri

    @property
    def protocol(self):
        r"""Gets the protocol of this SubscribeInstanceReportNewRequestBody.

        协议

        :return: The protocol of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SubscribeInstanceReportNewRequestBody.

        协议

        :param protocol: The protocol of this SubscribeInstanceReportNewRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        r"""Gets the endpoint of this SubscribeInstanceReportNewRequestBody.

        地址

        :return: The endpoint of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this SubscribeInstanceReportNewRequestBody.

        地址

        :param endpoint: The endpoint of this SubscribeInstanceReportNewRequestBody.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def topic(self):
        r"""Gets the topic of this SubscribeInstanceReportNewRequestBody.

        主题

        :return: The topic of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SubscribeInstanceReportNewRequestBody.

        主题

        :param topic: The topic of this SubscribeInstanceReportNewRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SubscribeInstanceReportNewRequestBody.

        主题地址

        :return: The topic_urn of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SubscribeInstanceReportNewRequestBody.

        主题地址

        :param topic_urn: The topic_urn of this SubscribeInstanceReportNewRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SubscribeInstanceReportNewRequestBody.

        桶名

        :return: The bucket_name of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SubscribeInstanceReportNewRequestBody.

        桶名

        :param bucket_name: The bucket_name of this SubscribeInstanceReportNewRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def level(self):
        r"""Gets the level of this SubscribeInstanceReportNewRequestBody.

        风险等级

        :return: The level of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this SubscribeInstanceReportNewRequestBody.

        风险等级

        :param level: The level of this SubscribeInstanceReportNewRequestBody.
        :type level: str
        """
        self._level = level

    @property
    def service_uri(self):
        r"""Gets the service_uri of this SubscribeInstanceReportNewRequestBody.

        服务URI

        :return: The service_uri of this SubscribeInstanceReportNewRequestBody.
        :rtype: str
        """
        return self._service_uri

    @service_uri.setter
    def service_uri(self, service_uri):
        r"""Sets the service_uri of this SubscribeInstanceReportNewRequestBody.

        服务URI

        :param service_uri: The service_uri of this SubscribeInstanceReportNewRequestBody.
        :type service_uri: str
        """
        self._service_uri = service_uri

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscribeInstanceReportNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
