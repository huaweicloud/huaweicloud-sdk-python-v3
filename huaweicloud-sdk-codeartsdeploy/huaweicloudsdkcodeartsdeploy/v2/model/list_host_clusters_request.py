# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'name': 'str',
        'os': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'sort_field': 'str',
        'sort_type': 'str',
        'is_proxy_mode': 'int',
        'slave_cluster_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'os': 'os',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'is_proxy_mode': 'is_proxy_mode',
        'slave_cluster_id': 'slave_cluster_id'
    }

    def __init__(self, project_id=None, name=None, os=None, page_index=None, page_size=None, sort_field=None, sort_type=None, is_proxy_mode=None, slave_cluster_id=None):
        """ListHostClustersRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param name: 主机集群模糊查询信息
        :type name: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param page_index: 页码数
        :type page_index: int
        :param page_size: 每页显示的条目数量，默认为10
        :type page_size: int
        :param sort_field: 排序字段：nick_name|name|owner_name|create_time，不传使用默认排序
        :type sort_field: str
        :param sort_type: 排序方式：DESC、ASC，默认为DESC
        :type sort_type: str
        :param is_proxy_mode: 是否为代理机
        :type is_proxy_mode: int
        :param slave_cluster_id: 自定义资源池id
        :type slave_cluster_id: str
        """
        
        

        self._project_id = None
        self._name = None
        self._os = None
        self._page_index = None
        self._page_size = None
        self._sort_field = None
        self._sort_type = None
        self._is_proxy_mode = None
        self._slave_cluster_id = None
        self.discriminator = None

        self.project_id = project_id
        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if is_proxy_mode is not None:
            self.is_proxy_mode = is_proxy_mode
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id

    @property
    def project_id(self):
        """Gets the project_id of this ListHostClustersRequest.

        项目ID

        :return: The project_id of this ListHostClustersRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListHostClustersRequest.

        项目ID

        :param project_id: The project_id of this ListHostClustersRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ListHostClustersRequest.

        主机集群模糊查询信息

        :return: The name of this ListHostClustersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHostClustersRequest.

        主机集群模糊查询信息

        :param name: The name of this ListHostClustersRequest.
        :type name: str
        """
        self._name = name

    @property
    def os(self):
        """Gets the os of this ListHostClustersRequest.

        操作系统：windows|linux

        :return: The os of this ListHostClustersRequest.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ListHostClustersRequest.

        操作系统：windows|linux

        :param os: The os of this ListHostClustersRequest.
        :type os: str
        """
        self._os = os

    @property
    def page_index(self):
        """Gets the page_index of this ListHostClustersRequest.

        页码数

        :return: The page_index of this ListHostClustersRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ListHostClustersRequest.

        页码数

        :param page_index: The page_index of this ListHostClustersRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ListHostClustersRequest.

        每页显示的条目数量，默认为10

        :return: The page_size of this ListHostClustersRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListHostClustersRequest.

        每页显示的条目数量，默认为10

        :param page_size: The page_size of this ListHostClustersRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_field(self):
        """Gets the sort_field of this ListHostClustersRequest.

        排序字段：nick_name|name|owner_name|create_time，不传使用默认排序

        :return: The sort_field of this ListHostClustersRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListHostClustersRequest.

        排序字段：nick_name|name|owner_name|create_time，不传使用默认排序

        :param sort_field: The sort_field of this ListHostClustersRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListHostClustersRequest.

        排序方式：DESC、ASC，默认为DESC

        :return: The sort_type of this ListHostClustersRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListHostClustersRequest.

        排序方式：DESC、ASC，默认为DESC

        :param sort_type: The sort_type of this ListHostClustersRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def is_proxy_mode(self):
        """Gets the is_proxy_mode of this ListHostClustersRequest.

        是否为代理机

        :return: The is_proxy_mode of this ListHostClustersRequest.
        :rtype: int
        """
        return self._is_proxy_mode

    @is_proxy_mode.setter
    def is_proxy_mode(self, is_proxy_mode):
        """Sets the is_proxy_mode of this ListHostClustersRequest.

        是否为代理机

        :param is_proxy_mode: The is_proxy_mode of this ListHostClustersRequest.
        :type is_proxy_mode: int
        """
        self._is_proxy_mode = is_proxy_mode

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this ListHostClustersRequest.

        自定义资源池id

        :return: The slave_cluster_id of this ListHostClustersRequest.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this ListHostClustersRequest.

        自定义资源池id

        :param slave_cluster_id: The slave_cluster_id of this ListHostClustersRequest.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

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
        if not isinstance(other, ListHostClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
