# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkSqlJobTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'order': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'order': 'order',
        'tags': 'tags'
    }

    def __init__(self, limit=None, name=None, offset=None, order=None, tags=None):
        r"""ListFlinkSqlJobTemplatesRequest

        The model defined in huaweicloud sdk

        :param limit: 返回的数据条数。默认为10。
        :type limit: int
        :param name: 模板名字
        :type name: str
        :param offset: 作业偏移量。
        :type offset: int
        :param order: 查询结果排序，升序asc和降序desc两种可选，默认降序。
        :type order: str
        :param tags: 
        :type tags: str
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._order = None
        self._tags = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if tags is not None:
            self.tags = tags

    @property
    def limit(self):
        r"""Gets the limit of this ListFlinkSqlJobTemplatesRequest.

        返回的数据条数。默认为10。

        :return: The limit of this ListFlinkSqlJobTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlinkSqlJobTemplatesRequest.

        返回的数据条数。默认为10。

        :param limit: The limit of this ListFlinkSqlJobTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListFlinkSqlJobTemplatesRequest.

        模板名字

        :return: The name of this ListFlinkSqlJobTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlinkSqlJobTemplatesRequest.

        模板名字

        :param name: The name of this ListFlinkSqlJobTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListFlinkSqlJobTemplatesRequest.

        作业偏移量。

        :return: The offset of this ListFlinkSqlJobTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFlinkSqlJobTemplatesRequest.

        作业偏移量。

        :param offset: The offset of this ListFlinkSqlJobTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this ListFlinkSqlJobTemplatesRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :return: The order of this ListFlinkSqlJobTemplatesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListFlinkSqlJobTemplatesRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :param order: The order of this ListFlinkSqlJobTemplatesRequest.
        :type order: str
        """
        self._order = order

    @property
    def tags(self):
        r"""Gets the tags of this ListFlinkSqlJobTemplatesRequest.

        :return: The tags of this ListFlinkSqlJobTemplatesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListFlinkSqlJobTemplatesRequest.

        :param tags: The tags of this ListFlinkSqlJobTemplatesRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListFlinkSqlJobTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
