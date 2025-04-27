# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIpRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'id': 'str',
        'address': 'str'
    }

    attribute_map = {
        'region': 'region',
        'id': 'id',
        'address': 'address'
    }

    def __init__(self, region=None, id=None, address=None):
        r"""PublicIpRes

        The model defined in huaweicloud sdk

        :param region: 弹性公网IP（EIP）所属的区域。
        :type region: str
        :param id: 弹性公网IP（EIP）的ID。
        :type id: str
        :param address: 弹性公网IP（EIP）。
        :type address: str
        """
        
        

        self._region = None
        self._id = None
        self._address = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address

    @property
    def region(self):
        r"""Gets the region of this PublicIpRes.

        弹性公网IP（EIP）所属的区域。

        :return: The region of this PublicIpRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this PublicIpRes.

        弹性公网IP（EIP）所属的区域。

        :param region: The region of this PublicIpRes.
        :type region: str
        """
        self._region = region

    @property
    def id(self):
        r"""Gets the id of this PublicIpRes.

        弹性公网IP（EIP）的ID。

        :return: The id of this PublicIpRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicIpRes.

        弹性公网IP（EIP）的ID。

        :param id: The id of this PublicIpRes.
        :type id: str
        """
        self._id = id

    @property
    def address(self):
        r"""Gets the address of this PublicIpRes.

        弹性公网IP（EIP）。

        :return: The address of this PublicIpRes.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this PublicIpRes.

        弹性公网IP（EIP）。

        :param address: The address of this PublicIpRes.
        :type address: str
        """
        self._address = address

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
        if not isinstance(other, PublicIpRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
