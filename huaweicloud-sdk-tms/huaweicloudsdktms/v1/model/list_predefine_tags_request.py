# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPredefineTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'limit': 'int',
        'marker': 'str',
        'order_field': 'str',
        'order_method': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'limit': 'limit',
        'marker': 'marker',
        'order_field': 'order_field',
        'order_method': 'order_method'
    }

    def __init__(self, key=None, value=None, limit=None, marker=None, order_field=None, order_method=None):
        """ListPredefineTagsRequest

        The model defined in huaweicloud sdk

        :param key: 键，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。
        :type key: str
        :param value: 值，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。
        :type value: str
        :param limit: 查询记录数。 最小为1，最大为1000，未输入时默认为10，为0时不限制查询数据条数。
        :type limit: int
        :param marker: 分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的tags为空列表时表示查询到最后一页。
        :type marker: str
        :param order_field: 排序字段： 可输入的值包含（区分大小写）：update_time（更新时间）、key（键）、value（值）。 只能选择以上排序字段中的一个，并按照排序方法字段order_method进行排序，如果不传则默认值为：update_time。 如以下： 若该字段为update_time，则剩余两个默认字段排序为key升序，value升序。 若该字段如为key，则剩余两个默认字段排序为update_time降序，value升序。 若该字段如为value，则剩余两个默认字段排序为update_time降序，key升序。 若该字段不传，默认字段为update_time，则剩余两个默认字段排序为key升序，value升序。
        :type order_field: str
        :param order_method: order_field字段的排序方法。 可输入的值包含（区分大小写）： asc（升序） desc（降序） 只能选择以上值的其中之一。 不传则默认值为：desc
        :type order_method: str
        """
        
        

        self._key = None
        self._value = None
        self._limit = None
        self._marker = None
        self._order_field = None
        self._order_method = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if order_field is not None:
            self.order_field = order_field
        if order_method is not None:
            self.order_method = order_method

    @property
    def key(self):
        """Gets the key of this ListPredefineTagsRequest.

        键，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。

        :return: The key of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListPredefineTagsRequest.

        键，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。

        :param key: The key of this ListPredefineTagsRequest.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ListPredefineTagsRequest.

        值，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。

        :return: The value of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListPredefineTagsRequest.

        值，支持模糊查询，不区分大小写，如果包含“non-URL-safe”的字符，需要进行“urlencoded”。

        :param value: The value of this ListPredefineTagsRequest.
        :type value: str
        """
        self._value = value

    @property
    def limit(self):
        """Gets the limit of this ListPredefineTagsRequest.

        查询记录数。 最小为1，最大为1000，未输入时默认为10，为0时不限制查询数据条数。

        :return: The limit of this ListPredefineTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPredefineTagsRequest.

        查询记录数。 最小为1，最大为1000，未输入时默认为10，为0时不限制查询数据条数。

        :param limit: The limit of this ListPredefineTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPredefineTagsRequest.

        分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的tags为空列表时表示查询到最后一页。

        :return: The marker of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPredefineTagsRequest.

        分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的tags为空列表时表示查询到最后一页。

        :param marker: The marker of this ListPredefineTagsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def order_field(self):
        """Gets the order_field of this ListPredefineTagsRequest.

        排序字段： 可输入的值包含（区分大小写）：update_time（更新时间）、key（键）、value（值）。 只能选择以上排序字段中的一个，并按照排序方法字段order_method进行排序，如果不传则默认值为：update_time。 如以下： 若该字段为update_time，则剩余两个默认字段排序为key升序，value升序。 若该字段如为key，则剩余两个默认字段排序为update_time降序，value升序。 若该字段如为value，则剩余两个默认字段排序为update_time降序，key升序。 若该字段不传，默认字段为update_time，则剩余两个默认字段排序为key升序，value升序。

        :return: The order_field of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        """Sets the order_field of this ListPredefineTagsRequest.

        排序字段： 可输入的值包含（区分大小写）：update_time（更新时间）、key（键）、value（值）。 只能选择以上排序字段中的一个，并按照排序方法字段order_method进行排序，如果不传则默认值为：update_time。 如以下： 若该字段为update_time，则剩余两个默认字段排序为key升序，value升序。 若该字段如为key，则剩余两个默认字段排序为update_time降序，value升序。 若该字段如为value，则剩余两个默认字段排序为update_time降序，key升序。 若该字段不传，默认字段为update_time，则剩余两个默认字段排序为key升序，value升序。

        :param order_field: The order_field of this ListPredefineTagsRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_method(self):
        """Gets the order_method of this ListPredefineTagsRequest.

        order_field字段的排序方法。 可输入的值包含（区分大小写）： asc（升序） desc（降序） 只能选择以上值的其中之一。 不传则默认值为：desc

        :return: The order_method of this ListPredefineTagsRequest.
        :rtype: str
        """
        return self._order_method

    @order_method.setter
    def order_method(self, order_method):
        """Sets the order_method of this ListPredefineTagsRequest.

        order_field字段的排序方法。 可输入的值包含（区分大小写）： asc（升序） desc（降序） 只能选择以上值的其中之一。 不传则默认值为：desc

        :param order_method: The order_method of this ListPredefineTagsRequest.
        :type order_method: str
        """
        self._order_method = order_method

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
        if not isinstance(other, ListPredefineTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
