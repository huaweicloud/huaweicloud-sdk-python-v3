# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessSitesRequest:

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
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'id': 'list[str]',
        'code': 'list[str]',
        'proxy_region': 'list[str]',
        'iec_az_code': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'fields': 'fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'code': 'code',
        'proxy_region': 'proxy_region',
        'iec_az_code': 'iec_az_code'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, sort_key=None, sort_dir=None, id=None, code=None, proxy_region=None, iec_az_code=None):
        """ListAccessSitesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条数
        :type limit: int
        :param offset: 分页起始点
        :type offset: int
        :param marker: 分页起始点
        :type marker: str
        :param page_reverse: 翻页方向
        :type page_reverse: bool
        :param fields: 
        :type fields: list[str]
        :param sort_key: 按照sort_key指定的字段排序
        :type sort_key: list[str]
        :param sort_dir: 排序的方向，倒序或者正序
        :type sort_dir: list[str]
        :param id: 
        :type id: list[str]
        :param code: 
        :type code: list[str]
        :param proxy_region: 
        :type proxy_region: list[str]
        :param iec_az_code: 
        :type iec_az_code: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._code = None
        self._proxy_region = None
        self._iec_az_code = None
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
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if proxy_region is not None:
            self.proxy_region = proxy_region
        if iec_az_code is not None:
            self.iec_az_code = iec_az_code

    @property
    def limit(self):
        """Gets the limit of this ListAccessSitesRequest.

        每页条数

        :return: The limit of this ListAccessSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAccessSitesRequest.

        每页条数

        :param limit: The limit of this ListAccessSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAccessSitesRequest.

        分页起始点

        :return: The offset of this ListAccessSitesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAccessSitesRequest.

        分页起始点

        :param offset: The offset of this ListAccessSitesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListAccessSitesRequest.

        分页起始点

        :return: The marker of this ListAccessSitesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAccessSitesRequest.

        分页起始点

        :param marker: The marker of this ListAccessSitesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListAccessSitesRequest.

        翻页方向

        :return: The page_reverse of this ListAccessSitesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListAccessSitesRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListAccessSitesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        """Gets the fields of this ListAccessSitesRequest.

        :return: The fields of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListAccessSitesRequest.

        :param fields: The fields of this ListAccessSitesRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAccessSitesRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAccessSitesRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListAccessSitesRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAccessSitesRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAccessSitesRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListAccessSitesRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListAccessSitesRequest.

        :return: The id of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAccessSitesRequest.

        :param id: The id of this ListAccessSitesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def code(self):
        """Gets the code of this ListAccessSitesRequest.

        :return: The code of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListAccessSitesRequest.

        :param code: The code of this ListAccessSitesRequest.
        :type code: list[str]
        """
        self._code = code

    @property
    def proxy_region(self):
        """Gets the proxy_region of this ListAccessSitesRequest.

        :return: The proxy_region of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._proxy_region

    @proxy_region.setter
    def proxy_region(self, proxy_region):
        """Sets the proxy_region of this ListAccessSitesRequest.

        :param proxy_region: The proxy_region of this ListAccessSitesRequest.
        :type proxy_region: list[str]
        """
        self._proxy_region = proxy_region

    @property
    def iec_az_code(self):
        """Gets the iec_az_code of this ListAccessSitesRequest.

        :return: The iec_az_code of this ListAccessSitesRequest.
        :rtype: list[str]
        """
        return self._iec_az_code

    @iec_az_code.setter
    def iec_az_code(self, iec_az_code):
        """Sets the iec_az_code of this ListAccessSitesRequest.

        :param iec_az_code: The iec_az_code of this ListAccessSitesRequest.
        :type iec_az_code: list[str]
        """
        self._iec_az_code = iec_az_code

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
        if not isinstance(other, ListAccessSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
