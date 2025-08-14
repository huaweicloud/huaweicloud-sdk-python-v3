# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventFileResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'file_alias': 'str',
        'file_size': 'int',
        'file_mtime': 'int',
        'file_atime': 'int',
        'file_ctime': 'int',
        'file_hash': 'str',
        'file_md5': 'str',
        'file_sha256': 'str',
        'file_type': 'str',
        'file_content': 'str',
        'file_attr': 'str',
        'file_operation': 'int',
        'file_action': 'str',
        'file_change_attr': 'str',
        'file_new_path': 'str',
        'file_desc': 'str',
        'file_key_word': 'str',
        'is_dir': 'bool',
        'fd_info': 'str',
        'fd_count': 'int'
    }

    attribute_map = {
        'file_path': 'file_path',
        'file_alias': 'file_alias',
        'file_size': 'file_size',
        'file_mtime': 'file_mtime',
        'file_atime': 'file_atime',
        'file_ctime': 'file_ctime',
        'file_hash': 'file_hash',
        'file_md5': 'file_md5',
        'file_sha256': 'file_sha256',
        'file_type': 'file_type',
        'file_content': 'file_content',
        'file_attr': 'file_attr',
        'file_operation': 'file_operation',
        'file_action': 'file_action',
        'file_change_attr': 'file_change_attr',
        'file_new_path': 'file_new_path',
        'file_desc': 'file_desc',
        'file_key_word': 'file_key_word',
        'is_dir': 'is_dir',
        'fd_info': 'fd_info',
        'fd_count': 'fd_count'
    }

    def __init__(self, file_path=None, file_alias=None, file_size=None, file_mtime=None, file_atime=None, file_ctime=None, file_hash=None, file_md5=None, file_sha256=None, file_type=None, file_content=None, file_attr=None, file_operation=None, file_action=None, file_change_attr=None, file_new_path=None, file_desc=None, file_key_word=None, is_dir=None, fd_info=None, fd_count=None):
        r"""EventFileResponseInfo

        The model defined in huaweicloud sdk

        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_alias: **参数解释**： 文件别名 **取值范围**： 字符长度1-256位 
        :type file_alias: str
        :param file_size: **参数解释**： 文件大小 **取值范围**： 最小值0，最大值2147483647 
        :type file_size: int
        :param file_mtime: **参数解释**： 文件最后一次修改时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type file_mtime: int
        :param file_atime: **参数解释**： 文件最后一次访问时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type file_atime: int
        :param file_ctime: **参数解释**： 文件最后一次状态改变时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type file_ctime: int
        :param file_hash: **参数解释**： 文件hash,当前为sha256 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_md5: **参数解释**： 文件md5 **取值范围**： 字符长度1-256位 
        :type file_md5: str
        :param file_sha256: **参数解释**： 文件sha256 **取值范围**： 字符长度1-256位 
        :type file_sha256: str
        :param file_type: **参数解释**： 文件类型 **取值范围**： 字符长度1-256位 
        :type file_type: str
        :param file_content: **参数解释**： 文件内容 **取值范围**： 字符长度1-256位 
        :type file_content: str
        :param file_attr: **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 
        :type file_attr: str
        :param file_operation: **参数解释**： 文件操作类型 **取值范围**： 最小值0，最大值2147483647 
        :type file_operation: int
        :param file_action: **参数解释**： 文件动作 **取值范围**： 字符长度1-256位 
        :type file_action: str
        :param file_change_attr: **参数解释**： 变更前后的属性 **取值范围**： 字符长度1-256位 
        :type file_change_attr: str
        :param file_new_path: **参数解释**： 新文件路径 **取值范围**： 字符长度1-256位 
        :type file_new_path: str
        :param file_desc: **参数解释**： 文件描述 **取值范围**： 字符长度1-256位 
        :type file_desc: str
        :param file_key_word: **参数解释**： 文件关键字 **取值范围**： 字符长度1-256位 
        :type file_key_word: str
        :param is_dir: **参数解释**： 是否目录 **取值范围**： - true：是目录 - false：不是目录 
        :type is_dir: bool
        :param fd_info: **参数解释**： 文件句柄信息 **取值范围**： 字符长度1-256位 
        :type fd_info: str
        :param fd_count: **参数解释**： 文件句柄数量 **取值范围**： 最小值0，最大值2147483647 
        :type fd_count: int
        """
        
        

        self._file_path = None
        self._file_alias = None
        self._file_size = None
        self._file_mtime = None
        self._file_atime = None
        self._file_ctime = None
        self._file_hash = None
        self._file_md5 = None
        self._file_sha256 = None
        self._file_type = None
        self._file_content = None
        self._file_attr = None
        self._file_operation = None
        self._file_action = None
        self._file_change_attr = None
        self._file_new_path = None
        self._file_desc = None
        self._file_key_word = None
        self._is_dir = None
        self._fd_info = None
        self._fd_count = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if file_alias is not None:
            self.file_alias = file_alias
        if file_size is not None:
            self.file_size = file_size
        if file_mtime is not None:
            self.file_mtime = file_mtime
        if file_atime is not None:
            self.file_atime = file_atime
        if file_ctime is not None:
            self.file_ctime = file_ctime
        if file_hash is not None:
            self.file_hash = file_hash
        if file_md5 is not None:
            self.file_md5 = file_md5
        if file_sha256 is not None:
            self.file_sha256 = file_sha256
        if file_type is not None:
            self.file_type = file_type
        if file_content is not None:
            self.file_content = file_content
        if file_attr is not None:
            self.file_attr = file_attr
        if file_operation is not None:
            self.file_operation = file_operation
        if file_action is not None:
            self.file_action = file_action
        if file_change_attr is not None:
            self.file_change_attr = file_change_attr
        if file_new_path is not None:
            self.file_new_path = file_new_path
        if file_desc is not None:
            self.file_desc = file_desc
        if file_key_word is not None:
            self.file_key_word = file_key_word
        if is_dir is not None:
            self.is_dir = is_dir
        if fd_info is not None:
            self.fd_info = fd_info
        if fd_count is not None:
            self.fd_count = fd_count

    @property
    def file_path(self):
        r"""Gets the file_path of this EventFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this EventFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this EventFileResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_alias(self):
        r"""Gets the file_alias of this EventFileResponseInfo.

        **参数解释**： 文件别名 **取值范围**： 字符长度1-256位 

        :return: The file_alias of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_alias

    @file_alias.setter
    def file_alias(self, file_alias):
        r"""Sets the file_alias of this EventFileResponseInfo.

        **参数解释**： 文件别名 **取值范围**： 字符长度1-256位 

        :param file_alias: The file_alias of this EventFileResponseInfo.
        :type file_alias: str
        """
        self._file_alias = file_alias

    @property
    def file_size(self):
        r"""Gets the file_size of this EventFileResponseInfo.

        **参数解释**： 文件大小 **取值范围**： 最小值0，最大值2147483647 

        :return: The file_size of this EventFileResponseInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this EventFileResponseInfo.

        **参数解释**： 文件大小 **取值范围**： 最小值0，最大值2147483647 

        :param file_size: The file_size of this EventFileResponseInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_mtime(self):
        r"""Gets the file_mtime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次修改时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The file_mtime of this EventFileResponseInfo.
        :rtype: int
        """
        return self._file_mtime

    @file_mtime.setter
    def file_mtime(self, file_mtime):
        r"""Sets the file_mtime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次修改时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param file_mtime: The file_mtime of this EventFileResponseInfo.
        :type file_mtime: int
        """
        self._file_mtime = file_mtime

    @property
    def file_atime(self):
        r"""Gets the file_atime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次访问时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The file_atime of this EventFileResponseInfo.
        :rtype: int
        """
        return self._file_atime

    @file_atime.setter
    def file_atime(self, file_atime):
        r"""Sets the file_atime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次访问时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param file_atime: The file_atime of this EventFileResponseInfo.
        :type file_atime: int
        """
        self._file_atime = file_atime

    @property
    def file_ctime(self):
        r"""Gets the file_ctime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次状态改变时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The file_ctime of this EventFileResponseInfo.
        :rtype: int
        """
        return self._file_ctime

    @file_ctime.setter
    def file_ctime(self, file_ctime):
        r"""Sets the file_ctime of this EventFileResponseInfo.

        **参数解释**： 文件最后一次状态改变时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param file_ctime: The file_ctime of this EventFileResponseInfo.
        :type file_ctime: int
        """
        self._file_ctime = file_ctime

    @property
    def file_hash(self):
        r"""Gets the file_hash of this EventFileResponseInfo.

        **参数解释**： 文件hash,当前为sha256 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this EventFileResponseInfo.

        **参数解释**： 文件hash,当前为sha256 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this EventFileResponseInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_md5(self):
        r"""Gets the file_md5 of this EventFileResponseInfo.

        **参数解释**： 文件md5 **取值范围**： 字符长度1-256位 

        :return: The file_md5 of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        r"""Sets the file_md5 of this EventFileResponseInfo.

        **参数解释**： 文件md5 **取值范围**： 字符长度1-256位 

        :param file_md5: The file_md5 of this EventFileResponseInfo.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_sha256(self):
        r"""Gets the file_sha256 of this EventFileResponseInfo.

        **参数解释**： 文件sha256 **取值范围**： 字符长度1-256位 

        :return: The file_sha256 of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_sha256

    @file_sha256.setter
    def file_sha256(self, file_sha256):
        r"""Sets the file_sha256 of this EventFileResponseInfo.

        **参数解释**： 文件sha256 **取值范围**： 字符长度1-256位 

        :param file_sha256: The file_sha256 of this EventFileResponseInfo.
        :type file_sha256: str
        """
        self._file_sha256 = file_sha256

    @property
    def file_type(self):
        r"""Gets the file_type of this EventFileResponseInfo.

        **参数解释**： 文件类型 **取值范围**： 字符长度1-256位 

        :return: The file_type of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this EventFileResponseInfo.

        **参数解释**： 文件类型 **取值范围**： 字符长度1-256位 

        :param file_type: The file_type of this EventFileResponseInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_content(self):
        r"""Gets the file_content of this EventFileResponseInfo.

        **参数解释**： 文件内容 **取值范围**： 字符长度1-256位 

        :return: The file_content of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        r"""Sets the file_content of this EventFileResponseInfo.

        **参数解释**： 文件内容 **取值范围**： 字符长度1-256位 

        :param file_content: The file_content of this EventFileResponseInfo.
        :type file_content: str
        """
        self._file_content = file_content

    @property
    def file_attr(self):
        r"""Gets the file_attr of this EventFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :return: The file_attr of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this EventFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this EventFileResponseInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def file_operation(self):
        r"""Gets the file_operation of this EventFileResponseInfo.

        **参数解释**： 文件操作类型 **取值范围**： 最小值0，最大值2147483647 

        :return: The file_operation of this EventFileResponseInfo.
        :rtype: int
        """
        return self._file_operation

    @file_operation.setter
    def file_operation(self, file_operation):
        r"""Sets the file_operation of this EventFileResponseInfo.

        **参数解释**： 文件操作类型 **取值范围**： 最小值0，最大值2147483647 

        :param file_operation: The file_operation of this EventFileResponseInfo.
        :type file_operation: int
        """
        self._file_operation = file_operation

    @property
    def file_action(self):
        r"""Gets the file_action of this EventFileResponseInfo.

        **参数解释**： 文件动作 **取值范围**： 字符长度1-256位 

        :return: The file_action of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_action

    @file_action.setter
    def file_action(self, file_action):
        r"""Sets the file_action of this EventFileResponseInfo.

        **参数解释**： 文件动作 **取值范围**： 字符长度1-256位 

        :param file_action: The file_action of this EventFileResponseInfo.
        :type file_action: str
        """
        self._file_action = file_action

    @property
    def file_change_attr(self):
        r"""Gets the file_change_attr of this EventFileResponseInfo.

        **参数解释**： 变更前后的属性 **取值范围**： 字符长度1-256位 

        :return: The file_change_attr of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_change_attr

    @file_change_attr.setter
    def file_change_attr(self, file_change_attr):
        r"""Sets the file_change_attr of this EventFileResponseInfo.

        **参数解释**： 变更前后的属性 **取值范围**： 字符长度1-256位 

        :param file_change_attr: The file_change_attr of this EventFileResponseInfo.
        :type file_change_attr: str
        """
        self._file_change_attr = file_change_attr

    @property
    def file_new_path(self):
        r"""Gets the file_new_path of this EventFileResponseInfo.

        **参数解释**： 新文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_new_path of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_new_path

    @file_new_path.setter
    def file_new_path(self, file_new_path):
        r"""Sets the file_new_path of this EventFileResponseInfo.

        **参数解释**： 新文件路径 **取值范围**： 字符长度1-256位 

        :param file_new_path: The file_new_path of this EventFileResponseInfo.
        :type file_new_path: str
        """
        self._file_new_path = file_new_path

    @property
    def file_desc(self):
        r"""Gets the file_desc of this EventFileResponseInfo.

        **参数解释**： 文件描述 **取值范围**： 字符长度1-256位 

        :return: The file_desc of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_desc

    @file_desc.setter
    def file_desc(self, file_desc):
        r"""Sets the file_desc of this EventFileResponseInfo.

        **参数解释**： 文件描述 **取值范围**： 字符长度1-256位 

        :param file_desc: The file_desc of this EventFileResponseInfo.
        :type file_desc: str
        """
        self._file_desc = file_desc

    @property
    def file_key_word(self):
        r"""Gets the file_key_word of this EventFileResponseInfo.

        **参数解释**： 文件关键字 **取值范围**： 字符长度1-256位 

        :return: The file_key_word of this EventFileResponseInfo.
        :rtype: str
        """
        return self._file_key_word

    @file_key_word.setter
    def file_key_word(self, file_key_word):
        r"""Sets the file_key_word of this EventFileResponseInfo.

        **参数解释**： 文件关键字 **取值范围**： 字符长度1-256位 

        :param file_key_word: The file_key_word of this EventFileResponseInfo.
        :type file_key_word: str
        """
        self._file_key_word = file_key_word

    @property
    def is_dir(self):
        r"""Gets the is_dir of this EventFileResponseInfo.

        **参数解释**： 是否目录 **取值范围**： - true：是目录 - false：不是目录 

        :return: The is_dir of this EventFileResponseInfo.
        :rtype: bool
        """
        return self._is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        r"""Sets the is_dir of this EventFileResponseInfo.

        **参数解释**： 是否目录 **取值范围**： - true：是目录 - false：不是目录 

        :param is_dir: The is_dir of this EventFileResponseInfo.
        :type is_dir: bool
        """
        self._is_dir = is_dir

    @property
    def fd_info(self):
        r"""Gets the fd_info of this EventFileResponseInfo.

        **参数解释**： 文件句柄信息 **取值范围**： 字符长度1-256位 

        :return: The fd_info of this EventFileResponseInfo.
        :rtype: str
        """
        return self._fd_info

    @fd_info.setter
    def fd_info(self, fd_info):
        r"""Sets the fd_info of this EventFileResponseInfo.

        **参数解释**： 文件句柄信息 **取值范围**： 字符长度1-256位 

        :param fd_info: The fd_info of this EventFileResponseInfo.
        :type fd_info: str
        """
        self._fd_info = fd_info

    @property
    def fd_count(self):
        r"""Gets the fd_count of this EventFileResponseInfo.

        **参数解释**： 文件句柄数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The fd_count of this EventFileResponseInfo.
        :rtype: int
        """
        return self._fd_count

    @fd_count.setter
    def fd_count(self, fd_count):
        r"""Sets the fd_count of this EventFileResponseInfo.

        **参数解释**： 文件句柄数量 **取值范围**： 最小值0，最大值2147483647 

        :param fd_count: The fd_count of this EventFileResponseInfo.
        :type fd_count: int
        """
        self._fd_count = fd_count

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
        if not isinstance(other, EventFileResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
