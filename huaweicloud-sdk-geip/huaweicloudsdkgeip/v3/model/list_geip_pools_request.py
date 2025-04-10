# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeipPoolsRequest:

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
        'access_site': 'list[str]',
        'isp': 'list[str]',
        'ip_version': 'list[str]',
        'status': 'list[str]',
        'type': 'list[str]'
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
        'access_site': 'access_site',
        'isp': 'isp',
        'ip_version': 'ip_version',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, sort_key=None, sort_dir=None, id=None, code=None, access_site=None, isp=None, ip_version=None, status=None, type=None):
        r"""ListGeipPoolsRequest

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
        :param access_site: 
        :type access_site: list[str]
        :param isp: 
        :type isp: list[str]
        :param ip_version: 
        :type ip_version: list[str]
        :param status: 
        :type status: list[str]
        :param type: 
        :type type: list[str]
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
        self._access_site = None
        self._isp = None
        self._ip_version = None
        self._status = None
        self._type = None
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
        if access_site is not None:
            self.access_site = access_site
        if isp is not None:
            self.isp = isp
        if ip_version is not None:
            self.ip_version = ip_version
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListGeipPoolsRequest.

        每页条数

        :return: The limit of this ListGeipPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGeipPoolsRequest.

        每页条数

        :param limit: The limit of this ListGeipPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListGeipPoolsRequest.

        分页起始点

        :return: The offset of this ListGeipPoolsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGeipPoolsRequest.

        分页起始点

        :param offset: The offset of this ListGeipPoolsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListGeipPoolsRequest.

        分页起始点

        :return: The marker of this ListGeipPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGeipPoolsRequest.

        分页起始点

        :param marker: The marker of this ListGeipPoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListGeipPoolsRequest.

        翻页方向

        :return: The page_reverse of this ListGeipPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListGeipPoolsRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListGeipPoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        r"""Gets the fields of this ListGeipPoolsRequest.

        :return: The fields of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListGeipPoolsRequest.

        :param fields: The fields of this ListGeipPoolsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListGeipPoolsRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListGeipPoolsRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListGeipPoolsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListGeipPoolsRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListGeipPoolsRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListGeipPoolsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListGeipPoolsRequest.

        :return: The id of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGeipPoolsRequest.

        :param id: The id of this ListGeipPoolsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this ListGeipPoolsRequest.

        :return: The code of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListGeipPoolsRequest.

        :param code: The code of this ListGeipPoolsRequest.
        :type code: list[str]
        """
        self._code = code

    @property
    def access_site(self):
        r"""Gets the access_site of this ListGeipPoolsRequest.

        :return: The access_site of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this ListGeipPoolsRequest.

        :param access_site: The access_site of this ListGeipPoolsRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def isp(self):
        r"""Gets the isp of this ListGeipPoolsRequest.

        :return: The isp of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this ListGeipPoolsRequest.

        :param isp: The isp of this ListGeipPoolsRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListGeipPoolsRequest.

        :return: The ip_version of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListGeipPoolsRequest.

        :param ip_version: The ip_version of this ListGeipPoolsRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def status(self):
        r"""Gets the status of this ListGeipPoolsRequest.

        :return: The status of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGeipPoolsRequest.

        :param status: The status of this ListGeipPoolsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListGeipPoolsRequest.

        :return: The type of this ListGeipPoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListGeipPoolsRequest.

        :param type: The type of this ListGeipPoolsRequest.
        :type type: list[str]
        """
        self._type = type

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
        if not isinstance(other, ListGeipPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
