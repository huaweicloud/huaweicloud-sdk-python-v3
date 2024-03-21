# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportRegionsRequest:

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
        'instance_type': 'list[str]',
        'public_border_group': 'list[str]',
        'access_site': 'list[str]',
        'region_id': 'list[str]',
        'remote_endpoint': 'list[str]',
        'status': 'list[str]'
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
        'instance_type': 'instance_type',
        'public_border_group': 'public_border_group',
        'access_site': 'access_site',
        'region_id': 'region_id',
        'remote_endpoint': 'remote_endpoint',
        'status': 'status'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, sort_key=None, sort_dir=None, id=None, instance_type=None, public_border_group=None, access_site=None, region_id=None, remote_endpoint=None, status=None):
        """ListSupportRegionsRequest

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
        :param instance_type: 
        :type instance_type: list[str]
        :param public_border_group: 
        :type public_border_group: list[str]
        :param access_site: 
        :type access_site: list[str]
        :param region_id: 
        :type region_id: list[str]
        :param remote_endpoint: 
        :type remote_endpoint: list[str]
        :param status: 
        :type status: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._instance_type = None
        self._public_border_group = None
        self._access_site = None
        self._region_id = None
        self._remote_endpoint = None
        self._status = None
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
        if instance_type is not None:
            self.instance_type = instance_type
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if access_site is not None:
            self.access_site = access_site
        if region_id is not None:
            self.region_id = region_id
        if remote_endpoint is not None:
            self.remote_endpoint = remote_endpoint
        if status is not None:
            self.status = status

    @property
    def limit(self):
        """Gets the limit of this ListSupportRegionsRequest.

        每页条数

        :return: The limit of this ListSupportRegionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSupportRegionsRequest.

        每页条数

        :param limit: The limit of this ListSupportRegionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSupportRegionsRequest.

        分页起始点

        :return: The offset of this ListSupportRegionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSupportRegionsRequest.

        分页起始点

        :param offset: The offset of this ListSupportRegionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListSupportRegionsRequest.

        分页起始点

        :return: The marker of this ListSupportRegionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSupportRegionsRequest.

        分页起始点

        :param marker: The marker of this ListSupportRegionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListSupportRegionsRequest.

        翻页方向

        :return: The page_reverse of this ListSupportRegionsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListSupportRegionsRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListSupportRegionsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        """Gets the fields of this ListSupportRegionsRequest.

        :return: The fields of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListSupportRegionsRequest.

        :param fields: The fields of this ListSupportRegionsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListSupportRegionsRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListSupportRegionsRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListSupportRegionsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListSupportRegionsRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListSupportRegionsRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListSupportRegionsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListSupportRegionsRequest.

        :return: The id of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSupportRegionsRequest.

        :param id: The id of this ListSupportRegionsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def instance_type(self):
        """Gets the instance_type of this ListSupportRegionsRequest.

        :return: The instance_type of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ListSupportRegionsRequest.

        :param instance_type: The instance_type of this ListSupportRegionsRequest.
        :type instance_type: list[str]
        """
        self._instance_type = instance_type

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListSupportRegionsRequest.

        :return: The public_border_group of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListSupportRegionsRequest.

        :param public_border_group: The public_border_group of this ListSupportRegionsRequest.
        :type public_border_group: list[str]
        """
        self._public_border_group = public_border_group

    @property
    def access_site(self):
        """Gets the access_site of this ListSupportRegionsRequest.

        :return: The access_site of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ListSupportRegionsRequest.

        :param access_site: The access_site of this ListSupportRegionsRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def region_id(self):
        """Gets the region_id of this ListSupportRegionsRequest.

        :return: The region_id of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListSupportRegionsRequest.

        :param region_id: The region_id of this ListSupportRegionsRequest.
        :type region_id: list[str]
        """
        self._region_id = region_id

    @property
    def remote_endpoint(self):
        """Gets the remote_endpoint of this ListSupportRegionsRequest.

        :return: The remote_endpoint of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._remote_endpoint

    @remote_endpoint.setter
    def remote_endpoint(self, remote_endpoint):
        """Sets the remote_endpoint of this ListSupportRegionsRequest.

        :param remote_endpoint: The remote_endpoint of this ListSupportRegionsRequest.
        :type remote_endpoint: list[str]
        """
        self._remote_endpoint = remote_endpoint

    @property
    def status(self):
        """Gets the status of this ListSupportRegionsRequest.

        :return: The status of this ListSupportRegionsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSupportRegionsRequest.

        :param status: The status of this ListSupportRegionsRequest.
        :type status: list[str]
        """
        self._status = status

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
        if not isinstance(other, ListSupportRegionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
