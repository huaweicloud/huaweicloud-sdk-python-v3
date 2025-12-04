# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListThreatsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recent': 'str',
        'hosts': 'list[str]'
    }

    attribute_map = {
        'recent': 'recent',
        'hosts': 'hosts'
    }

    def __init__(self, recent=None, hosts=None):
        r"""ListThreatsRequest

        The model defined in huaweicloud sdk

        :param recent: **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及
        :type recent: str
        :param hosts: 要查询事件的域名列表
        :type hosts: list[str]
        """
        
        

        self._recent = None
        self._hosts = None
        self.discriminator = None

        self.recent = recent
        if hosts is not None:
            self.hosts = hosts

    @property
    def recent(self):
        r"""Gets the recent of this ListThreatsRequest.

        **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及

        :return: The recent of this ListThreatsRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this ListThreatsRequest.

        **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及

        :param recent: The recent of this ListThreatsRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def hosts(self):
        r"""Gets the hosts of this ListThreatsRequest.

        要查询事件的域名列表

        :return: The hosts of this ListThreatsRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListThreatsRequest.

        要查询事件的域名列表

        :param hosts: The hosts of this ListThreatsRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

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
        if not isinstance(other, ListThreatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
