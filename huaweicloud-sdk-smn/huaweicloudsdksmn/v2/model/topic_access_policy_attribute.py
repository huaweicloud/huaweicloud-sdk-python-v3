# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicAccessPolicyAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_policy': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'access_policy': 'access_policy',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, access_policy=None, create_time=None, update_time=None):
        r"""TopicAccessPolicyAttribute

        The model defined in huaweicloud sdk

        :param access_policy: topic的访问策略
        :type access_policy: str
        :param create_time: topic的访问策略创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param update_time: topic的访问策略更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        """
        
        

        self._access_policy = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if access_policy is not None:
            self.access_policy = access_policy
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def access_policy(self):
        r"""Gets the access_policy of this TopicAccessPolicyAttribute.

        topic的访问策略

        :return: The access_policy of this TopicAccessPolicyAttribute.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this TopicAccessPolicyAttribute.

        topic的访问策略

        :param access_policy: The access_policy of this TopicAccessPolicyAttribute.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def create_time(self):
        r"""Gets the create_time of this TopicAccessPolicyAttribute.

        topic的访问策略创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this TopicAccessPolicyAttribute.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TopicAccessPolicyAttribute.

        topic的访问策略创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this TopicAccessPolicyAttribute.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TopicAccessPolicyAttribute.

        topic的访问策略更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this TopicAccessPolicyAttribute.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TopicAccessPolicyAttribute.

        topic的访问策略更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this TopicAccessPolicyAttribute.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, TopicAccessPolicyAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
