# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIpGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'ip_list': 'list[UpdateIpGroupIpOption]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'ip_list': 'ip_list'
    }

    def __init__(self, description=None, name=None, ip_list=None):
        r"""UpdateIpGroupOption

        The model defined in huaweicloud sdk

        :param description: **参数解释**：IP地址组的描述信息。  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及
        :type description: str
        :param name: **参数解释**：IP地址组的名称  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及
        :type name: str
        :param ip_list: **参数解释**：IP地址组的IP列表。 注意：只支持全量更新，即IP地址组中的ip_list将被全量覆盖，不在请求参数中的IP地址将被移除。  **约束限制**：不涉及
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.UpdateIpGroupIpOption`]
        """
        
        

        self._description = None
        self._name = None
        self._ip_list = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def description(self):
        r"""Gets the description of this UpdateIpGroupOption.

        **参数解释**：IP地址组的描述信息。  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及

        :return: The description of this UpdateIpGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateIpGroupOption.

        **参数解释**：IP地址组的描述信息。  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及

        :param description: The description of this UpdateIpGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateIpGroupOption.

        **参数解释**：IP地址组的名称  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及

        :return: The name of this UpdateIpGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateIpGroupOption.

        **参数解释**：IP地址组的名称  **约束限制**：不涉及  **取值范围**：长度为0-255个字符。  **默认取值**：不涉及

        :param name: The name of this UpdateIpGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def ip_list(self):
        r"""Gets the ip_list of this UpdateIpGroupOption.

        **参数解释**：IP地址组的IP列表。 注意：只支持全量更新，即IP地址组中的ip_list将被全量覆盖，不在请求参数中的IP地址将被移除。  **约束限制**：不涉及

        :return: The ip_list of this UpdateIpGroupOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.UpdateIpGroupIpOption`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this UpdateIpGroupOption.

        **参数解释**：IP地址组的IP列表。 注意：只支持全量更新，即IP地址组中的ip_list将被全量覆盖，不在请求参数中的IP地址将被移除。  **约束限制**：不涉及

        :param ip_list: The ip_list of this UpdateIpGroupOption.
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.UpdateIpGroupIpOption`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, UpdateIpGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
