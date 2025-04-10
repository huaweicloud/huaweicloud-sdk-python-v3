# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnTopics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'name': 'str',
        'push_policy': 'int',
        'status': 'int',
        'topic_urn': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'name': 'name',
        'push_policy': 'push_policy',
        'status': 'status',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, display_name=None, name=None, push_policy=None, status=None, topic_urn=None):
        r"""SmnTopics

        The model defined in huaweicloud sdk

        :param display_name: Topic的显示名，推送邮件消息时，作为邮件发件人显示。显示名的长度为192byte或64个中文。默认值为空。
        :type display_name: str
        :param name: 创建topic的名字。Topic名称只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度为1到255个字符。
        :type name: str
        :param push_policy: SMN消息推送策略。取值为0或1
        :type push_policy: int
        :param status: topic中订阅者的状态。0:主题已删除或主题下订阅列表为空。1:主题下的订阅列表存在状态为“已订阅”的订阅信息。2:主题下的订阅信息状态处于“未订阅”或“已取消”。
        :type status: int
        :param topic_urn: Topic的唯一的资源标识。
        :type topic_urn: str
        """
        
        

        self._display_name = None
        self._name = None
        self._push_policy = None
        self._status = None
        self._topic_urn = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        self.name = name
        self.push_policy = push_policy
        if status is not None:
            self.status = status
        self.topic_urn = topic_urn

    @property
    def display_name(self):
        r"""Gets the display_name of this SmnTopics.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。显示名的长度为192byte或64个中文。默认值为空。

        :return: The display_name of this SmnTopics.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SmnTopics.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。显示名的长度为192byte或64个中文。默认值为空。

        :param display_name: The display_name of this SmnTopics.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def name(self):
        r"""Gets the name of this SmnTopics.

        创建topic的名字。Topic名称只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度为1到255个字符。

        :return: The name of this SmnTopics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SmnTopics.

        创建topic的名字。Topic名称只能包含大写字母、小写字母、数字、-和_，且必须由大写字母、小写字母或数字开头，长度为1到255个字符。

        :param name: The name of this SmnTopics.
        :type name: str
        """
        self._name = name

    @property
    def push_policy(self):
        r"""Gets the push_policy of this SmnTopics.

        SMN消息推送策略。取值为0或1

        :return: The push_policy of this SmnTopics.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        r"""Sets the push_policy of this SmnTopics.

        SMN消息推送策略。取值为0或1

        :param push_policy: The push_policy of this SmnTopics.
        :type push_policy: int
        """
        self._push_policy = push_policy

    @property
    def status(self):
        r"""Gets the status of this SmnTopics.

        topic中订阅者的状态。0:主题已删除或主题下订阅列表为空。1:主题下的订阅列表存在状态为“已订阅”的订阅信息。2:主题下的订阅信息状态处于“未订阅”或“已取消”。

        :return: The status of this SmnTopics.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SmnTopics.

        topic中订阅者的状态。0:主题已删除或主题下订阅列表为空。1:主题下的订阅列表存在状态为“已订阅”的订阅信息。2:主题下的订阅信息状态处于“未订阅”或“已取消”。

        :param status: The status of this SmnTopics.
        :type status: int
        """
        self._status = status

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this SmnTopics.

        Topic的唯一的资源标识。

        :return: The topic_urn of this SmnTopics.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this SmnTopics.

        Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this SmnTopics.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmnTopics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
