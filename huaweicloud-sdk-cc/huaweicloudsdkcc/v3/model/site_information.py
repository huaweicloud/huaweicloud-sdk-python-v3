# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteInformation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'project_id': 'str',
        'gateway_type': 'GatewayTypeEnum',
        'gateway_id': 'str',
        'site_code': 'str',
        'asn': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'project_id': 'project_id',
        'gateway_type': 'gateway_type',
        'gateway_id': 'gateway_id',
        'site_code': 'site_code',
        'asn': 'asn'
    }

    def __init__(self, region_id=None, project_id=None, gateway_type=None, gateway_id=None, site_code=None, asn=None):
        """SiteInformation

        The model defined in huaweicloud sdk

        :param region_id: RegionID。
        :type region_id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param gateway_type: 
        :type gateway_type: :class:`huaweicloudsdkcc.v3.GatewayTypeEnum`
        :param gateway_id: 实例ID。
        :type gateway_id: str
        :param site_code: 站点编码定义
        :type site_code: str
        :param asn: 网络实例BGP协议的AS号。
        :type asn: int
        """
        
        

        self._region_id = None
        self._project_id = None
        self._gateway_type = None
        self._gateway_id = None
        self._site_code = None
        self._asn = None
        self.discriminator = None

        self.region_id = region_id
        self.project_id = project_id
        self.gateway_type = gateway_type
        self.gateway_id = gateway_id
        self.site_code = site_code
        self.asn = asn

    @property
    def region_id(self):
        """Gets the region_id of this SiteInformation.

        RegionID。

        :return: The region_id of this SiteInformation.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this SiteInformation.

        RegionID。

        :param region_id: The region_id of this SiteInformation.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this SiteInformation.

        实例所属项目ID。

        :return: The project_id of this SiteInformation.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SiteInformation.

        实例所属项目ID。

        :param project_id: The project_id of this SiteInformation.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def gateway_type(self):
        """Gets the gateway_type of this SiteInformation.

        :return: The gateway_type of this SiteInformation.
        :rtype: :class:`huaweicloudsdkcc.v3.GatewayTypeEnum`
        """
        return self._gateway_type

    @gateway_type.setter
    def gateway_type(self, gateway_type):
        """Sets the gateway_type of this SiteInformation.

        :param gateway_type: The gateway_type of this SiteInformation.
        :type gateway_type: :class:`huaweicloudsdkcc.v3.GatewayTypeEnum`
        """
        self._gateway_type = gateway_type

    @property
    def gateway_id(self):
        """Gets the gateway_id of this SiteInformation.

        实例ID。

        :return: The gateway_id of this SiteInformation.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this SiteInformation.

        实例ID。

        :param gateway_id: The gateway_id of this SiteInformation.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def site_code(self):
        """Gets the site_code of this SiteInformation.

        站点编码定义

        :return: The site_code of this SiteInformation.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        """Sets the site_code of this SiteInformation.

        站点编码定义

        :param site_code: The site_code of this SiteInformation.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def asn(self):
        """Gets the asn of this SiteInformation.

        网络实例BGP协议的AS号。

        :return: The asn of this SiteInformation.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this SiteInformation.

        网络实例BGP协议的AS号。

        :param asn: The asn of this SiteInformation.
        :type asn: int
        """
        self._asn = asn

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
        if not isinstance(other, SiteInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
