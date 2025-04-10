# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DlsAdmin:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manager_type': 'str',
        'manager_id': 'str',
        'manager_name': 'str'
    }

    attribute_map = {
        'manager_type': 'manager_type',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name'
    }

    def __init__(self, manager_type=None, manager_id=None, manager_name=None):
        r"""DlsAdmin

        The model defined in huaweicloud sdk

        :param manager_type: 管理员类型, USER:用户, USER_GROUP:用户组
        :type manager_type: str
        :param manager_id: 管理员id, 管理员类型为用户时, 请传入iam用户id; 管理员类型为用户组时, 请传入iam用户组id
        :type manager_id: str
        :param manager_name: 管理员名称, 管理员类型为用户时, 请传入iam用户名称; 管理员类型为用户组时, 请传入iam用户组名称
        :type manager_name: str
        """
        
        

        self._manager_type = None
        self._manager_id = None
        self._manager_name = None
        self.discriminator = None

        if manager_type is not None:
            self.manager_type = manager_type
        if manager_id is not None:
            self.manager_id = manager_id
        if manager_name is not None:
            self.manager_name = manager_name

    @property
    def manager_type(self):
        r"""Gets the manager_type of this DlsAdmin.

        管理员类型, USER:用户, USER_GROUP:用户组

        :return: The manager_type of this DlsAdmin.
        :rtype: str
        """
        return self._manager_type

    @manager_type.setter
    def manager_type(self, manager_type):
        r"""Sets the manager_type of this DlsAdmin.

        管理员类型, USER:用户, USER_GROUP:用户组

        :param manager_type: The manager_type of this DlsAdmin.
        :type manager_type: str
        """
        self._manager_type = manager_type

    @property
    def manager_id(self):
        r"""Gets the manager_id of this DlsAdmin.

        管理员id, 管理员类型为用户时, 请传入iam用户id; 管理员类型为用户组时, 请传入iam用户组id

        :return: The manager_id of this DlsAdmin.
        :rtype: str
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        r"""Sets the manager_id of this DlsAdmin.

        管理员id, 管理员类型为用户时, 请传入iam用户id; 管理员类型为用户组时, 请传入iam用户组id

        :param manager_id: The manager_id of this DlsAdmin.
        :type manager_id: str
        """
        self._manager_id = manager_id

    @property
    def manager_name(self):
        r"""Gets the manager_name of this DlsAdmin.

        管理员名称, 管理员类型为用户时, 请传入iam用户名称; 管理员类型为用户组时, 请传入iam用户组名称

        :return: The manager_name of this DlsAdmin.
        :rtype: str
        """
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name):
        r"""Sets the manager_name of this DlsAdmin.

        管理员名称, 管理员类型为用户时, 请传入iam用户名称; 管理员类型为用户组时, 请传入iam用户组名称

        :param manager_name: The manager_name of this DlsAdmin.
        :type manager_name: str
        """
        self._manager_name = manager_name

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
        if not isinstance(other, DlsAdmin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
