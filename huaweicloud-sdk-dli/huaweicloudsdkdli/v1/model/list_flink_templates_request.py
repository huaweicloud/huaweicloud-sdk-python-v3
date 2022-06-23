# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkTemplatesRequest:

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
        'tags': 'str',
        'offset': 'int',
        'order': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'offset': 'offset',
        'order': 'order',
        'limit': 'limit'
    }

    def __init__(self, name=None, tags=None, offset=None, order=None, limit=None):
        """ListFlinkTemplatesRequest

        The model defined in huaweicloud sdk

        :param name: 模板名字
        :type name: str
        :param tags: 
        :type tags: str
        :param offset: 作业偏移量。
        :type offset: int
        :param order: 查询结果排序，升序asc和降序desc两种可选，默认降序。
        :type order: str
        :param limit: 返回的数据条数。默认为10。
        :type limit: int
        """
        
        

        self._name = None
        self._tags = None
        self._offset = None
        self._order = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        """Gets the name of this ListFlinkTemplatesRequest.

        模板名字

        :return: The name of this ListFlinkTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFlinkTemplatesRequest.

        模板名字

        :param name: The name of this ListFlinkTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        """Gets the tags of this ListFlinkTemplatesRequest.


        :return: The tags of this ListFlinkTemplatesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListFlinkTemplatesRequest.


        :param tags: The tags of this ListFlinkTemplatesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def offset(self):
        """Gets the offset of this ListFlinkTemplatesRequest.

        作业偏移量。

        :return: The offset of this ListFlinkTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlinkTemplatesRequest.

        作业偏移量。

        :param offset: The offset of this ListFlinkTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        """Gets the order of this ListFlinkTemplatesRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :return: The order of this ListFlinkTemplatesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListFlinkTemplatesRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :param order: The order of this ListFlinkTemplatesRequest.
        :type order: str
        """
        self._order = order

    @property
    def limit(self):
        """Gets the limit of this ListFlinkTemplatesRequest.

        返回的数据条数。默认为10。

        :return: The limit of this ListFlinkTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlinkTemplatesRequest.

        返回的数据条数。默认为10。

        :param limit: The limit of this ListFlinkTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFlinkTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
