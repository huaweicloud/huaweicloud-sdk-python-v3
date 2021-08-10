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
        'domain_name': 'str',
        'business_type': 'str',
        'domain_status': 'str',
        'service_area': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'domain_status': 'domain_status',
        'service_area': 'service_area',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, business_type=None, domain_status=None, service_area=None, page_size=None, page_number=None, enterprise_project_id=None):
        """ListDomainsRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_name = None
        self._business_type = None
        self._domain_status = None
        self._service_area = None
        self._page_size = None
        self._page_number = None
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ListDomainsRequest.

        加速域名，采用模糊匹配的方式。（长度限制为1-255字符）。

        :return: The domain_name of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListDomainsRequest.

        加速域名，采用模糊匹配的方式。（长度限制为1-255字符）。

        :param domain_name: The domain_name of this ListDomainsRequest.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this ListDomainsRequest.

        加速域名的业务类型。取值： - web（图片及小文件分发） - download（大文件下载加速） - video（视音频点播加速） - wholeSite（全站加速）

        :return: The business_type of this ListDomainsRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this ListDomainsRequest.

        加速域名的业务类型。取值： - web（图片及小文件分发） - download（大文件下载加速） - video（视音频点播加速） - wholeSite（全站加速）

        :param business_type: The business_type of this ListDomainsRequest.
        :type: str
        """
        self._business_type = business_type

    @property
    def domain_status(self):
        """Gets the domain_status of this ListDomainsRequest.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核失败” - deleting表示“删除中”。

        :return: The domain_status of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this ListDomainsRequest.

        加速域名状态。取值意义： - online表示“已开启” - offline表示“已停用” - configuring表示“配置中” - configure_failed表示“配置失败” - checking表示“审核中” - check_failed表示“审核失败” - deleting表示“删除中”。

        :param domain_status: The domain_status of this ListDomainsRequest.
        :type: str
        """
        self._domain_status = domain_status

    @property
    def service_area(self):
        """Gets the service_area of this ListDomainsRequest.

        华为云CDN提供的加速服务范围，包含： - mainland_china 中国大陆 - outside_mainland_china 中国大陆境外 - global 全球。

        :return: The service_area of this ListDomainsRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ListDomainsRequest.

        华为云CDN提供的加速服务范围，包含： - mainland_china 中国大陆 - outside_mainland_china 中国大陆境外 - global 全球。

        :param service_area: The service_area of this ListDomainsRequest.
        :type: str
        """
        self._service_area = service_area

    @property
    def page_size(self):
        """Gets the page_size of this ListDomainsRequest.

        每页的数量，取值范围1-10000，不设值时默认值为30。

        :return: The page_size of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListDomainsRequest.

        每页的数量，取值范围1-10000，不设值时默认值为30。

        :param page_size: The page_size of this ListDomainsRequest.
        :type: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ListDomainsRequest.

        查询的页码。取值范围1-65535，不设值时默认值为1。

        :return: The page_number of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListDomainsRequest.

        查询的页码。取值范围1-65535，不设值时默认值为1。

        :param page_number: The page_number of this ListDomainsRequest.
        :type: int
        """
        self._page_number = page_number

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDomainsRequest.

        企业项目ID。该参数仅对开启了企业项目功能的用户生效，不传表示查询default项目。\"ALL\"表示查询所有该用户已授权项目的资源。

        :return: The enterprise_project_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDomainsRequest.

        企业项目ID。该参数仅对开启了企业项目功能的用户生效，不传表示查询default项目。\"ALL\"表示查询所有该用户已授权项目的资源。

        :param enterprise_project_id: The enterprise_project_id of this ListDomainsRequest.
        :type: str
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
