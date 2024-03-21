# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidthsRequest:

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
        'ext_fields': 'list[str]',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'id': 'list[str]',
        'size': 'list[int]',
        'name': 'list[str]',
        'name_like': 'str',
        'access_site': 'list[str]',
        'status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'tags': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'fields': 'fields',
        'ext_fields': 'ext-fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'size': 'size',
        'name': 'name',
        'name_like': 'name_like',
        'access_site': 'access_site',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, ext_fields=None, sort_key=None, sort_dir=None, id=None, size=None, name=None, name_like=None, access_site=None, status=None, enterprise_project_id=None, tags=None, type=None):
        """ListInternetBandwidthsRequest

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
        :param ext_fields: 
        :type ext_fields: list[str]
        :param sort_key: 按照sort_key指定的字段排序
        :type sort_key: list[str]
        :param sort_dir: 排序的方向，倒序或者正序
        :type sort_dir: list[str]
        :param id: 
        :type id: list[str]
        :param size: 
        :type size: list[int]
        :param name: 
        :type name: list[str]
        :param name_like: 
        :type name_like: str
        :param access_site: 
        :type access_site: list[str]
        :param status: 
        :type status: list[str]
        :param enterprise_project_id: 
        :type enterprise_project_id: list[str]
        :param tags: 
        :type tags: list[str]
        :param type: 
        :type type: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._ext_fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._size = None
        self._name = None
        self._name_like = None
        self._access_site = None
        self._status = None
        self._enterprise_project_id = None
        self._tags = None
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
        if ext_fields is not None:
            self.ext_fields = ext_fields
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if name_like is not None:
            self.name_like = name_like
        if access_site is not None:
            self.access_site = access_site
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def limit(self):
        """Gets the limit of this ListInternetBandwidthsRequest.

        每页条数

        :return: The limit of this ListInternetBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInternetBandwidthsRequest.

        每页条数

        :param limit: The limit of this ListInternetBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInternetBandwidthsRequest.

        分页起始点

        :return: The offset of this ListInternetBandwidthsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInternetBandwidthsRequest.

        分页起始点

        :param offset: The offset of this ListInternetBandwidthsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListInternetBandwidthsRequest.

        分页起始点

        :return: The marker of this ListInternetBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListInternetBandwidthsRequest.

        分页起始点

        :param marker: The marker of this ListInternetBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListInternetBandwidthsRequest.

        翻页方向

        :return: The page_reverse of this ListInternetBandwidthsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListInternetBandwidthsRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListInternetBandwidthsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        """Gets the fields of this ListInternetBandwidthsRequest.

        :return: The fields of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListInternetBandwidthsRequest.

        :param fields: The fields of this ListInternetBandwidthsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        """Gets the ext_fields of this ListInternetBandwidthsRequest.

        :return: The ext_fields of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        """Sets the ext_fields of this ListInternetBandwidthsRequest.

        :param ext_fields: The ext_fields of this ListInternetBandwidthsRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListInternetBandwidthsRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListInternetBandwidthsRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListInternetBandwidthsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListInternetBandwidthsRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListInternetBandwidthsRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListInternetBandwidthsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListInternetBandwidthsRequest.

        :return: The id of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInternetBandwidthsRequest.

        :param id: The id of this ListInternetBandwidthsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this ListInternetBandwidthsRequest.

        :return: The size of this ListInternetBandwidthsRequest.
        :rtype: list[int]
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListInternetBandwidthsRequest.

        :param size: The size of this ListInternetBandwidthsRequest.
        :type size: list[int]
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this ListInternetBandwidthsRequest.

        :return: The name of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInternetBandwidthsRequest.

        :param name: The name of this ListInternetBandwidthsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def name_like(self):
        """Gets the name_like of this ListInternetBandwidthsRequest.

        :return: The name_like of this ListInternetBandwidthsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this ListInternetBandwidthsRequest.

        :param name_like: The name_like of this ListInternetBandwidthsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def access_site(self):
        """Gets the access_site of this ListInternetBandwidthsRequest.

        :return: The access_site of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ListInternetBandwidthsRequest.

        :param access_site: The access_site of this ListInternetBandwidthsRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def status(self):
        """Gets the status of this ListInternetBandwidthsRequest.

        :return: The status of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInternetBandwidthsRequest.

        :param status: The status of this ListInternetBandwidthsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInternetBandwidthsRequest.

        :return: The enterprise_project_id of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInternetBandwidthsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListInternetBandwidthsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ListInternetBandwidthsRequest.

        :return: The tags of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListInternetBandwidthsRequest.

        :param tags: The tags of this ListInternetBandwidthsRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this ListInternetBandwidthsRequest.

        :return: The type of this ListInternetBandwidthsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInternetBandwidthsRequest.

        :param type: The type of this ListInternetBandwidthsRequest.
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
        if not isinstance(other, ListInternetBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
