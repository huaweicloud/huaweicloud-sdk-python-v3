# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeWafDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_num': 'int',
        'page_size': 'int',
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'page_num': 'page_num',
        'page_size': 'page_size',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type'
    }

    def __init__(self, page_num=None, page_size=None, domain_name=None, enterprise_project_id=None, type=None):
        """ListEdgeWafDomainsRequest

        The model defined in huaweicloud sdk

        :param page_num: 页码， 0全查
        :type page_num: int
        :param page_size: 每页显示的条目数量， waf每批最大查询数量为100
        :type page_size: int
        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param type: waf域名配置类别 0 基础信息，1 waf防护配置信息
        :type type: str
        """
        
        

        self._page_num = None
        self._page_size = None
        self._domain_name = None
        self._enterprise_project_id = None
        self._type = None
        self.discriminator = None

        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type

    @property
    def page_num(self):
        """Gets the page_num of this ListEdgeWafDomainsRequest.

        页码， 0全查

        :return: The page_num of this ListEdgeWafDomainsRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListEdgeWafDomainsRequest.

        页码， 0全查

        :param page_num: The page_num of this ListEdgeWafDomainsRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListEdgeWafDomainsRequest.

        每页显示的条目数量， waf每批最大查询数量为100

        :return: The page_size of this ListEdgeWafDomainsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListEdgeWafDomainsRequest.

        每页显示的条目数量， waf每批最大查询数量为100

        :param page_size: The page_size of this ListEdgeWafDomainsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def domain_name(self):
        """Gets the domain_name of this ListEdgeWafDomainsRequest.

        域名

        :return: The domain_name of this ListEdgeWafDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListEdgeWafDomainsRequest.

        域名

        :param domain_name: The domain_name of this ListEdgeWafDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListEdgeWafDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListEdgeWafDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListEdgeWafDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListEdgeWafDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this ListEdgeWafDomainsRequest.

        waf域名配置类别 0 基础信息，1 waf防护配置信息

        :return: The type of this ListEdgeWafDomainsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListEdgeWafDomainsRequest.

        waf域名配置类别 0 基础信息，1 waf防护配置信息

        :param type: The type of this ListEdgeWafDomainsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListEdgeWafDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
