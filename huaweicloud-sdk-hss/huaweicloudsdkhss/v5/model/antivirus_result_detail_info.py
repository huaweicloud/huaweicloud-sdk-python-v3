# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntivirusResultDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_id': 'str',
        'malware_name': 'str',
        'file_path': 'str',
        'file_hash': 'str',
        'file_size': 'int',
        'file_owner': 'str',
        'file_attr': 'str',
        'file_ctime': 'int',
        'file_mtime': 'int',
        'update_time': 'int',
        'agent_id': 'str'
    }

    attribute_map = {
        'result_id': 'result_id',
        'malware_name': 'malware_name',
        'file_path': 'file_path',
        'file_hash': 'file_hash',
        'file_size': 'file_size',
        'file_owner': 'file_owner',
        'file_attr': 'file_attr',
        'file_ctime': 'file_ctime',
        'file_mtime': 'file_mtime',
        'update_time': 'update_time',
        'agent_id': 'agent_id'
    }

    def __init__(self, result_id=None, malware_name=None, file_path=None, file_hash=None, file_size=None, file_owner=None, file_attr=None, file_ctime=None, file_mtime=None, update_time=None, agent_id=None):
        r"""AntivirusResultDetailInfo

        The model defined in huaweicloud sdk

        :param result_id: **参数解释**： 病毒查杀结果ID **取值范围**： 字符长度1-64位 
        :type result_id: str
        :param malware_name: **参数解释**： 病毒名称 **取值范围**： 字符长度1-128位 
        :type malware_name: str
        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_hash: **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_size: **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type file_size: int
        :param file_owner: **参数解释**： 文件属性 **取值范围**： 字符长度0-64位 
        :type file_owner: str
        :param file_attr: **参数解释**： 文件的系统属性（如读写权限、隐藏属性、执行权限等） **取值范围**： 字符长度1-256位 
        :type file_attr: str
        :param file_ctime: **参数解释**： 文件创建时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 
        :type file_ctime: int
        :param file_mtime: **参数解释**： 文件更新时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 
        :type file_mtime: int
        :param update_time: 更新时间，毫秒
        :type update_time: int
        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        """
        
        

        self._result_id = None
        self._malware_name = None
        self._file_path = None
        self._file_hash = None
        self._file_size = None
        self._file_owner = None
        self._file_attr = None
        self._file_ctime = None
        self._file_mtime = None
        self._update_time = None
        self._agent_id = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if malware_name is not None:
            self.malware_name = malware_name
        if file_path is not None:
            self.file_path = file_path
        if file_hash is not None:
            self.file_hash = file_hash
        if file_size is not None:
            self.file_size = file_size
        if file_owner is not None:
            self.file_owner = file_owner
        if file_attr is not None:
            self.file_attr = file_attr
        if file_ctime is not None:
            self.file_ctime = file_ctime
        if file_mtime is not None:
            self.file_mtime = file_mtime
        if update_time is not None:
            self.update_time = update_time
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def result_id(self):
        r"""Gets the result_id of this AntivirusResultDetailInfo.

        **参数解释**： 病毒查杀结果ID **取值范围**： 字符长度1-64位 

        :return: The result_id of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this AntivirusResultDetailInfo.

        **参数解释**： 病毒查杀结果ID **取值范围**： 字符长度1-64位 

        :param result_id: The result_id of this AntivirusResultDetailInfo.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def malware_name(self):
        r"""Gets the malware_name of this AntivirusResultDetailInfo.

        **参数解释**： 病毒名称 **取值范围**： 字符长度1-128位 

        :return: The malware_name of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        r"""Sets the malware_name of this AntivirusResultDetailInfo.

        **参数解释**： 病毒名称 **取值范围**： 字符长度1-128位 

        :param malware_name: The malware_name of this AntivirusResultDetailInfo.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def file_path(self):
        r"""Gets the file_path of this AntivirusResultDetailInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this AntivirusResultDetailInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this AntivirusResultDetailInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_hash(self):
        r"""Gets the file_hash of this AntivirusResultDetailInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this AntivirusResultDetailInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this AntivirusResultDetailInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_size(self):
        r"""Gets the file_size of this AntivirusResultDetailInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The file_size of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AntivirusResultDetailInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param file_size: The file_size of this AntivirusResultDetailInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_owner(self):
        r"""Gets the file_owner of this AntivirusResultDetailInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度0-64位 

        :return: The file_owner of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_owner

    @file_owner.setter
    def file_owner(self, file_owner):
        r"""Sets the file_owner of this AntivirusResultDetailInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度0-64位 

        :param file_owner: The file_owner of this AntivirusResultDetailInfo.
        :type file_owner: str
        """
        self._file_owner = file_owner

    @property
    def file_attr(self):
        r"""Gets the file_attr of this AntivirusResultDetailInfo.

        **参数解释**： 文件的系统属性（如读写权限、隐藏属性、执行权限等） **取值范围**： 字符长度1-256位 

        :return: The file_attr of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this AntivirusResultDetailInfo.

        **参数解释**： 文件的系统属性（如读写权限、隐藏属性、执行权限等） **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this AntivirusResultDetailInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def file_ctime(self):
        r"""Gets the file_ctime of this AntivirusResultDetailInfo.

        **参数解释**： 文件创建时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 

        :return: The file_ctime of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_ctime

    @file_ctime.setter
    def file_ctime(self, file_ctime):
        r"""Sets the file_ctime of this AntivirusResultDetailInfo.

        **参数解释**： 文件创建时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 

        :param file_ctime: The file_ctime of this AntivirusResultDetailInfo.
        :type file_ctime: int
        """
        self._file_ctime = file_ctime

    @property
    def file_mtime(self):
        r"""Gets the file_mtime of this AntivirusResultDetailInfo.

        **参数解释**： 文件更新时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 

        :return: The file_mtime of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_mtime

    @file_mtime.setter
    def file_mtime(self, file_mtime):
        r"""Sets the file_mtime of this AntivirusResultDetailInfo.

        **参数解释**： 文件更新时间 **取值范围**： 非负长整数，时间格式：毫秒级时间戳（UTC时区，从1970-01-01 00:00:00开始计算），单位：ms 

        :param file_mtime: The file_mtime of this AntivirusResultDetailInfo.
        :type file_mtime: int
        """
        self._file_mtime = file_mtime

    @property
    def update_time(self):
        r"""Gets the update_time of this AntivirusResultDetailInfo.

        更新时间，毫秒

        :return: The update_time of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AntivirusResultDetailInfo.

        更新时间，毫秒

        :param update_time: The update_time of this AntivirusResultDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AntivirusResultDetailInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AntivirusResultDetailInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AntivirusResultDetailInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

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
        if not isinstance(other, AntivirusResultDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
