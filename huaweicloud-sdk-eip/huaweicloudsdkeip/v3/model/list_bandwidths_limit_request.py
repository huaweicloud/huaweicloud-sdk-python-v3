# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthsLimitRequest:

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
        'offset': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'fields': 'list[str]',
        'charge_mode': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'fields': 'fields',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, charge_mode=None):
        r"""ListBandwidthsLimitRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条数
        :type limit: int
        :param offset: 分页起始点
        :type offset: int
        :param marker: 分页起始点
        :type marker: str
        :param page_reverse: 翻页方向
        :type page_reverse: bool
        :param fields: 只显示指定的字段。使用ext-fields时在默认显示的字段基础上追加字段
        :type fields: list[str]
        :param charge_mode: 根据charge_mode过滤
        :type charge_mode: str
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._charge_mode = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if fields is not None:
            self.fields = fields
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def limit(self):
        r"""Gets the limit of this ListBandwidthsLimitRequest.

        每页条数

        :return: The limit of this ListBandwidthsLimitRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBandwidthsLimitRequest.

        每页条数

        :param limit: The limit of this ListBandwidthsLimitRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListBandwidthsLimitRequest.

        分页起始点

        :return: The offset of this ListBandwidthsLimitRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBandwidthsLimitRequest.

        分页起始点

        :param offset: The offset of this ListBandwidthsLimitRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListBandwidthsLimitRequest.

        分页起始点

        :return: The marker of this ListBandwidthsLimitRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListBandwidthsLimitRequest.

        分页起始点

        :param marker: The marker of this ListBandwidthsLimitRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListBandwidthsLimitRequest.

        翻页方向

        :return: The page_reverse of this ListBandwidthsLimitRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListBandwidthsLimitRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListBandwidthsLimitRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        r"""Gets the fields of this ListBandwidthsLimitRequest.

        只显示指定的字段。使用ext-fields时在默认显示的字段基础上追加字段

        :return: The fields of this ListBandwidthsLimitRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListBandwidthsLimitRequest.

        只显示指定的字段。使用ext-fields时在默认显示的字段基础上追加字段

        :param fields: The fields of this ListBandwidthsLimitRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ListBandwidthsLimitRequest.

        根据charge_mode过滤

        :return: The charge_mode of this ListBandwidthsLimitRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ListBandwidthsLimitRequest.

        根据charge_mode过滤

        :param charge_mode: The charge_mode of this ListBandwidthsLimitRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, ListBandwidthsLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
