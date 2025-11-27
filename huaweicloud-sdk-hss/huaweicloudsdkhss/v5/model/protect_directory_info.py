# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectDirectoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_directory': 'str',
        'exclude_child_directory_list': 'list[str]',
        'exclude_file_list': 'list[str]',
        'backup_directory': 'str'
    }

    attribute_map = {
        'protect_directory': 'protect_directory',
        'exclude_child_directory_list': 'exclude_child_directory_list',
        'exclude_file_list': 'exclude_file_list',
        'backup_directory': 'backup_directory'
    }

    def __init__(self, protect_directory=None, exclude_child_directory_list=None, exclude_file_list=None, backup_directory=None):
        r"""ProtectDirectoryInfo

        The model defined in huaweicloud sdk

        :param protect_directory: **参数解释**： 防护目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 
        :type protect_directory: str
        :param exclude_child_directory_list: **参数解释**： 需要排除的子目录列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 
        :type exclude_child_directory_list: list[str]
        :param exclude_file_list: **参数解释**： 需要排除的子文件列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 
        :type exclude_file_list: list[str]
        :param backup_directory: **参数解释**： 备份目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 
        :type backup_directory: str
        """
        
        

        self._protect_directory = None
        self._exclude_child_directory_list = None
        self._exclude_file_list = None
        self._backup_directory = None
        self.discriminator = None

        self.protect_directory = protect_directory
        if exclude_child_directory_list is not None:
            self.exclude_child_directory_list = exclude_child_directory_list
        if exclude_file_list is not None:
            self.exclude_file_list = exclude_file_list
        if backup_directory is not None:
            self.backup_directory = backup_directory

    @property
    def protect_directory(self):
        r"""Gets the protect_directory of this ProtectDirectoryInfo.

        **参数解释**： 防护目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :return: The protect_directory of this ProtectDirectoryInfo.
        :rtype: str
        """
        return self._protect_directory

    @protect_directory.setter
    def protect_directory(self, protect_directory):
        r"""Sets the protect_directory of this ProtectDirectoryInfo.

        **参数解释**： 防护目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :param protect_directory: The protect_directory of this ProtectDirectoryInfo.
        :type protect_directory: str
        """
        self._protect_directory = protect_directory

    @property
    def exclude_child_directory_list(self):
        r"""Gets the exclude_child_directory_list of this ProtectDirectoryInfo.

        **参数解释**： 需要排除的子目录列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The exclude_child_directory_list of this ProtectDirectoryInfo.
        :rtype: list[str]
        """
        return self._exclude_child_directory_list

    @exclude_child_directory_list.setter
    def exclude_child_directory_list(self, exclude_child_directory_list):
        r"""Sets the exclude_child_directory_list of this ProtectDirectoryInfo.

        **参数解释**： 需要排除的子目录列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :param exclude_child_directory_list: The exclude_child_directory_list of this ProtectDirectoryInfo.
        :type exclude_child_directory_list: list[str]
        """
        self._exclude_child_directory_list = exclude_child_directory_list

    @property
    def exclude_file_list(self):
        r"""Gets the exclude_file_list of this ProtectDirectoryInfo.

        **参数解释**： 需要排除的子文件列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The exclude_file_list of this ProtectDirectoryInfo.
        :rtype: list[str]
        """
        return self._exclude_file_list

    @exclude_file_list.setter
    def exclude_file_list(self, exclude_file_list):
        r"""Sets the exclude_file_list of this ProtectDirectoryInfo.

        **参数解释**： 需要排除的子文件列表 **约束限制**: 不涉及 **取值范围**： 最少0条，最多10条 **默认取值**: 不涉及 

        :param exclude_file_list: The exclude_file_list of this ProtectDirectoryInfo.
        :type exclude_file_list: list[str]
        """
        self._exclude_file_list = exclude_file_list

    @property
    def backup_directory(self):
        r"""Gets the backup_directory of this ProtectDirectoryInfo.

        **参数解释**： 备份目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :return: The backup_directory of this ProtectDirectoryInfo.
        :rtype: str
        """
        return self._backup_directory

    @backup_directory.setter
    def backup_directory(self, backup_directory):
        r"""Sets the backup_directory of this ProtectDirectoryInfo.

        **参数解释**： 备份目录 **约束限制**: 不涉及 **取值范围**： 字符长度1-256位 **默认取值**: 不涉及 

        :param backup_directory: The backup_directory of this ProtectDirectoryInfo.
        :type backup_directory: str
        """
        self._backup_directory = backup_directory

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtectDirectoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
