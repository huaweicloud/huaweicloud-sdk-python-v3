# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolutionInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_public_zone_id': 'ZoneResolutionInstances',
        'dns_public_recordset_id': 'RsetResolutionInstances',
        'dns_private_zone_id': 'ZoneResolutionInstances',
        'vpc_id': 'VpcResolutionInstances'
    }

    attribute_map = {
        'dns_public_zone_id': 'dns_public_zone_id',
        'dns_public_recordset_id': 'dns_public_recordset_id',
        'dns_private_zone_id': 'dns_private_zone_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, dns_public_zone_id=None, dns_public_recordset_id=None, dns_private_zone_id=None, vpc_id=None):
        r"""ResolutionInstances

        The model defined in huaweicloud sdk

        :param dns_public_zone_id: 
        :type dns_public_zone_id: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        :param dns_public_recordset_id: 
        :type dns_public_recordset_id: :class:`huaweicloudsdkdns.v2.RsetResolutionInstances`
        :param dns_private_zone_id: 
        :type dns_private_zone_id: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        :param vpc_id: 
        :type vpc_id: :class:`huaweicloudsdkdns.v2.VpcResolutionInstances`
        """
        
        

        self._dns_public_zone_id = None
        self._dns_public_recordset_id = None
        self._dns_private_zone_id = None
        self._vpc_id = None
        self.discriminator = None

        if dns_public_zone_id is not None:
            self.dns_public_zone_id = dns_public_zone_id
        if dns_public_recordset_id is not None:
            self.dns_public_recordset_id = dns_public_recordset_id
        if dns_private_zone_id is not None:
            self.dns_private_zone_id = dns_private_zone_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def dns_public_zone_id(self):
        r"""Gets the dns_public_zone_id of this ResolutionInstances.

        :return: The dns_public_zone_id of this ResolutionInstances.
        :rtype: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        """
        return self._dns_public_zone_id

    @dns_public_zone_id.setter
    def dns_public_zone_id(self, dns_public_zone_id):
        r"""Sets the dns_public_zone_id of this ResolutionInstances.

        :param dns_public_zone_id: The dns_public_zone_id of this ResolutionInstances.
        :type dns_public_zone_id: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        """
        self._dns_public_zone_id = dns_public_zone_id

    @property
    def dns_public_recordset_id(self):
        r"""Gets the dns_public_recordset_id of this ResolutionInstances.

        :return: The dns_public_recordset_id of this ResolutionInstances.
        :rtype: :class:`huaweicloudsdkdns.v2.RsetResolutionInstances`
        """
        return self._dns_public_recordset_id

    @dns_public_recordset_id.setter
    def dns_public_recordset_id(self, dns_public_recordset_id):
        r"""Sets the dns_public_recordset_id of this ResolutionInstances.

        :param dns_public_recordset_id: The dns_public_recordset_id of this ResolutionInstances.
        :type dns_public_recordset_id: :class:`huaweicloudsdkdns.v2.RsetResolutionInstances`
        """
        self._dns_public_recordset_id = dns_public_recordset_id

    @property
    def dns_private_zone_id(self):
        r"""Gets the dns_private_zone_id of this ResolutionInstances.

        :return: The dns_private_zone_id of this ResolutionInstances.
        :rtype: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        """
        return self._dns_private_zone_id

    @dns_private_zone_id.setter
    def dns_private_zone_id(self, dns_private_zone_id):
        r"""Sets the dns_private_zone_id of this ResolutionInstances.

        :param dns_private_zone_id: The dns_private_zone_id of this ResolutionInstances.
        :type dns_private_zone_id: :class:`huaweicloudsdkdns.v2.ZoneResolutionInstances`
        """
        self._dns_private_zone_id = dns_private_zone_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ResolutionInstances.

        :return: The vpc_id of this ResolutionInstances.
        :rtype: :class:`huaweicloudsdkdns.v2.VpcResolutionInstances`
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ResolutionInstances.

        :param vpc_id: The vpc_id of this ResolutionInstances.
        :type vpc_id: :class:`huaweicloudsdkdns.v2.VpcResolutionInstances`
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ResolutionInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
