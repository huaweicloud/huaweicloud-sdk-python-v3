# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostGroupsRequest:

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
        'region_name': 'str',
        'os': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'region_name': 'region_name',
        'os': 'os',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_id=None, region_name=None, os=None, offset=None, limit=None, name=None, sort_key=None, sort_dir=None):
        r"""ListHostGroupsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param region_name: 局点信息
        :type region_name: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param offset: 偏移量,表示从此偏移量开始查询,offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量，默认为1000
        :type limit: int
        :param name: 主机集群名
        :type name: str
        :param sort_key: 排序字段：nickName|NAME|OWNER_NAME|CREATE_TIME|name|owner_name|create_time，不传使用默认排序
        :type sort_key: str
        :param sort_dir: 排序方式：DESC、ASC，默认为DESC
        :type sort_dir: str
        """
        
        

        self._project_id = None
        self._region_name = None
        self._os = None
        self._offset = None
        self._limit = None
        self._name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.project_id = project_id
        self.region_name = region_name
        if os is not None:
            self.os = os
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def project_id(self):
        r"""Gets the project_id of this ListHostGroupsRequest.

        项目id

        :return: The project_id of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListHostGroupsRequest.

        项目id

        :param project_id: The project_id of this ListHostGroupsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_name(self):
        r"""Gets the region_name of this ListHostGroupsRequest.

        局点信息

        :return: The region_name of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ListHostGroupsRequest.

        局点信息

        :param region_name: The region_name of this ListHostGroupsRequest.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def os(self):
        r"""Gets the os of this ListHostGroupsRequest.

        操作系统：windows|linux

        :return: The os of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ListHostGroupsRequest.

        操作系统：windows|linux

        :param os: The os of this ListHostGroupsRequest.
        :type os: str
        """
        self._os = os

    @property
    def offset(self):
        r"""Gets the offset of this ListHostGroupsRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :return: The offset of this ListHostGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostGroupsRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :param offset: The offset of this ListHostGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHostGroupsRequest.

        每页显示的条目数量，默认为1000

        :return: The limit of this ListHostGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostGroupsRequest.

        每页显示的条目数量，默认为1000

        :param limit: The limit of this ListHostGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListHostGroupsRequest.

        主机集群名

        :return: The name of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListHostGroupsRequest.

        主机集群名

        :param name: The name of this ListHostGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListHostGroupsRequest.

        排序字段：nickName|NAME|OWNER_NAME|CREATE_TIME|name|owner_name|create_time，不传使用默认排序

        :return: The sort_key of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListHostGroupsRequest.

        排序字段：nickName|NAME|OWNER_NAME|CREATE_TIME|name|owner_name|create_time，不传使用默认排序

        :param sort_key: The sort_key of this ListHostGroupsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListHostGroupsRequest.

        排序方式：DESC、ASC，默认为DESC

        :return: The sort_dir of this ListHostGroupsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListHostGroupsRequest.

        排序方式：DESC、ASC，默认为DESC

        :param sort_dir: The sort_dir of this ListHostGroupsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListHostGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
