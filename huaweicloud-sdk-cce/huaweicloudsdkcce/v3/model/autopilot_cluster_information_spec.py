# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutopilotClusterInformationSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'custom_san': 'list[str]',
        'eni_network': 'AutopilotEniNetworkUpdate'
    }

    attribute_map = {
        'description': 'description',
        'custom_san': 'customSan',
        'eni_network': 'eniNetwork'
    }

    def __init__(self, description=None, custom_san=None, eni_network=None):
        r"""AutopilotClusterInformationSpec

        The model defined in huaweicloud sdk

        :param description: 集群的描述信息。  1. 字符取值范围[0,200]。不包含~$%^&amp;*&lt;&gt;[]{}()&#39;\&quot;#\\等特殊字符。 2. 仅运行（Available）的集群允许修改。
        :type description: str
        :param custom_san: 集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: &#x60;&#x60;&#x60; SAN 1: DNS Name&#x3D;example.com SAN 2: DNS Name&#x3D;www.example.com SAN 3: DNS Name&#x3D;example.net SAN 4: IP Address&#x3D;93.184.216.34 &#x60;&#x60;&#x60;
        :type custom_san: list[str]
        :param eni_network: 
        :type eni_network: :class:`huaweicloudsdkcce.v3.AutopilotEniNetworkUpdate`
        """
        
        

        self._description = None
        self._custom_san = None
        self._eni_network = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if custom_san is not None:
            self.custom_san = custom_san
        if eni_network is not None:
            self.eni_network = eni_network

    @property
    def description(self):
        r"""Gets the description of this AutopilotClusterInformationSpec.

        集群的描述信息。  1. 字符取值范围[0,200]。不包含~$%^&*<>[]{}()'\"#\\等特殊字符。 2. 仅运行（Available）的集群允许修改。

        :return: The description of this AutopilotClusterInformationSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AutopilotClusterInformationSpec.

        集群的描述信息。  1. 字符取值范围[0,200]。不包含~$%^&*<>[]{}()'\"#\\等特殊字符。 2. 仅运行（Available）的集群允许修改。

        :param description: The description of this AutopilotClusterInformationSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        r"""Gets the custom_san of this AutopilotClusterInformationSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :return: The custom_san of this AutopilotClusterInformationSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        r"""Sets the custom_san of this AutopilotClusterInformationSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :param custom_san: The custom_san of this AutopilotClusterInformationSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def eni_network(self):
        r"""Gets the eni_network of this AutopilotClusterInformationSpec.

        :return: The eni_network of this AutopilotClusterInformationSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotEniNetworkUpdate`
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        r"""Sets the eni_network of this AutopilotClusterInformationSpec.

        :param eni_network: The eni_network of this AutopilotClusterInformationSpec.
        :type eni_network: :class:`huaweicloudsdkcce.v3.AutopilotEniNetworkUpdate`
        """
        self._eni_network = eni_network

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
        if not isinstance(other, AutopilotClusterInformationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
