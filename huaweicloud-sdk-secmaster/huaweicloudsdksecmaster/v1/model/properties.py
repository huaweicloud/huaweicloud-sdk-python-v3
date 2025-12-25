# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Properties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hwc_ecs': 'HwcEcs',
        'hwc_eip': 'HwcEip',
        'hwc_vpc': 'HwcVpc',
        'hwc_subnet': 'HwcSubnet',
        'hwc_rds': 'HwcRds',
        'hwc_domain': 'HwcDomain',
        'website': 'Website',
        'oca_ip': 'OcaIp'
    }

    attribute_map = {
        'hwc_ecs': 'hwc_ecs',
        'hwc_eip': 'hwc_eip',
        'hwc_vpc': 'hwc_vpc',
        'hwc_subnet': 'hwc_subnet',
        'hwc_rds': 'hwc_rds',
        'hwc_domain': 'hwc_domain',
        'website': 'website',
        'oca_ip': 'oca_ip'
    }

    def __init__(self, hwc_ecs=None, hwc_eip=None, hwc_vpc=None, hwc_subnet=None, hwc_rds=None, hwc_domain=None, website=None, oca_ip=None):
        r"""Properties

        The model defined in huaweicloud sdk

        :param hwc_ecs: 
        :type hwc_ecs: :class:`huaweicloudsdksecmaster.v1.HwcEcs`
        :param hwc_eip: 
        :type hwc_eip: :class:`huaweicloudsdksecmaster.v1.HwcEip`
        :param hwc_vpc: 
        :type hwc_vpc: :class:`huaweicloudsdksecmaster.v1.HwcVpc`
        :param hwc_subnet: 
        :type hwc_subnet: :class:`huaweicloudsdksecmaster.v1.HwcSubnet`
        :param hwc_rds: 
        :type hwc_rds: :class:`huaweicloudsdksecmaster.v1.HwcRds`
        :param hwc_domain: 
        :type hwc_domain: :class:`huaweicloudsdksecmaster.v1.HwcDomain`
        :param website: 
        :type website: :class:`huaweicloudsdksecmaster.v1.Website`
        :param oca_ip: 
        :type oca_ip: :class:`huaweicloudsdksecmaster.v1.OcaIp`
        """
        
        

        self._hwc_ecs = None
        self._hwc_eip = None
        self._hwc_vpc = None
        self._hwc_subnet = None
        self._hwc_rds = None
        self._hwc_domain = None
        self._website = None
        self._oca_ip = None
        self.discriminator = None

        if hwc_ecs is not None:
            self.hwc_ecs = hwc_ecs
        if hwc_eip is not None:
            self.hwc_eip = hwc_eip
        if hwc_vpc is not None:
            self.hwc_vpc = hwc_vpc
        if hwc_subnet is not None:
            self.hwc_subnet = hwc_subnet
        if hwc_rds is not None:
            self.hwc_rds = hwc_rds
        if hwc_domain is not None:
            self.hwc_domain = hwc_domain
        if website is not None:
            self.website = website
        if oca_ip is not None:
            self.oca_ip = oca_ip

    @property
    def hwc_ecs(self):
        r"""Gets the hwc_ecs of this Properties.

        :return: The hwc_ecs of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEcs`
        """
        return self._hwc_ecs

    @hwc_ecs.setter
    def hwc_ecs(self, hwc_ecs):
        r"""Sets the hwc_ecs of this Properties.

        :param hwc_ecs: The hwc_ecs of this Properties.
        :type hwc_ecs: :class:`huaweicloudsdksecmaster.v1.HwcEcs`
        """
        self._hwc_ecs = hwc_ecs

    @property
    def hwc_eip(self):
        r"""Gets the hwc_eip of this Properties.

        :return: The hwc_eip of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEip`
        """
        return self._hwc_eip

    @hwc_eip.setter
    def hwc_eip(self, hwc_eip):
        r"""Sets the hwc_eip of this Properties.

        :param hwc_eip: The hwc_eip of this Properties.
        :type hwc_eip: :class:`huaweicloudsdksecmaster.v1.HwcEip`
        """
        self._hwc_eip = hwc_eip

    @property
    def hwc_vpc(self):
        r"""Gets the hwc_vpc of this Properties.

        :return: The hwc_vpc of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcVpc`
        """
        return self._hwc_vpc

    @hwc_vpc.setter
    def hwc_vpc(self, hwc_vpc):
        r"""Sets the hwc_vpc of this Properties.

        :param hwc_vpc: The hwc_vpc of this Properties.
        :type hwc_vpc: :class:`huaweicloudsdksecmaster.v1.HwcVpc`
        """
        self._hwc_vpc = hwc_vpc

    @property
    def hwc_subnet(self):
        r"""Gets the hwc_subnet of this Properties.

        :return: The hwc_subnet of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcSubnet`
        """
        return self._hwc_subnet

    @hwc_subnet.setter
    def hwc_subnet(self, hwc_subnet):
        r"""Sets the hwc_subnet of this Properties.

        :param hwc_subnet: The hwc_subnet of this Properties.
        :type hwc_subnet: :class:`huaweicloudsdksecmaster.v1.HwcSubnet`
        """
        self._hwc_subnet = hwc_subnet

    @property
    def hwc_rds(self):
        r"""Gets the hwc_rds of this Properties.

        :return: The hwc_rds of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcRds`
        """
        return self._hwc_rds

    @hwc_rds.setter
    def hwc_rds(self, hwc_rds):
        r"""Sets the hwc_rds of this Properties.

        :param hwc_rds: The hwc_rds of this Properties.
        :type hwc_rds: :class:`huaweicloudsdksecmaster.v1.HwcRds`
        """
        self._hwc_rds = hwc_rds

    @property
    def hwc_domain(self):
        r"""Gets the hwc_domain of this Properties.

        :return: The hwc_domain of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcDomain`
        """
        return self._hwc_domain

    @hwc_domain.setter
    def hwc_domain(self, hwc_domain):
        r"""Sets the hwc_domain of this Properties.

        :param hwc_domain: The hwc_domain of this Properties.
        :type hwc_domain: :class:`huaweicloudsdksecmaster.v1.HwcDomain`
        """
        self._hwc_domain = hwc_domain

    @property
    def website(self):
        r"""Gets the website of this Properties.

        :return: The website of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Website`
        """
        return self._website

    @website.setter
    def website(self, website):
        r"""Sets the website of this Properties.

        :param website: The website of this Properties.
        :type website: :class:`huaweicloudsdksecmaster.v1.Website`
        """
        self._website = website

    @property
    def oca_ip(self):
        r"""Gets the oca_ip of this Properties.

        :return: The oca_ip of this Properties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIp`
        """
        return self._oca_ip

    @oca_ip.setter
    def oca_ip(self, oca_ip):
        r"""Sets the oca_ip of this Properties.

        :param oca_ip: The oca_ip of this Properties.
        :type oca_ip: :class:`huaweicloudsdksecmaster.v1.OcaIp`
        """
        self._oca_ip = oca_ip

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Properties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
