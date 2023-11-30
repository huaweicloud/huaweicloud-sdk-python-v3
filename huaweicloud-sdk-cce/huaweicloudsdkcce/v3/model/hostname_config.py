# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostnameConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):
        """HostnameConfig

        The model defined in huaweicloud sdk

        :param type: K8S节点名称配置类型, 默认为“privateIp”。  -  privateIp: 将节点私有IP作为K8S节点名称 -  cceNodeName: 将CCE节点名称作为K8S节点名称  &gt; - 配置为cceNodeName的节点, 其节点名称、K8S节点名称以及虚机名称相同。节点名称不支持修改, 并且在ECS侧修改了虚机名称，同步云服务器时，不会将修改后的虚机名称同步到节点。 &gt; - 配置为cceNodeName的节点，为了避免K8S节点名称冲突，系统会自动在节点名称后添加后缀，后缀的格式为中划线(-)+五位随机字符，随机字符的取值为[a-z0-9]。 
        :type type: str
        """
        
        

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        """Gets the type of this HostnameConfig.

        K8S节点名称配置类型, 默认为“privateIp”。  -  privateIp: 将节点私有IP作为K8S节点名称 -  cceNodeName: 将CCE节点名称作为K8S节点名称  > - 配置为cceNodeName的节点, 其节点名称、K8S节点名称以及虚机名称相同。节点名称不支持修改, 并且在ECS侧修改了虚机名称，同步云服务器时，不会将修改后的虚机名称同步到节点。 > - 配置为cceNodeName的节点，为了避免K8S节点名称冲突，系统会自动在节点名称后添加后缀，后缀的格式为中划线(-)+五位随机字符，随机字符的取值为[a-z0-9]。 

        :return: The type of this HostnameConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostnameConfig.

        K8S节点名称配置类型, 默认为“privateIp”。  -  privateIp: 将节点私有IP作为K8S节点名称 -  cceNodeName: 将CCE节点名称作为K8S节点名称  > - 配置为cceNodeName的节点, 其节点名称、K8S节点名称以及虚机名称相同。节点名称不支持修改, 并且在ECS侧修改了虚机名称，同步云服务器时，不会将修改后的虚机名称同步到节点。 > - 配置为cceNodeName的节点，为了避免K8S节点名称冲突，系统会自动在节点名称后添加后缀，后缀的格式为中划线(-)+五位随机字符，随机字符的取值为[a-z0-9]。 

        :param type: The type of this HostnameConfig.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, HostnameConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
