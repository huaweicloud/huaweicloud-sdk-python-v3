# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateHookVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_id': 'str',
        'hook_version': 'str',
        'hook_version_description': 'str',
        'policy_uri': 'str',
        'policy_body': 'str'
    }

    attribute_map = {
        'hook_id': 'hook_id',
        'hook_version': 'hook_version',
        'hook_version_description': 'hook_version_description',
        'policy_uri': 'policy_uri',
        'policy_body': 'policy_body'
    }

    def __init__(self, hook_id=None, hook_version=None, hook_version_description=None, policy_uri=None, policy_body=None):
        r"""CreatePrivateHookVersionRequestBody

        The model defined in huaweicloud sdk

        :param hook_id: 私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。
        :type hook_id: str
        :param hook_version: 私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type hook_version: str
        :param hook_version_description: 私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。
        :type hook_version_description: str
        :param policy_uri: 策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\&quot;.rego\&quot;结尾，压缩包当前只支持zip格式，文件需要以&#x60;.zip&#x60;结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在
        :type policy_uri: str
        :param policy_body: 策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在
        :type policy_body: str
        """
        
        

        self._hook_id = None
        self._hook_version = None
        self._hook_version_description = None
        self._policy_uri = None
        self._policy_body = None
        self.discriminator = None

        if hook_id is not None:
            self.hook_id = hook_id
        self.hook_version = hook_version
        if hook_version_description is not None:
            self.hook_version_description = hook_version_description
        if policy_uri is not None:
            self.policy_uri = policy_uri
        if policy_body is not None:
            self.policy_body = policy_body

    @property
    def hook_id(self):
        r"""Gets the hook_id of this CreatePrivateHookVersionRequestBody.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :return: The hook_id of this CreatePrivateHookVersionRequestBody.
        :rtype: str
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this CreatePrivateHookVersionRequestBody.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :param hook_id: The hook_id of this CreatePrivateHookVersionRequestBody.
        :type hook_id: str
        """
        self._hook_id = hook_id

    @property
    def hook_version(self):
        r"""Gets the hook_version of this CreatePrivateHookVersionRequestBody.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The hook_version of this CreatePrivateHookVersionRequestBody.
        :rtype: str
        """
        return self._hook_version

    @hook_version.setter
    def hook_version(self, hook_version):
        r"""Sets the hook_version of this CreatePrivateHookVersionRequestBody.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param hook_version: The hook_version of this CreatePrivateHookVersionRequestBody.
        :type hook_version: str
        """
        self._hook_version = hook_version

    @property
    def hook_version_description(self):
        r"""Gets the hook_version_description of this CreatePrivateHookVersionRequestBody.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :return: The hook_version_description of this CreatePrivateHookVersionRequestBody.
        :rtype: str
        """
        return self._hook_version_description

    @hook_version_description.setter
    def hook_version_description(self, hook_version_description):
        r"""Sets the hook_version_description of this CreatePrivateHookVersionRequestBody.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :param hook_version_description: The hook_version_description of this CreatePrivateHookVersionRequestBody.
        :type hook_version_description: str
        """
        self._hook_version_description = hook_version_description

    @property
    def policy_uri(self):
        r"""Gets the policy_uri of this CreatePrivateHookVersionRequestBody.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :return: The policy_uri of this CreatePrivateHookVersionRequestBody.
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        r"""Sets the policy_uri of this CreatePrivateHookVersionRequestBody.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :param policy_uri: The policy_uri of this CreatePrivateHookVersionRequestBody.
        :type policy_uri: str
        """
        self._policy_uri = policy_uri

    @property
    def policy_body(self):
        r"""Gets the policy_body of this CreatePrivateHookVersionRequestBody.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :return: The policy_body of this CreatePrivateHookVersionRequestBody.
        :rtype: str
        """
        return self._policy_body

    @policy_body.setter
    def policy_body(self, policy_body):
        r"""Sets the policy_body of this CreatePrivateHookVersionRequestBody.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :param policy_body: The policy_body of this CreatePrivateHookVersionRequestBody.
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
        if not isinstance(other, CreatePrivateHookVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
