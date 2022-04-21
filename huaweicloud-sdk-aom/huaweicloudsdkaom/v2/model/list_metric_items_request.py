# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'limit': 'str',
        'start': 'str',
        'body': 'MetricAPIQueryItemParam'
    }

    attribute_map = {
        'type': 'type',
        'limit': 'limit',
        'start': 'start',
        'body': 'body'
    }

    def __init__(self, type=None, limit=None, start=None, body=None):
        """ListMetricItemsRequest

        The model defined in huaweicloud sdk

        :param type: 指标查询方式。
        :type type: str
        :param limit: 用于限制本次返回的结果数据条数。 取值范围(0,1000]，默认值为1000。
        :type limit: str
        :param start: 分页查询起始位置，为非负整数。
        :type start: str
        :param body: Body of the ListMetricItemsRequest
        :type body: :class:`huaweicloudsdkaom.v2.MetricAPIQueryItemParam`
        """
        
        

        self._type = None
        self._limit = None
        self._start = None
        self._body = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if start is not None:
            self.start = start
        if body is not None:
            self.body = body

    @property
    def type(self):
        """Gets the type of this ListMetricItemsRequest.

        指标查询方式。

        :return: The type of this ListMetricItemsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListMetricItemsRequest.

        指标查询方式。

        :param type: The type of this ListMetricItemsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListMetricItemsRequest.

        用于限制本次返回的结果数据条数。 取值范围(0,1000]，默认值为1000。

        :return: The limit of this ListMetricItemsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMetricItemsRequest.

        用于限制本次返回的结果数据条数。 取值范围(0,1000]，默认值为1000。

        :param limit: The limit of this ListMetricItemsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def start(self):
        """Gets the start of this ListMetricItemsRequest.

        分页查询起始位置，为非负整数。

        :return: The start of this ListMetricItemsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListMetricItemsRequest.

        分页查询起始位置，为非负整数。

        :param start: The start of this ListMetricItemsRequest.
        :type start: str
        """
        self._start = start

    @property
    def body(self):
        """Gets the body of this ListMetricItemsRequest.


        :return: The body of this ListMetricItemsRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricAPIQueryItemParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListMetricItemsRequest.


        :param body: The body of this ListMetricItemsRequest.
        :type body: :class:`huaweicloudsdkaom.v2.MetricAPIQueryItemParam`
        """
        self._body = body

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
        if not isinstance(other, ListMetricItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
