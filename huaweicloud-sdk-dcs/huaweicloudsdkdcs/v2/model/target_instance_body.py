# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'password': 'password'
    }

    def __init__(self, id=None, name=None, password=None):
        """TargetInstanceBody

        The model defined in huaweicloud sdk

        :param id: Redis实例ID（target_instance信息中必须填写）。
        :type id: str
        :param name: Redis实例名称(target_instance信息中填写)。
        :type name: str
        :param password: Redis密码，如果设置了密码，则必须填写。
        :type password: str
        """
        
        

        self._id = None
        self._name = None
        self._password = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password

    @property
    def id(self):
        """Gets the id of this TargetInstanceBody.

        Redis实例ID（target_instance信息中必须填写）。

        :return: The id of this TargetInstanceBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetInstanceBody.

        Redis实例ID（target_instance信息中必须填写）。

        :param id: The id of this TargetInstanceBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TargetInstanceBody.

        Redis实例名称(target_instance信息中填写)。

        :return: The name of this TargetInstanceBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetInstanceBody.

        Redis实例名称(target_instance信息中填写)。

        :param name: The name of this TargetInstanceBody.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this TargetInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :return: The password of this TargetInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TargetInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :param password: The password of this TargetInstanceBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, TargetInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
