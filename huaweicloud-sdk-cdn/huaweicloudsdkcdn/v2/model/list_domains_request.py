# coding: utf-8

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
        'domain_name': 'str',
        'business_type': 'str',
        'domain_status': 'str',
        'service_area': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'show_tags': 'bool',
        'exact_match': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'domain_status': 'domain_status',
        'service_area': 'service_area',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'show_tags': 'show_tags',
        'exact_match': 'exact_match',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, business_type=None, domain_status=None, service_area=None, page_size=None, page_number=None, show_tags=None, exact_match=None, enterprise_project_id=None):
        r"""ListDomainsRequest

        The model defined in huaweicloud sdk

        :param domain_name: 加速域名，采用模糊匹配的方式。（长度限制为1-255字符）。
        :type domain_name: str
        :param business_type: 加速域名的业务类型。取值： - web（网站加速） - download（文件下载加速） - video（点播加速） - wholeSite（全站加速）
        :type business_type: str
        :param domain_status: 加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。
        :type domain_status: str
        :param service_area: 华为云CDN提供的加速服务范围，包含： - mainland_china 中国大陆 - outside_mainland_china 中国大陆境外 - global 全球。
        :type service_area: str
        :param page_size: 每页加速域名的数量，取值范围1-10000，默认值为30。
        :type page_size: int
        :param page_number: 查询的页码，即：从哪一页开始查询，取值范围1-65535，默认值为1。
        :type page_number: int
        :param show_tags: 展示标签标识 true：展示 false：不展示。
        :type show_tags: bool
        :param exact_match: 精准匹配 true：开启 false：关闭。
        :type exact_match: bool
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._business_type = None
        self._domain_status = None
        self._service_area = None
        self._page_size = None
        self._page_number = None
        self._show_tags = None
        self._exact_match = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if business_type is not None:
            self.business_type = business_type
        if domain_status is not None:
            self.domain_status = domain_status
        if service_area is not None:
            self.service_area = service_area
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if show_tags is not None:
            self.show_tags = show_tags
        if exact_match is not None:
            self.exact_match = exact_match
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListDomainsRequest.

        加速域名，采用模糊匹配的方式。（长度限制为1-255字符）。

        :return: The domain_name of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListDomainsRequest.

        加速域名，采用模糊匹配的方式。（长度限制为1-255字符）。

        :param domain_name: The domain_name of this ListDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        r"""Gets the business_type of this ListDomainsRequest.

        加速域名的业务类型。取值： - web（网站加速） - download（文件下载加速） - video（点播加速） - wholeSite（全站加速）

        :return: The business_type of this ListDomainsRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ListDomainsRequest.

        加速域名的业务类型。取值： - web（网站加速） - download（文件下载加速） - video（点播加速） - wholeSite（全站加速）

        :param business_type: The business_type of this ListDomainsRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def domain_status(self):
        r"""Gets the domain_status of this ListDomainsRequest.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :return: The domain_status of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        r"""Sets the domain_status of this ListDomainsRequest.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核未通过” - deleting表示“删除中”。

        :param domain_status: The domain_status of this ListDomainsRequest.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def service_area(self):
        r"""Gets the service_area of this ListDomainsRequest.

        华为云CDN提供的加速服务范围，包含： - mainland_china 中国大陆 - outside_mainland_china 中国大陆境外 - global 全球。

        :return: The service_area of this ListDomainsRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ListDomainsRequest.

        华为云CDN提供的加速服务范围，包含： - mainland_china 中国大陆 - outside_mainland_china 中国大陆境外 - global 全球。

        :param service_area: The service_area of this ListDomainsRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDomainsRequest.

        每页加速域名的数量，取值范围1-10000，默认值为30。

        :return: The page_size of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDomainsRequest.

        每页加速域名的数量，取值范围1-10000，默认值为30。

        :param page_size: The page_size of this ListDomainsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ListDomainsRequest.

        查询的页码，即：从哪一页开始查询，取值范围1-65535，默认值为1。

        :return: The page_number of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListDomainsRequest.

        查询的页码，即：从哪一页开始查询，取值范围1-65535，默认值为1。

        :param page_number: The page_number of this ListDomainsRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def show_tags(self):
        r"""Gets the show_tags of this ListDomainsRequest.

        展示标签标识 true：展示 false：不展示。

        :return: The show_tags of this ListDomainsRequest.
        :rtype: bool
        """
        return self._show_tags

    @show_tags.setter
    def show_tags(self, show_tags):
        r"""Sets the show_tags of this ListDomainsRequest.

        展示标签标识 true：展示 false：不展示。

        :param show_tags: The show_tags of this ListDomainsRequest.
        :type show_tags: bool
        """
        self._show_tags = show_tags

    @property
    def exact_match(self):
        r"""Gets the exact_match of this ListDomainsRequest.

        精准匹配 true：开启 false：关闭。

        :return: The exact_match of this ListDomainsRequest.
        :rtype: bool
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        r"""Sets the exact_match of this ListDomainsRequest.

        精准匹配 true：开启 false：关闭。

        :param exact_match: The exact_match of this ListDomainsRequest.
        :type exact_match: bool
        """
        self._exact_match = exact_match

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDomainsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDomainsRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ListDomainsRequest.
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
        if not isinstance(other, ListDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
