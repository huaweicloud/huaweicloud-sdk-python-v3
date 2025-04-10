# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBacklogPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'description': 'str',
        'backlog_size': 'int',
        'backlog_time': 'int'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'description': 'description',
        'backlog_size': 'backlog_size',
        'backlog_time': 'backlog_time'
    }

    def __init__(self, policy_name=None, description=None, backlog_size=None, backlog_time=None):
        r"""AddBacklogPolicy

        The model defined in huaweicloud sdk

        :param policy_name: **参数说明**：数据流转积压策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type policy_name: str
        :param description: **参数说明**：用户自定义的数据流转积压策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type description: str
        :param backlog_size: **参数说明**：数据积压大小。单位为B（字节），取值范围为0~1073741823的整数，默认为1073741823（即1GB）。当backlog_size为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。
        :type backlog_size: int
        :param backlog_time: **参数说明**：数据积压时间。单位为s（秒），取值范围为0~86399的整数，默认为86399（即1天）。当backlog_time为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。
        :type backlog_time: int
        """
        
        

        self._policy_name = None
        self._description = None
        self._backlog_size = None
        self._backlog_time = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if description is not None:
            self.description = description
        if backlog_size is not None:
            self.backlog_size = backlog_size
        if backlog_time is not None:
            self.backlog_time = backlog_time

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AddBacklogPolicy.

        **参数说明**：数据流转积压策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The policy_name of this AddBacklogPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AddBacklogPolicy.

        **参数说明**：数据流转积压策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param policy_name: The policy_name of this AddBacklogPolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def description(self):
        r"""Gets the description of this AddBacklogPolicy.

        **参数说明**：用户自定义的数据流转积压策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The description of this AddBacklogPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddBacklogPolicy.

        **参数说明**：用户自定义的数据流转积压策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param description: The description of this AddBacklogPolicy.
        :type description: str
        """
        self._description = description

    @property
    def backlog_size(self):
        r"""Gets the backlog_size of this AddBacklogPolicy.

        **参数说明**：数据积压大小。单位为B（字节），取值范围为0~1073741823的整数，默认为1073741823（即1GB）。当backlog_size为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。

        :return: The backlog_size of this AddBacklogPolicy.
        :rtype: int
        """
        return self._backlog_size

    @backlog_size.setter
    def backlog_size(self, backlog_size):
        r"""Sets the backlog_size of this AddBacklogPolicy.

        **参数说明**：数据积压大小。单位为B（字节），取值范围为0~1073741823的整数，默认为1073741823（即1GB）。当backlog_size为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。

        :param backlog_size: The backlog_size of this AddBacklogPolicy.
        :type backlog_size: int
        """
        self._backlog_size = backlog_size

    @property
    def backlog_time(self):
        r"""Gets the backlog_time of this AddBacklogPolicy.

        **参数说明**：数据积压时间。单位为s（秒），取值范围为0~86399的整数，默认为86399（即1天）。当backlog_time为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。

        :return: The backlog_time of this AddBacklogPolicy.
        :rtype: int
        """
        return self._backlog_time

    @backlog_time.setter
    def backlog_time(self, backlog_time):
        r"""Sets the backlog_time of this AddBacklogPolicy.

        **参数说明**：数据积压时间。单位为s（秒），取值范围为0~86399的整数，默认为86399（即1天）。当backlog_time为0时，表示不积压。若同时配置了backlog_size和backlog_time两个维度，则以最先达到阈值的维度为准。

        :param backlog_time: The backlog_time of this AddBacklogPolicy.
        :type backlog_time: int
        """
        self._backlog_time = backlog_time

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
        if not isinstance(other, AddBacklogPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
