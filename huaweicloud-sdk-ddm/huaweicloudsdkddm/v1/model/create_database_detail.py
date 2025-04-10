# coding: utf-8

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
        r"""CreateDatabaseDetail

        The model defined in huaweicloud sdk

        :param name: 逻辑库名称，需要满足以下条件：  - 长度为2-48个字符。 - 必须以小写字母开头。 - 可以包含小写字母、数字、下划线，不能包含大写字母和其它特殊字符。 - 禁用关键字：  \&quot;information_schema\&quot;、\&quot;mysql\&quot;、\&quot;performance_schema\&quot;、\&quot;sys\&quot;。
        :type name: str
        :param shard_mode: 逻辑库的拆分模式。 - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。
        :type shard_mode: str
        :param shard_number: 同一种工作模式下逻辑库分片的数量。 - shard_unit不为空， shard_unit与关联rds数量的乘积 - shard_unit为空，大于关联的RDS数量，小于等于关联rds数量*64。
        :type shard_number: int
        :param shard_unit: 单个RDS上的逻辑库分片数。非必选  - 非拆分逻辑库，固定为1。 - 拆分逻辑库，大于等于1，小于等于64。
        :type shard_unit: int
        :param used_rds: 逻辑库关联的RDS。
        :type used_rds: list[:class:`huaweicloudsdkddm.v1.DatabaseInstabcesParam`]
        """
        
        

        self._name = None
        self._shard_mode = None
        self._shard_number = None
        self._shard_unit = None
        self._used_rds = None
        self.discriminator = None

        self.name = name
        self.shard_mode = shard_mode
        self.shard_number = shard_number
        if shard_unit is not None:
            self.shard_unit = shard_unit
        self.used_rds = used_rds

    @property
    def name(self):
        r"""Gets the name of this CreateDatabaseDetail.

        逻辑库名称，需要满足以下条件：  - 长度为2-48个字符。 - 必须以小写字母开头。 - 可以包含小写字母、数字、下划线，不能包含大写字母和其它特殊字符。 - 禁用关键字：  \"information_schema\"、\"mysql\"、\"performance_schema\"、\"sys\"。

        :return: The name of this CreateDatabaseDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDatabaseDetail.

        逻辑库名称，需要满足以下条件：  - 长度为2-48个字符。 - 必须以小写字母开头。 - 可以包含小写字母、数字、下划线，不能包含大写字母和其它特殊字符。 - 禁用关键字：  \"information_schema\"、\"mysql\"、\"performance_schema\"、\"sys\"。

        :param name: The name of this CreateDatabaseDetail.
        :type name: str
        """
        self._name = name

    @property
    def shard_mode(self):
        r"""Gets the shard_mode of this CreateDatabaseDetail.

        逻辑库的拆分模式。 - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :return: The shard_mode of this CreateDatabaseDetail.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        r"""Sets the shard_mode of this CreateDatabaseDetail.

        逻辑库的拆分模式。 - cluster表示逻辑库是拆分模式。 - single表示逻辑库是非拆分模式。

        :param shard_mode: The shard_mode of this CreateDatabaseDetail.
        :type shard_mode: str
        """
        self._shard_mode = shard_mode

    @property
    def shard_number(self):
        r"""Gets the shard_number of this CreateDatabaseDetail.

        同一种工作模式下逻辑库分片的数量。 - shard_unit不为空， shard_unit与关联rds数量的乘积 - shard_unit为空，大于关联的RDS数量，小于等于关联rds数量*64。

        :return: The shard_number of this CreateDatabaseDetail.
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        r"""Sets the shard_number of this CreateDatabaseDetail.

        同一种工作模式下逻辑库分片的数量。 - shard_unit不为空， shard_unit与关联rds数量的乘积 - shard_unit为空，大于关联的RDS数量，小于等于关联rds数量*64。

        :param shard_number: The shard_number of this CreateDatabaseDetail.
        :type shard_number: int
        """
        self._shard_number = shard_number

    @property
    def shard_unit(self):
        r"""Gets the shard_unit of this CreateDatabaseDetail.

        单个RDS上的逻辑库分片数。非必选  - 非拆分逻辑库，固定为1。 - 拆分逻辑库，大于等于1，小于等于64。

        :return: The shard_unit of this CreateDatabaseDetail.
        :rtype: int
        """
        return self._shard_unit

    @shard_unit.setter
    def shard_unit(self, shard_unit):
        r"""Sets the shard_unit of this CreateDatabaseDetail.

        单个RDS上的逻辑库分片数。非必选  - 非拆分逻辑库，固定为1。 - 拆分逻辑库，大于等于1，小于等于64。

        :param shard_unit: The shard_unit of this CreateDatabaseDetail.
        :type shard_unit: int
        """
        self._shard_unit = shard_unit

    @property
    def used_rds(self):
        r"""Gets the used_rds of this CreateDatabaseDetail.

        逻辑库关联的RDS。

        :return: The used_rds of this CreateDatabaseDetail.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DatabaseInstabcesParam`]
        """
        return self._used_rds

    @used_rds.setter
    def used_rds(self, used_rds):
        r"""Sets the used_rds of this CreateDatabaseDetail.

        逻辑库关联的RDS。

        :param used_rds: The used_rds of this CreateDatabaseDetail.
        :type used_rds: list[:class:`huaweicloudsdkddm.v1.DatabaseInstabcesParam`]
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
