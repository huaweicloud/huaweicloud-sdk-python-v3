# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntityPrivilegeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'privileges': 'list[str]',
        'inherit_privileges': 'list[str]'
    }

    attribute_map = {
        'privileges': 'privileges',
        'inherit_privileges': 'inherit_privileges'
    }

    def __init__(self, privileges=None, inherit_privileges=None):
        r"""EntityPrivilegeInfo

        The model defined in huaweicloud sdk

        :param privileges: 特权列表
        :type privileges: list[str]
        :param inherit_privileges: 继承特权列表
        :type inherit_privileges: list[str]
        """
        
        

        self._privileges = None
        self._inherit_privileges = None
        self.discriminator = None

        if privileges is not None:
            self.privileges = privileges
        if inherit_privileges is not None:
            self.inherit_privileges = inherit_privileges

    @property
    def privileges(self):
        r"""Gets the privileges of this EntityPrivilegeInfo.

        特权列表

        :return: The privileges of this EntityPrivilegeInfo.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        r"""Sets the privileges of this EntityPrivilegeInfo.

        特权列表

        :param privileges: The privileges of this EntityPrivilegeInfo.
        :type privileges: list[str]
        """
        self._privileges = privileges

    @property
    def inherit_privileges(self):
        r"""Gets the inherit_privileges of this EntityPrivilegeInfo.

        继承特权列表

        :return: The inherit_privileges of this EntityPrivilegeInfo.
        :rtype: list[str]
        """
        return self._inherit_privileges

    @inherit_privileges.setter
    def inherit_privileges(self, inherit_privileges):
        r"""Sets the inherit_privileges of this EntityPrivilegeInfo.

        继承特权列表

        :param inherit_privileges: The inherit_privileges of this EntityPrivilegeInfo.
        :type inherit_privileges: list[str]
        """
        self._inherit_privileges = inherit_privileges

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
        if not isinstance(other, EntityPrivilegeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
