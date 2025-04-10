# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivatePolicyURIPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_uri': 'str'
    }

    attribute_map = {
        'policy_uri': 'policy_uri'
    }

    def __init__(self, policy_uri=None):
        r"""PrivatePolicyURIPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param policy_uri: 策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\&quot;.rego\&quot;结尾，压缩包当前只支持zip格式，文件需要以&#x60;.zip&#x60;结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在
        :type policy_uri: str
        """
        
        

        self._policy_uri = None
        self.discriminator = None

        if policy_uri is not None:
            self.policy_uri = policy_uri

    @property
    def policy_uri(self):
        r"""Gets the policy_uri of this PrivatePolicyURIPrimitiveTypeHolder.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :return: The policy_uri of this PrivatePolicyURIPrimitiveTypeHolder.
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        r"""Sets the policy_uri of this PrivatePolicyURIPrimitiveTypeHolder.

        策略文件的OBS地址。内容仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  请确保OBS地址所在局点与使用RFS服务局点一致。  策略文件当前支持单文件或zip压缩包，单文件需要以\".rego\"结尾，压缩包当前只支持zip格式，文件需要以`.zip`结尾。  关于策略文件的校验要求如下：   * 文件必须是UTF8编码   * 创建时会对大小、格式、语法等进行校验   * 策略文件必须是UTF-8编码   * 单文件或压缩包解压前后的大小应控制在1MB以内   * 压缩包内的文件数量不能超过100个   * 压缩包内的文件路径最长为2048   * 压缩包内的文件名最长为255个字节  policy_uri和policy_body必须有且只有一个存在

        :param policy_uri: The policy_uri of this PrivatePolicyURIPrimitiveTypeHolder.
        :type policy_uri: str
        """
        self._policy_uri = policy_uri

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
        if not isinstance(other, PrivatePolicyURIPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
