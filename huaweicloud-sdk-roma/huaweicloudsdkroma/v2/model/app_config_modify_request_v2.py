# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppConfigModifyRequestV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'str',
        'config_value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'config_type': 'config_type',
        'config_value': 'config_value',
        'description': 'description'
    }

    def __init__(self, config_type=None, config_value=None, description=None):
        """AppConfigModifyRequestV2

        The model defined in huaweicloud sdk

        :param config_type: 应用配置类型： - variable：模板变量 - password：密码 - certificate：证书
        :type config_type: str
        :param config_value: 应用配置值： - config_type &#x3D; variable：config_value为模板变量的值 - config_type &#x3D; password：config_value为密码值 - config_type &#x3D; certificate：config_value需要包含证书public_key（必填），私钥private_key（必填）和密码passphrase（非必填），格式如：\&quot;{\\\\\&quot;public_key\\\\\&quot;: \\\&quot;\\,\\\\\&quot;private_key\\\\\&quot;:\\\\\&quot;\\\\\&quot;,\\\\\&quot;passphrase\\\\\&quot;:\\\\\&quot;\\\\\&quot;}\&quot;
        :type config_value: str
        :param description: 应用配置描述
        :type description: str
        """
        
        

        self._config_type = None
        self._config_value = None
        self._description = None
        self.discriminator = None

        self.config_type = config_type
        if config_value is not None:
            self.config_value = config_value
        if description is not None:
            self.description = description

    @property
    def config_type(self):
        """Gets the config_type of this AppConfigModifyRequestV2.

        应用配置类型： - variable：模板变量 - password：密码 - certificate：证书

        :return: The config_type of this AppConfigModifyRequestV2.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this AppConfigModifyRequestV2.

        应用配置类型： - variable：模板变量 - password：密码 - certificate：证书

        :param config_type: The config_type of this AppConfigModifyRequestV2.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def config_value(self):
        """Gets the config_value of this AppConfigModifyRequestV2.

        应用配置值： - config_type = variable：config_value为模板变量的值 - config_type = password：config_value为密码值 - config_type = certificate：config_value需要包含证书public_key（必填），私钥private_key（必填）和密码passphrase（非必填），格式如：\"{\\\\\"public_key\\\\\": \\\"\\,\\\\\"private_key\\\\\":\\\\\"\\\\\",\\\\\"passphrase\\\\\":\\\\\"\\\\\"}\"

        :return: The config_value of this AppConfigModifyRequestV2.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this AppConfigModifyRequestV2.

        应用配置值： - config_type = variable：config_value为模板变量的值 - config_type = password：config_value为密码值 - config_type = certificate：config_value需要包含证书public_key（必填），私钥private_key（必填）和密码passphrase（非必填），格式如：\"{\\\\\"public_key\\\\\": \\\"\\,\\\\\"private_key\\\\\":\\\\\"\\\\\",\\\\\"passphrase\\\\\":\\\\\"\\\\\"}\"

        :param config_value: The config_value of this AppConfigModifyRequestV2.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def description(self):
        """Gets the description of this AppConfigModifyRequestV2.

        应用配置描述

        :return: The description of this AppConfigModifyRequestV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppConfigModifyRequestV2.

        应用配置描述

        :param description: The description of this AppConfigModifyRequestV2.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AppConfigModifyRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
