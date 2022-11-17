# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDbUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'db_user_id': 'str',
        'x_language': 'str',
        'body': 'UpdateDbUserRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'db_user_id': 'db_user_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, instance_id=None, db_user_id=None, x_language=None, body=None):
        """UpdateDbUserRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param x_language: 语言
        :type x_language: str
        :param body: Body of the UpdateDbUserRequest
        :type body: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequestBody`
        """
        
        

        self._instance_id = None
        self._db_user_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.db_user_id = db_user_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDbUserRequest.

        实例ID

        :return: The instance_id of this UpdateDbUserRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDbUserRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateDbUserRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_user_id(self):
        """Gets the db_user_id of this UpdateDbUserRequest.

        数据库用户ID

        :return: The db_user_id of this UpdateDbUserRequest.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        """Sets the db_user_id of this UpdateDbUserRequest.

        数据库用户ID

        :param db_user_id: The db_user_id of this UpdateDbUserRequest.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def x_language(self):
        """Gets the x_language of this UpdateDbUserRequest.

        语言

        :return: The x_language of this UpdateDbUserRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this UpdateDbUserRequest.

        语言

        :param x_language: The x_language of this UpdateDbUserRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this UpdateDbUserRequest.

        :return: The body of this UpdateDbUserRequest.
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDbUserRequest.

        :param body: The body of this UpdateDbUserRequest.
        :type body: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateDbUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
