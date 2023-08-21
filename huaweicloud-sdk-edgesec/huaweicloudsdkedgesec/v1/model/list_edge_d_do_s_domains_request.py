# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeDDoSDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, offset=None, limit=None):
        """ListEdgeDDoSDomainsRequest

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_name(self):
        """Gets the domain_name of this ListEdgeDDoSDomainsRequest.

        域名

        :return: The domain_name of this ListEdgeDDoSDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListEdgeDDoSDomainsRequest.

        域名

        :param domain_name: The domain_name of this ListEdgeDDoSDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListEdgeDDoSDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListEdgeDDoSDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListEdgeDDoSDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListEdgeDDoSDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListEdgeDDoSDomainsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListEdgeDDoSDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEdgeDDoSDomainsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListEdgeDDoSDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEdgeDDoSDomainsRequest.

        每页显示的条目数量

        :return: The limit of this ListEdgeDDoSDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeDDoSDomainsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListEdgeDDoSDomainsRequest.
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
        if not isinstance(other, ListEdgeDDoSDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
