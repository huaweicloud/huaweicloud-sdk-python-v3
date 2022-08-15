# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pci_3ds': 'str',
        'pci_dss': 'str',
        'cname': 'str',
        'is_dual_az': 'str',
        'ipv6': 'str'
    }

    attribute_map = {
        'pci_3ds': 'pci_3ds',
        'pci_dss': 'pci_dss',
        'cname': 'cname',
        'is_dual_az': 'is_dual_az',
        'ipv6': 'ipv6'
    }

    def __init__(self, pci_3ds=None, pci_dss=None, cname=None, is_dual_az=None, ipv6=None):
        """Flag

        The model defined in huaweicloud sdk

        :param pci_3ds: 是否开启pci_3ds合规认证   - true：开启   - false：不开启
        :type pci_3ds: str
        :param pci_dss: 是否开启pci_dss合规认证   - true：开启   - false：不开启
        :type pci_dss: str
        :param cname: old：代表域名使用的老的cname，new：代表域名使用新的cname
        :type cname: str
        :param is_dual_az: 域名是否开启ipv6   - true：支持   - false：不支持
        :type is_dual_az: str
        :param ipv6: 域名是否开启ipv6   - true：支持   - false：不支持
        :type ipv6: str
        """
        
        

        self._pci_3ds = None
        self._pci_dss = None
        self._cname = None
        self._is_dual_az = None
        self._ipv6 = None
        self.discriminator = None

        if pci_3ds is not None:
            self.pci_3ds = pci_3ds
        if pci_dss is not None:
            self.pci_dss = pci_dss
        if cname is not None:
            self.cname = cname
        if is_dual_az is not None:
            self.is_dual_az = is_dual_az
        if ipv6 is not None:
            self.ipv6 = ipv6

    @property
    def pci_3ds(self):
        """Gets the pci_3ds of this Flag.

        是否开启pci_3ds合规认证   - true：开启   - false：不开启

        :return: The pci_3ds of this Flag.
        :rtype: str
        """
        return self._pci_3ds

    @pci_3ds.setter
    def pci_3ds(self, pci_3ds):
        """Sets the pci_3ds of this Flag.

        是否开启pci_3ds合规认证   - true：开启   - false：不开启

        :param pci_3ds: The pci_3ds of this Flag.
        :type pci_3ds: str
        """
        self._pci_3ds = pci_3ds

    @property
    def pci_dss(self):
        """Gets the pci_dss of this Flag.

        是否开启pci_dss合规认证   - true：开启   - false：不开启

        :return: The pci_dss of this Flag.
        :rtype: str
        """
        return self._pci_dss

    @pci_dss.setter
    def pci_dss(self, pci_dss):
        """Sets the pci_dss of this Flag.

        是否开启pci_dss合规认证   - true：开启   - false：不开启

        :param pci_dss: The pci_dss of this Flag.
        :type pci_dss: str
        """
        self._pci_dss = pci_dss

    @property
    def cname(self):
        """Gets the cname of this Flag.

        old：代表域名使用的老的cname，new：代表域名使用新的cname

        :return: The cname of this Flag.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this Flag.

        old：代表域名使用的老的cname，new：代表域名使用新的cname

        :param cname: The cname of this Flag.
        :type cname: str
        """
        self._cname = cname

    @property
    def is_dual_az(self):
        """Gets the is_dual_az of this Flag.

        域名是否开启ipv6   - true：支持   - false：不支持

        :return: The is_dual_az of this Flag.
        :rtype: str
        """
        return self._is_dual_az

    @is_dual_az.setter
    def is_dual_az(self, is_dual_az):
        """Sets the is_dual_az of this Flag.

        域名是否开启ipv6   - true：支持   - false：不支持

        :param is_dual_az: The is_dual_az of this Flag.
        :type is_dual_az: str
        """
        self._is_dual_az = is_dual_az

    @property
    def ipv6(self):
        """Gets the ipv6 of this Flag.

        域名是否开启ipv6   - true：支持   - false：不支持

        :return: The ipv6 of this Flag.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this Flag.

        域名是否开启ipv6   - true：支持   - false：不支持

        :param ipv6: The ipv6 of this Flag.
        :type ipv6: str
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
        if not isinstance(other, Flag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
