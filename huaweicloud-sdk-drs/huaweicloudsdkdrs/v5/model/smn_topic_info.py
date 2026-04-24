# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnTopicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'urn': 'str',
        'description': 'str',
        'push_policy': 'str'
    }

    attribute_map = {
        'name': 'name',
        'urn': 'urn',
        'description': 'description',
        'push_policy': 'push_policy'
    }

    def __init__(self, name=None, urn=None, description=None, push_policy=None):
        r"""SmnTopicInfo

        The model defined in huaweicloud sdk

        :param name: Topic的名字。
        :type name: str
        :param urn: Topic的唯一的资源标识。
        :type urn: str
        :param description: Topic的描述信息。
        :type description: str
        :param push_policy: 消息推送的策略，取值： - RETRY_ON_FAILURE：发送失败，保留到失败队列。 - DROP_ON_FAILURE：直接丢弃发送失败的消息。
        :type push_policy: str
        """
        
        

        self._name = None
        self._urn = None
        self._description = None
        self._push_policy = None
        self.discriminator = None

        self.name = name
        self.urn = urn
        if description is not None:
            self.description = description
        self.push_policy = push_policy

    @property
    def name(self):
        r"""Gets the name of this SmnTopicInfo.

        Topic的名字。

        :return: The name of this SmnTopicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SmnTopicInfo.

        Topic的名字。

        :param name: The name of this SmnTopicInfo.
        :type name: str
        """
        self._name = name

    @property
    def urn(self):
        r"""Gets the urn of this SmnTopicInfo.

        Topic的唯一的资源标识。

        :return: The urn of this SmnTopicInfo.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this SmnTopicInfo.

        Topic的唯一的资源标识。

        :param urn: The urn of this SmnTopicInfo.
        :type urn: str
        """
        self._urn = urn

    @property
    def description(self):
        r"""Gets the description of this SmnTopicInfo.

        Topic的描述信息。

        :return: The description of this SmnTopicInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SmnTopicInfo.

        Topic的描述信息。

        :param description: The description of this SmnTopicInfo.
        :type description: str
        """
        self._description = description

    @property
    def push_policy(self):
        r"""Gets the push_policy of this SmnTopicInfo.

        消息推送的策略，取值： - RETRY_ON_FAILURE：发送失败，保留到失败队列。 - DROP_ON_FAILURE：直接丢弃发送失败的消息。

        :return: The push_policy of this SmnTopicInfo.
        :rtype: str
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        r"""Sets the push_policy of this SmnTopicInfo.

        消息推送的策略，取值： - RETRY_ON_FAILURE：发送失败，保留到失败队列。 - DROP_ON_FAILURE：直接丢弃发送失败的消息。

        :param push_policy: The push_policy of this SmnTopicInfo.
        :type push_policy: str
        """
        self._push_policy = push_policy

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
        if not isinstance(other, SmnTopicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
