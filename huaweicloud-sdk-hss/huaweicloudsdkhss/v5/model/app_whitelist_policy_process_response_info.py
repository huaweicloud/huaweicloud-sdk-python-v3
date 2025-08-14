# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistPolicyProcessResponseInfo:

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
        'handle_status': 'str',
        'specified_path': 'str',
        'cmdline': 'str',
        'file_size': 'int',
        'file_signer': 'str',
        'process_type': 'int',
        'os_type': 'str',
        'app_type': 'str',
        'whitelist_count': 'int',
        'blacklist_count': 'int',
        'trust_status_source': 'int',
        'process_status': 'str'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_hash': 'process_hash',
        'handle_status': 'handle_status',
        'specified_path': 'specified_path',
        'cmdline': 'cmdline',
        'file_size': 'file_size',
        'file_signer': 'file_signer',
        'process_type': 'process_type',
        'os_type': 'os_type',
        'app_type': 'app_type',
        'whitelist_count': 'whitelist_count',
        'blacklist_count': 'blacklist_count',
        'trust_status_source': 'trust_status_source',
        'process_status': 'process_status'
    }

    def __init__(self, process_name=None, process_path=None, process_hash=None, handle_status=None, specified_path=None, cmdline=None, file_size=None, file_signer=None, process_type=None, os_type=None, app_type=None, whitelist_count=None, blacklist_count=None, trust_status_source=None, process_status=None):
        r"""AppWhitelistPolicyProcessResponseInfo

        The model defined in huaweicloud sdk

        :param process_name: **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 
        :type process_name: str
        :param process_path: **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 
        :type process_path: str
        :param process_hash: 进程hash
        :type process_hash: str
        :param handle_status: **参数解释**： 处理方式 **取值范围**: - confirmed：已确认 - unconfirmed：未确认 
        :type handle_status: str
        :param specified_path: **参数解释**： 指定目录 **取值范围**： 字符长度1-512位 
        :type specified_path: str
        :param cmdline: **参数解释**： 进程命令行 **约束限制**： 不涉及 
        :type cmdline: str
        :param file_size: **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type file_size: int
        :param file_signer: **参数解释**： 文件签名 **取值范围**： 字符长度1-128位 
        :type file_signer: str
        :param process_type: **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - 1：系统程序 - 2：解释类程序 - 3：普通可执行程序 
        :type process_type: int
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param app_type: **参数解释**： 应用类型 **约束限制**： 不涉及 
        :type app_type: str
        :param whitelist_count: **参数解释**: 白名单确认次数 **约束限制**: 不涉及 
        :type whitelist_count: int
        :param blacklist_count: **参数解释**: 黑名单确认次数 **约束限制**: 不涉及 
        :type blacklist_count: int
        :param trust_status_source: **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - 0：情报 - 1：恶意软件 - 2：人工确认 - 3：自学习  **默认取值**: 不涉及 
        :type trust_status_source: int
        :param process_status: **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 
        :type process_status: str
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_hash = None
        self._handle_status = None
        self._specified_path = None
        self._cmdline = None
        self._file_size = None
        self._file_signer = None
        self._process_type = None
        self._os_type = None
        self._app_type = None
        self._whitelist_count = None
        self._blacklist_count = None
        self._trust_status_source = None
        self._process_status = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_hash is not None:
            self.process_hash = process_hash
        if handle_status is not None:
            self.handle_status = handle_status
        if specified_path is not None:
            self.specified_path = specified_path
        if cmdline is not None:
            self.cmdline = cmdline
        if file_size is not None:
            self.file_size = file_size
        if file_signer is not None:
            self.file_signer = file_signer
        if process_type is not None:
            self.process_type = process_type
        if os_type is not None:
            self.os_type = os_type
        if app_type is not None:
            self.app_type = app_type
        if whitelist_count is not None:
            self.whitelist_count = whitelist_count
        if blacklist_count is not None:
            self.blacklist_count = blacklist_count
        if trust_status_source is not None:
            self.trust_status_source = trust_status_source
        if process_status is not None:
            self.process_status = process_status

    @property
    def process_name(self):
        r"""Gets the process_name of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :return: The process_name of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :param process_name: The process_name of this AppWhitelistPolicyProcessResponseInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        r"""Gets the process_path of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :return: The process_path of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :param process_path: The process_path of this AppWhitelistPolicyProcessResponseInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_hash(self):
        r"""Gets the process_hash of this AppWhitelistPolicyProcessResponseInfo.

        进程hash

        :return: The process_hash of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        r"""Sets the process_hash of this AppWhitelistPolicyProcessResponseInfo.

        进程hash

        :param process_hash: The process_hash of this AppWhitelistPolicyProcessResponseInfo.
        :type process_hash: str
        """
        self._process_hash = process_hash

    @property
    def handle_status(self):
        r"""Gets the handle_status of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 处理方式 **取值范围**: - confirmed：已确认 - unconfirmed：未确认 

        :return: The handle_status of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 处理方式 **取值范围**: - confirmed：已确认 - unconfirmed：未确认 

        :param handle_status: The handle_status of this AppWhitelistPolicyProcessResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def specified_path(self):
        r"""Gets the specified_path of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 指定目录 **取值范围**： 字符长度1-512位 

        :return: The specified_path of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._specified_path

    @specified_path.setter
    def specified_path(self, specified_path):
        r"""Sets the specified_path of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 指定目录 **取值范围**： 字符长度1-512位 

        :param specified_path: The specified_path of this AppWhitelistPolicyProcessResponseInfo.
        :type specified_path: str
        """
        self._specified_path = specified_path

    @property
    def cmdline(self):
        r"""Gets the cmdline of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :return: The cmdline of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        r"""Sets the cmdline of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :param cmdline: The cmdline of this AppWhitelistPolicyProcessResponseInfo.
        :type cmdline: str
        """
        self._cmdline = cmdline

    @property
    def file_size(self):
        r"""Gets the file_size of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The file_size of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param file_size: The file_size of this AppWhitelistPolicyProcessResponseInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_signer(self):
        r"""Gets the file_signer of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 文件签名 **取值范围**： 字符长度1-128位 

        :return: The file_signer of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._file_signer

    @file_signer.setter
    def file_signer(self, file_signer):
        r"""Sets the file_signer of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 文件签名 **取值范围**： 字符长度1-128位 

        :param file_signer: The file_signer of this AppWhitelistPolicyProcessResponseInfo.
        :type file_signer: str
        """
        self._file_signer = file_signer

    @property
    def process_type(self):
        r"""Gets the process_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - 1：系统程序 - 2：解释类程序 - 3：普通可执行程序 

        :return: The process_type of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: int
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        r"""Sets the process_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程类型 **约束限制**: 不涉及 **取值范围**: - 1：系统程序 - 2：解释类程序 - 3：普通可执行程序 

        :param process_type: The process_type of this AppWhitelistPolicyProcessResponseInfo.
        :type process_type: int
        """
        self._process_type = process_type

    @property
    def os_type(self):
        r"""Gets the os_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this AppWhitelistPolicyProcessResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def app_type(self):
        r"""Gets the app_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 应用类型 **约束限制**： 不涉及 

        :return: The app_type of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 应用类型 **约束限制**： 不涉及 

        :param app_type: The app_type of this AppWhitelistPolicyProcessResponseInfo.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def whitelist_count(self):
        r"""Gets the whitelist_count of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 白名单确认次数 **约束限制**: 不涉及 

        :return: The whitelist_count of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: int
        """
        return self._whitelist_count

    @whitelist_count.setter
    def whitelist_count(self, whitelist_count):
        r"""Sets the whitelist_count of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 白名单确认次数 **约束限制**: 不涉及 

        :param whitelist_count: The whitelist_count of this AppWhitelistPolicyProcessResponseInfo.
        :type whitelist_count: int
        """
        self._whitelist_count = whitelist_count

    @property
    def blacklist_count(self):
        r"""Gets the blacklist_count of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 黑名单确认次数 **约束限制**: 不涉及 

        :return: The blacklist_count of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: int
        """
        return self._blacklist_count

    @blacklist_count.setter
    def blacklist_count(self, blacklist_count):
        r"""Sets the blacklist_count of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**: 黑名单确认次数 **约束限制**: 不涉及 

        :param blacklist_count: The blacklist_count of this AppWhitelistPolicyProcessResponseInfo.
        :type blacklist_count: int
        """
        self._blacklist_count = blacklist_count

    @property
    def trust_status_source(self):
        r"""Gets the trust_status_source of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - 0：情报 - 1：恶意软件 - 2：人工确认 - 3：自学习  **默认取值**: 不涉及 

        :return: The trust_status_source of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: int
        """
        return self._trust_status_source

    @trust_status_source.setter
    def trust_status_source(self, trust_status_source):
        r"""Sets the trust_status_source of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - 0：情报 - 1：恶意软件 - 2：人工确认 - 3：自学习  **默认取值**: 不涉及 

        :param trust_status_source: The trust_status_source of this AppWhitelistPolicyProcessResponseInfo.
        :type trust_status_source: int
        """
        self._trust_status_source = trust_status_source

    @property
    def process_status(self):
        r"""Gets the process_status of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 

        :return: The process_status of this AppWhitelistPolicyProcessResponseInfo.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this AppWhitelistPolicyProcessResponseInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 

        :param process_status: The process_status of this AppWhitelistPolicyProcessResponseInfo.
        :type process_status: str
        """
        self._process_status = process_status

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
        if not isinstance(other, AppWhitelistPolicyProcessResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
