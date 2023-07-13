# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDomainCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'domain_type': 'str',
        'region': 'str',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'region': 'region',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain=None, domain_type=None, region=None, service_area=None, enterprise_project_id=None):
        """LiveDomainCreateReq

        The model defined in huaweicloud sdk

        :param domain: 直播域名
        :type domain: str
        :param domain_type: 域名类型 - pull表示播放域名 - push表示推流域名 
        :type domain_type: str
        :param region: 直播所属的直播中心
        :type region: str
        :param service_area: 域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 
        :type service_area: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._domain = None
        self._domain_type = None
        self._region = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain = domain
        self.domain_type = domain_type
        self.region = region
        if service_area is not None:
            self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain(self):
        """Gets the domain of this LiveDomainCreateReq.

        直播域名

        :return: The domain of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LiveDomainCreateReq.

        直播域名

        :param domain: The domain of this LiveDomainCreateReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def domain_type(self):
        """Gets the domain_type of this LiveDomainCreateReq.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :return: The domain_type of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this LiveDomainCreateReq.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :param domain_type: The domain_type of this LiveDomainCreateReq.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def region(self):
        """Gets the region of this LiveDomainCreateReq.

        直播所属的直播中心

        :return: The region of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this LiveDomainCreateReq.

        直播所属的直播中心

        :param region: The region of this LiveDomainCreateReq.
        :type region: str
        """
        self._region = region

    @property
    def service_area(self):
        """Gets the service_area of this LiveDomainCreateReq.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :return: The service_area of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this LiveDomainCreateReq.

        域名应用区域 - mainland_china表示中国大陆区域 - outside_mainland_china表示中国大陆以外区域 

        :param service_area: The service_area of this LiveDomainCreateReq.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LiveDomainCreateReq.

        企业项目ID

        :return: The enterprise_project_id of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LiveDomainCreateReq.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this LiveDomainCreateReq.
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
        if not isinstance(other, LiveDomainCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
