# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstancePasswordOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'instance_id_set': 'list[str]'
    }

    attribute_map = {
        'new_password': 'new_password',
        'instance_id_set': 'instance_id_set'
    }

    def __init__(self, new_password=None, instance_id_set=None):
        r"""ChangeInstancePasswordOptions

        The model defined in huaweicloud sdk

        :param new_password: 设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。
        :type new_password: str
        :param instance_id_set: instance id set
        :type instance_id_set: list[str]
        """
        
        

        self._new_password = None
        self._instance_id_set = None
        self.discriminator = None

        self.new_password = new_password
        if instance_id_set is not None:
            self.instance_id_set = instance_id_set

    @property
    def new_password(self):
        r"""Gets the new_password of this ChangeInstancePasswordOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :return: The new_password of this ChangeInstancePasswordOptions.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ChangeInstancePasswordOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :param new_password: The new_password of this ChangeInstancePasswordOptions.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def instance_id_set(self):
        r"""Gets the instance_id_set of this ChangeInstancePasswordOptions.

        instance id set

        :return: The instance_id_set of this ChangeInstancePasswordOptions.
        :rtype: list[str]
        """
        return self._instance_id_set

    @instance_id_set.setter
    def instance_id_set(self, instance_id_set):
        r"""Sets the instance_id_set of this ChangeInstancePasswordOptions.

        instance id set

        :param instance_id_set: The instance_id_set of this ChangeInstancePasswordOptions.
        :type instance_id_set: list[str]
        """
        self._instance_id_set = instance_id_set

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
        if not isinstance(other, ChangeInstancePasswordOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
