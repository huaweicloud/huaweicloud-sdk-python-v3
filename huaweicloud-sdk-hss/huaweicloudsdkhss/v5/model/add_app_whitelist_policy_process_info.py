# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAppWhitelistPolicyProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_name': 'str',
        'process_path': 'str',
        'process_hash': 'str',
        'container_id': 'str',
        'cmdline': 'str',
        'file_size': 'int'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_hash': 'process_hash',
        'container_id': 'container_id',
        'cmdline': 'cmdline',
        'file_size': 'file_size'
    }

    def __init__(self, process_name=None, process_path=None, process_hash=None, container_id=None, cmdline=None, file_size=None):
        r"""AddAppWhitelistPolicyProcessInfo

        The model defined in huaweicloud sdk

        :param process_name: **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 
        :type process_name: str
        :param process_path: **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 
        :type process_path: str
        :param process_hash: 进程hash
        :type process_hash: str
        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-128位 
        :type container_id: str
        :param cmdline: **参数解释**： 进程命令行 **约束限制**： 不涉及 
        :type cmdline: str
        :param file_size: **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type file_size: int
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_hash = None
        self._container_id = None
        self._cmdline = None
        self._file_size = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_hash is not None:
            self.process_hash = process_hash
        if container_id is not None:
            self.container_id = container_id
        if cmdline is not None:
            self.cmdline = cmdline
        if file_size is not None:
            self.file_size = file_size

    @property
    def process_name(self):
        r"""Gets the process_name of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :return: The process_name of this AddAppWhitelistPolicyProcessInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :param process_name: The process_name of this AddAppWhitelistPolicyProcessInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        r"""Gets the process_path of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :return: The process_path of this AddAppWhitelistPolicyProcessInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :param process_path: The process_path of this AddAppWhitelistPolicyProcessInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_hash(self):
        r"""Gets the process_hash of this AddAppWhitelistPolicyProcessInfo.

        进程hash

        :return: The process_hash of this AddAppWhitelistPolicyProcessInfo.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        r"""Sets the process_hash of this AddAppWhitelistPolicyProcessInfo.

        进程hash

        :param process_hash: The process_hash of this AddAppWhitelistPolicyProcessInfo.
        :type process_hash: str
        """
        self._process_hash = process_hash

    @property
    def container_id(self):
        r"""Gets the container_id of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :return: The container_id of this AddAppWhitelistPolicyProcessInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :param container_id: The container_id of this AddAppWhitelistPolicyProcessInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def cmdline(self):
        r"""Gets the cmdline of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :return: The cmdline of this AddAppWhitelistPolicyProcessInfo.
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        r"""Sets the cmdline of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :param cmdline: The cmdline of this AddAppWhitelistPolicyProcessInfo.
        :type cmdline: str
        """
        self._cmdline = cmdline

    @property
    def file_size(self):
        r"""Gets the file_size of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The file_size of this AddAppWhitelistPolicyProcessInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AddAppWhitelistPolicyProcessInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param file_size: The file_size of this AddAppWhitelistPolicyProcessInfo.
        :type file_size: int
        """
        self._file_size = file_size

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
        if not isinstance(other, AddAppWhitelistPolicyProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
