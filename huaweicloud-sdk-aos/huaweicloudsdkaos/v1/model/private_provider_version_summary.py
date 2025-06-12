# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateProviderVersionSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'provider_name': 'str',
        'provider_version': 'str',
        'version_description': 'str',
        'function_graph_urn': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'provider_version': 'provider_version',
        'version_description': 'version_description',
        'function_graph_urn': 'function_graph_urn',
        'create_time': 'create_time'
    }

    def __init__(self, provider_id=None, provider_name=None, provider_version=None, version_description=None, function_graph_urn=None, create_time=None):
        r"""PrivateProviderVersionSummary

        The model defined in huaweicloud sdk

        :param provider_id: 私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400
        :type provider_id: str
        :param provider_name: 私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。
        :type provider_name: str
        :param provider_version: provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义
        :type provider_version: str
        :param version_description: 私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建
        :type version_description: str
        :param function_graph_urn: FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html
        :type function_graph_urn: str
        :param create_time: 私有provider（private-provider）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        """
        
        

        self._provider_id = None
        self._provider_name = None
        self._provider_version = None
        self._version_description = None
        self._function_graph_urn = None
        self._create_time = None
        self.discriminator = None

        if provider_id is not None:
            self.provider_id = provider_id
        self.provider_name = provider_name
        if provider_version is not None:
            self.provider_version = provider_version
        if version_description is not None:
            self.version_description = version_description
        if function_graph_urn is not None:
            self.function_graph_urn = function_graph_urn
        if create_time is not None:
            self.create_time = create_time

    @property
    def provider_id(self):
        r"""Gets the provider_id of this PrivateProviderVersionSummary.

        私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400

        :return: The provider_id of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this PrivateProviderVersionSummary.

        私有provider（private-provider）的唯一Id。  此Id由资源编排服务在生成provider的时候生成，为UUID。  由于私有provider名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有provider，删除，再重新创建一个同名私有provider。  对于团队并行开发，用户可能希望确保，当前我操作的私有provider就是我以为的那个，而不是其他队友删除后创建的同名私有provider。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有provider所对应的Id都不相同，更新不会影响Id。如果给予的provider_id和当前provider的Id不一致，则返回400

        :param provider_id: The provider_id of this PrivateProviderVersionSummary.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this PrivateProviderVersionSummary.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :return: The provider_name of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this PrivateProviderVersionSummary.

        私有provider（private-provider）的名称。此名字在domain_id+region下应唯一，可以使用小写英文、数字、中划线。仅支持以小写英文、数字开头结尾。  按照HCL最佳实践，该名称推荐为在模板中定义的provider的本地名称（local_name）。  创建私有Provider（CreatePrivateProvider）API 还会以 “huawei.com/private-provider”为固定前缀，并以“huawei.com/private-provider/{provider_name}”的形式返回provider_source字段。关于provider_name和provider_source字段在模板中的使用细节，详见创建私有Provider的API描述。

        :param provider_name: The provider_name of this PrivateProviderVersionSummary.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_version(self):
        r"""Gets the provider_version of this PrivateProviderVersionSummary.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :return: The provider_version of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        r"""Sets the provider_version of this PrivateProviderVersionSummary.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :param provider_version: The provider_version of this PrivateProviderVersionSummary.
        :type provider_version: str
        """
        self._provider_version = provider_version

    @property
    def version_description(self):
        r"""Gets the version_description of this PrivateProviderVersionSummary.

        私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建

        :return: The version_description of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this PrivateProviderVersionSummary.

        私有provider版本（provider version）的描述。可用于客户识别并管理私有provider的版本。注意：provider版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建

        :param version_description: The version_description of this PrivateProviderVersionSummary.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def function_graph_urn(self):
        r"""Gets the function_graph_urn of this PrivateProviderVersionSummary.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :return: The function_graph_urn of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._function_graph_urn

    @function_graph_urn.setter
    def function_graph_urn(self, function_graph_urn):
        r"""Sets the function_graph_urn of this PrivateProviderVersionSummary.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :param function_graph_urn: The function_graph_urn of this PrivateProviderVersionSummary.
        :type function_graph_urn: str
        """
        self._function_graph_urn = function_graph_urn

    @property
    def create_time(self):
        r"""Gets the create_time of this PrivateProviderVersionSummary.

        私有provider（private-provider）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this PrivateProviderVersionSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PrivateProviderVersionSummary.

        私有provider（private-provider）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this PrivateProviderVersionSummary.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, PrivateProviderVersionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
