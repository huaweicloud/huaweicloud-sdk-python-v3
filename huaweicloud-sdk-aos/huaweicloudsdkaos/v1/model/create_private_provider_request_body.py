# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateProviderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_name': 'str',
        'provider_description': 'str',
        'provider_version': 'str',
        'version_description': 'str',
        'function_graph_urn': 'str'
    }

    attribute_map = {
        'provider_name': 'provider_name',
        'provider_description': 'provider_description',
        'provider_version': 'provider_version',
        'version_description': 'version_description',
        'function_graph_urn': 'function_graph_urn'
    }

    def __init__(self, provider_name=None, provider_description=None, provider_version=None, version_description=None, function_graph_urn=None):
        """CreatePrivateProviderRequestBody

        The model defined in huaweicloud sdk

        :param provider_name: 私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。
        :type provider_name: str
        :param provider_description: 私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。
        :type provider_description: str
        :param provider_version: provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义
        :type provider_version: str
        :param version_description: 私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建
        :type version_description: str
        :param function_graph_urn: FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html
        :type function_graph_urn: str
        """
        
        

        self._provider_name = None
        self._provider_description = None
        self._provider_version = None
        self._version_description = None
        self._function_graph_urn = None
        self.discriminator = None

        self.provider_name = provider_name
        if provider_description is not None:
            self.provider_description = provider_description
        if provider_version is not None:
            self.provider_version = provider_version
        if version_description is not None:
            self.version_description = version_description
        if function_graph_urn is not None:
            self.function_graph_urn = function_graph_urn

    @property
    def provider_name(self):
        """Gets the provider_name of this CreatePrivateProviderRequestBody.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :return: The provider_name of this CreatePrivateProviderRequestBody.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this CreatePrivateProviderRequestBody.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :param provider_name: The provider_name of this CreatePrivateProviderRequestBody.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_description(self):
        """Gets the provider_description of this CreatePrivateProviderRequestBody.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :return: The provider_description of this CreatePrivateProviderRequestBody.
        :rtype: str
        """
        return self._provider_description

    @provider_description.setter
    def provider_description(self, provider_description):
        """Sets the provider_description of this CreatePrivateProviderRequestBody.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :param provider_description: The provider_description of this CreatePrivateProviderRequestBody.
        :type provider_description: str
        """
        self._provider_description = provider_description

    @property
    def provider_version(self):
        """Gets the provider_version of this CreatePrivateProviderRequestBody.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :return: The provider_version of this CreatePrivateProviderRequestBody.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """Sets the provider_version of this CreatePrivateProviderRequestBody.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :param provider_version: The provider_version of this CreatePrivateProviderRequestBody.
        :type provider_version: str
        """
        self._provider_version = provider_version

    @property
    def version_description(self):
        """Gets the version_description of this CreatePrivateProviderRequestBody.

        私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建

        :return: The version_description of this CreatePrivateProviderRequestBody.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """Sets the version_description of this CreatePrivateProviderRequestBody.

        私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建

        :param version_description: The version_description of this CreatePrivateProviderRequestBody.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def function_graph_urn(self):
        """Gets the function_graph_urn of this CreatePrivateProviderRequestBody.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :return: The function_graph_urn of this CreatePrivateProviderRequestBody.
        :rtype: str
        """
        return self._function_graph_urn

    @function_graph_urn.setter
    def function_graph_urn(self, function_graph_urn):
        """Sets the function_graph_urn of this CreatePrivateProviderRequestBody.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :param function_graph_urn: The function_graph_urn of this CreatePrivateProviderRequestBody.
        :type function_graph_urn: str
        """
        self._function_graph_urn = function_graph_urn

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
        if not isinstance(other, CreatePrivateProviderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
