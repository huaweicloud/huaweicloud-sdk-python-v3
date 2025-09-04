# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuthenticationTemplateBody:

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
        'resources': 'UpdateAuthenticationTemplateResource'
    }

    attribute_map = {
        'parameters': 'parameters',
        'resources': 'resources'
    }

    def __init__(self, parameters=None, resources=None):
        r"""UpdateAuthenticationTemplateBody

        The model defined in huaweicloud sdk

        :param parameters: **参数说明**：鉴权模板参数，目前平台预制了mqtt协议连接参数中的clientId，username与设备证书中的属性，参数名定义如下: - iotda::mqtt::client_id ：mqtt连接参数三元组中的Client Id - iotda::mqtt::username ：mqtt连接参数三元组中的User Name - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber) - iotda::device::secret ：表示设备原始秘钥
        :type parameters: object
        :param resources: 
        :type resources: :class:`huaweicloudsdkiotda.v5.UpdateAuthenticationTemplateResource`
        """
        
        

        self._parameters = None
        self._resources = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if resources is not None:
            self.resources = resources

    @property
    def parameters(self):
        r"""Gets the parameters of this UpdateAuthenticationTemplateBody.

        **参数说明**：鉴权模板参数，目前平台预制了mqtt协议连接参数中的clientId，username与设备证书中的属性，参数名定义如下: - iotda::mqtt::client_id ：mqtt连接参数三元组中的Client Id - iotda::mqtt::username ：mqtt连接参数三元组中的User Name - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber) - iotda::device::secret ：表示设备原始秘钥

        :return: The parameters of this UpdateAuthenticationTemplateBody.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this UpdateAuthenticationTemplateBody.

        **参数说明**：鉴权模板参数，目前平台预制了mqtt协议连接参数中的clientId，username与设备证书中的属性，参数名定义如下: - iotda::mqtt::client_id ：mqtt连接参数三元组中的Client Id - iotda::mqtt::username ：mqtt连接参数三元组中的User Name - iotda::certificate::country (国家/地区,C ) - iotda::certificate::organization (组织,O) - iotda::certificate::organizational_unit (组织单位,OU) - iotda::certificate::distinguished_name_qualifier (可辨别名称限定符,dnQualifier) - iotda::certificate::state_name (省市,ST) - iotda::certificate::common_name (公用名,CN) - iotda::certificate::serial_number (序列号,serialNumber) - iotda::device::secret ：表示设备原始秘钥

        :param parameters: The parameters of this UpdateAuthenticationTemplateBody.
        :type parameters: object
        """
        self._parameters = parameters

    @property
    def resources(self):
        r"""Gets the resources of this UpdateAuthenticationTemplateBody.

        :return: The resources of this UpdateAuthenticationTemplateBody.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateAuthenticationTemplateResource`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this UpdateAuthenticationTemplateBody.

        :param resources: The resources of this UpdateAuthenticationTemplateBody.
        :type resources: :class:`huaweicloudsdkiotda.v5.UpdateAuthenticationTemplateResource`
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
        if not isinstance(other, UpdateAuthenticationTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
