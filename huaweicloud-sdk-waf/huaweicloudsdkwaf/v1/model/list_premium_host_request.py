# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPremiumHostRequest:

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
        'page': 'str',
        'pagesize': 'str',
        'hostname': 'str',
        'policyname': 'str',
        'protect_status': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'hostname': 'hostname',
        'policyname': 'policyname',
        'protect_status': 'protect_status'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, hostname=None, policyname=None, protect_status=None):
        r"""ListPremiumHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param page: 分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。
        :type page: str
        :param pagesize: 分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。
        :type pagesize: str
        :param hostname: 域名
        :type hostname: str
        :param policyname: 策略名称
        :type policyname: str
        :param protect_status: 域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测
        :type protect_status: int
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._hostname = None
        self._policyname = None
        self._protect_status = None
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
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPremiumHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListPremiumHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPremiumHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListPremiumHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        r"""Gets the page of this ListPremiumHostRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :return: The page of this ListPremiumHostRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListPremiumHostRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :param page: The page of this ListPremiumHostRequest.
        :type page: str
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListPremiumHostRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。

        :return: The pagesize of this ListPremiumHostRequest.
        :rtype: str
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListPremiumHostRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。如果需要一次查全部域名，该参数值填-1。

        :param pagesize: The pagesize of this ListPremiumHostRequest.
        :type pagesize: str
        """
        self._pagesize = pagesize

    @property
    def hostname(self):
        r"""Gets the hostname of this ListPremiumHostRequest.

        域名

        :return: The hostname of this ListPremiumHostRequest.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this ListPremiumHostRequest.

        域名

        :param hostname: The hostname of this ListPremiumHostRequest.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def policyname(self):
        r"""Gets the policyname of this ListPremiumHostRequest.

        策略名称

        :return: The policyname of this ListPremiumHostRequest.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        r"""Sets the policyname of this ListPremiumHostRequest.

        策略名称

        :param policyname: The policyname of this ListPremiumHostRequest.
        :type policyname: str
        """
        self._policyname = policyname

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListPremiumHostRequest.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :return: The protect_status of this ListPremiumHostRequest.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListPremiumHostRequest.

        域名防护状态：  - 0：暂停防护，WAF只转发该域名的请求，不做攻击检测  - 1：开启防护，WAF根据您配置的策略进行攻击检测

        :param protect_status: The protect_status of this ListPremiumHostRequest.
        :type protect_status: int
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ListPremiumHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
