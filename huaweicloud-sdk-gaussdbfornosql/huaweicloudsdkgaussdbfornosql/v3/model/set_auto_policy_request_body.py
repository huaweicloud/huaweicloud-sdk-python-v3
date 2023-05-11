# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAutoPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'switch_option': 'str',
        'policy': 'list[DiskAutoExpansionPolicy]'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'switch_option': 'switch_option',
        'policy': 'policy'
    }

    def __init__(self, instance_ids=None, switch_option=None, policy=None):
        """SetAutoPolicyRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 设置磁盘自动扩容的实例组ID。
        :type instance_ids: list[str]
        :param switch_option: 自动扩容开关。  “on”，表示开启磁盘自动扩容策略。  “off”，表示关闭磁盘自动扩容策略。 默认值为“on”。
        :type switch_option: str
        :param policy: 磁盘自动扩容策略
        :type policy: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DiskAutoExpansionPolicy`]
        """
        
        

        self._instance_ids = None
        self._switch_option = None
        self._policy = None
        self.discriminator = None

        self.instance_ids = instance_ids
        if switch_option is not None:
            self.switch_option = switch_option
        if policy is not None:
            self.policy = policy

    @property
    def instance_ids(self):
        """Gets the instance_ids of this SetAutoPolicyRequestBody.

        设置磁盘自动扩容的实例组ID。

        :return: The instance_ids of this SetAutoPolicyRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this SetAutoPolicyRequestBody.

        设置磁盘自动扩容的实例组ID。

        :param instance_ids: The instance_ids of this SetAutoPolicyRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def switch_option(self):
        """Gets the switch_option of this SetAutoPolicyRequestBody.

        自动扩容开关。  “on”，表示开启磁盘自动扩容策略。  “off”，表示关闭磁盘自动扩容策略。 默认值为“on”。

        :return: The switch_option of this SetAutoPolicyRequestBody.
        :rtype: str
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        """Sets the switch_option of this SetAutoPolicyRequestBody.

        自动扩容开关。  “on”，表示开启磁盘自动扩容策略。  “off”，表示关闭磁盘自动扩容策略。 默认值为“on”。

        :param switch_option: The switch_option of this SetAutoPolicyRequestBody.
        :type switch_option: str
        """
        self._switch_option = switch_option

    @property
    def policy(self):
        """Gets the policy of this SetAutoPolicyRequestBody.

        磁盘自动扩容策略

        :return: The policy of this SetAutoPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DiskAutoExpansionPolicy`]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this SetAutoPolicyRequestBody.

        磁盘自动扩容策略

        :param policy: The policy of this SetAutoPolicyRequestBody.
        :type policy: list[:class:`huaweicloudsdkgaussdbfornosql.v3.DiskAutoExpansionPolicy`]
        """
        self._policy = policy

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
        if not isinstance(other, SetAutoPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
