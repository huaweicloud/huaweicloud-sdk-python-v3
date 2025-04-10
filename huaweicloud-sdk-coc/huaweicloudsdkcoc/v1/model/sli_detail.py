# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SliDetail:

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
        'sort_id': 'int',
        'sli_type': 'str',
        'name': 'str',
        'description': 'str',
        'comparison_operator': 'str',
        'numerical_value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sort_id': 'sort_id',
        'sli_type': 'sli_type',
        'name': 'name',
        'description': 'description',
        'comparison_operator': 'comparison_operator',
        'numerical_value': 'numerical_value',
        'unit': 'unit'
    }

    def __init__(self, id=None, sort_id=None, sli_type=None, name=None, description=None, comparison_operator=None, numerical_value=None, unit=None):
        r"""SliDetail

        The model defined in huaweicloud sdk

        :param id: SLi的ID
        :type id: str
        :param sort_id: 顺序
        :type sort_id: int
        :param sli_type: SLI类型 REQUEST 请求型SLI指标 INSTANCES 实例型SLI指标
        :type sli_type: str
        :param name: SLI名称
        :type name: str
        :param description: SLI描述
        :type description: str
        :param comparison_operator: 比较符 LESS_THAN 小于 LESS_THAN_OR_EQUAL_TO 小于等于 EQUALS 等于 GREATER_THAN 大于 GREATER_THAN_OR_EQUAL_TO 大于等于
        :type comparison_operator: str
        :param numerical_value: 数值
        :type numerical_value: float
        :param unit: 单位 PERCENT_SIGN 百分号 MILLISECONDS 毫秒 NUMBER_OF_REQUESTS_PER_SECOND 每秒请求数量
        :type unit: str
        """
        
        

        self._id = None
        self._sort_id = None
        self._sli_type = None
        self._name = None
        self._description = None
        self._comparison_operator = None
        self._numerical_value = None
        self._unit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sort_id is not None:
            self.sort_id = sort_id
        self.sli_type = sli_type
        self.name = name
        self.description = description
        self.comparison_operator = comparison_operator
        self.numerical_value = numerical_value
        self.unit = unit

    @property
    def id(self):
        r"""Gets the id of this SliDetail.

        SLi的ID

        :return: The id of this SliDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SliDetail.

        SLi的ID

        :param id: The id of this SliDetail.
        :type id: str
        """
        self._id = id

    @property
    def sort_id(self):
        r"""Gets the sort_id of this SliDetail.

        顺序

        :return: The sort_id of this SliDetail.
        :rtype: int
        """
        return self._sort_id

    @sort_id.setter
    def sort_id(self, sort_id):
        r"""Sets the sort_id of this SliDetail.

        顺序

        :param sort_id: The sort_id of this SliDetail.
        :type sort_id: int
        """
        self._sort_id = sort_id

    @property
    def sli_type(self):
        r"""Gets the sli_type of this SliDetail.

        SLI类型 REQUEST 请求型SLI指标 INSTANCES 实例型SLI指标

        :return: The sli_type of this SliDetail.
        :rtype: str
        """
        return self._sli_type

    @sli_type.setter
    def sli_type(self, sli_type):
        r"""Sets the sli_type of this SliDetail.

        SLI类型 REQUEST 请求型SLI指标 INSTANCES 实例型SLI指标

        :param sli_type: The sli_type of this SliDetail.
        :type sli_type: str
        """
        self._sli_type = sli_type

    @property
    def name(self):
        r"""Gets the name of this SliDetail.

        SLI名称

        :return: The name of this SliDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SliDetail.

        SLI名称

        :param name: The name of this SliDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SliDetail.

        SLI描述

        :return: The description of this SliDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SliDetail.

        SLI描述

        :param description: The description of this SliDetail.
        :type description: str
        """
        self._description = description

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this SliDetail.

        比较符 LESS_THAN 小于 LESS_THAN_OR_EQUAL_TO 小于等于 EQUALS 等于 GREATER_THAN 大于 GREATER_THAN_OR_EQUAL_TO 大于等于

        :return: The comparison_operator of this SliDetail.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this SliDetail.

        比较符 LESS_THAN 小于 LESS_THAN_OR_EQUAL_TO 小于等于 EQUALS 等于 GREATER_THAN 大于 GREATER_THAN_OR_EQUAL_TO 大于等于

        :param comparison_operator: The comparison_operator of this SliDetail.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def numerical_value(self):
        r"""Gets the numerical_value of this SliDetail.

        数值

        :return: The numerical_value of this SliDetail.
        :rtype: float
        """
        return self._numerical_value

    @numerical_value.setter
    def numerical_value(self, numerical_value):
        r"""Sets the numerical_value of this SliDetail.

        数值

        :param numerical_value: The numerical_value of this SliDetail.
        :type numerical_value: float
        """
        self._numerical_value = numerical_value

    @property
    def unit(self):
        r"""Gets the unit of this SliDetail.

        单位 PERCENT_SIGN 百分号 MILLISECONDS 毫秒 NUMBER_OF_REQUESTS_PER_SECOND 每秒请求数量

        :return: The unit of this SliDetail.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this SliDetail.

        单位 PERCENT_SIGN 百分号 MILLISECONDS 毫秒 NUMBER_OF_REQUESTS_PER_SECOND 每秒请求数量

        :param unit: The unit of this SliDetail.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, SliDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
