# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmailRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'send_at': 'int',
        'send_status': 'int',
        'email': 'str',
        'topic': 'str',
        'topic_urn': 'str',
        'instance_health_report_list': 'list[InstanceHealthReport]'
    }

    attribute_map = {
        'send_at': 'send_at',
        'send_status': 'send_status',
        'email': 'email',
        'topic': 'topic',
        'topic_urn': 'topic_urn',
        'instance_health_report_list': 'instance_health_report_list'
    }

    def __init__(self, send_at=None, send_status=None, email=None, topic=None, topic_urn=None, instance_health_report_list=None):
        r"""EmailRecord

        The model defined in huaweicloud sdk

        :param send_at: 发送时间（Unix timestamp），单位：毫秒。
        :type send_at: int
        :param send_status: 发送状态
        :type send_status: int
        :param email: 邮箱地址
        :type email: str
        :param topic: 主题名称
        :type topic: str
        :param topic_urn: 主题标识符
        :type topic_urn: str
        :param instance_health_report_list: 实例诊断报告列表
        :type instance_health_report_list: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReport`]
        """
        
        

        self._send_at = None
        self._send_status = None
        self._email = None
        self._topic = None
        self._topic_urn = None
        self._instance_health_report_list = None
        self.discriminator = None

        self.send_at = send_at
        self.send_status = send_status
        self.email = email
        self.topic = topic
        self.topic_urn = topic_urn
        self.instance_health_report_list = instance_health_report_list

    @property
    def send_at(self):
        r"""Gets the send_at of this EmailRecord.

        发送时间（Unix timestamp），单位：毫秒。

        :return: The send_at of this EmailRecord.
        :rtype: int
        """
        return self._send_at

    @send_at.setter
    def send_at(self, send_at):
        r"""Sets the send_at of this EmailRecord.

        发送时间（Unix timestamp），单位：毫秒。

        :param send_at: The send_at of this EmailRecord.
        :type send_at: int
        """
        self._send_at = send_at

    @property
    def send_status(self):
        r"""Gets the send_status of this EmailRecord.

        发送状态

        :return: The send_status of this EmailRecord.
        :rtype: int
        """
        return self._send_status

    @send_status.setter
    def send_status(self, send_status):
        r"""Sets the send_status of this EmailRecord.

        发送状态

        :param send_status: The send_status of this EmailRecord.
        :type send_status: int
        """
        self._send_status = send_status

    @property
    def email(self):
        r"""Gets the email of this EmailRecord.

        邮箱地址

        :return: The email of this EmailRecord.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this EmailRecord.

        邮箱地址

        :param email: The email of this EmailRecord.
        :type email: str
        """
        self._email = email

    @property
    def topic(self):
        r"""Gets the topic of this EmailRecord.

        主题名称

        :return: The topic of this EmailRecord.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this EmailRecord.

        主题名称

        :param topic: The topic of this EmailRecord.
        :type topic: str
        """
        self._topic = topic

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this EmailRecord.

        主题标识符

        :return: The topic_urn of this EmailRecord.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this EmailRecord.

        主题标识符

        :param topic_urn: The topic_urn of this EmailRecord.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def instance_health_report_list(self):
        r"""Gets the instance_health_report_list of this EmailRecord.

        实例诊断报告列表

        :return: The instance_health_report_list of this EmailRecord.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReport`]
        """
        return self._instance_health_report_list

    @instance_health_report_list.setter
    def instance_health_report_list(self, instance_health_report_list):
        r"""Sets the instance_health_report_list of this EmailRecord.

        实例诊断报告列表

        :param instance_health_report_list: The instance_health_report_list of this EmailRecord.
        :type instance_health_report_list: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReport`]
        """
        self._instance_health_report_list = instance_health_report_list

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
        if not isinstance(other, EmailRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
