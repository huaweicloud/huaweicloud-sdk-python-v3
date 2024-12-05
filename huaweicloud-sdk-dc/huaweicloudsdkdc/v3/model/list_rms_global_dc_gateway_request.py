# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRmsGlobalDcGatewayRequest:

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
        'rp_name': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'resource_type': 'str',
        'fields': 'list[str]',
        'ext_fields': 'list[str]',
        'sort_key': 'str',
        'sort_dir': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'global_center_network_id': 'list[str]',
        'site_network_id': 'list[str]',
        'cloud_connection_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'rp_name': 'rp_name',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'resource_type': 'resource_type',
        'fields': 'fields',
        'ext_fields': 'ext_fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'global_center_network_id': 'global_center_network_id',
        'site_network_id': 'site_network_id',
        'cloud_connection_id': 'cloud_connection_id'
    }

    def __init__(self, limit=None, offset=None, marker=None, page_reverse=None, rp_name=None, domain_id=None, region_id=None, resource_type=None, fields=None, ext_fields=None, sort_key=None, sort_dir=None, id=None, name=None, status=None, enterprise_project_id=None, global_center_network_id=None, site_network_id=None, cloud_connection_id=None):
        """ListRmsGlobalDcGatewayRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param offset: 
        :type offset: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param page_reverse: 
        :type page_reverse: bool
        :param rp_name: 通过rp_name过滤记录
        :type rp_name: str
        :param domain_id: domain_id
        :type domain_id: str
        :param region_id: region_id
        :type region_id: str
        :param resource_type: resource_type
        :type resource_type: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param id: 根据资源ID过滤实例
        :type id: list[str]
        :param name: 根据名字过滤查询，可查询多个名字。
        :type name: list[str]
        :param status: 根椐资源状态过淲实例
        :type status: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤资源实例
        :type enterprise_project_id: list[str]
        :param global_center_network_id: 全球中心网络ID
        :type global_center_network_id: list[str]
        :param site_network_id: 站点网络ID
        :type site_network_id: list[str]
        :param cloud_connection_id: 云连接ID
        :type cloud_connection_id: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._marker = None
        self._page_reverse = None
        self._rp_name = None
        self._domain_id = None
        self._region_id = None
        self._resource_type = None
        self._fields = None
        self._ext_fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._status = None
        self._enterprise_project_id = None
        self._global_center_network_id = None
        self._site_network_id = None
        self._cloud_connection_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        self.rp_name = rp_name
        self.domain_id = domain_id
        self.region_id = region_id
        self.resource_type = resource_type
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
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_center_network_id is not None:
            self.global_center_network_id = global_center_network_id
        if site_network_id is not None:
            self.site_network_id = site_network_id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id

    @property
    def limit(self):
        """Gets the limit of this ListRmsGlobalDcGatewayRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListRmsGlobalDcGatewayRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRmsGlobalDcGatewayRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListRmsGlobalDcGatewayRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRmsGlobalDcGatewayRequest.

        :return: The offset of this ListRmsGlobalDcGatewayRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRmsGlobalDcGatewayRequest.

        :param offset: The offset of this ListRmsGlobalDcGatewayRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListRmsGlobalDcGatewayRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRmsGlobalDcGatewayRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListRmsGlobalDcGatewayRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListRmsGlobalDcGatewayRequest.

        :return: The page_reverse of this ListRmsGlobalDcGatewayRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListRmsGlobalDcGatewayRequest.

        :param page_reverse: The page_reverse of this ListRmsGlobalDcGatewayRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def rp_name(self):
        """Gets the rp_name of this ListRmsGlobalDcGatewayRequest.

        通过rp_name过滤记录

        :return: The rp_name of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._rp_name

    @rp_name.setter
    def rp_name(self, rp_name):
        """Sets the rp_name of this ListRmsGlobalDcGatewayRequest.

        通过rp_name过滤记录

        :param rp_name: The rp_name of this ListRmsGlobalDcGatewayRequest.
        :type rp_name: str
        """
        self._rp_name = rp_name

    @property
    def domain_id(self):
        """Gets the domain_id of this ListRmsGlobalDcGatewayRequest.

        domain_id

        :return: The domain_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListRmsGlobalDcGatewayRequest.

        domain_id

        :param domain_id: The domain_id of this ListRmsGlobalDcGatewayRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        """Gets the region_id of this ListRmsGlobalDcGatewayRequest.

        region_id

        :return: The region_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListRmsGlobalDcGatewayRequest.

        region_id

        :param region_id: The region_id of this ListRmsGlobalDcGatewayRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ListRmsGlobalDcGatewayRequest.

        resource_type

        :return: The resource_type of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListRmsGlobalDcGatewayRequest.

        resource_type

        :param resource_type: The resource_type of this ListRmsGlobalDcGatewayRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def fields(self):
        """Gets the fields of this ListRmsGlobalDcGatewayRequest.

        显示字段列表

        :return: The fields of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListRmsGlobalDcGatewayRequest.

        显示字段列表

        :param fields: The fields of this ListRmsGlobalDcGatewayRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        """Gets the ext_fields of this ListRmsGlobalDcGatewayRequest.

        show response ext-fields

        :return: The ext_fields of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        """Sets the ext_fields of this ListRmsGlobalDcGatewayRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ListRmsGlobalDcGatewayRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListRmsGlobalDcGatewayRequest.

        排序字段。

        :return: The sort_key of this ListRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListRmsGlobalDcGatewayRequest.

        排序字段。

        :param sort_key: The sort_key of this ListRmsGlobalDcGatewayRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListRmsGlobalDcGatewayRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListRmsGlobalDcGatewayRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListRmsGlobalDcGatewayRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListRmsGlobalDcGatewayRequest.

        根据资源ID过滤实例

        :return: The id of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRmsGlobalDcGatewayRequest.

        根据资源ID过滤实例

        :param id: The id of this ListRmsGlobalDcGatewayRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListRmsGlobalDcGatewayRequest.

        根据名字过滤查询，可查询多个名字。

        :return: The name of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRmsGlobalDcGatewayRequest.

        根据名字过滤查询，可查询多个名字。

        :param name: The name of this ListRmsGlobalDcGatewayRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListRmsGlobalDcGatewayRequest.

        根椐资源状态过淲实例

        :return: The status of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRmsGlobalDcGatewayRequest.

        根椐资源状态过淲实例

        :param status: The status of this ListRmsGlobalDcGatewayRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListRmsGlobalDcGatewayRequest.

        根据企业项目ID过滤资源实例

        :return: The enterprise_project_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListRmsGlobalDcGatewayRequest.

        根据企业项目ID过滤资源实例

        :param enterprise_project_id: The enterprise_project_id of this ListRmsGlobalDcGatewayRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_center_network_id(self):
        """Gets the global_center_network_id of this ListRmsGlobalDcGatewayRequest.

        全球中心网络ID

        :return: The global_center_network_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._global_center_network_id

    @global_center_network_id.setter
    def global_center_network_id(self, global_center_network_id):
        """Sets the global_center_network_id of this ListRmsGlobalDcGatewayRequest.

        全球中心网络ID

        :param global_center_network_id: The global_center_network_id of this ListRmsGlobalDcGatewayRequest.
        :type global_center_network_id: list[str]
        """
        self._global_center_network_id = global_center_network_id

    @property
    def site_network_id(self):
        """Gets the site_network_id of this ListRmsGlobalDcGatewayRequest.

        站点网络ID

        :return: The site_network_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        """Sets the site_network_id of this ListRmsGlobalDcGatewayRequest.

        站点网络ID

        :param site_network_id: The site_network_id of this ListRmsGlobalDcGatewayRequest.
        :type site_network_id: list[str]
        """
        self._site_network_id = site_network_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this ListRmsGlobalDcGatewayRequest.

        云连接ID

        :return: The cloud_connection_id of this ListRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this ListRmsGlobalDcGatewayRequest.

        云连接ID

        :param cloud_connection_id: The cloud_connection_id of this ListRmsGlobalDcGatewayRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

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
        if not isinstance(other, ListRmsGlobalDcGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
