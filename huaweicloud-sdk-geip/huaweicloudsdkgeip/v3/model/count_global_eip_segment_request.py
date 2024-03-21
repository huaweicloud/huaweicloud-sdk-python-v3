# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountGlobalEipSegmentRequest:

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
        'id': 'list[str]',
        'internet_bandwidth_id': 'list[str]',
        'name': 'list[str]',
        'name_like': 'str',
        'access_site': 'list[str]',
        'geip_pool_name': 'list[str]',
        'isp': 'list[str]',
        'ip_version': 'list[int]',
        'cidr': 'list[str]',
        'cidr_v6': 'list[str]',
        'freezen': 'list[bool]',
        'internet_bandwidth_is_null': 'list[bool]',
        'status': 'list[str]',
        'associate_instance_region': 'list[str]',
        'associate_instance_public_border_group': 'list[str]',
        'associate_instance_instance_site': 'list[str]',
        'associate_instance_instance_type': 'list[str]',
        'associate_instance_instance_id': 'list[str]',
        'associate_instance_project_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'fields': 'fields',
        'id': 'id',
        'internet_bandwidth_id': 'internet_bandwidth_id',
        'name': 'name',
        'name_like': 'name_like',
        'access_site': 'access_site',
        'geip_pool_name': 'geip_pool_name',
        'isp': 'isp',
        'ip_version': 'ip_version',
        'cidr': 'cidr',
        'cidr_v6': 'cidr_v6',
        'freezen': 'freezen',
        'internet_bandwidth_is_null': 'internet_bandwidth_is_null',
        'status': 'status',
        'associate_instance_region': 'associate_instance.region',
        'associate_instance_public_border_group': 'associate_instance.public_border_group',
        'associate_instance_instance_site': 'associate_instance.instance_site',
        'associate_instance_instance_type': 'associate_instance.instance_type',
        'associate_instance_instance_id': 'associate_instance.instance_id',
        'associate_instance_project_id': 'associate_instance.project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, id=None, internet_bandwidth_id=None, name=None, name_like=None, access_site=None, geip_pool_name=None, isp=None, ip_version=None, cidr=None, cidr_v6=None, freezen=None, internet_bandwidth_is_null=None, status=None, associate_instance_region=None, associate_instance_public_border_group=None, associate_instance_instance_site=None, associate_instance_instance_type=None, associate_instance_instance_id=None, associate_instance_project_id=None, enterprise_project_id=None, tags=None):
        """CountGlobalEipSegmentRequest

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
        :param id: 
        :type id: list[str]
        :param internet_bandwidth_id: 
        :type internet_bandwidth_id: list[str]
        :param name: 
        :type name: list[str]
        :param name_like: 
        :type name_like: str
        :param access_site: 
        :type access_site: list[str]
        :param geip_pool_name: 
        :type geip_pool_name: list[str]
        :param isp: 
        :type isp: list[str]
        :param ip_version: 
        :type ip_version: list[int]
        :param cidr: 
        :type cidr: list[str]
        :param cidr_v6: 
        :type cidr_v6: list[str]
        :param freezen: 
        :type freezen: list[bool]
        :param internet_bandwidth_is_null: 
        :type internet_bandwidth_is_null: list[bool]
        :param status: 
        :type status: list[str]
        :param associate_instance_region: 
        :type associate_instance_region: list[str]
        :param associate_instance_public_border_group: 
        :type associate_instance_public_border_group: list[str]
        :param associate_instance_instance_site: 
        :type associate_instance_instance_site: list[str]
        :param associate_instance_instance_type: 
        :type associate_instance_instance_type: list[str]
        :param associate_instance_instance_id: 
        :type associate_instance_instance_id: list[str]
        :param associate_instance_project_id: 
        :type associate_instance_project_id: list[str]
        :param enterprise_project_id: 
        :type enterprise_project_id: list[str]
        :param tags: 
        :type tags: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._id = None
        self._internet_bandwidth_id = None
        self._name = None
        self._name_like = None
        self._access_site = None
        self._geip_pool_name = None
        self._isp = None
        self._ip_version = None
        self._cidr = None
        self._cidr_v6 = None
        self._freezen = None
        self._internet_bandwidth_is_null = None
        self._status = None
        self._associate_instance_region = None
        self._associate_instance_public_border_group = None
        self._associate_instance_instance_site = None
        self._associate_instance_instance_type = None
        self._associate_instance_instance_id = None
        self._associate_instance_project_id = None
        self._enterprise_project_id = None
        self._tags = None
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
        if id is not None:
            self.id = id
        if internet_bandwidth_id is not None:
            self.internet_bandwidth_id = internet_bandwidth_id
        if name is not None:
            self.name = name
        if name_like is not None:
            self.name_like = name_like
        if access_site is not None:
            self.access_site = access_site
        if geip_pool_name is not None:
            self.geip_pool_name = geip_pool_name
        if isp is not None:
            self.isp = isp
        if ip_version is not None:
            self.ip_version = ip_version
        if cidr is not None:
            self.cidr = cidr
        if cidr_v6 is not None:
            self.cidr_v6 = cidr_v6
        if freezen is not None:
            self.freezen = freezen
        if internet_bandwidth_is_null is not None:
            self.internet_bandwidth_is_null = internet_bandwidth_is_null
        if status is not None:
            self.status = status
        if associate_instance_region is not None:
            self.associate_instance_region = associate_instance_region
        if associate_instance_public_border_group is not None:
            self.associate_instance_public_border_group = associate_instance_public_border_group
        if associate_instance_instance_site is not None:
            self.associate_instance_instance_site = associate_instance_instance_site
        if associate_instance_instance_type is not None:
            self.associate_instance_instance_type = associate_instance_instance_type
        if associate_instance_instance_id is not None:
            self.associate_instance_instance_id = associate_instance_instance_id
        if associate_instance_project_id is not None:
            self.associate_instance_project_id = associate_instance_project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def limit(self):
        """Gets the limit of this CountGlobalEipSegmentRequest.

        每页条数

        :return: The limit of this CountGlobalEipSegmentRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CountGlobalEipSegmentRequest.

        每页条数

        :param limit: The limit of this CountGlobalEipSegmentRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this CountGlobalEipSegmentRequest.

        分页起始点

        :return: The offset of this CountGlobalEipSegmentRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CountGlobalEipSegmentRequest.

        分页起始点

        :param offset: The offset of this CountGlobalEipSegmentRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this CountGlobalEipSegmentRequest.

        分页起始点

        :return: The marker of this CountGlobalEipSegmentRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this CountGlobalEipSegmentRequest.

        分页起始点

        :param marker: The marker of this CountGlobalEipSegmentRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this CountGlobalEipSegmentRequest.

        翻页方向

        :return: The page_reverse of this CountGlobalEipSegmentRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this CountGlobalEipSegmentRequest.

        翻页方向

        :param page_reverse: The page_reverse of this CountGlobalEipSegmentRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        """Gets the fields of this CountGlobalEipSegmentRequest.

        :return: The fields of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CountGlobalEipSegmentRequest.

        :param fields: The fields of this CountGlobalEipSegmentRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def id(self):
        """Gets the id of this CountGlobalEipSegmentRequest.

        :return: The id of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CountGlobalEipSegmentRequest.

        :param id: The id of this CountGlobalEipSegmentRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def internet_bandwidth_id(self):
        """Gets the internet_bandwidth_id of this CountGlobalEipSegmentRequest.

        :return: The internet_bandwidth_id of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._internet_bandwidth_id

    @internet_bandwidth_id.setter
    def internet_bandwidth_id(self, internet_bandwidth_id):
        """Sets the internet_bandwidth_id of this CountGlobalEipSegmentRequest.

        :param internet_bandwidth_id: The internet_bandwidth_id of this CountGlobalEipSegmentRequest.
        :type internet_bandwidth_id: list[str]
        """
        self._internet_bandwidth_id = internet_bandwidth_id

    @property
    def name(self):
        """Gets the name of this CountGlobalEipSegmentRequest.

        :return: The name of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountGlobalEipSegmentRequest.

        :param name: The name of this CountGlobalEipSegmentRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def name_like(self):
        """Gets the name_like of this CountGlobalEipSegmentRequest.

        :return: The name_like of this CountGlobalEipSegmentRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this CountGlobalEipSegmentRequest.

        :param name_like: The name_like of this CountGlobalEipSegmentRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def access_site(self):
        """Gets the access_site of this CountGlobalEipSegmentRequest.

        :return: The access_site of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this CountGlobalEipSegmentRequest.

        :param access_site: The access_site of this CountGlobalEipSegmentRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def geip_pool_name(self):
        """Gets the geip_pool_name of this CountGlobalEipSegmentRequest.

        :return: The geip_pool_name of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._geip_pool_name

    @geip_pool_name.setter
    def geip_pool_name(self, geip_pool_name):
        """Sets the geip_pool_name of this CountGlobalEipSegmentRequest.

        :param geip_pool_name: The geip_pool_name of this CountGlobalEipSegmentRequest.
        :type geip_pool_name: list[str]
        """
        self._geip_pool_name = geip_pool_name

    @property
    def isp(self):
        """Gets the isp of this CountGlobalEipSegmentRequest.

        :return: The isp of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this CountGlobalEipSegmentRequest.

        :param isp: The isp of this CountGlobalEipSegmentRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def ip_version(self):
        """Gets the ip_version of this CountGlobalEipSegmentRequest.

        :return: The ip_version of this CountGlobalEipSegmentRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CountGlobalEipSegmentRequest.

        :param ip_version: The ip_version of this CountGlobalEipSegmentRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        """Gets the cidr of this CountGlobalEipSegmentRequest.

        :return: The cidr of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CountGlobalEipSegmentRequest.

        :param cidr: The cidr of this CountGlobalEipSegmentRequest.
        :type cidr: list[str]
        """
        self._cidr = cidr

    @property
    def cidr_v6(self):
        """Gets the cidr_v6 of this CountGlobalEipSegmentRequest.

        :return: The cidr_v6 of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._cidr_v6

    @cidr_v6.setter
    def cidr_v6(self, cidr_v6):
        """Sets the cidr_v6 of this CountGlobalEipSegmentRequest.

        :param cidr_v6: The cidr_v6 of this CountGlobalEipSegmentRequest.
        :type cidr_v6: list[str]
        """
        self._cidr_v6 = cidr_v6

    @property
    def freezen(self):
        """Gets the freezen of this CountGlobalEipSegmentRequest.

        :return: The freezen of this CountGlobalEipSegmentRequest.
        :rtype: list[bool]
        """
        return self._freezen

    @freezen.setter
    def freezen(self, freezen):
        """Sets the freezen of this CountGlobalEipSegmentRequest.

        :param freezen: The freezen of this CountGlobalEipSegmentRequest.
        :type freezen: list[bool]
        """
        self._freezen = freezen

    @property
    def internet_bandwidth_is_null(self):
        """Gets the internet_bandwidth_is_null of this CountGlobalEipSegmentRequest.

        :return: The internet_bandwidth_is_null of this CountGlobalEipSegmentRequest.
        :rtype: list[bool]
        """
        return self._internet_bandwidth_is_null

    @internet_bandwidth_is_null.setter
    def internet_bandwidth_is_null(self, internet_bandwidth_is_null):
        """Sets the internet_bandwidth_is_null of this CountGlobalEipSegmentRequest.

        :param internet_bandwidth_is_null: The internet_bandwidth_is_null of this CountGlobalEipSegmentRequest.
        :type internet_bandwidth_is_null: list[bool]
        """
        self._internet_bandwidth_is_null = internet_bandwidth_is_null

    @property
    def status(self):
        """Gets the status of this CountGlobalEipSegmentRequest.

        :return: The status of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CountGlobalEipSegmentRequest.

        :param status: The status of this CountGlobalEipSegmentRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def associate_instance_region(self):
        """Gets the associate_instance_region of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_region of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_region

    @associate_instance_region.setter
    def associate_instance_region(self, associate_instance_region):
        """Sets the associate_instance_region of this CountGlobalEipSegmentRequest.

        :param associate_instance_region: The associate_instance_region of this CountGlobalEipSegmentRequest.
        :type associate_instance_region: list[str]
        """
        self._associate_instance_region = associate_instance_region

    @property
    def associate_instance_public_border_group(self):
        """Gets the associate_instance_public_border_group of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_public_border_group of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_public_border_group

    @associate_instance_public_border_group.setter
    def associate_instance_public_border_group(self, associate_instance_public_border_group):
        """Sets the associate_instance_public_border_group of this CountGlobalEipSegmentRequest.

        :param associate_instance_public_border_group: The associate_instance_public_border_group of this CountGlobalEipSegmentRequest.
        :type associate_instance_public_border_group: list[str]
        """
        self._associate_instance_public_border_group = associate_instance_public_border_group

    @property
    def associate_instance_instance_site(self):
        """Gets the associate_instance_instance_site of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_instance_site of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_site

    @associate_instance_instance_site.setter
    def associate_instance_instance_site(self, associate_instance_instance_site):
        """Sets the associate_instance_instance_site of this CountGlobalEipSegmentRequest.

        :param associate_instance_instance_site: The associate_instance_instance_site of this CountGlobalEipSegmentRequest.
        :type associate_instance_instance_site: list[str]
        """
        self._associate_instance_instance_site = associate_instance_instance_site

    @property
    def associate_instance_instance_type(self):
        """Gets the associate_instance_instance_type of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_instance_type of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_type

    @associate_instance_instance_type.setter
    def associate_instance_instance_type(self, associate_instance_instance_type):
        """Sets the associate_instance_instance_type of this CountGlobalEipSegmentRequest.

        :param associate_instance_instance_type: The associate_instance_instance_type of this CountGlobalEipSegmentRequest.
        :type associate_instance_instance_type: list[str]
        """
        self._associate_instance_instance_type = associate_instance_instance_type

    @property
    def associate_instance_instance_id(self):
        """Gets the associate_instance_instance_id of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_instance_id of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_id

    @associate_instance_instance_id.setter
    def associate_instance_instance_id(self, associate_instance_instance_id):
        """Sets the associate_instance_instance_id of this CountGlobalEipSegmentRequest.

        :param associate_instance_instance_id: The associate_instance_instance_id of this CountGlobalEipSegmentRequest.
        :type associate_instance_instance_id: list[str]
        """
        self._associate_instance_instance_id = associate_instance_instance_id

    @property
    def associate_instance_project_id(self):
        """Gets the associate_instance_project_id of this CountGlobalEipSegmentRequest.

        :return: The associate_instance_project_id of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._associate_instance_project_id

    @associate_instance_project_id.setter
    def associate_instance_project_id(self, associate_instance_project_id):
        """Sets the associate_instance_project_id of this CountGlobalEipSegmentRequest.

        :param associate_instance_project_id: The associate_instance_project_id of this CountGlobalEipSegmentRequest.
        :type associate_instance_project_id: list[str]
        """
        self._associate_instance_project_id = associate_instance_project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CountGlobalEipSegmentRequest.

        :return: The enterprise_project_id of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CountGlobalEipSegmentRequest.

        :param enterprise_project_id: The enterprise_project_id of this CountGlobalEipSegmentRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CountGlobalEipSegmentRequest.

        :return: The tags of this CountGlobalEipSegmentRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CountGlobalEipSegmentRequest.

        :param tags: The tags of this CountGlobalEipSegmentRequest.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CountGlobalEipSegmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
