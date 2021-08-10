# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostFlag:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pci_dss': 'str',
        'pci_3ds': 'str',
        'cname': 'str',
        'is_dual_az': 'str',
        'ipv6': 'str'
    }

    attribute_map = {
        'pci_dss': 'pci_dss',
        'pci_3ds': 'pci_3ds',
        'cname': 'cname',
        'is_dual_az': 'is_dual_az',
        'ipv6': 'ipv6'
    }

    def __init__(self, pci_dss=None, pci_3ds=None, cname=None, is_dual_az=None, ipv6=None):
        """HostFlag - a model defined in huaweicloud sdk"""
        
        

        self._pci_dss = None
        self._pci_3ds = None
        self._cname = None
        self._is_dual_az = None
        self._ipv6 = None
        self.discriminator = None

        if pci_dss is not None:
            self.pci_dss = pci_dss
        if pci_3ds is not None:
            self.pci_3ds = pci_3ds
        if cname is not None:
            self.cname = cname
        if is_dual_az is not None:
            self.is_dual_az = is_dual_az
        if ipv6 is not None:
            self.ipv6 = ipv6

    @property
    def pci_dss(self):
        """Gets the pci_dss of this HostFlag.

        true/false

        :return: The pci_dss of this HostFlag.
        :rtype: str
        """
        return self._pci_dss

    @pci_dss.setter
    def pci_dss(self, pci_dss):
        """Sets the pci_dss of this HostFlag.

        true/false

        :param pci_dss: The pci_dss of this HostFlag.
        :type: str
        """
        self._pci_dss = pci_dss

    @property
    def pci_3ds(self):
        """Gets the pci_3ds of this HostFlag.

        true/false

        :return: The pci_3ds of this HostFlag.
        :rtype: str
        """
        return self._pci_3ds

    @pci_3ds.setter
    def pci_3ds(self, pci_3ds):
        """Sets the pci_3ds of this HostFlag.

        true/false

        :param pci_3ds: The pci_3ds of this HostFlag.
        :type: str
        """
        self._pci_3ds = pci_3ds

    @property
    def cname(self):
        """Gets the cname of this HostFlag.

        old/new

        :return: The cname of this HostFlag.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this HostFlag.

        old/new

        :param cname: The cname of this HostFlag.
        :type: str
        """
        self._cname = cname

    @property
    def is_dual_az(self):
        """Gets the is_dual_az of this HostFlag.

        true/false

        :return: The is_dual_az of this HostFlag.
        :rtype: str
        """
        return self._is_dual_az

    @is_dual_az.setter
    def is_dual_az(self, is_dual_az):
        """Sets the is_dual_az of this HostFlag.

        true/false

        :param is_dual_az: The is_dual_az of this HostFlag.
        :type: str
        """
        self._is_dual_az = is_dual_az

    @property
    def ipv6(self):
        """Gets the ipv6 of this HostFlag.

        true/false

        :return: The ipv6 of this HostFlag.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this HostFlag.

        true/false

        :param ipv6: The ipv6 of this HostFlag.
        :type: str
        """
        self._ipv6 = ipv6

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
        if not isinstance(other, HostFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
