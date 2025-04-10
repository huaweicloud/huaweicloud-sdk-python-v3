# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpOverviewsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'DomainClassificationItem',
        'attack_type': 'AttackTypeClassificationItem',
        'ip': 'IpClassificationItem',
        'url': 'UrlClassificationItem',
        'geo': 'GeoClassificationItem'
    }

    attribute_map = {
        'domain': 'domain',
        'attack_type': 'attack_type',
        'ip': 'ip',
        'url': 'url',
        'geo': 'geo'
    }

    def __init__(self, domain=None, attack_type=None, ip=None, url=None, geo=None):
        r"""ShowHttpOverviewsResponse

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkedgesec.v2.DomainClassificationItem`
        :param attack_type: 
        :type attack_type: :class:`huaweicloudsdkedgesec.v2.AttackTypeClassificationItem`
        :param ip: 
        :type ip: :class:`huaweicloudsdkedgesec.v2.IpClassificationItem`
        :param url: 
        :type url: :class:`huaweicloudsdkedgesec.v2.UrlClassificationItem`
        :param geo: 
        :type geo: :class:`huaweicloudsdkedgesec.v2.GeoClassificationItem`
        """
        
        super(ShowHttpOverviewsResponse, self).__init__()

        self._domain = None
        self._attack_type = None
        self._ip = None
        self._url = None
        self._geo = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if attack_type is not None:
            self.attack_type = attack_type
        if ip is not None:
            self.ip = ip
        if url is not None:
            self.url = url
        if geo is not None:
            self.geo = geo

    @property
    def domain(self):
        r"""Gets the domain of this ShowHttpOverviewsResponse.

        :return: The domain of this ShowHttpOverviewsResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.DomainClassificationItem`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ShowHttpOverviewsResponse.

        :param domain: The domain of this ShowHttpOverviewsResponse.
        :type domain: :class:`huaweicloudsdkedgesec.v2.DomainClassificationItem`
        """
        self._domain = domain

    @property
    def attack_type(self):
        r"""Gets the attack_type of this ShowHttpOverviewsResponse.

        :return: The attack_type of this ShowHttpOverviewsResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.AttackTypeClassificationItem`
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this ShowHttpOverviewsResponse.

        :param attack_type: The attack_type of this ShowHttpOverviewsResponse.
        :type attack_type: :class:`huaweicloudsdkedgesec.v2.AttackTypeClassificationItem`
        """
        self._attack_type = attack_type

    @property
    def ip(self):
        r"""Gets the ip of this ShowHttpOverviewsResponse.

        :return: The ip of this ShowHttpOverviewsResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.IpClassificationItem`
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ShowHttpOverviewsResponse.

        :param ip: The ip of this ShowHttpOverviewsResponse.
        :type ip: :class:`huaweicloudsdkedgesec.v2.IpClassificationItem`
        """
        self._ip = ip

    @property
    def url(self):
        r"""Gets the url of this ShowHttpOverviewsResponse.

        :return: The url of this ShowHttpOverviewsResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.UrlClassificationItem`
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowHttpOverviewsResponse.

        :param url: The url of this ShowHttpOverviewsResponse.
        :type url: :class:`huaweicloudsdkedgesec.v2.UrlClassificationItem`
        """
        self._url = url

    @property
    def geo(self):
        r"""Gets the geo of this ShowHttpOverviewsResponse.

        :return: The geo of this ShowHttpOverviewsResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.GeoClassificationItem`
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        r"""Sets the geo of this ShowHttpOverviewsResponse.

        :param geo: The geo of this ShowHttpOverviewsResponse.
        :type geo: :class:`huaweicloudsdkedgesec.v2.GeoClassificationItem`
        """
        self._geo = geo

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
        if not isinstance(other, ShowHttpOverviewsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
