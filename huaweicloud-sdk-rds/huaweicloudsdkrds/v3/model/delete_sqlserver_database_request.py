# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSqlserverDatabaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'db_name': 'str',
        'body': 'DropDatabaseV3Req'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'db_name': 'db_name',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, db_name=None, body=None):
        """DeleteSqlserverDatabaseRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param db_name: 需要删除的数据库名。
        :type db_name: str
        :param body: Body of the DeleteSqlserverDatabaseRequest
        :type body: :class:`huaweicloudsdkrds.v3.DropDatabaseV3Req`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._db_name = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.db_name = db_name
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this DeleteSqlserverDatabaseRequest.

        语言

        :return: The x_language of this DeleteSqlserverDatabaseRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DeleteSqlserverDatabaseRequest.

        语言

        :param x_language: The x_language of this DeleteSqlserverDatabaseRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteSqlserverDatabaseRequest.

        实例ID。

        :return: The instance_id of this DeleteSqlserverDatabaseRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteSqlserverDatabaseRequest.

        实例ID。

        :param instance_id: The instance_id of this DeleteSqlserverDatabaseRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_name(self):
        """Gets the db_name of this DeleteSqlserverDatabaseRequest.

        需要删除的数据库名。

        :return: The db_name of this DeleteSqlserverDatabaseRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DeleteSqlserverDatabaseRequest.

        需要删除的数据库名。

        :param db_name: The db_name of this DeleteSqlserverDatabaseRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def body(self):
        """Gets the body of this DeleteSqlserverDatabaseRequest.

        :return: The body of this DeleteSqlserverDatabaseRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.DropDatabaseV3Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteSqlserverDatabaseRequest.

        :param body: The body of this DeleteSqlserverDatabaseRequest.
        :type body: :class:`huaweicloudsdkrds.v3.DropDatabaseV3Req`
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
        if not isinstance(other, DeleteSqlserverDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
