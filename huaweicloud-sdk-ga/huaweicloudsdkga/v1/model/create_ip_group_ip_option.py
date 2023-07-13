# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpGroupIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr': 'str',
        'description': 'str'
    }

    attribute_map = {
        'cidr': 'cidr',
        'description': 'description'
    }

    def __init__(self, cidr=None, description=None):
        """CreateIpGroupIpOption

        The model defined in huaweicloud sdk

        :param cidr: IP地址组中的IP网段，cidr格式。
        :type cidr: str
        :param description: IP地址组中的IP网段描述，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        """
        
        

        self._cidr = None
        self._description = None
        self.discriminator = None

        self.cidr = cidr
        if description is not None:
            self.description = description

    @property
    def cidr(self):
        """Gets the cidr of this CreateIpGroupIpOption.

        IP地址组中的IP网段，cidr格式。

        :return: The cidr of this CreateIpGroupIpOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateIpGroupIpOption.

        IP地址组中的IP网段，cidr格式。

        :param cidr: The cidr of this CreateIpGroupIpOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this CreateIpGroupIpOption.

        IP地址组中的IP网段描述，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this CreateIpGroupIpOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIpGroupIpOption.

        IP地址组中的IP网段描述，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this CreateIpGroupIpOption.
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
        if not isinstance(other, CreateIpGroupIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
