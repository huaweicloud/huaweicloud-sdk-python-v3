# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Compress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'file_type': 'file_type'
    }

    def __init__(self, status=None, type=None, file_type=None):
        r"""Compress

        The model defined in huaweicloud sdk

        :param status: 智能压缩开关（on：开启，off：关闭）。
        :type status: str
        :param type: 智能压缩类型（gzip：gzip压缩，br：brotli压缩）。
        :type type: str
        :param file_type: 压缩格式，内容总长度不可超过200个字符，  多种格式用“,”分割，每组内容不可超过50个字符， 开启状态下，首次传空时默认值为.js,.html,.css,.xml,.json,.shtml,.htm，否则为上次设置的结果。
        :type file_type: str
        """
        
        

        self._status = None
        self._type = None
        self._file_type = None
        self.discriminator = None

        self.status = status
        if type is not None:
            self.type = type
        if file_type is not None:
            self.file_type = file_type

    @property
    def status(self):
        r"""Gets the status of this Compress.

        智能压缩开关（on：开启，off：关闭）。

        :return: The status of this Compress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Compress.

        智能压缩开关（on：开启，off：关闭）。

        :param status: The status of this Compress.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this Compress.

        智能压缩类型（gzip：gzip压缩，br：brotli压缩）。

        :return: The type of this Compress.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Compress.

        智能压缩类型（gzip：gzip压缩，br：brotli压缩）。

        :param type: The type of this Compress.
        :type type: str
        """
        self._type = type

    @property
    def file_type(self):
        r"""Gets the file_type of this Compress.

        压缩格式，内容总长度不可超过200个字符，  多种格式用“,”分割，每组内容不可超过50个字符， 开启状态下，首次传空时默认值为.js,.html,.css,.xml,.json,.shtml,.htm，否则为上次设置的结果。

        :return: The file_type of this Compress.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this Compress.

        压缩格式，内容总长度不可超过200个字符，  多种格式用“,”分割，每组内容不可超过50个字符， 开启状态下，首次传空时默认值为.js,.html,.css,.xml,.json,.shtml,.htm，否则为上次设置的结果。

        :param file_type: The file_type of this Compress.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, Compress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
