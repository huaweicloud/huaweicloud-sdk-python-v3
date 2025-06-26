# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'database_name': 'str',
        'total_value': 'int',
        'perm_space': 'int',
        'skew_percent': 'float',
        'min_value': 'int',
        'max_value': 'int',
        'min_dn': 'str',
        'max_dn': 'str',
        'dn_num': 'int'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'database_name': 'database_name',
        'total_value': 'total_value',
        'perm_space': 'perm_space',
        'skew_percent': 'skew_percent',
        'min_value': 'min_value',
        'max_value': 'max_value',
        'min_dn': 'min_dn',
        'max_dn': 'max_dn',
        'dn_num': 'dn_num'
    }

    def __init__(self, schema_name=None, database_name=None, total_value=None, perm_space=None, skew_percent=None, min_value=None, max_value=None, min_dn=None, max_dn=None, dn_num=None):
        r"""SchemaInfo

        The model defined in huaweicloud sdk

        :param schema_name: **参数解释**： 集群模式名称。 **取值范围**： 不涉及。
        :type schema_name: str
        :param database_name: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type database_name: str
        :param total_value: **参数解释**： 集群模式使用空间总值。 **取值范围**： 不涉及。
        :type total_value: int
        :param perm_space: **参数解释**： 集群模式空间阈值。 **取值范围**： 不涉及。
        :type perm_space: int
        :param skew_percent: **参数解释**： 倾斜率。 **取值范围**： 不涉及。
        :type skew_percent: float
        :param min_value: **参数解释**： 最小值。 **取值范围**： 不涉及。
        :type min_value: int
        :param max_value: **参数解释**： 最大值。 **取值范围**： 不涉及。
        :type max_value: int
        :param min_dn: **参数解释**： 最小dn节点。 **取值范围**： 不涉及。
        :type min_dn: str
        :param max_dn: **参数解释**： 最大cn节点。 **取值范围**： 不涉及。
        :type max_dn: str
        :param dn_num: **参数解释**： dn节点数量。 **取值范围**： 不涉及。
        :type dn_num: int
        """
        
        

        self._schema_name = None
        self._database_name = None
        self._total_value = None
        self._perm_space = None
        self._skew_percent = None
        self._min_value = None
        self._max_value = None
        self._min_dn = None
        self._max_dn = None
        self._dn_num = None
        self.discriminator = None

        self.schema_name = schema_name
        self.database_name = database_name
        self.total_value = total_value
        self.perm_space = perm_space
        self.skew_percent = skew_percent
        self.min_value = min_value
        self.max_value = max_value
        self.min_dn = min_dn
        self.max_dn = max_dn
        self.dn_num = dn_num

    @property
    def schema_name(self):
        r"""Gets the schema_name of this SchemaInfo.

        **参数解释**： 集群模式名称。 **取值范围**： 不涉及。

        :return: The schema_name of this SchemaInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this SchemaInfo.

        **参数解释**： 集群模式名称。 **取值范围**： 不涉及。

        :param schema_name: The schema_name of this SchemaInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def database_name(self):
        r"""Gets the database_name of this SchemaInfo.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The database_name of this SchemaInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SchemaInfo.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param database_name: The database_name of this SchemaInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def total_value(self):
        r"""Gets the total_value of this SchemaInfo.

        **参数解释**： 集群模式使用空间总值。 **取值范围**： 不涉及。

        :return: The total_value of this SchemaInfo.
        :rtype: int
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        r"""Sets the total_value of this SchemaInfo.

        **参数解释**： 集群模式使用空间总值。 **取值范围**： 不涉及。

        :param total_value: The total_value of this SchemaInfo.
        :type total_value: int
        """
        self._total_value = total_value

    @property
    def perm_space(self):
        r"""Gets the perm_space of this SchemaInfo.

        **参数解释**： 集群模式空间阈值。 **取值范围**： 不涉及。

        :return: The perm_space of this SchemaInfo.
        :rtype: int
        """
        return self._perm_space

    @perm_space.setter
    def perm_space(self, perm_space):
        r"""Sets the perm_space of this SchemaInfo.

        **参数解释**： 集群模式空间阈值。 **取值范围**： 不涉及。

        :param perm_space: The perm_space of this SchemaInfo.
        :type perm_space: int
        """
        self._perm_space = perm_space

    @property
    def skew_percent(self):
        r"""Gets the skew_percent of this SchemaInfo.

        **参数解释**： 倾斜率。 **取值范围**： 不涉及。

        :return: The skew_percent of this SchemaInfo.
        :rtype: float
        """
        return self._skew_percent

    @skew_percent.setter
    def skew_percent(self, skew_percent):
        r"""Sets the skew_percent of this SchemaInfo.

        **参数解释**： 倾斜率。 **取值范围**： 不涉及。

        :param skew_percent: The skew_percent of this SchemaInfo.
        :type skew_percent: float
        """
        self._skew_percent = skew_percent

    @property
    def min_value(self):
        r"""Gets the min_value of this SchemaInfo.

        **参数解释**： 最小值。 **取值范围**： 不涉及。

        :return: The min_value of this SchemaInfo.
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        r"""Sets the min_value of this SchemaInfo.

        **参数解释**： 最小值。 **取值范围**： 不涉及。

        :param min_value: The min_value of this SchemaInfo.
        :type min_value: int
        """
        self._min_value = min_value

    @property
    def max_value(self):
        r"""Gets the max_value of this SchemaInfo.

        **参数解释**： 最大值。 **取值范围**： 不涉及。

        :return: The max_value of this SchemaInfo.
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this SchemaInfo.

        **参数解释**： 最大值。 **取值范围**： 不涉及。

        :param max_value: The max_value of this SchemaInfo.
        :type max_value: int
        """
        self._max_value = max_value

    @property
    def min_dn(self):
        r"""Gets the min_dn of this SchemaInfo.

        **参数解释**： 最小dn节点。 **取值范围**： 不涉及。

        :return: The min_dn of this SchemaInfo.
        :rtype: str
        """
        return self._min_dn

    @min_dn.setter
    def min_dn(self, min_dn):
        r"""Sets the min_dn of this SchemaInfo.

        **参数解释**： 最小dn节点。 **取值范围**： 不涉及。

        :param min_dn: The min_dn of this SchemaInfo.
        :type min_dn: str
        """
        self._min_dn = min_dn

    @property
    def max_dn(self):
        r"""Gets the max_dn of this SchemaInfo.

        **参数解释**： 最大cn节点。 **取值范围**： 不涉及。

        :return: The max_dn of this SchemaInfo.
        :rtype: str
        """
        return self._max_dn

    @max_dn.setter
    def max_dn(self, max_dn):
        r"""Sets the max_dn of this SchemaInfo.

        **参数解释**： 最大cn节点。 **取值范围**： 不涉及。

        :param max_dn: The max_dn of this SchemaInfo.
        :type max_dn: str
        """
        self._max_dn = max_dn

    @property
    def dn_num(self):
        r"""Gets the dn_num of this SchemaInfo.

        **参数解释**： dn节点数量。 **取值范围**： 不涉及。

        :return: The dn_num of this SchemaInfo.
        :rtype: int
        """
        return self._dn_num

    @dn_num.setter
    def dn_num(self, dn_num):
        r"""Sets the dn_num of this SchemaInfo.

        **参数解释**： dn节点数量。 **取值范围**： 不涉及。

        :param dn_num: The dn_num of this SchemaInfo.
        :type dn_num: int
        """
        self._dn_num = dn_num

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
        if not isinstance(other, SchemaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
