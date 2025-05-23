# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetDBInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'password': 'str',
        'service_name': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'password': 'password',
        'service_name': 'service_name',
        'instance_id': 'instance_id'
    }

    def __init__(self, user_name=None, password=None, service_name=None, instance_id=None):
        r"""TargetDBInfo

        The model defined in huaweicloud sdk

        :param user_name: 用户名。
        :type user_name: str
        :param password: 用户密码。
        :type password: str
        :param service_name: service名称。
        :type service_name: str
        :param instance_id: RDS数据库的实例ID。
        :type instance_id: str
        """
        
        

        self._user_name = None
        self._password = None
        self._service_name = None
        self._instance_id = None
        self.discriminator = None

        self.user_name = user_name
        self.password = password
        self.service_name = service_name
        self.instance_id = instance_id

    @property
    def user_name(self):
        r"""Gets the user_name of this TargetDBInfo.

        用户名。

        :return: The user_name of this TargetDBInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TargetDBInfo.

        用户名。

        :param user_name: The user_name of this TargetDBInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this TargetDBInfo.

        用户密码。

        :return: The password of this TargetDBInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this TargetDBInfo.

        用户密码。

        :param password: The password of this TargetDBInfo.
        :type password: str
        """
        self._password = password

    @property
    def service_name(self):
        r"""Gets the service_name of this TargetDBInfo.

        service名称。

        :return: The service_name of this TargetDBInfo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this TargetDBInfo.

        service名称。

        :param service_name: The service_name of this TargetDBInfo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TargetDBInfo.

        RDS数据库的实例ID。

        :return: The instance_id of this TargetDBInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TargetDBInfo.

        RDS数据库的实例ID。

        :param instance_id: The instance_id of this TargetDBInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, TargetDBInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
