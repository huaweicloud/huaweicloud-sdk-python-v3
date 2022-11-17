# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'as_proxy': 'bool',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'with_auth': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'as_proxy': 'as_proxy',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'with_auth': 'with_auth'
    }

    def __init__(self, group_id=None, as_proxy=None, offset=None, limit=None, name=None, sort_key=None, sort_dir=None, with_auth=None):
        """ListHostsRequest

        The model defined in huaweicloud sdk

        :param group_id: 主机组id
        :type group_id: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        :param offset: 偏移量,表示从此偏移量开始查询,offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量，默认为1000
        :type limit: int
        :param name: 主机名，可输入中英文，数字和符号(-_.)
        :type name: str
        :param sort_key: 排序字段，支持：AS_PROXY|HOST_NAME|OS|OWNER_NAME|as_proxy|host_name|os|owner_name|nickName。不填默认为：as_proxy
        :type sort_key: str
        :param sort_dir: 排序方式,默认为：DESC。DESC：降序排序。ASC：升序排序
        :type sort_dir: str
        :param with_auth: 返回结果是否加密
        :type with_auth: bool
        """
        
        

        self._group_id = None
        self._as_proxy = None
        self._offset = None
        self._limit = None
        self._name = None
        self._sort_key = None
        self._sort_dir = None
        self._with_auth = None
        self.discriminator = None

        self.group_id = group_id
        if as_proxy is not None:
            self.as_proxy = as_proxy
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
        if with_auth is not None:
            self.with_auth = with_auth

    @property
    def group_id(self):
        """Gets the group_id of this ListHostsRequest.

        主机组id

        :return: The group_id of this ListHostsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListHostsRequest.

        主机组id

        :param group_id: The group_id of this ListHostsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def as_proxy(self):
        """Gets the as_proxy of this ListHostsRequest.

        是否为代理机

        :return: The as_proxy of this ListHostsRequest.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        """Sets the as_proxy of this ListHostsRequest.

        是否为代理机

        :param as_proxy: The as_proxy of this ListHostsRequest.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def offset(self):
        """Gets the offset of this ListHostsRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :return: The offset of this ListHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostsRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :param offset: The offset of this ListHostsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHostsRequest.

        每页显示的条目数量，默认为1000

        :return: The limit of this ListHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostsRequest.

        每页显示的条目数量，默认为1000

        :param limit: The limit of this ListHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListHostsRequest.

        主机名，可输入中英文，数字和符号(-_.)

        :return: The name of this ListHostsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHostsRequest.

        主机名，可输入中英文，数字和符号(-_.)

        :param name: The name of this ListHostsRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort_key(self):
        """Gets the sort_key of this ListHostsRequest.

        排序字段，支持：AS_PROXY|HOST_NAME|OS|OWNER_NAME|as_proxy|host_name|os|owner_name|nickName。不填默认为：as_proxy

        :return: The sort_key of this ListHostsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListHostsRequest.

        排序字段，支持：AS_PROXY|HOST_NAME|OS|OWNER_NAME|as_proxy|host_name|os|owner_name|nickName。不填默认为：as_proxy

        :param sort_key: The sort_key of this ListHostsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListHostsRequest.

        排序方式,默认为：DESC。DESC：降序排序。ASC：升序排序

        :return: The sort_dir of this ListHostsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListHostsRequest.

        排序方式,默认为：DESC。DESC：降序排序。ASC：升序排序

        :param sort_dir: The sort_dir of this ListHostsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def with_auth(self):
        """Gets the with_auth of this ListHostsRequest.

        返回结果是否加密

        :return: The with_auth of this ListHostsRequest.
        :rtype: bool
        """
        return self._with_auth

    @with_auth.setter
    def with_auth(self, with_auth):
        """Sets the with_auth of this ListHostsRequest.

        返回结果是否加密

        :param with_auth: The with_auth of this ListHostsRequest.
        :type with_auth: bool
        """
        self._with_auth = with_auth

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
        if not isinstance(other, ListHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
