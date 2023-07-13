# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostRequest:

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
        'hostname': 'str',
        'policyname': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'hostname': 'hostname',
        'policyname': 'policyname'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, hostname=None, policyname=None):
        """ListHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param page: 分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。
        :type page: int
        :param pagesize: 分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。
        :type pagesize: int
        :param hostname: 要查询的防护域名，用于查询指定防护域名信息；可不传，查询用户云模式下所有防护域名
        :type hostname: str
        :param policyname: 防护策略名，用于查询指定防护策略下的域名，可不传
        :type policyname: str
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._hostname = None
        self._policyname = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if hostname is not None:
            self.hostname = hostname
        if policyname is not None:
            self.policyname = policyname

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        """Gets the page of this ListHostRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :return: The page of this ListHostRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListHostRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :param page: The page of this ListHostRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListHostRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。

        :return: The pagesize of this ListHostRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListHostRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。

        :param pagesize: The pagesize of this ListHostRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def hostname(self):
        """Gets the hostname of this ListHostRequest.

        要查询的防护域名，用于查询指定防护域名信息；可不传，查询用户云模式下所有防护域名

        :return: The hostname of this ListHostRequest.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ListHostRequest.

        要查询的防护域名，用于查询指定防护域名信息；可不传，查询用户云模式下所有防护域名

        :param hostname: The hostname of this ListHostRequest.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyname(self):
        """Gets the policyname of this ListHostRequest.

        防护策略名，用于查询指定防护策略下的域名，可不传

        :return: The policyname of this ListHostRequest.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        """Sets the policyname of this ListHostRequest.

        防护策略名，用于查询指定防护策略下的域名，可不传

        :param policyname: The policyname of this ListHostRequest.
        :type policyname: str
        """
        self._policyname = policyname

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
        if not isinstance(other, ListHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
