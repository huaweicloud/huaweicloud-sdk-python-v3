# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultFileResponseInfo:

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
        'file_hash': 'str',
        'file_size': 'int',
        'file_owner': 'str',
        'file_attr': 'str',
        'file_ctime': 'int',
        'file_mtime': 'int'
    }

    attribute_map = {
        'file_path': 'file_path',
        'file_hash': 'file_hash',
        'file_size': 'file_size',
        'file_owner': 'file_owner',
        'file_attr': 'file_attr',
        'file_ctime': 'file_ctime',
        'file_mtime': 'file_mtime'
    }

    def __init__(self, file_path=None, file_hash=None, file_size=None, file_owner=None, file_attr=None, file_ctime=None, file_mtime=None):
        r"""ResultFileResponseInfo

        The model defined in huaweicloud sdk

        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_hash: **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_size: **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type file_size: int
        :param file_owner: 文件属主
        :type file_owner: str
        :param file_attr: **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 
        :type file_attr: str
        :param file_ctime: 文件创建时间
        :type file_ctime: int
        :param file_mtime: 文件更新时间
        :type file_mtime: int
        """
        
        

        self._file_path = None
        self._file_hash = None
        self._file_size = None
        self._file_owner = None
        self._file_attr = None
        self._file_ctime = None
        self._file_mtime = None
        self.discriminator = None

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

    @property
    def file_path(self):
        r"""Gets the file_path of this ResultFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this ResultFileResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ResultFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this ResultFileResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_hash(self):
        r"""Gets the file_hash of this ResultFileResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this ResultFileResponseInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this ResultFileResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this ResultFileResponseInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_size(self):
        r"""Gets the file_size of this ResultFileResponseInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The file_size of this ResultFileResponseInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this ResultFileResponseInfo.

        **参数解释**: 文件大小 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param file_size: The file_size of this ResultFileResponseInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_owner(self):
        r"""Gets the file_owner of this ResultFileResponseInfo.

        文件属主

        :return: The file_owner of this ResultFileResponseInfo.
        :rtype: str
        """
        return self._file_owner

    @file_owner.setter
    def file_owner(self, file_owner):
        r"""Sets the file_owner of this ResultFileResponseInfo.

        文件属主

        :param file_owner: The file_owner of this ResultFileResponseInfo.
        :type file_owner: str
        """
        self._file_owner = file_owner

    @property
    def file_attr(self):
        r"""Gets the file_attr of this ResultFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :return: The file_attr of this ResultFileResponseInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this ResultFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this ResultFileResponseInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def file_ctime(self):
        r"""Gets the file_ctime of this ResultFileResponseInfo.

        文件创建时间

        :return: The file_ctime of this ResultFileResponseInfo.
        :rtype: int
        """
        return self._file_ctime

    @file_ctime.setter
    def file_ctime(self, file_ctime):
        r"""Sets the file_ctime of this ResultFileResponseInfo.

        文件创建时间

        :param file_ctime: The file_ctime of this ResultFileResponseInfo.
        :type file_ctime: int
        """
        self._file_ctime = file_ctime

    @property
    def file_mtime(self):
        r"""Gets the file_mtime of this ResultFileResponseInfo.

        文件更新时间

        :return: The file_mtime of this ResultFileResponseInfo.
        :rtype: int
        """
        return self._file_mtime

    @file_mtime.setter
    def file_mtime(self, file_mtime):
        r"""Sets the file_mtime of this ResultFileResponseInfo.

        文件更新时间

        :param file_mtime: The file_mtime of this ResultFileResponseInfo.
        :type file_mtime: int
        """
        self._file_mtime = file_mtime

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
        if not isinstance(other, ResultFileResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
