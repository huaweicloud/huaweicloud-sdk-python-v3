# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAndDeletePrivilegeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation': 'str',
        'privilege': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'privilege': 'privilege'
    }

    def __init__(self, operation=None, privilege=None):
        r"""CreateAndDeletePrivilegeReq

        The model defined in huaweicloud sdk

        :param operation: 执行的操作(create|delete)
        :type operation: str
        :param privilege: 权限标识
        :type privilege: str
        """
        
        

        self._operation = None
        self._privilege = None
        self.discriminator = None

        self.operation = operation
        if privilege is not None:
            self.privilege = privilege

    @property
    def operation(self):
        r"""Gets the operation of this CreateAndDeletePrivilegeReq.

        执行的操作(create|delete)

        :return: The operation of this CreateAndDeletePrivilegeReq.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this CreateAndDeletePrivilegeReq.

        执行的操作(create|delete)

        :param operation: The operation of this CreateAndDeletePrivilegeReq.
        :type operation: str
        """
        self._operation = operation

    @property
    def privilege(self):
        r"""Gets the privilege of this CreateAndDeletePrivilegeReq.

        权限标识

        :return: The privilege of this CreateAndDeletePrivilegeReq.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        r"""Sets the privilege of this CreateAndDeletePrivilegeReq.

        权限标识

        :param privilege: The privilege of this CreateAndDeletePrivilegeReq.
        :type privilege: str
        """
        self._privilege = privilege

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
        if not isinstance(other, CreateAndDeletePrivilegeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
