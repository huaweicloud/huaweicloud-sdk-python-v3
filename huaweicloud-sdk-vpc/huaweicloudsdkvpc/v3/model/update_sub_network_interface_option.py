# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubNetworkInterfaceOption:

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
        'security_groups': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'security_groups': 'security_groups'
    }

    def __init__(self, description=None, security_groups=None):
        """UpdateSubNetworkInterfaceOption

        The model defined in huaweicloud sdk

        :param description: 功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param security_groups: 功能说明：安全组的ID列表；例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;]
        :type security_groups: list[str]
        """
        
        

        self._description = None
        self._security_groups = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def description(self):
        """Gets the description of this UpdateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this UpdateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this UpdateSubNetworkInterfaceOption.
        :type description: str
        """
        self._description = description

    @property
    def security_groups(self):
        """Gets the security_groups of this UpdateSubNetworkInterfaceOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]

        :return: The security_groups of this UpdateSubNetworkInterfaceOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this UpdateSubNetworkInterfaceOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]

        :param security_groups: The security_groups of this UpdateSubNetworkInterfaceOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, UpdateSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
