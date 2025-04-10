# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateSnatOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transit_ip_ids': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'transit_ip_ids': 'transit_ip_ids',
        'description': 'description'
    }

    def __init__(self, transit_ip_ids=None, description=None):
        r"""UpdatePrivateSnatOption

        The model defined in huaweicloud sdk

        :param transit_ip_ids: 中转IP的ID的列表。
        :type transit_ip_ids: list[str]
        :param description: SNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        """
        
        

        self._transit_ip_ids = None
        self._description = None
        self.discriminator = None

        if transit_ip_ids is not None:
            self.transit_ip_ids = transit_ip_ids
        if description is not None:
            self.description = description

    @property
    def transit_ip_ids(self):
        r"""Gets the transit_ip_ids of this UpdatePrivateSnatOption.

        中转IP的ID的列表。

        :return: The transit_ip_ids of this UpdatePrivateSnatOption.
        :rtype: list[str]
        """
        return self._transit_ip_ids

    @transit_ip_ids.setter
    def transit_ip_ids(self, transit_ip_ids):
        r"""Sets the transit_ip_ids of this UpdatePrivateSnatOption.

        中转IP的ID的列表。

        :param transit_ip_ids: The transit_ip_ids of this UpdatePrivateSnatOption.
        :type transit_ip_ids: list[str]
        """
        self._transit_ip_ids = transit_ip_ids

    @property
    def description(self):
        r"""Gets the description of this UpdatePrivateSnatOption.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this UpdatePrivateSnatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePrivateSnatOption.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this UpdatePrivateSnatOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdatePrivateSnatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
