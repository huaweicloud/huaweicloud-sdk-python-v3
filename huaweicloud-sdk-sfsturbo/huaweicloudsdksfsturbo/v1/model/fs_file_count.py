# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FsFileCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dir': 'int',
        'regular': 'int',
        'pipe': 'int',
        'char': 'int',
        'block': 'int',
        'socket': 'int',
        'symlink': 'int'
    }

    attribute_map = {
        'dir': 'dir',
        'regular': 'regular',
        'pipe': 'pipe',
        'char': 'char',
        'block': 'block',
        'socket': 'socket',
        'symlink': 'symlink'
    }

    def __init__(self, dir=None, regular=None, pipe=None, char=None, block=None, socket=None, symlink=None):
        r"""FsFileCount

        The model defined in huaweicloud sdk

        :param dir: 目录数目
        :type dir: int
        :param regular: 普通文件数目
        :type regular: int
        :param pipe: 管道文件数目
        :type pipe: int
        :param char: 字符设备数目
        :type char: int
        :param block: 块设备数目
        :type block: int
        :param socket: 套接字数目
        :type socket: int
        :param symlink: 符号链接数目
        :type symlink: int
        """
        
        

        self._dir = None
        self._regular = None
        self._pipe = None
        self._char = None
        self._block = None
        self._socket = None
        self._symlink = None
        self.discriminator = None

        if dir is not None:
            self.dir = dir
        if regular is not None:
            self.regular = regular
        if pipe is not None:
            self.pipe = pipe
        if char is not None:
            self.char = char
        if block is not None:
            self.block = block
        if socket is not None:
            self.socket = socket
        if symlink is not None:
            self.symlink = symlink

    @property
    def dir(self):
        r"""Gets the dir of this FsFileCount.

        目录数目

        :return: The dir of this FsFileCount.
        :rtype: int
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        r"""Sets the dir of this FsFileCount.

        目录数目

        :param dir: The dir of this FsFileCount.
        :type dir: int
        """
        self._dir = dir

    @property
    def regular(self):
        r"""Gets the regular of this FsFileCount.

        普通文件数目

        :return: The regular of this FsFileCount.
        :rtype: int
        """
        return self._regular

    @regular.setter
    def regular(self, regular):
        r"""Sets the regular of this FsFileCount.

        普通文件数目

        :param regular: The regular of this FsFileCount.
        :type regular: int
        """
        self._regular = regular

    @property
    def pipe(self):
        r"""Gets the pipe of this FsFileCount.

        管道文件数目

        :return: The pipe of this FsFileCount.
        :rtype: int
        """
        return self._pipe

    @pipe.setter
    def pipe(self, pipe):
        r"""Sets the pipe of this FsFileCount.

        管道文件数目

        :param pipe: The pipe of this FsFileCount.
        :type pipe: int
        """
        self._pipe = pipe

    @property
    def char(self):
        r"""Gets the char of this FsFileCount.

        字符设备数目

        :return: The char of this FsFileCount.
        :rtype: int
        """
        return self._char

    @char.setter
    def char(self, char):
        r"""Sets the char of this FsFileCount.

        字符设备数目

        :param char: The char of this FsFileCount.
        :type char: int
        """
        self._char = char

    @property
    def block(self):
        r"""Gets the block of this FsFileCount.

        块设备数目

        :return: The block of this FsFileCount.
        :rtype: int
        """
        return self._block

    @block.setter
    def block(self, block):
        r"""Sets the block of this FsFileCount.

        块设备数目

        :param block: The block of this FsFileCount.
        :type block: int
        """
        self._block = block

    @property
    def socket(self):
        r"""Gets the socket of this FsFileCount.

        套接字数目

        :return: The socket of this FsFileCount.
        :rtype: int
        """
        return self._socket

    @socket.setter
    def socket(self, socket):
        r"""Sets the socket of this FsFileCount.

        套接字数目

        :param socket: The socket of this FsFileCount.
        :type socket: int
        """
        self._socket = socket

    @property
    def symlink(self):
        r"""Gets the symlink of this FsFileCount.

        符号链接数目

        :return: The symlink of this FsFileCount.
        :rtype: int
        """
        return self._symlink

    @symlink.setter
    def symlink(self, symlink):
        r"""Sets the symlink of this FsFileCount.

        符号链接数目

        :param symlink: The symlink of this FsFileCount.
        :type symlink: int
        """
        self._symlink = symlink

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
        if not isinstance(other, FsFileCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
