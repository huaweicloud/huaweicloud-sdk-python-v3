# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateModuleSummary:

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
        'module_description': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'module_name': 'module_name',
        'module_id': 'module_id',
        'module_description': 'module_description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, module_name=None, module_id=None, module_description=None, create_time=None, update_time=None):
        r"""PrivateModuleSummary

        The model defined in huaweicloud sdk

        :param module_name: 私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type module_name: str
        :param module_id: 私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400
        :type module_id: str
        :param module_description: 私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。
        :type module_description: str
        :param create_time: 私有模块（private-module）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 私有模块（private-module）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        

        self._module_name = None
        self._module_id = None
        self._module_description = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.module_name = module_name
        if module_id is not None:
            self.module_id = module_id
        if module_description is not None:
            self.module_description = module_description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def module_name(self):
        r"""Gets the module_name of this PrivateModuleSummary.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The module_name of this PrivateModuleSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this PrivateModuleSummary.

        私有模块（private-module）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param module_name: The module_name of this PrivateModuleSummary.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_id(self):
        r"""Gets the module_id of this PrivateModuleSummary.

        私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400

        :return: The module_id of this PrivateModuleSummary.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this PrivateModuleSummary.

        私有模块（private-module）的唯一Id。  此Id由资源编排服务在生成模块的时候生成，为UUID。  由于私有模块名仅在同一时间下唯一，即允许用户先生成一个叫HelloWorld的私有模块，删除，再重新创建一个同名私有模块。  对于团队并行开发，用户可能希望确保，当前我操作的私有模块就是我以为的那个，而不是其他队友删除后创建的同名私有模块。因此，使用Id就可以做到强匹配。  资源编排服务保证每次创建的私有模块所对应的Id都不相同，更新不会影响Id。如果给予的module_id和当前模块的Id不一致，则返回400

        :param module_id: The module_id of this PrivateModuleSummary.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def module_description(self):
        r"""Gets the module_description of this PrivateModuleSummary.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :return: The module_description of this PrivateModuleSummary.
        :rtype: str
        """
        return self._module_description

    @module_description.setter
    def module_description(self, module_description):
        r"""Sets the module_description of this PrivateModuleSummary.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :param module_description: The module_description of this PrivateModuleSummary.
        :type module_description: str
        """
        self._module_description = module_description

    @property
    def create_time(self):
        r"""Gets the create_time of this PrivateModuleSummary.

        私有模块（private-module）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this PrivateModuleSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PrivateModuleSummary.

        私有模块（private-module）的生成时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this PrivateModuleSummary.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PrivateModuleSummary.

        私有模块（private-module）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this PrivateModuleSummary.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PrivateModuleSummary.

        私有模块（private-module）的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this PrivateModuleSummary.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, PrivateModuleSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
