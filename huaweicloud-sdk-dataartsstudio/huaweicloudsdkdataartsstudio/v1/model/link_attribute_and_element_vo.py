# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinkAttributeAndElementVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'stand_row_id': 'str',
        'table_id': 'str',
        'biz_type': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'stand_row_id': 'stand_row_id',
        'table_id': 'table_id',
        'biz_type': 'biz_type'
    }

    def __init__(self, ids=None, stand_row_id=None, table_id=None, biz_type=None):
        r"""LinkAttributeAndElementVO

        The model defined in huaweicloud sdk

        :param ids: 属性ID列表，ID字符串。
        :type ids: list[str]
        :param stand_row_id: 关联的数据标准的ID，ID字符串。
        :type stand_row_id: str
        :param table_id: 表ID，ID字符串。
        :type table_id: str
        :param biz_type: 表类型，默认是TABLE_MODEL。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 
        :type biz_type: str
        """
        
        

        self._ids = None
        self._stand_row_id = None
        self._table_id = None
        self._biz_type = None
        self.discriminator = None

        self.ids = ids
        self.stand_row_id = stand_row_id
        self.table_id = table_id
        self.biz_type = biz_type

    @property
    def ids(self):
        r"""Gets the ids of this LinkAttributeAndElementVO.

        属性ID列表，ID字符串。

        :return: The ids of this LinkAttributeAndElementVO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this LinkAttributeAndElementVO.

        属性ID列表，ID字符串。

        :param ids: The ids of this LinkAttributeAndElementVO.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def stand_row_id(self):
        r"""Gets the stand_row_id of this LinkAttributeAndElementVO.

        关联的数据标准的ID，ID字符串。

        :return: The stand_row_id of this LinkAttributeAndElementVO.
        :rtype: str
        """
        return self._stand_row_id

    @stand_row_id.setter
    def stand_row_id(self, stand_row_id):
        r"""Sets the stand_row_id of this LinkAttributeAndElementVO.

        关联的数据标准的ID，ID字符串。

        :param stand_row_id: The stand_row_id of this LinkAttributeAndElementVO.
        :type stand_row_id: str
        """
        self._stand_row_id = stand_row_id

    @property
    def table_id(self):
        r"""Gets the table_id of this LinkAttributeAndElementVO.

        表ID，ID字符串。

        :return: The table_id of this LinkAttributeAndElementVO.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this LinkAttributeAndElementVO.

        表ID，ID字符串。

        :param table_id: The table_id of this LinkAttributeAndElementVO.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this LinkAttributeAndElementVO.

        表类型，默认是TABLE_MODEL。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 

        :return: The biz_type of this LinkAttributeAndElementVO.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this LinkAttributeAndElementVO.

        表类型，默认是TABLE_MODEL。 枚举值：   - TABLE_MODEL: 关系模型（逻辑模型/物理模型）   - AGGREGATION_LOGIC_TABLE: 汇总表   - FACT_LOGIC_TABLE: 事实表   - DIMENSION: 维度   - DIMENSION_LOGIC_TABLE: 维度表 

        :param biz_type: The biz_type of this LinkAttributeAndElementVO.
        :type biz_type: str
        """
        self._biz_type = biz_type

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
        if not isinstance(other, LinkAttributeAndElementVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
