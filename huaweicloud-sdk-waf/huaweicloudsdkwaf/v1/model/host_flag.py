# coding: utf-8

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
        'pci_3ds': 'str',
        'pci_dss': 'str'
    }

    attribute_map = {
        'pci_3ds': 'pci_3ds',
        'pci_dss': 'pci_dss'
    }

    def __init__(self, pci_3ds=None, pci_dss=None):
        """HostFlag

        The model defined in huaweicloud sdk

        :param pci_3ds: 是否开启pci_3ds合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：pci_3ds合规认证开启后不支持关闭，在开启pci_3ds合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_3ds合规认证的说明   - true：开启   - false：不开启
        :type pci_3ds: str
        :param pci_dss: 是否开启pci_dss合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：在开启pci_dss合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_dss合规认证的说明   - true：开启   - false：不开启
        :type pci_dss: str
        """
        
        

        self._pci_3ds = None
        self._pci_dss = None
        self.discriminator = None

        if pci_3ds is not None:
            self.pci_3ds = pci_3ds
        if pci_dss is not None:
            self.pci_dss = pci_dss

    @property
    def pci_3ds(self):
        """Gets the pci_3ds of this HostFlag.

        是否开启pci_3ds合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：pci_3ds合规认证开启后不支持关闭，在开启pci_3ds合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_3ds合规认证的说明   - true：开启   - false：不开启

        :return: The pci_3ds of this HostFlag.
        :rtype: str
        """
        return self._pci_3ds

    @pci_3ds.setter
    def pci_3ds(self, pci_3ds):
        """Sets the pci_3ds of this HostFlag.

        是否开启pci_3ds合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：pci_3ds合规认证开启后不支持关闭，在开启pci_3ds合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_3ds合规认证的说明   - true：开启   - false：不开启

        :param pci_3ds: The pci_3ds of this HostFlag.
        :type pci_3ds: str
        """
        self._pci_3ds = pci_3ds

    @property
    def pci_dss(self):
        """Gets the pci_dss of this HostFlag.

        是否开启pci_dss合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：在开启pci_dss合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_dss合规认证的说明   - true：开启   - false：不开启

        :return: The pci_dss of this HostFlag.
        :rtype: str
        """
        return self._pci_dss

    @pci_dss.setter
    def pci_dss(self, pci_dss):
        """Sets the pci_dss of this HostFlag.

        是否开启pci_dss合规认证，该参数需要与tls和cipher参数同时使用，且tls参数值需要设置为TLS v1.2，cipher参数值设置为cipher_2。注：在开启pci_dss合规认证前，请先阅读帮助中心Web应用防火墙WAF文档中关于pci_dss合规认证的说明   - true：开启   - false：不开启

        :param pci_dss: The pci_dss of this HostFlag.
        :type pci_dss: str
        """
        self._pci_dss = pci_dss

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
