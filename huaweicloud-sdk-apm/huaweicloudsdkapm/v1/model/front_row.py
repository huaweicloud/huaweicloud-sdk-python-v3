# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrontRow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cell_list': 'list[FrontCell]',
        'filter': 'str',
        'header': 'bool',
        'tx_id': 'int'
    }

    attribute_map = {
        'cell_list': 'cell_list',
        'filter': 'filter',
        'header': 'header',
        'tx_id': 'tx_id'
    }

    def __init__(self, cell_list=None, filter=None, header=None, tx_id=None):
        """FrontRow

        The model defined in huaweicloud sdk

        :param cell_list: 数据单元集合
        :type cell_list: list[:class:`huaweicloudsdkapm.v1.FrontCell`]
        :param filter: 将group by的字段拼接成过滤字符串，用于后续点网格点击使用
        :type filter: str
        :param header: 是否是header信息
        :type header: bool
        :param tx_id: 是否是事务
        :type tx_id: int
        """
        
        

        self._cell_list = None
        self._filter = None
        self._header = None
        self._tx_id = None
        self.discriminator = None

        if cell_list is not None:
            self.cell_list = cell_list
        if filter is not None:
            self.filter = filter
        if header is not None:
            self.header = header
        if tx_id is not None:
            self.tx_id = tx_id

    @property
    def cell_list(self):
        """Gets the cell_list of this FrontRow.

        数据单元集合

        :return: The cell_list of this FrontRow.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontCell`]
        """
        return self._cell_list

    @cell_list.setter
    def cell_list(self, cell_list):
        """Sets the cell_list of this FrontRow.

        数据单元集合

        :param cell_list: The cell_list of this FrontRow.
        :type cell_list: list[:class:`huaweicloudsdkapm.v1.FrontCell`]
        """
        self._cell_list = cell_list

    @property
    def filter(self):
        """Gets the filter of this FrontRow.

        将group by的字段拼接成过滤字符串，用于后续点网格点击使用

        :return: The filter of this FrontRow.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this FrontRow.

        将group by的字段拼接成过滤字符串，用于后续点网格点击使用

        :param filter: The filter of this FrontRow.
        :type filter: str
        """
        self._filter = filter

    @property
    def header(self):
        """Gets the header of this FrontRow.

        是否是header信息

        :return: The header of this FrontRow.
        :rtype: bool
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this FrontRow.

        是否是header信息

        :param header: The header of this FrontRow.
        :type header: bool
        """
        self._header = header

    @property
    def tx_id(self):
        """Gets the tx_id of this FrontRow.

        是否是事务

        :return: The tx_id of this FrontRow.
        :rtype: int
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this FrontRow.

        是否是事务

        :param tx_id: The tx_id of this FrontRow.
        :type tx_id: int
        """
        self._tx_id = tx_id

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
        if not isinstance(other, FrontRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
