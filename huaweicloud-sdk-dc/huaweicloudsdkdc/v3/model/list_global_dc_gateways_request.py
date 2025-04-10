# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalDcGatewaysRequest:

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
        'fields': 'list[str]',
        'marker': 'str',
        'sort_key': 'str',
        'sort_dir': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'site_network_id': 'list[str]',
        'cloud_connection_id': 'list[str]',
        'status': 'list[str]',
        'global_center_network_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'fields': 'fields',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'site_network_id': 'site_network_id',
        'cloud_connection_id': 'cloud_connection_id',
        'status': 'status',
        'global_center_network_id': 'global_center_network_id'
    }

    def __init__(self, limit=None, fields=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, enterprise_project_id=None, site_network_id=None, cloud_connection_id=None, status=None, global_center_network_id=None):
        r"""ListGlobalDcGatewaysRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param fields: 显示字段列表
        :type fields: list[str]
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param id: 根据资源ID过滤实例
        :type id: list[str]
        :param name: 根据名字过滤查询，可查询多个名字。
        :type name: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤资源实例
        :type enterprise_project_id: list[str]
        :param site_network_id: 站点网络ID
        :type site_network_id: list[str]
        :param cloud_connection_id: 云连接ID
        :type cloud_connection_id: list[str]
        :param status: 根椐资源状态过滤实例
        :type status: list[str]
        :param global_center_network_id: 全球中心网络ID
        :type global_center_network_id: list[str]
        """
        
        

        self._limit = None
        self._fields = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._enterprise_project_id = None
        self._site_network_id = None
        self._cloud_connection_id = None
        self._status = None
        self._global_center_network_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if fields is not None:
            self.fields = fields
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if site_network_id is not None:
            self.site_network_id = site_network_id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if status is not None:
            self.status = status
        if global_center_network_id is not None:
            self.global_center_network_id = global_center_network_id

    @property
    def limit(self):
        r"""Gets the limit of this ListGlobalDcGatewaysRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListGlobalDcGatewaysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGlobalDcGatewaysRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListGlobalDcGatewaysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fields(self):
        r"""Gets the fields of this ListGlobalDcGatewaysRequest.

        显示字段列表

        :return: The fields of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListGlobalDcGatewaysRequest.

        显示字段列表

        :param fields: The fields of this ListGlobalDcGatewaysRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def marker(self):
        r"""Gets the marker of this ListGlobalDcGatewaysRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListGlobalDcGatewaysRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGlobalDcGatewaysRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListGlobalDcGatewaysRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListGlobalDcGatewaysRequest.

        排序字段。

        :return: The sort_key of this ListGlobalDcGatewaysRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListGlobalDcGatewaysRequest.

        排序字段。

        :param sort_key: The sort_key of this ListGlobalDcGatewaysRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListGlobalDcGatewaysRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListGlobalDcGatewaysRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListGlobalDcGatewaysRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListGlobalDcGatewaysRequest.

        根据资源ID过滤实例

        :return: The id of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGlobalDcGatewaysRequest.

        根据资源ID过滤实例

        :param id: The id of this ListGlobalDcGatewaysRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListGlobalDcGatewaysRequest.

        根据名字过滤查询，可查询多个名字。

        :return: The name of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListGlobalDcGatewaysRequest.

        根据名字过滤查询，可查询多个名字。

        :param name: The name of this ListGlobalDcGatewaysRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListGlobalDcGatewaysRequest.

        根据企业项目ID过滤资源实例

        :return: The enterprise_project_id of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListGlobalDcGatewaysRequest.

        根据企业项目ID过滤资源实例

        :param enterprise_project_id: The enterprise_project_id of this ListGlobalDcGatewaysRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def site_network_id(self):
        r"""Gets the site_network_id of this ListGlobalDcGatewaysRequest.

        站点网络ID

        :return: The site_network_id of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        r"""Sets the site_network_id of this ListGlobalDcGatewaysRequest.

        站点网络ID

        :param site_network_id: The site_network_id of this ListGlobalDcGatewaysRequest.
        :type site_network_id: list[str]
        """
        self._site_network_id = site_network_id

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this ListGlobalDcGatewaysRequest.

        云连接ID

        :return: The cloud_connection_id of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this ListGlobalDcGatewaysRequest.

        云连接ID

        :param cloud_connection_id: The cloud_connection_id of this ListGlobalDcGatewaysRequest.
        :type cloud_connection_id: list[str]
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def status(self):
        r"""Gets the status of this ListGlobalDcGatewaysRequest.

        根椐资源状态过滤实例

        :return: The status of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGlobalDcGatewaysRequest.

        根椐资源状态过滤实例

        :param status: The status of this ListGlobalDcGatewaysRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def global_center_network_id(self):
        r"""Gets the global_center_network_id of this ListGlobalDcGatewaysRequest.

        全球中心网络ID

        :return: The global_center_network_id of this ListGlobalDcGatewaysRequest.
        :rtype: list[str]
        """
        return self._global_center_network_id

    @global_center_network_id.setter
    def global_center_network_id(self, global_center_network_id):
        r"""Sets the global_center_network_id of this ListGlobalDcGatewaysRequest.

        全球中心网络ID

        :param global_center_network_id: The global_center_network_id of this ListGlobalDcGatewaysRequest.
        :type global_center_network_id: list[str]
        """
        self._global_center_network_id = global_center_network_id

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
        if not isinstance(other, ListGlobalDcGatewaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
