# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IacScanRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_mode': 'str',
        'path': 'str'
    }

    attribute_map = {
        'configuration_mode': 'configuration_mode',
        'path': 'path'
    }

    def __init__(self, configuration_mode=None, path=None):
        r"""IacScanRequestInfo

        The model defined in huaweicloud sdk

        :param configuration_mode: **参数解释**: 配置方式 **约束限制**: 不涉及 **取值范围**: - local_directory：本地目录。 - remote_address：https远程地址。 - git_repository_address：git仓库地址。  **默认取值**: 不涉及 
        :type configuration_mode: str
        :param path: **参数解释**: 配置文件路径 **约束限制**: 不涉及 **取值范围**: 字符取值1-256 **默认取值**: 不涉及 
        :type path: str
        """
        
        

        self._configuration_mode = None
        self._path = None
        self.discriminator = None

        if configuration_mode is not None:
            self.configuration_mode = configuration_mode
        if path is not None:
            self.path = path

    @property
    def configuration_mode(self):
        r"""Gets the configuration_mode of this IacScanRequestInfo.

        **参数解释**: 配置方式 **约束限制**: 不涉及 **取值范围**: - local_directory：本地目录。 - remote_address：https远程地址。 - git_repository_address：git仓库地址。  **默认取值**: 不涉及 

        :return: The configuration_mode of this IacScanRequestInfo.
        :rtype: str
        """
        return self._configuration_mode

    @configuration_mode.setter
    def configuration_mode(self, configuration_mode):
        r"""Sets the configuration_mode of this IacScanRequestInfo.

        **参数解释**: 配置方式 **约束限制**: 不涉及 **取值范围**: - local_directory：本地目录。 - remote_address：https远程地址。 - git_repository_address：git仓库地址。  **默认取值**: 不涉及 

        :param configuration_mode: The configuration_mode of this IacScanRequestInfo.
        :type configuration_mode: str
        """
        self._configuration_mode = configuration_mode

    @property
    def path(self):
        r"""Gets the path of this IacScanRequestInfo.

        **参数解释**: 配置文件路径 **约束限制**: 不涉及 **取值范围**: 字符取值1-256 **默认取值**: 不涉及 

        :return: The path of this IacScanRequestInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this IacScanRequestInfo.

        **参数解释**: 配置文件路径 **约束限制**: 不涉及 **取值范围**: 字符取值1-256 **默认取值**: 不涉及 

        :param path: The path of this IacScanRequestInfo.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, IacScanRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
