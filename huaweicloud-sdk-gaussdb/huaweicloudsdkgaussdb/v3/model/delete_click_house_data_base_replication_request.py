# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClickHouseDataBaseReplicationRequest:

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
        'database_name': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'database_name': 'database_name',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, database_name=None, x_language=None):
        """DeleteClickHouseDataBaseReplicationRequest

        The model defined in huaweicloud sdk

        :param instance_id: ClickHouse实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param database_name: 数据库名。
        :type database_name: str
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._database_name = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.database_name = database_name
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteClickHouseDataBaseReplicationRequest.

        ClickHouse实例ID，严格匹配UUID规则。

        :return: The instance_id of this DeleteClickHouseDataBaseReplicationRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteClickHouseDataBaseReplicationRequest.

        ClickHouse实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this DeleteClickHouseDataBaseReplicationRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def database_name(self):
        """Gets the database_name of this DeleteClickHouseDataBaseReplicationRequest.

        数据库名。

        :return: The database_name of this DeleteClickHouseDataBaseReplicationRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DeleteClickHouseDataBaseReplicationRequest.

        数据库名。

        :param database_name: The database_name of this DeleteClickHouseDataBaseReplicationRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def x_language(self):
        """Gets the x_language of this DeleteClickHouseDataBaseReplicationRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this DeleteClickHouseDataBaseReplicationRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DeleteClickHouseDataBaseReplicationRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this DeleteClickHouseDataBaseReplicationRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, DeleteClickHouseDataBaseReplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
