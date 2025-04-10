# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criteria': 'list[CriteriaSnake]',
        'page_number': 'int',
        'page_size': 'int',
        'sort_by': 'int',
        'sort_order': 'int'
    }

    attribute_map = {
        'criteria': 'criteria',
        'page_number': 'page_number',
        'page_size': 'page_size',
        'sort_by': 'sort_by',
        'sort_order': 'sort_order'
    }

    def __init__(self, criteria=None, page_number=None, page_size=None, sort_by=None, sort_order=None):
        r"""FilterSnake

        The model defined in huaweicloud sdk

        :param criteria: 过滤集合
        :type criteria: list[:class:`huaweicloudsdkcloudide.v2.CriteriaSnake`]
        :param page_number: 页码
        :type page_number: int
        :param page_size: 分页大小
        :type page_size: int
        :param sort_by: 排序字段. - 1 修改日期 - 2 插件名称 - 3 插件作者名称
        :type sort_by: int
        :param sort_order: 排序顺序. - 1 升序 - 2 降序
        :type sort_order: int
        """
        
        

        self._criteria = None
        self._page_number = None
        self._page_size = None
        self._sort_by = None
        self._sort_order = None
        self.discriminator = None

        if criteria is not None:
            self.criteria = criteria
        self.page_number = page_number
        self.page_size = page_size
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def criteria(self):
        r"""Gets the criteria of this FilterSnake.

        过滤集合

        :return: The criteria of this FilterSnake.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.CriteriaSnake`]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this FilterSnake.

        过滤集合

        :param criteria: The criteria of this FilterSnake.
        :type criteria: list[:class:`huaweicloudsdkcloudide.v2.CriteriaSnake`]
        """
        self._criteria = criteria

    @property
    def page_number(self):
        r"""Gets the page_number of this FilterSnake.

        页码

        :return: The page_number of this FilterSnake.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this FilterSnake.

        页码

        :param page_number: The page_number of this FilterSnake.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this FilterSnake.

        分页大小

        :return: The page_size of this FilterSnake.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this FilterSnake.

        分页大小

        :param page_size: The page_size of this FilterSnake.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_by(self):
        r"""Gets the sort_by of this FilterSnake.

        排序字段. - 1 修改日期 - 2 插件名称 - 3 插件作者名称

        :return: The sort_by of this FilterSnake.
        :rtype: int
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this FilterSnake.

        排序字段. - 1 修改日期 - 2 插件名称 - 3 插件作者名称

        :param sort_by: The sort_by of this FilterSnake.
        :type sort_by: int
        """
        self._sort_by = sort_by

    @property
    def sort_order(self):
        r"""Gets the sort_order of this FilterSnake.

        排序顺序. - 1 升序 - 2 降序

        :return: The sort_order of this FilterSnake.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this FilterSnake.

        排序顺序. - 1 升序 - 2 降序

        :param sort_order: The sort_order of this FilterSnake.
        :type sort_order: int
        """
        self._sort_order = sort_order

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
        if not isinstance(other, FilterSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
