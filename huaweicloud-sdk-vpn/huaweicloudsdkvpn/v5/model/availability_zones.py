# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic': 'VpnGatewayAvailabilityZones',
        'professional1': 'VpnGatewayAvailabilityZones',
        'professional2': 'VpnGatewayAvailabilityZones',
        'gm': 'VpnGatewayAvailabilityZones'
    }

    attribute_map = {
        'basic': 'basic',
        'professional1': 'professional1',
        'professional2': 'professional2',
        'gm': 'gm'
    }

    def __init__(self, basic=None, professional1=None, professional2=None, gm=None):
        """AvailabilityZones

        The model defined in huaweicloud sdk

        :param basic: 
        :type basic: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        :param professional1: 
        :type professional1: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        :param professional2: 
        :type professional2: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        :param gm: 
        :type gm: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        
        

        self._basic = None
        self._professional1 = None
        self._professional2 = None
        self._gm = None
        self.discriminator = None

        if basic is not None:
            self.basic = basic
        if professional1 is not None:
            self.professional1 = professional1
        if professional2 is not None:
            self.professional2 = professional2
        if gm is not None:
            self.gm = gm

    @property
    def basic(self):
        """Gets the basic of this AvailabilityZones.

        :return: The basic of this AvailabilityZones.
        :rtype: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this AvailabilityZones.

        :param basic: The basic of this AvailabilityZones.
        :type basic: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        self._basic = basic

    @property
    def professional1(self):
        """Gets the professional1 of this AvailabilityZones.

        :return: The professional1 of this AvailabilityZones.
        :rtype: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        return self._professional1

    @professional1.setter
    def professional1(self, professional1):
        """Sets the professional1 of this AvailabilityZones.

        :param professional1: The professional1 of this AvailabilityZones.
        :type professional1: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        self._professional1 = professional1

    @property
    def professional2(self):
        """Gets the professional2 of this AvailabilityZones.

        :return: The professional2 of this AvailabilityZones.
        :rtype: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        return self._professional2

    @professional2.setter
    def professional2(self, professional2):
        """Sets the professional2 of this AvailabilityZones.

        :param professional2: The professional2 of this AvailabilityZones.
        :type professional2: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        self._professional2 = professional2

    @property
    def gm(self):
        """Gets the gm of this AvailabilityZones.

        :return: The gm of this AvailabilityZones.
        :rtype: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        return self._gm

    @gm.setter
    def gm(self, gm):
        """Sets the gm of this AvailabilityZones.

        :param gm: The gm of this AvailabilityZones.
        :type gm: :class:`huaweicloudsdkvpn.v5.VpnGatewayAvailabilityZones`
        """
        self._gm = gm

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
        if not isinstance(other, AvailabilityZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
