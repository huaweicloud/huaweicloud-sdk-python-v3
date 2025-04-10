# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateHookRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_name': 'str',
        'hook_version': 'str',
        'hook_description': 'str',
        'hook_version_description': 'str',
        'configuration': 'ConfigurationPrimitiveTypeHolderConfiguration',
        'policy_uri': 'str',
        'policy_body': 'str'
    }

    attribute_map = {
        'hook_name': 'hook_name',
        'hook_version': 'hook_version',
        'hook_description': 'hook_description',
        'hook_version_description': 'hook_version_description',
        'configuration': 'configuration',
        'policy_uri': 'policy_uri',
        'policy_body': 'policy_body'
    }

    def __init__(self, hook_name=None, hook_version=None, hook_description=None, hook_version_description=None, configuration=None, policy_uri=None, policy_body=None):
        r"""CreatePrivateHookRequestBody

        The model defined in huaweicloud sdk

        :param hook_name: 私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。
        :type hook_name: str
        :param hook_version: 私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type hook_version: str
        :param hook_description: 私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。
        :type hook_description: str
        :param hook_version_description: 私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。
        :type hook_version_description: str
        :param configuration: 
        :type configuration: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        :param policy_uri: 策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\&quot;.rego\&quot;结尾，压缩包当前只支持zip格式，文件需要以&#x60;.zip&#x60;结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在
        :type policy_uri: str
        :param policy_body: 策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在
        :type policy_body: str
        """
        
        

        self._hook_name = None
        self._hook_version = None
        self._hook_description = None
        self._hook_version_description = None
        self._configuration = None
        self._policy_uri = None
        self._policy_body = None
        self.discriminator = None

        self.hook_name = hook_name
        self.hook_version = hook_version
        if hook_description is not None:
            self.hook_description = hook_description
        if hook_version_description is not None:
            self.hook_version_description = hook_version_description
        if configuration is not None:
            self.configuration = configuration
        if policy_uri is not None:
            self.policy_uri = policy_uri
        if policy_body is not None:
            self.policy_body = policy_body

    @property
    def hook_name(self):
        r"""Gets the hook_name of this CreatePrivateHookRequestBody.

        私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。

        :return: The hook_name of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._hook_name

    @hook_name.setter
    def hook_name(self, hook_name):
        r"""Sets the hook_name of this CreatePrivateHookRequestBody.

        私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。

        :param hook_name: The hook_name of this CreatePrivateHookRequestBody.
        :type hook_name: str
        """
        self._hook_name = hook_name

    @property
    def hook_version(self):
        r"""Gets the hook_version of this CreatePrivateHookRequestBody.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The hook_version of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._hook_version

    @hook_version.setter
    def hook_version(self, hook_version):
        r"""Sets the hook_version of this CreatePrivateHookRequestBody.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param hook_version: The hook_version of this CreatePrivateHookRequestBody.
        :type hook_version: str
        """
        self._hook_version = hook_version

    @property
    def hook_description(self):
        r"""Gets the hook_description of this CreatePrivateHookRequestBody.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :return: The hook_description of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._hook_description

    @hook_description.setter
    def hook_description(self, hook_description):
        r"""Sets the hook_description of this CreatePrivateHookRequestBody.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :param hook_description: The hook_description of this CreatePrivateHookRequestBody.
        :type hook_description: str
        """
        self._hook_description = hook_description

    @property
    def hook_version_description(self):
        r"""Gets the hook_version_description of this CreatePrivateHookRequestBody.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :return: The hook_version_description of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._hook_version_description

    @hook_version_description.setter
    def hook_version_description(self, hook_version_description):
        r"""Sets the hook_version_description of this CreatePrivateHookRequestBody.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :param hook_version_description: The hook_version_description of this CreatePrivateHookRequestBody.
        :type hook_version_description: str
        """
        self._hook_version_description = hook_version_description

    @property
    def configuration(self):
        r"""Gets the configuration of this CreatePrivateHookRequestBody.

        :return: The configuration of this CreatePrivateHookRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this CreatePrivateHookRequestBody.

        :param configuration: The configuration of this CreatePrivateHookRequestBody.
        :type configuration: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        """
        self._configuration = configuration

    @property
    def policy_uri(self):
        r"""Gets the policy_uri of this CreatePrivateHookRequestBody.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :return: The policy_uri of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        r"""Sets the policy_uri of this CreatePrivateHookRequestBody.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :param policy_uri: The policy_uri of this CreatePrivateHookRequestBody.
        :type policy_uri: str
        """
        self._policy_uri = policy_uri

    @property
    def policy_body(self):
        r"""Gets the policy_body of this CreatePrivateHookRequestBody.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :return: The policy_body of this CreatePrivateHookRequestBody.
        :rtype: str
        """
        return self._policy_body

    @policy_body.setter
    def policy_body(self, policy_body):
        r"""Sets the policy_body of this CreatePrivateHookRequestBody.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :param policy_body: The policy_body of this CreatePrivateHookRequestBody.
        :type policy_body: str
        """
        self._policy_body = policy_body

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
        if not isinstance(other, CreatePrivateHookRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
