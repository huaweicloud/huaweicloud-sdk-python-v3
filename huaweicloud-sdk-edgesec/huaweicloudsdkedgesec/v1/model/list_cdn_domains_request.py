# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'domain_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, offset=None, limit=None, domain_name=None, enterprise_project_id=None):
        """ListCdnDomainsRequest

        The model defined in huaweicloud sdk

        :param offset: 分页查询参数，偏移量
        :type offset: int
        :param limit: 分页查询参数，每页显示limit条记录
        :type limit: int
        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._domain_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListCdnDomainsRequest.

        分页查询参数，偏移量

        :return: The offset of this ListCdnDomainsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCdnDomainsRequest.

        分页查询参数，偏移量

        :param offset: The offset of this ListCdnDomainsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCdnDomainsRequest.

        分页查询参数，每页显示limit条记录

        :return: The limit of this ListCdnDomainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCdnDomainsRequest.

        分页查询参数，每页显示limit条记录

        :param limit: The limit of this ListCdnDomainsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def domain_name(self):
        """Gets the domain_name of this ListCdnDomainsRequest.

        域名

        :return: The domain_name of this ListCdnDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListCdnDomainsRequest.

        域名

        :param domain_name: The domain_name of this ListCdnDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCdnDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListCdnDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCdnDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListCdnDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListCdnDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
