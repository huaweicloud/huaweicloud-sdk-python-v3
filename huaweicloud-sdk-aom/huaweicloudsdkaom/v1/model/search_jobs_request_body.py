# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchJobsRequestBody:

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
        'page_num': 'int',
        'page_size': 'int',
        'order_by_column': 'str',
        'sort_order': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'order_by_column': 'order_by_column',
        'sort_order': 'sort_order',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, page_num=None, page_size=None, order_by_column=None, sort_order=None, enterprise_project_id=None):
        """SearchJobsRequestBody

        The model defined in huaweicloud sdk

        :param name: name为作业名称。
        :type name: str
        :param page_num: 当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。
        :type page_num: int
        :param page_size: 每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。
        :type page_size: int
        :param order_by_column: 需要排序的字段(默认为更新时间),支持字段有name,create_time,update_time。
        :type order_by_column: str
        :param sort_order: 排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。
        :type sort_order: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._page_num = None
        self._page_size = None
        self._order_by_column = None
        self._sort_order = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        self.order_by_column = order_by_column
        if sort_order is not None:
            self.sort_order = sort_order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this SearchJobsRequestBody.

        name为作业名称。

        :return: The name of this SearchJobsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchJobsRequestBody.

        name为作业名称。

        :param name: The name of this SearchJobsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def page_num(self):
        """Gets the page_num of this SearchJobsRequestBody.

        当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。

        :return: The page_num of this SearchJobsRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this SearchJobsRequestBody.

        当前页，查询的当前页，page_num为正整数，不能是0和负数，当输入参数为负数，0和大于1000，自动修正参数为1，默认值是1（用户不传，值是1）。

        :param page_num: The page_num of this SearchJobsRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this SearchJobsRequestBody.

        每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。

        :return: The page_size of this SearchJobsRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchJobsRequestBody.

        每页显示的条数，每页查询的总条数，page_size为正整数，不能是0和负数，当输入参数为负数，0和大于101，自动修正参数为10，默认值是10（用户不传时，值是10）。

        :param page_size: The page_size of this SearchJobsRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def order_by_column(self):
        """Gets the order_by_column of this SearchJobsRequestBody.

        需要排序的字段(默认为更新时间),支持字段有name,create_time,update_time。

        :return: The order_by_column of this SearchJobsRequestBody.
        :rtype: str
        """
        return self._order_by_column

    @order_by_column.setter
    def order_by_column(self, order_by_column):
        """Sets the order_by_column of this SearchJobsRequestBody.

        需要排序的字段(默认为更新时间),支持字段有name,create_time,update_time。

        :param order_by_column: The order_by_column of this SearchJobsRequestBody.
        :type order_by_column: str
        """
        self._order_by_column = order_by_column

    @property
    def sort_order(self):
        """Gets the sort_order of this SearchJobsRequestBody.

        排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。

        :return: The sort_order of this SearchJobsRequestBody.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SearchJobsRequestBody.

        排序规则(默认降序) 传入升序或降序，升序：ASC，降序：DESC。

        :param sort_order: The sort_order of this SearchJobsRequestBody.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SearchJobsRequestBody.

        企业项目id

        :return: The enterprise_project_id of this SearchJobsRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SearchJobsRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this SearchJobsRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, SearchJobsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
