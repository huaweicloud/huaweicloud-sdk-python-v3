# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'auth_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'auth_status': 'auth_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, auth_status=None, offset=None, limit=None):
        """ListDomainsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 域名ID
        :type domain_id: str
        :param auth_status: 域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 
        :type auth_status: str
        :param offset: 分页查询，偏移量，表示从此偏移量开始查询
        :type offset: int
        :param limit: 分页查询，每页显示的条目数量
        :type limit: int
        """
        
        

        self._domain_id = None
        self._auth_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if auth_status is not None:
            self.auth_status = auth_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        """Gets the domain_id of this ListDomainsRequest.

        域名ID

        :return: The domain_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListDomainsRequest.

        域名ID

        :param domain_id: The domain_id of this ListDomainsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def auth_status(self):
        """Gets the auth_status of this ListDomainsRequest.

        域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 

        :return: The auth_status of this ListDomainsRequest.
        :rtype: str
        """
        return self._auth_status

    @auth_status.setter
    def auth_status(self, auth_status):
        """Sets the auth_status of this ListDomainsRequest.

        域名的认证状态:   * unauth - 未认证   * auth - 已认证   * invalid - 认证文件无效   * manual - 人工认证   * skip - 免认证 

        :param auth_status: The auth_status of this ListDomainsRequest.
        :type auth_status: str
        """
        self._auth_status = auth_status

    @property
    def offset(self):
        """Gets the offset of this ListDomainsRequest.

        分页查询，偏移量，表示从此偏移量开始查询

        :return: The offset of this ListDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDomainsRequest.

        分页查询，偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDomainsRequest.

        分页查询，每页显示的条目数量

        :return: The limit of this ListDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDomainsRequest.

        分页查询，每页显示的条目数量

        :param limit: The limit of this ListDomainsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
