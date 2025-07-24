# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIDcsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'limit': 'str',
        'order': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'region': 'region',
        'limit': 'limit',
        'order': 'order',
        'marker': 'marker'
    }

    def __init__(self, region=None, limit=None, order=None, marker=None):
        r"""ListIDcsRequest

        The model defined in huaweicloud sdk

        :param region: 区域
        :type region: str
        :param limit: 分页大小，取值范围为[1,2000]，默认2000
        :type limit: str
        :param order: 排序升、降序
        :type order: str
        :param marker: 上一页数据的最后一条记录id
        :type marker: str
        """
        
        

        self._region = None
        self._limit = None
        self._order = None
        self._marker = None
        self.discriminator = None

        self.region = region
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if marker is not None:
            self.marker = marker

    @property
    def region(self):
        r"""Gets the region of this ListIDcsRequest.

        区域

        :return: The region of this ListIDcsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListIDcsRequest.

        区域

        :param region: The region of this ListIDcsRequest.
        :type region: str
        """
        self._region = region

    @property
    def limit(self):
        r"""Gets the limit of this ListIDcsRequest.

        分页大小，取值范围为[1,2000]，默认2000

        :return: The limit of this ListIDcsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIDcsRequest.

        分页大小，取值范围为[1,2000]，默认2000

        :param limit: The limit of this ListIDcsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListIDcsRequest.

        排序升、降序

        :return: The order of this ListIDcsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListIDcsRequest.

        排序升、降序

        :param order: The order of this ListIDcsRequest.
        :type order: str
        """
        self._order = order

    @property
    def marker(self):
        r"""Gets the marker of this ListIDcsRequest.

        上一页数据的最后一条记录id

        :return: The marker of this ListIDcsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListIDcsRequest.

        上一页数据的最后一条记录id

        :param marker: The marker of this ListIDcsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListIDcsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
