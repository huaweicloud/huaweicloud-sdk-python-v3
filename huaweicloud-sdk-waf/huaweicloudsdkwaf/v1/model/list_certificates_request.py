# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'page': 'int',
        'pagesize': 'int',
        'name': 'str',
        'host': 'bool',
        'exp_status': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name',
        'host': 'host',
        'exp_status': 'exp_status'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, name=None, host=None, exp_status=None):
        """ListCertificatesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param page: 分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。
        :type page: int
        :param pagesize: 分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。
        :type pagesize: int
        :param name: 证书名称
        :type name: str
        :param host: 是否获取证书关联的域名，默认为false   -true:获取已关联域名的证书   -false:获取未关联域名的证书
        :type host: bool
        :param exp_status: 证书过期状态，0-未过期，1-已过期，2-即将过期（证书将在一个月内过期）
        :type exp_status: int
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._name = None
        self._host = None
        self._exp_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if exp_status is not None:
            self.exp_status = exp_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCertificatesRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCertificatesRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListCertificatesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        """Gets the page of this ListCertificatesRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :return: The page of this ListCertificatesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCertificatesRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :param page: The page of this ListCertificatesRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListCertificatesRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。

        :return: The pagesize of this ListCertificatesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListCertificatesRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。

        :param pagesize: The pagesize of this ListCertificatesRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.

        证书名称

        :return: The name of this ListCertificatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.

        证书名称

        :param name: The name of this ListCertificatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def host(self):
        """Gets the host of this ListCertificatesRequest.

        是否获取证书关联的域名，默认为false   -true:获取已关联域名的证书   -false:获取未关联域名的证书

        :return: The host of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ListCertificatesRequest.

        是否获取证书关联的域名，默认为false   -true:获取已关联域名的证书   -false:获取未关联域名的证书

        :param host: The host of this ListCertificatesRequest.
        :type host: bool
        """
        self._host = host

    @property
    def exp_status(self):
        """Gets the exp_status of this ListCertificatesRequest.

        证书过期状态，0-未过期，1-已过期，2-即将过期（证书将在一个月内过期）

        :return: The exp_status of this ListCertificatesRequest.
        :rtype: int
        """
        return self._exp_status

    @exp_status.setter
    def exp_status(self, exp_status):
        """Sets the exp_status of this ListCertificatesRequest.

        证书过期状态，0-未过期，1-已过期，2-即将过期（证书将在一个月内过期）

        :param exp_status: The exp_status of this ListCertificatesRequest.
        :type exp_status: int
        """
        self._exp_status = exp_status

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
