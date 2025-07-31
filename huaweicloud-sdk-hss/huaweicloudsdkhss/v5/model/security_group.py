# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str',
        'security_group_name': 'str',
        'security_group_description': 'str'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'security_group_description': 'security_group_description'
    }

    def __init__(self, security_group_id=None, security_group_name=None, security_group_description=None):
        r"""SecurityGroup

        The model defined in huaweicloud sdk

        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param security_group_name: 安全组名称
        :type security_group_name: str
        :param security_group_description: 安全组描述
        :type security_group_description: str
        """
        
        

        self._security_group_id = None
        self._security_group_name = None
        self._security_group_description = None
        self.discriminator = None

        self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if security_group_description is not None:
            self.security_group_description = security_group_description

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this SecurityGroup.

        安全组ID

        :return: The security_group_id of this SecurityGroup.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this SecurityGroup.

        安全组ID

        :param security_group_id: The security_group_id of this SecurityGroup.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        r"""Gets the security_group_name of this SecurityGroup.

        安全组名称

        :return: The security_group_name of this SecurityGroup.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        r"""Sets the security_group_name of this SecurityGroup.

        安全组名称

        :param security_group_name: The security_group_name of this SecurityGroup.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def security_group_description(self):
        r"""Gets the security_group_description of this SecurityGroup.

        安全组描述

        :return: The security_group_description of this SecurityGroup.
        :rtype: str
        """
        return self._security_group_description

    @security_group_description.setter
    def security_group_description(self, security_group_description):
        r"""Sets the security_group_description of this SecurityGroup.

        安全组描述

        :param security_group_description: The security_group_description of this SecurityGroup.
        :type security_group_description: str
        """
        self._security_group_description = security_group_description

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
        if not isinstance(other, SecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
