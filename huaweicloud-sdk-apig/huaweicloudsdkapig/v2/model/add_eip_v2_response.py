# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddEipV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_id': 'str',
        'eip_address': 'str',
        'eip_status': 'str',
        'eip_ipv6_address': 'str'
    }

    attribute_map = {
        'eip_id': 'eip_id',
        'eip_address': 'eip_address',
        'eip_status': 'eip_status',
        'eip_ipv6_address': 'eip_ipv6_address'
    }

    def __init__(self, eip_id=None, eip_address=None, eip_status=None, eip_ipv6_address=None):
        r"""AddEipV2Response

        The model defined in huaweicloud sdk

        :param eip_id: 弹性公网IP编号
        :type eip_id: str
        :param eip_address: 弹性公网IP
        :type eip_address: str
        :param eip_status: 弹性公网IP状态
        :type eip_status: str
        :param eip_ipv6_address: 弹性公网IP(IPV6)
        :type eip_ipv6_address: str
        """
        
        super(AddEipV2Response, self).__init__()

        self._eip_id = None
        self._eip_address = None
        self._eip_status = None
        self._eip_ipv6_address = None
        self.discriminator = None

        if eip_id is not None:
            self.eip_id = eip_id
        if eip_address is not None:
            self.eip_address = eip_address
        if eip_status is not None:
            self.eip_status = eip_status
        if eip_ipv6_address is not None:
            self.eip_ipv6_address = eip_ipv6_address

    @property
    def eip_id(self):
        r"""Gets the eip_id of this AddEipV2Response.

        弹性公网IP编号

        :return: The eip_id of this AddEipV2Response.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        r"""Sets the eip_id of this AddEipV2Response.

        弹性公网IP编号

        :param eip_id: The eip_id of this AddEipV2Response.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def eip_address(self):
        r"""Gets the eip_address of this AddEipV2Response.

        弹性公网IP

        :return: The eip_address of this AddEipV2Response.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        r"""Sets the eip_address of this AddEipV2Response.

        弹性公网IP

        :param eip_address: The eip_address of this AddEipV2Response.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def eip_status(self):
        r"""Gets the eip_status of this AddEipV2Response.

        弹性公网IP状态

        :return: The eip_status of this AddEipV2Response.
        :rtype: str
        """
        return self._eip_status

    @eip_status.setter
    def eip_status(self, eip_status):
        r"""Sets the eip_status of this AddEipV2Response.

        弹性公网IP状态

        :param eip_status: The eip_status of this AddEipV2Response.
        :type eip_status: str
        """
        self._eip_status = eip_status

    @property
    def eip_ipv6_address(self):
        r"""Gets the eip_ipv6_address of this AddEipV2Response.

        弹性公网IP(IPV6)

        :return: The eip_ipv6_address of this AddEipV2Response.
        :rtype: str
        """
        return self._eip_ipv6_address

    @eip_ipv6_address.setter
    def eip_ipv6_address(self, eip_ipv6_address):
        r"""Sets the eip_ipv6_address of this AddEipV2Response.

        弹性公网IP(IPV6)

        :param eip_ipv6_address: The eip_ipv6_address of this AddEipV2Response.
        :type eip_ipv6_address: str
        """
        self._eip_ipv6_address = eip_ipv6_address

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
        if not isinstance(other, AddEipV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
