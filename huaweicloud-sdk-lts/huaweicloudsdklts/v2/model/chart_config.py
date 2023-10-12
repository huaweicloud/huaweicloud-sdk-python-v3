# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChartConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_sort': 'bool',
        'can_search': 'bool',
        'page_size': 'int'
    }

    attribute_map = {
        'can_sort': 'canSort',
        'can_search': 'canSearch',
        'page_size': 'pageSize'
    }

    def __init__(self, can_sort=None, can_search=None, page_size=None):
        """ChartConfig

        The model defined in huaweicloud sdk

        :param can_sort: 是否开启排序
        :type can_sort: bool
        :param can_search: 是否开启搜索
        :type can_search: bool
        :param page_size: 每页显示数量
        :type page_size: int
        """
        
        

        self._can_sort = None
        self._can_search = None
        self._page_size = None
        self.discriminator = None

        self.can_sort = can_sort
        self.can_search = can_search
        self.page_size = page_size

    @property
    def can_sort(self):
        """Gets the can_sort of this ChartConfig.

        是否开启排序

        :return: The can_sort of this ChartConfig.
        :rtype: bool
        """
        return self._can_sort

    @can_sort.setter
    def can_sort(self, can_sort):
        """Sets the can_sort of this ChartConfig.

        是否开启排序

        :param can_sort: The can_sort of this ChartConfig.
        :type can_sort: bool
        """
        self._can_sort = can_sort

    @property
    def can_search(self):
        """Gets the can_search of this ChartConfig.

        是否开启搜索

        :return: The can_search of this ChartConfig.
        :rtype: bool
        """
        return self._can_search

    @can_search.setter
    def can_search(self, can_search):
        """Sets the can_search of this ChartConfig.

        是否开启搜索

        :param can_search: The can_search of this ChartConfig.
        :type can_search: bool
        """
        self._can_search = can_search

    @property
    def page_size(self):
        """Gets the page_size of this ChartConfig.

        每页显示数量

        :return: The page_size of this ChartConfig.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ChartConfig.

        每页显示数量

        :param page_size: The page_size of this ChartConfig.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ChartConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
