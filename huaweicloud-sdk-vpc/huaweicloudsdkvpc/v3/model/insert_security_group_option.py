# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertSecurityGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_groups': 'list[str]',
        'index': 'int'
    }

    attribute_map = {
        'security_groups': 'security_groups',
        'index': 'index'
    }

    def __init__(self, security_groups=None, index=None):
        """InsertSecurityGroupOption

        The model defined in huaweicloud sdk

        :param security_groups: 功能说明：安全组的ID列表；例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;]
        :type security_groups: list[str]
        :param index: 安全组插入的位置，从0开始计数。 举例： 1. 要插入到已关联安全组列表的首位，index&#x3D;0； 2. 要插入到已关联安全组列表的第n个安全组后面，index&#x3D;n。 默认插入到端口已关联的安全组列表末尾。
        :type index: int
        """
        
        

        self._security_groups = None
        self._index = None
        self.discriminator = None

        self.security_groups = security_groups
        if index is not None:
            self.index = index

    @property
    def security_groups(self):
        """Gets the security_groups of this InsertSecurityGroupOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]

        :return: The security_groups of this InsertSecurityGroupOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this InsertSecurityGroupOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]

        :param security_groups: The security_groups of this InsertSecurityGroupOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def index(self):
        """Gets the index of this InsertSecurityGroupOption.

        安全组插入的位置，从0开始计数。 举例： 1. 要插入到已关联安全组列表的首位，index=0； 2. 要插入到已关联安全组列表的第n个安全组后面，index=n。 默认插入到端口已关联的安全组列表末尾。

        :return: The index of this InsertSecurityGroupOption.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InsertSecurityGroupOption.

        安全组插入的位置，从0开始计数。 举例： 1. 要插入到已关联安全组列表的首位，index=0； 2. 要插入到已关联安全组列表的第n个安全组后面，index=n。 默认插入到端口已关联的安全组列表末尾。

        :param index: The index of this InsertSecurityGroupOption.
        :type index: int
        """
        self._index = index

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
        if not isinstance(other, InsertSecurityGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
