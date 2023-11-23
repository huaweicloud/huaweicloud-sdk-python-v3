# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInspectionHistoriesRequest:

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
        'target_version': 'str',
        'is_available': 'bool',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sort_field': 'sort_field',
        'target_version': 'target_version',
        'is_available': 'is_available',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, order=None, sort_field=None, target_version=None, is_available=None, x_language=None):
        """ListInspectionHistoriesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param order: 排序方式。 DESC，降序。 ASC，升序。 默认降序。
        :type order: str
        :param sort_field: 排序字段。 check_time 检查时间。 expiration_time 过期时间。 默认检查时间。
        :type sort_field: str
        :param target_version: 目标版本。
        :type target_version: str
        :param is_available: 是否有效。 true 表示有效。 false 表示无效。
        :type is_available: bool
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sort_field = None
        self._target_version = None
        self._is_available = None
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
        if target_version is not None:
            self.target_version = target_version
        if is_available is not None:
            self.is_available = is_available
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInspectionHistoriesRequest.

        实例ID

        :return: The instance_id of this ListInspectionHistoriesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInspectionHistoriesRequest.

        实例ID

        :param instance_id: The instance_id of this ListInspectionHistoriesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListInspectionHistoriesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListInspectionHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInspectionHistoriesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListInspectionHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInspectionHistoriesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListInspectionHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInspectionHistoriesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListInspectionHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        """Gets the order of this ListInspectionHistoriesRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :return: The order of this ListInspectionHistoriesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListInspectionHistoriesRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :param order: The order of this ListInspectionHistoriesRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_field(self):
        """Gets the sort_field of this ListInspectionHistoriesRequest.

        排序字段。 check_time 检查时间。 expiration_time 过期时间。 默认检查时间。

        :return: The sort_field of this ListInspectionHistoriesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListInspectionHistoriesRequest.

        排序字段。 check_time 检查时间。 expiration_time 过期时间。 默认检查时间。

        :param sort_field: The sort_field of this ListInspectionHistoriesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def target_version(self):
        """Gets the target_version of this ListInspectionHistoriesRequest.

        目标版本。

        :return: The target_version of this ListInspectionHistoriesRequest.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ListInspectionHistoriesRequest.

        目标版本。

        :param target_version: The target_version of this ListInspectionHistoriesRequest.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def is_available(self):
        """Gets the is_available of this ListInspectionHistoriesRequest.

        是否有效。 true 表示有效。 false 表示无效。

        :return: The is_available of this ListInspectionHistoriesRequest.
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this ListInspectionHistoriesRequest.

        是否有效。 true 表示有效。 false 表示无效。

        :param is_available: The is_available of this ListInspectionHistoriesRequest.
        :type is_available: bool
        """
        self._is_available = is_available

    @property
    def x_language(self):
        """Gets the x_language of this ListInspectionHistoriesRequest.

        语言。默认en-us。

        :return: The x_language of this ListInspectionHistoriesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListInspectionHistoriesRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListInspectionHistoriesRequest.
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
        if not isinstance(other, ListInspectionHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
