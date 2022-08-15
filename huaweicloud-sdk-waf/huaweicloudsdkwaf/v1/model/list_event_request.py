# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventRequest:

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
        'recent': 'str',
        '_from': 'int',
        'to': 'int',
        'attacks': 'list[str]',
        'hosts': 'list[str]',
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'recent': 'recent',
        '_from': 'from',
        'to': 'to',
        'attacks': 'attacks',
        'hosts': 'hosts',
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, enterprise_project_id=None, recent=None, _from=None, to=None, attacks=None, hosts=None, page=None, pagesize=None):
        """ListEventRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param recent: 查询日志的时间范围（不能和from、to同时使用，同时使用以recent为准），且recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准
        :type recent: str
        :param _from: 起始时间(13位时间戳)，需要和to同时使用，不能和recent参数同时使用
        :type _from: int
        :param to: 结束时间(13位时间戳)，需要和from同时使用，不能和recent参数同时使用
        :type to: int
        :param attacks: 攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - cc: cc攻击   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 
        :type attacks: list[str]
        :param hosts: 域名id，从获取防护网站列表（ListHost）接口获取域名id
        :type hosts: list[str]
        :param page: 分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。
        :type page: int
        :param pagesize: 分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。
        :type pagesize: int
        """
        
        

        self._enterprise_project_id = None
        self._recent = None
        self.__from = None
        self._to = None
        self._attacks = None
        self._hosts = None
        self._page = None
        self._pagesize = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if recent is not None:
            self.recent = recent
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if attacks is not None:
            self.attacks = attacks
        if hosts is not None:
            self.hosts = hosts
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListEventRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListEventRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListEventRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def recent(self):
        """Gets the recent of this ListEventRequest.

        查询日志的时间范围（不能和from、to同时使用，同时使用以recent为准），且recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准

        :return: The recent of this ListEventRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        """Sets the recent of this ListEventRequest.

        查询日志的时间范围（不能和from、to同时使用，同时使用以recent为准），且recent参数与from、to必须使用其中一个。当同时使用recent参数与from、to时，以recent参数为准

        :param recent: The recent of this ListEventRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def _from(self):
        """Gets the _from of this ListEventRequest.

        起始时间(13位时间戳)，需要和to同时使用，不能和recent参数同时使用

        :return: The _from of this ListEventRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListEventRequest.

        起始时间(13位时间戳)，需要和to同时使用，不能和recent参数同时使用

        :param _from: The _from of this ListEventRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListEventRequest.

        结束时间(13位时间戳)，需要和from同时使用，不能和recent参数同时使用

        :return: The to of this ListEventRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListEventRequest.

        结束时间(13位时间戳)，需要和from同时使用，不能和recent参数同时使用

        :param to: The to of this ListEventRequest.
        :type to: int
        """
        self._to = to

    @property
    def attacks(self):
        """Gets the attacks of this ListEventRequest.

        攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - cc: cc攻击   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 

        :return: The attacks of this ListEventRequest.
        :rtype: list[str]
        """
        return self._attacks

    @attacks.setter
    def attacks(self, attacks):
        """Sets the attacks of this ListEventRequest.

        攻击类型:   - vuln：其它攻击类型   - sqli： sql注入攻击   - lfi： 本地文件包含  - cmdi：命令注入攻击   - xss：XSS攻击   - robot：恶意爬虫   - rfi：远程文件包含   - custom_custom：精准防护   - cc: cc攻击   - webshell：网站木马   - custom_whiteblackip：黑白名单拦截   - custom_geoip：地理访问控制拦截   - antitamper：防篡改   - anticrawler：反爬虫    - leakage：网站信息防泄漏   - illegal：非法请求 

        :param attacks: The attacks of this ListEventRequest.
        :type attacks: list[str]
        """
        self._attacks = attacks

    @property
    def hosts(self):
        """Gets the hosts of this ListEventRequest.

        域名id，从获取防护网站列表（ListHost）接口获取域名id

        :return: The hosts of this ListEventRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListEventRequest.

        域名id，从获取防护网站列表（ListHost）接口获取域名id

        :param hosts: The hosts of this ListEventRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def page(self):
        """Gets the page of this ListEventRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :return: The page of this ListEventRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListEventRequest.

        分页查询时，返回第几页数据。默认值为1，表示返回第1页数据。

        :param page: The page of this ListEventRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListEventRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。

        :return: The pagesize of this ListEventRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListEventRequest.

        分页查询时，每页包含多少条结果。范围1-100，默认值为10，表示每页包含10条结果。

        :param pagesize: The pagesize of this ListEventRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

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
        if not isinstance(other, ListEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
