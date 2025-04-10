# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateHookVersionSummary:

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
        'hook_id': 'str',
        'hook_version': 'str',
        'hook_version_description': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'hook_name': 'hook_name',
        'hook_id': 'hook_id',
        'hook_version': 'hook_version',
        'hook_version_description': 'hook_version_description',
        'create_time': 'create_time'
    }

    def __init__(self, hook_name=None, hook_id=None, hook_version=None, hook_version_description=None, create_time=None):
        r"""PrivateHookVersionSummary

        The model defined in huaweicloud sdk

        :param hook_name: 私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。
        :type hook_name: str
        :param hook_id: 私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。
        :type hook_id: str
        :param hook_version: 私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type hook_version: str
        :param hook_version_description: 私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。
        :type hook_version_description: str
        :param create_time: 私有Hook Version（private-hook-version）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        """
        
        

        self._hook_name = None
        self._hook_id = None
        self._hook_version = None
        self._hook_version_description = None
        self._create_time = None
        self.discriminator = None

        self.hook_name = hook_name
        if hook_id is not None:
            self.hook_id = hook_id
        self.hook_version = hook_version
        if hook_version_description is not None:
            self.hook_version_description = hook_version_description
        if create_time is not None:
            self.create_time = create_time

    @property
    def hook_name(self):
        r"""Gets the hook_name of this PrivateHookVersionSummary.

        私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。

        :return: The hook_name of this PrivateHookVersionSummary.
        :rtype: str
        """
        return self._hook_name

    @hook_name.setter
    def hook_name(self, hook_name):
        r"""Sets the hook_name of this PrivateHookVersionSummary.

        私有hook的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。  推荐用户使用三段命名空间：{自定义hook名称}-{hook应用场景}-hook。

        :param hook_name: The hook_name of this PrivateHookVersionSummary.
        :type hook_name: str
        """
        self._hook_name = hook_name

    @property
    def hook_id(self):
        r"""Gets the hook_id of this PrivateHookVersionSummary.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :return: The hook_id of this PrivateHookVersionSummary.
        :rtype: str
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this PrivateHookVersionSummary.

        私有hook（private-hook）的唯一Id。  此Id由资源编排服务在生成私有hook的时候生成，为UUID。  由于私有hook名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的私有hook，删除，再重新创建一个同名私有hook。  对于团队并行开发，用户可能希望确保，当前我操作的私有hook就是我认为的那个，而不是其他队友删除后创建的同名私有hook。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有hook所对应的Id都不相同，更新不会影响Id。如果给予的hook_id和当前hook的Id不一致，则返回400。

        :param hook_id: The hook_id of this PrivateHookVersionSummary.
        :type hook_id: str
        """
        self._hook_id = hook_id

    @property
    def hook_version(self):
        r"""Gets the hook_version of this PrivateHookVersionSummary.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The hook_version of this PrivateHookVersionSummary.
        :rtype: str
        """
        return self._hook_version

    @hook_version.setter
    def hook_version(self, hook_version):
        r"""Sets the hook_version of this PrivateHookVersionSummary.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param hook_version: The hook_version of this PrivateHookVersionSummary.
        :type hook_version: str
        """
        self._hook_version = hook_version

    @property
    def hook_version_description(self):
        r"""Gets the hook_version_description of this PrivateHookVersionSummary.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :return: The hook_version_description of this PrivateHookVersionSummary.
        :rtype: str
        """
        return self._hook_version_description

    @hook_version_description.setter
    def hook_version_description(self, hook_version_description):
        r"""Sets the hook_version_description of this PrivateHookVersionSummary.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :param hook_version_description: The hook_version_description of this PrivateHookVersionSummary.
        :type hook_version_description: str
        """
        self._hook_version_description = hook_version_description

    @property
    def create_time(self):
        r"""Gets the create_time of this PrivateHookVersionSummary.

        私有Hook Version（private-hook-version）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this PrivateHookVersionSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PrivateHookVersionSummary.

        私有Hook Version（private-hook-version）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this PrivateHookVersionSummary.
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
        if not isinstance(other, PrivateHookVersionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
