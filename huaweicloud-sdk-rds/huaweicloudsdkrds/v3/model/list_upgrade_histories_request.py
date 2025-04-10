# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpgradeHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'order': 'str',
        'sort_field': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sort_field': 'sort_field',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, order=None, sort_field=None, x_language=None):
        r"""ListUpgradeHistoriesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param order: 排序方式。 DESC，降序。 ASC，升序。 默认降序。
        :type order: str
        :param sort_field: 排序字段。 start_time 开始时间。 end_time 结束时间。 默认开始时间。
        :type sort_field: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sort_field = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if sort_field is not None:
            self.sort_field = sort_field
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListUpgradeHistoriesRequest.

        实例ID

        :return: The instance_id of this ListUpgradeHistoriesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListUpgradeHistoriesRequest.

        实例ID

        :param instance_id: The instance_id of this ListUpgradeHistoriesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListUpgradeHistoriesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListUpgradeHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUpgradeHistoriesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListUpgradeHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUpgradeHistoriesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListUpgradeHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUpgradeHistoriesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListUpgradeHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListUpgradeHistoriesRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :return: The order of this ListUpgradeHistoriesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListUpgradeHistoriesRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :param order: The order of this ListUpgradeHistoriesRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListUpgradeHistoriesRequest.

        排序字段。 start_time 开始时间。 end_time 结束时间。 默认开始时间。

        :return: The sort_field of this ListUpgradeHistoriesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListUpgradeHistoriesRequest.

        排序字段。 start_time 开始时间。 end_time 结束时间。 默认开始时间。

        :param sort_field: The sort_field of this ListUpgradeHistoriesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def x_language(self):
        r"""Gets the x_language of this ListUpgradeHistoriesRequest.

        语言。默认en-us。

        :return: The x_language of this ListUpgradeHistoriesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListUpgradeHistoriesRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListUpgradeHistoriesRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListUpgradeHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
