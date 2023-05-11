# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterDmsKafkaInstanceRequestBodyConnectInfo:

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
        'pwd': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'pwd': 'pwd'
    }

    def __init__(self, user_name=None, pwd=None):
        """RegisterDmsKafkaInstanceRequestBodyConnectInfo

        The model defined in huaweicloud sdk

        :param user_name: 账号
        :type user_name: str
        :param pwd: 密码
        :type pwd: str
        """
        
        

        self._user_name = None
        self._pwd = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if pwd is not None:
            self.pwd = pwd

    @property
    def user_name(self):
        """Gets the user_name of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.

        账号

        :return: The user_name of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.

        账号

        :param user_name: The user_name of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def pwd(self):
        """Gets the pwd of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.

        密码

        :return: The pwd of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.

        密码

        :param pwd: The pwd of this RegisterDmsKafkaInstanceRequestBodyConnectInfo.
        :type pwd: str
        """
        self._pwd = pwd

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
        if not isinstance(other, RegisterDmsKafkaInstanceRequestBodyConnectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
