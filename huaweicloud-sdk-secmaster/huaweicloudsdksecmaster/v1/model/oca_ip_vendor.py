# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpVendor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'is_xc': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_xc': 'is_xc'
    }

    def __init__(self, name=None, is_xc=None):
        r"""OcaIpVendor

        The model defined in huaweicloud sdk

        :param name: 供应名称
        :type name: str
        :param is_xc: 供应商是否是国产
        :type is_xc: bool
        """
        
        

        self._name = None
        self._is_xc = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_xc is not None:
            self.is_xc = is_xc

    @property
    def name(self):
        r"""Gets the name of this OcaIpVendor.

        供应名称

        :return: The name of this OcaIpVendor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OcaIpVendor.

        供应名称

        :param name: The name of this OcaIpVendor.
        :type name: str
        """
        self._name = name

    @property
    def is_xc(self):
        r"""Gets the is_xc of this OcaIpVendor.

        供应商是否是国产

        :return: The is_xc of this OcaIpVendor.
        :rtype: bool
        """
        return self._is_xc

    @is_xc.setter
    def is_xc(self, is_xc):
        r"""Sets the is_xc of this OcaIpVendor.

        供应商是否是国产

        :param is_xc: The is_xc of this OcaIpVendor.
        :type is_xc: bool
        """
        self._is_xc = is_xc

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
        if not isinstance(other, OcaIpVendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
