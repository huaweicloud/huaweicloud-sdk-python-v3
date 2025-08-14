# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateModuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_name': 'str',
        'module_version': 'str',
        'module_description': 'str',
        'module_uri': 'str',
        'version_description': 'str'
    }

    attribute_map = {
        'module_name': 'module_name',
        'module_version': 'module_version',
        'module_description': 'module_description',
        'module_uri': 'module_uri',
        'version_description': 'version_description'
    }

    def __init__(self, module_name=None, module_version=None, module_description=None, module_uri=None, version_description=None):
        r"""CreatePrivateModuleRequestBody

        The model defined in huaweicloud sdk

        :param module_name: 私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type module_name: str
        :param module_version: 模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义
        :type module_version: str
        :param module_description: 私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。
        :type module_description: str
        :param module_uri: 模块（module）包的OBS地址。模块允许用户将可复用的代码编辑在一起供模块使用。  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  模块包只支持zip压缩包，文件需要以\&quot;.zip\&quot;结尾。关于模块包的校验要求如下：   * 模块包中不得包含以\&quot;.tfvars\&quot;结尾的文件   * 模块包解压前后的大小均应控制在1MB以内   * 模块包内的文件数量不能超过100个   * 模块包内的文件路径不允许以正斜线（/）开头   * 模块包内的文件路径分隔符之间不允许为空格、\&quot;.\&quot;和\&quot;..\&quot;   * 模块包内的文件路径最长为2048   * 模块包内的文件名最长为255   * 模块包内应至少有一份模板文件（以\&quot;.tf\&quot;或\&quot;.tf.json\&quot;结尾的文件）  **注意：**   * 模块中的内容不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储module_uri对应的模块包。
        :type module_uri: str
        :param version_description: 模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建
        :type version_description: str
        """
        
        

        self._module_name = None
        self._module_version = None
        self._module_description = None
        self._module_uri = None
        self._version_description = None
        self.discriminator = None

        self.module_name = module_name
        if module_version is not None:
            self.module_version = module_version
        if module_description is not None:
            self.module_description = module_description
        if module_uri is not None:
            self.module_uri = module_uri
        if version_description is not None:
            self.version_description = version_description

    @property
    def module_name(self):
        r"""Gets the module_name of this CreatePrivateModuleRequestBody.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The module_name of this CreatePrivateModuleRequestBody.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this CreatePrivateModuleRequestBody.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param module_name: The module_name of this CreatePrivateModuleRequestBody.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_version(self):
        r"""Gets the module_version of this CreatePrivateModuleRequestBody.

        模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :return: The module_version of this CreatePrivateModuleRequestBody.
        :rtype: str
        """
        return self._module_version

    @module_version.setter
    def module_version(self, module_version):
        r"""Sets the module_version of this CreatePrivateModuleRequestBody.

        模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :param module_version: The module_version of this CreatePrivateModuleRequestBody.
        :type module_version: str
        """
        self._module_version = module_version

    @property
    def module_description(self):
        r"""Gets the module_description of this CreatePrivateModuleRequestBody.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :return: The module_description of this CreatePrivateModuleRequestBody.
        :rtype: str
        """
        return self._module_description

    @module_description.setter
    def module_description(self, module_description):
        r"""Sets the module_description of this CreatePrivateModuleRequestBody.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :param module_description: The module_description of this CreatePrivateModuleRequestBody.
        :type module_description: str
        """
        self._module_description = module_description

    @property
    def module_uri(self):
        r"""Gets the module_uri of this CreatePrivateModuleRequestBody.

        模块（module）包的OBS地址。模块允许用户将可复用的代码编辑在一起供模块使用。  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  模块包只支持zip压缩包，文件需要以\".zip\"结尾。关于模块包的校验要求如下：   * 模块包中不得包含以\".tfvars\"结尾的文件   * 模块包解压前后的大小均应控制在1MB以内   * 模块包内的文件数量不能超过100个   * 模块包内的文件路径不允许以正斜线（/）开头   * 模块包内的文件路径分隔符之间不允许为空格、\".\"和\"..\"   * 模块包内的文件路径最长为2048   * 模块包内的文件名最长为255   * 模块包内应至少有一份模板文件（以\".tf\"或\".tf.json\"结尾的文件）  **注意：**   * 模块中的内容不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储module_uri对应的模块包。

        :return: The module_uri of this CreatePrivateModuleRequestBody.
        :rtype: str
        """
        return self._module_uri

    @module_uri.setter
    def module_uri(self, module_uri):
        r"""Sets the module_uri of this CreatePrivateModuleRequestBody.

        模块（module）包的OBS地址。模块允许用户将可复用的代码编辑在一起供模块使用。  OBS地址支持同类型Region之间进行互相访问（Region分为通用Region和专属Region，通用Region指面向公共租户提供通用云服务的Region；专属Region指只承载同一类业务或只面向特定租户提供业务服务的专用Region）  模块包只支持zip压缩包，文件需要以\".zip\"结尾。关于模块包的校验要求如下：   * 模块包中不得包含以\".tfvars\"结尾的文件   * 模块包解压前后的大小均应控制在1MB以内   * 模块包内的文件数量不能超过100个   * 模块包内的文件路径不允许以正斜线（/）开头   * 模块包内的文件路径分隔符之间不允许为空格、\".\"和\"..\"   * 模块包内的文件路径最长为2048   * 模块包内的文件名最长为255   * 模块包内应至少有一份模板文件（以\".tf\"或\".tf.json\"结尾的文件）  **注意：**   * 模块中的内容不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储module_uri对应的模块包。

        :param module_uri: The module_uri of this CreatePrivateModuleRequestBody.
        :type module_uri: str
        """
        self._module_uri = module_uri

    @property
    def version_description(self):
        r"""Gets the version_description of this CreatePrivateModuleRequestBody.

        模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建

        :return: The version_description of this CreatePrivateModuleRequestBody.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this CreatePrivateModuleRequestBody.

        模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建

        :param version_description: The version_description of this CreatePrivateModuleRequestBody.
        :type version_description: str
        """
        self._version_description = version_description

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
        if not isinstance(other, CreatePrivateModuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
