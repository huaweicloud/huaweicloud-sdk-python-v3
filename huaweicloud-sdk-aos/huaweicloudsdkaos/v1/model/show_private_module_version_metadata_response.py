# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrivateModuleVersionMetadataResponse(SdkResponse):

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
        'module_id': 'str',
        'module_version': 'str',
        'version_description': 'str',
        'create_time': 'str',
        'module_source': 'str'
    }

    attribute_map = {
        'module_name': 'module_name',
        'module_id': 'module_id',
        'module_version': 'module_version',
        'version_description': 'version_description',
        'create_time': 'create_time',
        'module_source': 'module_source'
    }

    def __init__(self, module_name=None, module_id=None, module_version=None, version_description=None, create_time=None, module_source=None):
        r"""ShowPrivateModuleVersionMetadataResponse

        The model defined in huaweicloud sdk

        :param module_name: 私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type module_name: str
        :param module_id: 私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400
        :type module_id: str
        :param module_version: 模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义
        :type module_version: str
        :param version_description: 模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建
        :type version_description: str
        :param create_time: 私有模块（private-module）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param module_source: 在模板中使用模块需要定义如下格式：   module \&quot;my_hello_word_module\&quot; {     source &#x3D; {module_source}   }  其中{module_source}为本参数
        :type module_source: str
        """
        
        super(ShowPrivateModuleVersionMetadataResponse, self).__init__()

        self._module_name = None
        self._module_id = None
        self._module_version = None
        self._version_description = None
        self._create_time = None
        self._module_source = None
        self.discriminator = None

        self.module_name = module_name
        if module_id is not None:
            self.module_id = module_id
        if module_version is not None:
            self.module_version = module_version
        if version_description is not None:
            self.version_description = version_description
        if create_time is not None:
            self.create_time = create_time
        if module_source is not None:
            self.module_source = module_source

    @property
    def module_name(self):
        r"""Gets the module_name of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The module_name of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param module_name: The module_name of this ShowPrivateModuleVersionMetadataResponse.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_id(self):
        r"""Gets the module_id of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400

        :return: The module_id of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400

        :param module_id: The module_id of this ShowPrivateModuleVersionMetadataResponse.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_version(self):
        r"""Gets the module_version of this ShowPrivateModuleVersionMetadataResponse.

        模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :return: The module_version of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._module_version

    @module_version.setter
    def module_version(self, module_version):
        r"""Sets the module_version of this ShowPrivateModuleVersionMetadataResponse.

        模块的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :param module_version: The module_version of this ShowPrivateModuleVersionMetadataResponse.
        :type module_version: str
        """
        self._module_version = module_version

    @property
    def version_description(self):
        r"""Gets the version_description of this ShowPrivateModuleVersionMetadataResponse.

        模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建

        :return: The version_description of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ShowPrivateModuleVersionMetadataResponse.

        模块版本（module version）的描述。可用于客户识别并管理模块的版本。注意：模块版本为不可更新（immutable），即描述不可更新，如果需要更新，请删除后重建

        :param version_description: The version_description of this ShowPrivateModuleVersionMetadataResponse.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPrivateModuleVersionMetadataResponse.

        私有模块（private-module）版本的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this ShowPrivateModuleVersionMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def module_source(self):
        r"""Gets the module_source of this ShowPrivateModuleVersionMetadataResponse.

        在模板中使用模块需要定义如下格式：   module \"my_hello_word_module\" {     source = {module_source}   }  其中{module_source}为本参数

        :return: The module_source of this ShowPrivateModuleVersionMetadataResponse.
        :rtype: str
        """
        return self._module_source

    @module_source.setter
    def module_source(self, module_source):
        r"""Sets the module_source of this ShowPrivateModuleVersionMetadataResponse.

        在模板中使用模块需要定义如下格式：   module \"my_hello_word_module\" {     source = {module_source}   }  其中{module_source}为本参数

        :param module_source: The module_source of this ShowPrivateModuleVersionMetadataResponse.
        :type module_source: str
        """
        self._module_source = module_source

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
        if not isinstance(other, ShowPrivateModuleVersionMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
