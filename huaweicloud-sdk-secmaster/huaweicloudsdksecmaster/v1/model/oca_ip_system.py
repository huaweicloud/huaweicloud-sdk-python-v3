# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpSystem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'family': 'str',
        'name': 'str',
        'version': 'str',
        'vendor': 'OcaIpVendor'
    }

    attribute_map = {
        'family': 'family',
        'name': 'name',
        'version': 'version',
        'vendor': 'vendor'
    }

    def __init__(self, family=None, name=None, version=None, vendor=None):
        r"""OcaIpSystem

        The model defined in huaweicloud sdk

        :param family: 系统类型
        :type family: str
        :param name: 系统名称
        :type name: str
        :param version: 系统版本
        :type version: str
        :param vendor: 
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        
        

        self._family = None
        self._name = None
        self._version = None
        self._vendor = None
        self.discriminator = None

        if family is not None:
            self.family = family
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if vendor is not None:
            self.vendor = vendor

    @property
    def family(self):
        r"""Gets the family of this OcaIpSystem.

        系统类型

        :return: The family of this OcaIpSystem.
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        r"""Sets the family of this OcaIpSystem.

        系统类型

        :param family: The family of this OcaIpSystem.
        :type family: str
        """
        self._family = family

    @property
    def name(self):
        r"""Gets the name of this OcaIpSystem.

        系统名称

        :return: The name of this OcaIpSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OcaIpSystem.

        系统名称

        :param name: The name of this OcaIpSystem.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this OcaIpSystem.

        系统版本

        :return: The version of this OcaIpSystem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OcaIpSystem.

        系统版本

        :param version: The version of this OcaIpSystem.
        :type version: str
        """
        self._version = version

    @property
    def vendor(self):
        r"""Gets the vendor of this OcaIpSystem.

        :return: The vendor of this OcaIpSystem.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this OcaIpSystem.

        :param vendor: The vendor of this OcaIpSystem.
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        self._vendor = vendor

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
        if not isinstance(other, OcaIpSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
