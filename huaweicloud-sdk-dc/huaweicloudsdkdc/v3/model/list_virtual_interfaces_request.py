# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVirtualInterfacesRequest:

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
        'marker': 'str',
        'fields': 'list[str]',
        'sort_dir': 'list[str]',
        'sort_key': 'str',
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'status': 'list[str]',
        'direct_connect_id': 'list[str]',
        'vgw_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'fields': 'fields',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'status': 'status',
        'direct_connect_id': 'direct_connect_id',
        'vgw_id': 'vgw_id'
    }

    def __init__(self, limit=None, marker=None, fields=None, sort_dir=None, sort_key=None, enterprise_project_id=None, id=None, status=None, direct_connect_id=None, vgw_id=None):
        r"""ListVirtualInterfacesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param sort_key: 排序字段。
        :type sort_key: str
        :param enterprise_project_id: 根据企业项目ID过滤资源实例
        :type enterprise_project_id: list[str]
        :param id: 根据资源ID过滤实例
        :type id: list[str]
        :param status: 根椐资源状态过滤实例
        :type status: list[str]
        :param direct_connect_id: 根椐物理专线ID过滤查询实例信息
        :type direct_connect_id: list[str]
        :param vgw_id: 根椐虚拟网关ID过滤查询实例信息
        :type vgw_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._fields = None
        self._sort_dir = None
        self._sort_key = None
        self._enterprise_project_id = None
        self._id = None
        self._status = None
        self._direct_connect_id = None
        self._vgw_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if fields is not None:
            self.fields = fields
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if direct_connect_id is not None:
            self.direct_connect_id = direct_connect_id
        if vgw_id is not None:
            self.vgw_id = vgw_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVirtualInterfacesRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListVirtualInterfacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVirtualInterfacesRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListVirtualInterfacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVirtualInterfacesRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListVirtualInterfacesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVirtualInterfacesRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListVirtualInterfacesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def fields(self):
        r"""Gets the fields of this ListVirtualInterfacesRequest.

        显示字段列表

        :return: The fields of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ListVirtualInterfacesRequest.

        显示字段列表

        :param fields: The fields of this ListVirtualInterfacesRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListVirtualInterfacesRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListVirtualInterfacesRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListVirtualInterfacesRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListVirtualInterfacesRequest.

        排序字段。

        :return: The sort_key of this ListVirtualInterfacesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListVirtualInterfacesRequest.

        排序字段。

        :param sort_key: The sort_key of this ListVirtualInterfacesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVirtualInterfacesRequest.

        根据企业项目ID过滤资源实例

        :return: The enterprise_project_id of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVirtualInterfacesRequest.

        根据企业项目ID过滤资源实例

        :param enterprise_project_id: The enterprise_project_id of this ListVirtualInterfacesRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ListVirtualInterfacesRequest.

        根据资源ID过滤实例

        :return: The id of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVirtualInterfacesRequest.

        根据资源ID过滤实例

        :param id: The id of this ListVirtualInterfacesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ListVirtualInterfacesRequest.

        根椐资源状态过滤实例

        :return: The status of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVirtualInterfacesRequest.

        根椐资源状态过滤实例

        :param status: The status of this ListVirtualInterfacesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def direct_connect_id(self):
        r"""Gets the direct_connect_id of this ListVirtualInterfacesRequest.

        根椐物理专线ID过滤查询实例信息

        :return: The direct_connect_id of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._direct_connect_id

    @direct_connect_id.setter
    def direct_connect_id(self, direct_connect_id):
        r"""Sets the direct_connect_id of this ListVirtualInterfacesRequest.

        根椐物理专线ID过滤查询实例信息

        :param direct_connect_id: The direct_connect_id of this ListVirtualInterfacesRequest.
        :type direct_connect_id: list[str]
        """
        self._direct_connect_id = direct_connect_id

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ListVirtualInterfacesRequest.

        根椐虚拟网关ID过滤查询实例信息

        :return: The vgw_id of this ListVirtualInterfacesRequest.
        :rtype: list[str]
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ListVirtualInterfacesRequest.

        根椐虚拟网关ID过滤查询实例信息

        :param vgw_id: The vgw_id of this ListVirtualInterfacesRequest.
        :type vgw_id: list[str]
        """
        self._vgw_id = vgw_id

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
        if not isinstance(other, ListVirtualInterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
