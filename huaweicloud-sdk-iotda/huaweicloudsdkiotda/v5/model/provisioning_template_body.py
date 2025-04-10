# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvisioningTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'object',
        'resources': 'TemplateResource'
    }

    attribute_map = {
        'parameters': 'parameters',
        'resources': 'resources'
    }

    def __init__(self, parameters=None, resources=None):
        r"""ProvisioningTemplateBody

        The model defined in huaweicloud sdk

        :param parameters: **参数说明**：预调配模板参数， ，配置格式为{\&quot;parameter\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;}} ，其中parameter目前支持从预调配设备的证书的使用者字段提取内容，证书必须包含模板中定义的所有参数值，华为云IoT平台定义了可在预调配模板中声明和引用的如下参数: - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber)  type描述parameter的类型，目前仅支持string。  配置样例：  &#39;{\&quot;iotda::certificate::country\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::organization\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::organizational_unit\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::distinguished_name_qualifier\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::state_name\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::common_name\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;},  \&quot;iotda::certificate::serial_number\&quot;:{\&quot;type\&quot;:\&quot;String\&quot;}}&#39;
        :type parameters: object
        :param resources: 
        :type resources: :class:`huaweicloudsdkiotda.v5.TemplateResource`
        """
        
        

        self._parameters = None
        self._resources = None
        self.discriminator = None

        self.parameters = parameters
        self.resources = resources

    @property
    def parameters(self):
        r"""Gets the parameters of this ProvisioningTemplateBody.

        **参数说明**：预调配模板参数， ，配置格式为{\"parameter\":{\"type\":\"String\"}} ，其中parameter目前支持从预调配设备的证书的使用者字段提取内容，证书必须包含模板中定义的所有参数值，华为云IoT平台定义了可在预调配模板中声明和引用的如下参数: - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber)  type描述parameter的类型，目前仅支持string。  配置样例：  '{\"iotda::certificate::country\":{\"type\":\"String\"},  \"iotda::certificate::organization\":{\"type\":\"String\"},  \"iotda::certificate::organizational_unit\":{\"type\":\"String\"},  \"iotda::certificate::distinguished_name_qualifier\":{\"type\":\"String\"},  \"iotda::certificate::state_name\":{\"type\":\"String\"},  \"iotda::certificate::common_name\":{\"type\":\"String\"},  \"iotda::certificate::serial_number\":{\"type\":\"String\"}}'

        :return: The parameters of this ProvisioningTemplateBody.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ProvisioningTemplateBody.

        **参数说明**：预调配模板参数， ，配置格式为{\"parameter\":{\"type\":\"String\"}} ，其中parameter目前支持从预调配设备的证书的使用者字段提取内容，证书必须包含模板中定义的所有参数值，华为云IoT平台定义了可在预调配模板中声明和引用的如下参数: - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber)  type描述parameter的类型，目前仅支持string。  配置样例：  '{\"iotda::certificate::country\":{\"type\":\"String\"},  \"iotda::certificate::organization\":{\"type\":\"String\"},  \"iotda::certificate::organizational_unit\":{\"type\":\"String\"},  \"iotda::certificate::distinguished_name_qualifier\":{\"type\":\"String\"},  \"iotda::certificate::state_name\":{\"type\":\"String\"},  \"iotda::certificate::common_name\":{\"type\":\"String\"},  \"iotda::certificate::serial_number\":{\"type\":\"String\"}}'

        :param parameters: The parameters of this ProvisioningTemplateBody.
        :type parameters: object
        """
        self._parameters = parameters

    @property
    def resources(self):
        r"""Gets the resources of this ProvisioningTemplateBody.

        :return: The resources of this ProvisioningTemplateBody.
        :rtype: :class:`huaweicloudsdkiotda.v5.TemplateResource`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ProvisioningTemplateBody.

        :param resources: The resources of this ProvisioningTemplateBody.
        :type resources: :class:`huaweicloudsdkiotda.v5.TemplateResource`
        """
        self._resources = resources

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
        if not isinstance(other, ProvisioningTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
