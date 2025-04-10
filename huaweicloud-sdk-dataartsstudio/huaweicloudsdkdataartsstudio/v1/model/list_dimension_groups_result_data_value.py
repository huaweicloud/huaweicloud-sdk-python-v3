# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDimensionGroupsResultDataValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_table': 'FactLogicTableVO',
        'dimension_tables': 'list[DimensionLogicTableVO]'
    }

    attribute_map = {
        'main_table': 'main_table',
        'dimension_tables': 'dimension_tables'
    }

    def __init__(self, main_table=None, dimension_tables=None):
        r"""ListDimensionGroupsResultDataValue

        The model defined in huaweicloud sdk

        :param main_table: 
        :type main_table: :class:`huaweicloudsdkdataartsstudio.v1.FactLogicTableVO`
        :param dimension_tables: 维度。
        :type dimension_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionLogicTableVO`]
        """
        
        

        self._main_table = None
        self._dimension_tables = None
        self.discriminator = None

        if main_table is not None:
            self.main_table = main_table
        if dimension_tables is not None:
            self.dimension_tables = dimension_tables

    @property
    def main_table(self):
        r"""Gets the main_table of this ListDimensionGroupsResultDataValue.

        :return: The main_table of this ListDimensionGroupsResultDataValue.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.FactLogicTableVO`
        """
        return self._main_table

    @main_table.setter
    def main_table(self, main_table):
        r"""Sets the main_table of this ListDimensionGroupsResultDataValue.

        :param main_table: The main_table of this ListDimensionGroupsResultDataValue.
        :type main_table: :class:`huaweicloudsdkdataartsstudio.v1.FactLogicTableVO`
        """
        self._main_table = main_table

    @property
    def dimension_tables(self):
        r"""Gets the dimension_tables of this ListDimensionGroupsResultDataValue.

        维度。

        :return: The dimension_tables of this ListDimensionGroupsResultDataValue.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionLogicTableVO`]
        """
        return self._dimension_tables

    @dimension_tables.setter
    def dimension_tables(self, dimension_tables):
        r"""Sets the dimension_tables of this ListDimensionGroupsResultDataValue.

        维度。

        :param dimension_tables: The dimension_tables of this ListDimensionGroupsResultDataValue.
        :type dimension_tables: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionLogicTableVO`]
        """
        self._dimension_tables = dimension_tables

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
        if not isinstance(other, ListDimensionGroupsResultDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
