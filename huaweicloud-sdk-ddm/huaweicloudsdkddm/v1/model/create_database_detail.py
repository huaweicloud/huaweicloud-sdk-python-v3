# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'shard_mode': 'str',
        'shard_number': 'int',
        'shard_unit': 'int',
        'used_rds': 'list[DatabaseInstabcesParam]'
    }

    attribute_map = {
        'name': 'name',
        'shard_mode': 'shard_mode',
        'shard_number': 'shard_number',
        'shard_unit': 'shard_unit',
        'used_rds': 'used_rds'
    }

    def __init__(self, name=None, shard_mode=None, shard_number=None, shard_unit=None, used_rds=None):
        """CreateDatabaseDetail - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._shard_mode = None
        self._shard_number = None
        self._shard_unit = None
        self._used_rds = None
        self.discriminator = None

        self.name = name
        self.shard_mode = shard_mode
        self.shard_number = shard_number
        self.shard_unit = shard_unit
        self.used_rds = used_rds

    @property
    def name(self):
        """Gets the name of this CreateDatabaseDetail.

        逻辑库名称，需要满足以下条件：  - 长度为2-24个字符。 - 必须以字母开头，且不区分大小写。 - 可以包含字母、数字、下划线，不能包含其它特殊字符。 - 禁用关键字：  \"information_schema\"、\"mysql\"、\"performance_schema\"、\"sys\"。

        :return: The name of this CreateDatabaseDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDatabaseDetail.

        逻辑库名称，需要满足以下条件：  - 长度为2-24个字符。 - 必须以字母开头，且不区分大小写。 - 可以包含字母、数字、下划线，不能包含其它特殊字符。 - 禁用关键字：  \"information_schema\"、\"mysql\"、\"performance_schema\"、\"sys\"。

        :param name: The name of this CreateDatabaseDetail.
        :type: str
        """
        self._name = name

    @property
    def shard_mode(self):
        """Gets the shard_mode of this CreateDatabaseDetail.

        逻辑库的拆分模式。 - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :return: The shard_mode of this CreateDatabaseDetail.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        """Sets the shard_mode of this CreateDatabaseDetail.

        逻辑库的拆分模式。 - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :param shard_mode: The shard_mode of this CreateDatabaseDetail.
        :type: str
        """
        self._shard_mode = shard_mode

    @property
    def shard_number(self):
        """Gets the shard_number of this CreateDatabaseDetail.

        同一种工作模式下逻辑库分片的数量，shard_unit与关联rds数量的乘积。

        :return: The shard_number of this CreateDatabaseDetail.
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this CreateDatabaseDetail.

        同一种工作模式下逻辑库分片的数量，shard_unit与关联rds数量的乘积。

        :param shard_number: The shard_number of this CreateDatabaseDetail.
        :type: int
        """
        self._shard_number = shard_number

    @property
    def shard_unit(self):
        """Gets the shard_unit of this CreateDatabaseDetail.

        单个RDS上的逻辑库分片数。  - 非拆分逻辑库，固定为1。 - 拆分逻辑库缺省为8，可以根据需要配置为8、16。

        :return: The shard_unit of this CreateDatabaseDetail.
        :rtype: int
        """
        return self._shard_unit

    @shard_unit.setter
    def shard_unit(self, shard_unit):
        """Sets the shard_unit of this CreateDatabaseDetail.

        单个RDS上的逻辑库分片数。  - 非拆分逻辑库，固定为1。 - 拆分逻辑库缺省为8，可以根据需要配置为8、16。

        :param shard_unit: The shard_unit of this CreateDatabaseDetail.
        :type: int
        """
        self._shard_unit = shard_unit

    @property
    def used_rds(self):
        """Gets the used_rds of this CreateDatabaseDetail.

        逻辑库关联的RDS。

        :return: The used_rds of this CreateDatabaseDetail.
        :rtype: list[DatabaseInstabcesParam]
        """
        return self._used_rds

    @used_rds.setter
    def used_rds(self, used_rds):
        """Sets the used_rds of this CreateDatabaseDetail.

        逻辑库关联的RDS。

        :param used_rds: The used_rds of this CreateDatabaseDetail.
        :type: list[DatabaseInstabcesParam]
        """
        self._used_rds = used_rds

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
        if not isinstance(other, CreateDatabaseDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
