# coding: utf-8

import re
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
        """DomainBody - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the domain_name of this DomainBody.

        加速域名。（ 国际英文域名：域名用字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成，各级域名之间用实点（.）连接，国际域名75个字符。注意连接符（-）不能作为域名的开头或结尾字符。）

        :return: The domain_name of this DomainBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainBody.

        加速域名。（ 国际英文域名：域名用字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成，各级域名之间用实点（.）连接，国际域名75个字符。注意连接符（-）不能作为域名的开头或结尾字符。）

        :param domain_name: The domain_name of this DomainBody.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this DomainBody.

        域名业务类型，若为web，则表示类型为静态加速；若为download，则表示业务类型为下载加速；若为video，则表示业务类型为流媒体加速；若为wholeSite，则表示业务类型为全站加速。

        :return: The business_type of this DomainBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this DomainBody.

        域名业务类型，若为web，则表示类型为静态加速；若为download，则表示业务类型为下载加速；若为video，则表示业务类型为流媒体加速；若为wholeSite，则表示业务类型为全站加速。

        :param business_type: The business_type of this DomainBody.
        :type: str
        """
        self._business_type = business_type

    @property
    def sources(self):
        """Gets the sources of this DomainBody.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :return: The sources of this DomainBody.
        :rtype: list[Sources]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DomainBody.

        源站域名或源站IP，源站为IP类型时，仅支持IPv4，如需传入多个源站IP，以多个源站对象传入，除IP其他参数请保持一致，主源站最多支持15个源站IP对象，备源站最多支持15个源站IP对象；源站为域名类型时仅支持1个源站对象。不支持IP源站和域名源站混用。

        :param sources: The sources of this DomainBody.
        :type: list[Sources]
        """
        self._sources = sources

    @property
    def service_area(self):
        """Gets the service_area of this DomainBody.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :return: The service_area of this DomainBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DomainBody.

        域名服务范围，若为mainland_china，则表示服务范围为中国大陆；若为outside_mainland_china，则表示服务范围为中国大陆境外；若为global，则表示服务范围为全球。

        :param service_area: The service_area of this DomainBody.
        :type: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DomainBody.

        企业项目ID，创建域名归属的项目。

        :return: The enterprise_project_id of this DomainBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DomainBody.

        企业项目ID，创建域名归属的项目。

        :param enterprise_project_id: The enterprise_project_id of this DomainBody.
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
        if not isinstance(other, DomainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
