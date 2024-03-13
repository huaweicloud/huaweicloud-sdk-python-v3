# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalEipSegmentsRequest:

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
        'associate_instance_instance_type': 'list[str]',
        'associate_instance_public_border_group': 'list[str]',
        'associate_instance_instance_site': 'list[str]',
        'associate_instance_instance_id': 'list[str]',
        'associate_instance_project_id': 'list[str]',
        'associate_instance_service_id': 'list[str]',
        'associate_instance_service_type': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'tags': 'list[str]'
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
        'associate_instance_instance_type': 'associate_instance.instance_type',
        'associate_instance_public_border_group': 'associate_instance.public_border_group',
        'associate_instance_instance_site': 'associate_instance.instance_site',
        'associate_instance_instance_id': 'associate_instance.instance_id',
        'associate_instance_project_id': 'associate_instance.project_id',
        'associate_instance_service_id': 'associate_instance.service_id',
        'associate_instance_service_type': 'associate_instance.service_type',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, fields=None, sort_key=None, sort_dir=None, id=None, internet_bandwidth_id=None, name=None, name_like=None, access_site=None, geip_pool_name=None, isp=None, ip_version=None, cidr=None, cidr_v6=None, freezen=None, internet_bandwidth_is_null=None, status=None, associate_instance_region=None, associate_instance_instance_type=None, associate_instance_public_border_group=None, associate_instance_instance_site=None, associate_instance_instance_id=None, associate_instance_project_id=None, associate_instance_service_id=None, associate_instance_service_type=None, enterprise_project_id=None, tags=None):
        """ListGlobalEipSegmentsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条数
        :type limit: int
        :param offset: 分页起始点
        :type offset: int
        :param marker: 分页起始点
        :type marker: str
        :param page_reverse: 翻页方向
        :type page_reverse: bool
        :param fields: 只显示指定的字段
        :type fields: list[str]
        :param sort_key: 按照sort_key指定的字段排序
        :type sort_key: list[str]
        :param sort_dir: 排序的方向，倒序或者正序
        :type sort_dir: list[str]
        :param id: 根据资源ID过滤
        :type id: list[str]
        :param internet_bandwidth_id: 根据全域公网带宽的ID过滤
        :type internet_bandwidth_id: list[str]
        :param name: 根据名称过滤
        :type name: list[str]
        :param name_like: 根据名称模糊匹配
        :type name_like: str
        :param access_site: 根据接入点过滤
        :type access_site: list[str]
        :param geip_pool_name: 根据全域弹性公网IP池名称过滤
        :type geip_pool_name: list[str]
        :param isp: 根据运营商线路过滤
        :type isp: list[str]
        :param ip_version: 根据可分配的IP版本过滤
        :type ip_version: list[int]
        :param cidr: 根据分配的CIDR过滤
        :type cidr: list[str]
        :param cidr_v6: 根据分配的IPv6 CIDR过滤
        :type cidr_v6: list[str]
        :param freezen: 根据是否冻结过滤
        :type freezen: list[bool]
        :param internet_bandwidth_is_null: 根据是否绑定全域公网带宽过滤
        :type internet_bandwidth_is_null: list[bool]
        :param status: 根据状态过滤
        :type status: list[str]
        :param associate_instance_region: 根据绑定实例所属的局点过滤
        :type associate_instance_region: list[str]
        :param associate_instance_instance_type: 根据绑定实例的类型过滤
        :type associate_instance_instance_type: list[str]
        :param associate_instance_public_border_group: 根据绑定实例所属的边缘信息过滤
        :type associate_instance_public_border_group: list[str]
        :param associate_instance_instance_site: 根据绑定实例所在的站点过滤
        :type associate_instance_instance_site: list[str]
        :param associate_instance_instance_id: 根据绑定实例的ID过滤
        :type associate_instance_instance_id: list[str]
        :param associate_instance_project_id: 根据绑定实例所属的项目ID过滤
        :type associate_instance_project_id: list[str]
        :param associate_instance_service_id: 根据绑定实例所属的服务ID过滤
        :type associate_instance_service_id: list[str]
        :param associate_instance_service_type: 根据绑定实例的服务类型过滤
        :type associate_instance_service_type: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤
        :type enterprise_project_id: list[str]
        :param tags: 根据标签过滤
        :type tags: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._fields = None
        self._sort_key = None
        self._sort_dir = None
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
        self._associate_instance_instance_type = None
        self._associate_instance_public_border_group = None
        self._associate_instance_instance_site = None
        self._associate_instance_instance_id = None
        self._associate_instance_project_id = None
        self._associate_instance_service_id = None
        self._associate_instance_service_type = None
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
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
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
        if associate_instance_instance_type is not None:
            self.associate_instance_instance_type = associate_instance_instance_type
        if associate_instance_public_border_group is not None:
            self.associate_instance_public_border_group = associate_instance_public_border_group
        if associate_instance_instance_site is not None:
            self.associate_instance_instance_site = associate_instance_instance_site
        if associate_instance_instance_id is not None:
            self.associate_instance_instance_id = associate_instance_instance_id
        if associate_instance_project_id is not None:
            self.associate_instance_project_id = associate_instance_project_id
        if associate_instance_service_id is not None:
            self.associate_instance_service_id = associate_instance_service_id
        if associate_instance_service_type is not None:
            self.associate_instance_service_type = associate_instance_service_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def limit(self):
        """Gets the limit of this ListGlobalEipSegmentsRequest.

        每页条数

        :return: The limit of this ListGlobalEipSegmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGlobalEipSegmentsRequest.

        每页条数

        :param limit: The limit of this ListGlobalEipSegmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListGlobalEipSegmentsRequest.

        分页起始点

        :return: The offset of this ListGlobalEipSegmentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGlobalEipSegmentsRequest.

        分页起始点

        :param offset: The offset of this ListGlobalEipSegmentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListGlobalEipSegmentsRequest.

        分页起始点

        :return: The marker of this ListGlobalEipSegmentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListGlobalEipSegmentsRequest.

        分页起始点

        :param marker: The marker of this ListGlobalEipSegmentsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListGlobalEipSegmentsRequest.

        翻页方向

        :return: The page_reverse of this ListGlobalEipSegmentsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListGlobalEipSegmentsRequest.

        翻页方向

        :param page_reverse: The page_reverse of this ListGlobalEipSegmentsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def fields(self):
        """Gets the fields of this ListGlobalEipSegmentsRequest.

        只显示指定的字段

        :return: The fields of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListGlobalEipSegmentsRequest.

        只显示指定的字段

        :param fields: The fields of this ListGlobalEipSegmentsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListGlobalEipSegmentsRequest.

        按照sort_key指定的字段排序

        :return: The sort_key of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListGlobalEipSegmentsRequest.

        按照sort_key指定的字段排序

        :param sort_key: The sort_key of this ListGlobalEipSegmentsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListGlobalEipSegmentsRequest.

        排序的方向，倒序或者正序

        :return: The sort_dir of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListGlobalEipSegmentsRequest.

        排序的方向，倒序或者正序

        :param sort_dir: The sort_dir of this ListGlobalEipSegmentsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListGlobalEipSegmentsRequest.

        根据资源ID过滤

        :return: The id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGlobalEipSegmentsRequest.

        根据资源ID过滤

        :param id: The id of this ListGlobalEipSegmentsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def internet_bandwidth_id(self):
        """Gets the internet_bandwidth_id of this ListGlobalEipSegmentsRequest.

        根据全域公网带宽的ID过滤

        :return: The internet_bandwidth_id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._internet_bandwidth_id

    @internet_bandwidth_id.setter
    def internet_bandwidth_id(self, internet_bandwidth_id):
        """Sets the internet_bandwidth_id of this ListGlobalEipSegmentsRequest.

        根据全域公网带宽的ID过滤

        :param internet_bandwidth_id: The internet_bandwidth_id of this ListGlobalEipSegmentsRequest.
        :type internet_bandwidth_id: list[str]
        """
        self._internet_bandwidth_id = internet_bandwidth_id

    @property
    def name(self):
        """Gets the name of this ListGlobalEipSegmentsRequest.

        根据名称过滤

        :return: The name of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGlobalEipSegmentsRequest.

        根据名称过滤

        :param name: The name of this ListGlobalEipSegmentsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def name_like(self):
        """Gets the name_like of this ListGlobalEipSegmentsRequest.

        根据名称模糊匹配

        :return: The name_like of this ListGlobalEipSegmentsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this ListGlobalEipSegmentsRequest.

        根据名称模糊匹配

        :param name_like: The name_like of this ListGlobalEipSegmentsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def access_site(self):
        """Gets the access_site of this ListGlobalEipSegmentsRequest.

        根据接入点过滤

        :return: The access_site of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ListGlobalEipSegmentsRequest.

        根据接入点过滤

        :param access_site: The access_site of this ListGlobalEipSegmentsRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def geip_pool_name(self):
        """Gets the geip_pool_name of this ListGlobalEipSegmentsRequest.

        根据全域弹性公网IP池名称过滤

        :return: The geip_pool_name of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._geip_pool_name

    @geip_pool_name.setter
    def geip_pool_name(self, geip_pool_name):
        """Sets the geip_pool_name of this ListGlobalEipSegmentsRequest.

        根据全域弹性公网IP池名称过滤

        :param geip_pool_name: The geip_pool_name of this ListGlobalEipSegmentsRequest.
        :type geip_pool_name: list[str]
        """
        self._geip_pool_name = geip_pool_name

    @property
    def isp(self):
        """Gets the isp of this ListGlobalEipSegmentsRequest.

        根据运营商线路过滤

        :return: The isp of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListGlobalEipSegmentsRequest.

        根据运营商线路过滤

        :param isp: The isp of this ListGlobalEipSegmentsRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def ip_version(self):
        """Gets the ip_version of this ListGlobalEipSegmentsRequest.

        根据可分配的IP版本过滤

        :return: The ip_version of this ListGlobalEipSegmentsRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListGlobalEipSegmentsRequest.

        根据可分配的IP版本过滤

        :param ip_version: The ip_version of this ListGlobalEipSegmentsRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        """Gets the cidr of this ListGlobalEipSegmentsRequest.

        根据分配的CIDR过滤

        :return: The cidr of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ListGlobalEipSegmentsRequest.

        根据分配的CIDR过滤

        :param cidr: The cidr of this ListGlobalEipSegmentsRequest.
        :type cidr: list[str]
        """
        self._cidr = cidr

    @property
    def cidr_v6(self):
        """Gets the cidr_v6 of this ListGlobalEipSegmentsRequest.

        根据分配的IPv6 CIDR过滤

        :return: The cidr_v6 of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._cidr_v6

    @cidr_v6.setter
    def cidr_v6(self, cidr_v6):
        """Sets the cidr_v6 of this ListGlobalEipSegmentsRequest.

        根据分配的IPv6 CIDR过滤

        :param cidr_v6: The cidr_v6 of this ListGlobalEipSegmentsRequest.
        :type cidr_v6: list[str]
        """
        self._cidr_v6 = cidr_v6

    @property
    def freezen(self):
        """Gets the freezen of this ListGlobalEipSegmentsRequest.

        根据是否冻结过滤

        :return: The freezen of this ListGlobalEipSegmentsRequest.
        :rtype: list[bool]
        """
        return self._freezen

    @freezen.setter
    def freezen(self, freezen):
        """Sets the freezen of this ListGlobalEipSegmentsRequest.

        根据是否冻结过滤

        :param freezen: The freezen of this ListGlobalEipSegmentsRequest.
        :type freezen: list[bool]
        """
        self._freezen = freezen

    @property
    def internet_bandwidth_is_null(self):
        """Gets the internet_bandwidth_is_null of this ListGlobalEipSegmentsRequest.

        根据是否绑定全域公网带宽过滤

        :return: The internet_bandwidth_is_null of this ListGlobalEipSegmentsRequest.
        :rtype: list[bool]
        """
        return self._internet_bandwidth_is_null

    @internet_bandwidth_is_null.setter
    def internet_bandwidth_is_null(self, internet_bandwidth_is_null):
        """Sets the internet_bandwidth_is_null of this ListGlobalEipSegmentsRequest.

        根据是否绑定全域公网带宽过滤

        :param internet_bandwidth_is_null: The internet_bandwidth_is_null of this ListGlobalEipSegmentsRequest.
        :type internet_bandwidth_is_null: list[bool]
        """
        self._internet_bandwidth_is_null = internet_bandwidth_is_null

    @property
    def status(self):
        """Gets the status of this ListGlobalEipSegmentsRequest.

        根据状态过滤

        :return: The status of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListGlobalEipSegmentsRequest.

        根据状态过滤

        :param status: The status of this ListGlobalEipSegmentsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def associate_instance_region(self):
        """Gets the associate_instance_region of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的局点过滤

        :return: The associate_instance_region of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_region

    @associate_instance_region.setter
    def associate_instance_region(self, associate_instance_region):
        """Sets the associate_instance_region of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的局点过滤

        :param associate_instance_region: The associate_instance_region of this ListGlobalEipSegmentsRequest.
        :type associate_instance_region: list[str]
        """
        self._associate_instance_region = associate_instance_region

    @property
    def associate_instance_instance_type(self):
        """Gets the associate_instance_instance_type of this ListGlobalEipSegmentsRequest.

        根据绑定实例的类型过滤

        :return: The associate_instance_instance_type of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_type

    @associate_instance_instance_type.setter
    def associate_instance_instance_type(self, associate_instance_instance_type):
        """Sets the associate_instance_instance_type of this ListGlobalEipSegmentsRequest.

        根据绑定实例的类型过滤

        :param associate_instance_instance_type: The associate_instance_instance_type of this ListGlobalEipSegmentsRequest.
        :type associate_instance_instance_type: list[str]
        """
        self._associate_instance_instance_type = associate_instance_instance_type

    @property
    def associate_instance_public_border_group(self):
        """Gets the associate_instance_public_border_group of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的边缘信息过滤

        :return: The associate_instance_public_border_group of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_public_border_group

    @associate_instance_public_border_group.setter
    def associate_instance_public_border_group(self, associate_instance_public_border_group):
        """Sets the associate_instance_public_border_group of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的边缘信息过滤

        :param associate_instance_public_border_group: The associate_instance_public_border_group of this ListGlobalEipSegmentsRequest.
        :type associate_instance_public_border_group: list[str]
        """
        self._associate_instance_public_border_group = associate_instance_public_border_group

    @property
    def associate_instance_instance_site(self):
        """Gets the associate_instance_instance_site of this ListGlobalEipSegmentsRequest.

        根据绑定实例所在的站点过滤

        :return: The associate_instance_instance_site of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_site

    @associate_instance_instance_site.setter
    def associate_instance_instance_site(self, associate_instance_instance_site):
        """Sets the associate_instance_instance_site of this ListGlobalEipSegmentsRequest.

        根据绑定实例所在的站点过滤

        :param associate_instance_instance_site: The associate_instance_instance_site of this ListGlobalEipSegmentsRequest.
        :type associate_instance_instance_site: list[str]
        """
        self._associate_instance_instance_site = associate_instance_instance_site

    @property
    def associate_instance_instance_id(self):
        """Gets the associate_instance_instance_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例的ID过滤

        :return: The associate_instance_instance_id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_instance_id

    @associate_instance_instance_id.setter
    def associate_instance_instance_id(self, associate_instance_instance_id):
        """Sets the associate_instance_instance_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例的ID过滤

        :param associate_instance_instance_id: The associate_instance_instance_id of this ListGlobalEipSegmentsRequest.
        :type associate_instance_instance_id: list[str]
        """
        self._associate_instance_instance_id = associate_instance_instance_id

    @property
    def associate_instance_project_id(self):
        """Gets the associate_instance_project_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的项目ID过滤

        :return: The associate_instance_project_id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_project_id

    @associate_instance_project_id.setter
    def associate_instance_project_id(self, associate_instance_project_id):
        """Sets the associate_instance_project_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的项目ID过滤

        :param associate_instance_project_id: The associate_instance_project_id of this ListGlobalEipSegmentsRequest.
        :type associate_instance_project_id: list[str]
        """
        self._associate_instance_project_id = associate_instance_project_id

    @property
    def associate_instance_service_id(self):
        """Gets the associate_instance_service_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的服务ID过滤

        :return: The associate_instance_service_id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_service_id

    @associate_instance_service_id.setter
    def associate_instance_service_id(self, associate_instance_service_id):
        """Sets the associate_instance_service_id of this ListGlobalEipSegmentsRequest.

        根据绑定实例所属的服务ID过滤

        :param associate_instance_service_id: The associate_instance_service_id of this ListGlobalEipSegmentsRequest.
        :type associate_instance_service_id: list[str]
        """
        self._associate_instance_service_id = associate_instance_service_id

    @property
    def associate_instance_service_type(self):
        """Gets the associate_instance_service_type of this ListGlobalEipSegmentsRequest.

        根据绑定实例的服务类型过滤

        :return: The associate_instance_service_type of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_service_type

    @associate_instance_service_type.setter
    def associate_instance_service_type(self, associate_instance_service_type):
        """Sets the associate_instance_service_type of this ListGlobalEipSegmentsRequest.

        根据绑定实例的服务类型过滤

        :param associate_instance_service_type: The associate_instance_service_type of this ListGlobalEipSegmentsRequest.
        :type associate_instance_service_type: list[str]
        """
        self._associate_instance_service_type = associate_instance_service_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListGlobalEipSegmentsRequest.

        根据企业项目ID过滤

        :return: The enterprise_project_id of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListGlobalEipSegmentsRequest.

        根据企业项目ID过滤

        :param enterprise_project_id: The enterprise_project_id of this ListGlobalEipSegmentsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ListGlobalEipSegmentsRequest.

        根据标签过滤

        :return: The tags of this ListGlobalEipSegmentsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListGlobalEipSegmentsRequest.

        根据标签过滤

        :param tags: The tags of this ListGlobalEipSegmentsRequest.
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
        if not isinstance(other, ListGlobalEipSegmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
