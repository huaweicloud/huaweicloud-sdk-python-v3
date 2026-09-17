# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportSubscription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscribe_id': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'endpoint': 'str',
        'topic': 'str',
        'topic_urn': 'str',
        'obs_bucket_name': 'str',
        'level': 'str',
        'locale': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'subscribe_id': 'subscribe_id',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'topic': 'topic',
        'topic_urn': 'topic_urn',
        'obs_bucket_name': 'obs_bucket_name',
        'level': 'level',
        'locale': 'locale',
        'extra': 'extra'
    }

    def __init__(self, subscribe_id=None, instance_id=None, project_id=None, protocol=None, endpoint=None, topic=None, topic_urn=None, obs_bucket_name=None, level=None, locale=None, extra=None):
        r"""ReportSubscription

        The model defined in huaweicloud sdk

        :param subscribe_id: 订阅ID
        :type subscribe_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param project_id: 租户在某一Region下的项目ID
        :type project_id: str
        :param protocol: 协议
        :type protocol: str
        :param endpoint: 地址
        :type endpoint: str
        :param topic: 主题
        :type topic: str
        :param topic_urn: 主题地址
        :type topic_urn: str
        :param obs_bucket_name: 桶名
        :type obs_bucket_name: str
        :param level: 风险等级
        :type level: str
        :param locale: 语言
        :type locale: str
        :param extra: 额外信息
        :type extra: object
        """
        
        

        self._subscribe_id = None
        self._instance_id = None
        self._project_id = None
        self._protocol = None
        self._endpoint = None
        self._topic = None
        self._topic_urn = None
        self._obs_bucket_name = None
        self._level = None
        self._locale = None
        self._extra = None
        self.discriminator = None

        if subscribe_id is not None:
            self.subscribe_id = subscribe_id
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if protocol is not None:
            self.protocol = protocol
        if endpoint is not None:
            self.endpoint = endpoint
        if topic is not None:
            self.topic = topic
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if level is not None:
            self.level = level
        if locale is not None:
            self.locale = locale
        if extra is not None:
            self.extra = extra

    @property
    def subscribe_id(self):
        r"""Gets the subscribe_id of this ReportSubscription.

        订阅ID

        :return: The subscribe_id of this ReportSubscription.
        :rtype: str
        """
        return self._subscribe_id

    @subscribe_id.setter
    def subscribe_id(self, subscribe_id):
        r"""Sets the subscribe_id of this ReportSubscription.

        订阅ID

        :param subscribe_id: The subscribe_id of this ReportSubscription.
        :type subscribe_id: str
        """
        self._subscribe_id = subscribe_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ReportSubscription.

        实例ID

        :return: The instance_id of this ReportSubscription.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ReportSubscription.

        实例ID

        :param instance_id: The instance_id of this ReportSubscription.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ReportSubscription.

        租户在某一Region下的项目ID

        :return: The project_id of this ReportSubscription.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ReportSubscription.

        租户在某一Region下的项目ID

        :param project_id: The project_id of this ReportSubscription.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        r"""Gets the protocol of this ReportSubscription.

        协议

        :return: The protocol of this ReportSubscription.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ReportSubscription.

        协议

        :param protocol: The protocol of this ReportSubscription.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ReportSubscription.

        地址

        :return: The endpoint of this ReportSubscription.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ReportSubscription.

        地址

        :param endpoint: The endpoint of this ReportSubscription.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def topic(self):
        r"""Gets the topic of this ReportSubscription.

        主题

        :return: The topic of this ReportSubscription.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ReportSubscription.

        主题

        :param topic: The topic of this ReportSubscription.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ReportSubscription.

        主题地址

        :return: The topic_urn of this ReportSubscription.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ReportSubscription.

        主题地址

        :param topic_urn: The topic_urn of this ReportSubscription.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ReportSubscription.

        桶名

        :return: The obs_bucket_name of this ReportSubscription.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ReportSubscription.

        桶名

        :param obs_bucket_name: The obs_bucket_name of this ReportSubscription.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def level(self):
        r"""Gets the level of this ReportSubscription.

        风险等级

        :return: The level of this ReportSubscription.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ReportSubscription.

        风险等级

        :param level: The level of this ReportSubscription.
        :type level: str
        """
        self._level = level

    @property
    def locale(self):
        r"""Gets the locale of this ReportSubscription.

        语言

        :return: The locale of this ReportSubscription.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ReportSubscription.

        语言

        :param locale: The locale of this ReportSubscription.
        :type locale: str
        """
        self._locale = locale

    @property
    def extra(self):
        r"""Gets the extra of this ReportSubscription.

        额外信息

        :return: The extra of this ReportSubscription.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        r"""Sets the extra of this ReportSubscription.

        额外信息

        :param extra: The extra of this ReportSubscription.
        :type extra: object
        """
        self._extra = extra

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
        if not isinstance(other, ReportSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
