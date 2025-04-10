# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainBody:

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
        'sources': 'list[Sources]',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'sources': 'sources',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, business_type=None, sources=None, service_area=None, enterprise_project_id=None):
        r"""DomainBody

        The model defined in huaweicloud sdk

        :param domain_name: 加速域名。（ 由字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成，各级域名之间用（.）连接，域名长度不超过75个字符。连接符（-）不能作为域名的开头或结尾字符。）
        :type domain_name: str
        :param business_type: 域名业务类型，若为web，则表示类型为网页加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示业务类型为全站加速。
        :type business_type: str
        :param sources: 源站配置。
        :type sources: list[:class:`huaweicloudsdkcdn.v1.Sources`]
        :param service_area: 域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。
        :type service_area: str
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示添加加速域名到该企业项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._business_type = None
        self._sources = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain_name = domain_name
        self.business_type = business_type
        self.sources = sources
        self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DomainBody.

        加速域名。（ 由字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成，各级域名之间用（.）连接，域名长度不超过75个字符。连接符（-）不能作为域名的开头或结尾字符。）

        :return: The domain_name of this DomainBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DomainBody.

        加速域名。（ 由字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成，各级域名之间用（.）连接，域名长度不超过75个字符。连接符（-）不能作为域名的开头或结尾字符。）

        :param domain_name: The domain_name of this DomainBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        r"""Gets the business_type of this DomainBody.

        域名业务类型，若为web，则表示类型为网页加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示业务类型为全站加速。

        :return: The business_type of this DomainBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this DomainBody.

        域名业务类型，若为web，则表示类型为网页加速；若为download，则表示业务类型为文件下载加速；若为video，则表示业务类型为点播加速；若为wholeSite，则表示业务类型为全站加速。

        :param business_type: The business_type of this DomainBody.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def sources(self):
        r"""Gets the sources of this DomainBody.

        源站配置。

        :return: The sources of this DomainBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.Sources`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this DomainBody.

        源站配置。

        :param sources: The sources of this DomainBody.
        :type sources: list[:class:`huaweicloudsdkcdn.v1.Sources`]
        """
        self._sources = sources

    @property
    def service_area(self):
        r"""Gets the service_area of this DomainBody.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :return: The service_area of this DomainBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this DomainBody.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :param service_area: The service_area of this DomainBody.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DomainBody.

        当用户开启企业项目功能时，该参数生效，表示添加加速域名到该企业项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :return: The enterprise_project_id of this DomainBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DomainBody.

        当用户开启企业项目功能时，该参数生效，表示添加加速域名到该企业项目。注意：当使用子帐号调用接口时，该参数必传。  您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this DomainBody.
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
        if not isinstance(other, DomainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
