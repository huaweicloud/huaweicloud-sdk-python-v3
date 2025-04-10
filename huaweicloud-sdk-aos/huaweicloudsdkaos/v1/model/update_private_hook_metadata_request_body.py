# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateHookMetadataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_description': 'str',
        'hook_id': 'str',
        'default_version': 'str',
        'configuration': 'ConfigurationPrimitiveTypeHolderConfiguration'
    }

    attribute_map = {
        'hook_description': 'hook_description',
        'hook_id': 'hook_id',
        'default_version': 'default_version',
        'configuration': 'configuration'
    }

    def __init__(self, hook_description=None, hook_id=None, default_version=None, configuration=None):
        r"""UpdatePrivateHookMetadataRequestBody

        The model defined in huaweicloud sdk

        :param hook_description: 私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。
        :type hook_description: str
        :param hook_id: 私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。
        :type hook_id: str
        :param default_version: 私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type default_version: str
        :param configuration: 
        :type configuration: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        """
        
        

        self._hook_description = None
        self._hook_id = None
        self._default_version = None
        self._configuration = None
        self.discriminator = None

        if hook_description is not None:
            self.hook_description = hook_description
        if hook_id is not None:
            self.hook_id = hook_id
        if default_version is not None:
            self.default_version = default_version
        if configuration is not None:
            self.configuration = configuration

    @property
    def hook_description(self):
        r"""Gets the hook_description of this UpdatePrivateHookMetadataRequestBody.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :return: The hook_description of this UpdatePrivateHookMetadataRequestBody.
        :rtype: str
        """
        return self._hook_description

    @hook_description.setter
    def hook_description(self, hook_description):
        r"""Sets the hook_description of this UpdatePrivateHookMetadataRequestBody.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :param hook_description: The hook_description of this UpdatePrivateHookMetadataRequestBody.
        :type hook_description: str
        """
        self._hook_description = hook_description

    @property
    def hook_id(self):
        r"""Gets the hook_id of this UpdatePrivateHookMetadataRequestBody.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :return: The hook_id of this UpdatePrivateHookMetadataRequestBody.
        :rtype: str
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this UpdatePrivateHookMetadataRequestBody.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :param hook_id: The hook_id of this UpdatePrivateHookMetadataRequestBody.
        :type hook_id: str
        """
        self._hook_id = hook_id

    @property
    def default_version(self):
        r"""Gets the default_version of this UpdatePrivateHookMetadataRequestBody.

        私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The default_version of this UpdatePrivateHookMetadataRequestBody.
        :rtype: str
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        r"""Sets the default_version of this UpdatePrivateHookMetadataRequestBody.

        私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param default_version: The default_version of this UpdatePrivateHookMetadataRequestBody.
        :type default_version: str
        """
        self._default_version = default_version

    @property
    def configuration(self):
        r"""Gets the configuration of this UpdatePrivateHookMetadataRequestBody.

        :return: The configuration of this UpdatePrivateHookMetadataRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this UpdatePrivateHookMetadataRequestBody.

        :param configuration: The configuration of this UpdatePrivateHookMetadataRequestBody.
        :type configuration: :class:`huaweicloudsdkaos.v1.ConfigurationPrimitiveTypeHolderConfiguration`
        """
        self._configuration = configuration

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
        if not isinstance(other, UpdatePrivateHookMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
