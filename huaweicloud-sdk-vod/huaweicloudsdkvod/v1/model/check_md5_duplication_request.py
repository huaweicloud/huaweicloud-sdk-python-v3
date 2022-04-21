# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckMd5DuplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'md5': 'str'
    }

    attribute_map = {
        'size': 'size',
        'md5': 'md5'
    }

    def __init__(self, size=None, md5=None):
        """CheckMd5DuplicationRequest

        The model defined in huaweicloud sdk

        :param size: 文件大小
        :type size: int
        :param md5: 文件MD5。  建议参考[上传校验](https://support.huaweicloud.com/api-vod/vod_04_0212.html#vod_04_0212__section575102165412)生成对应的MD5值。
        :type md5: str
        """
        
        

        self._size = None
        self._md5 = None
        self.discriminator = None

        self.size = size
        self.md5 = md5

    @property
    def size(self):
        """Gets the size of this CheckMd5DuplicationRequest.

        文件大小

        :return: The size of this CheckMd5DuplicationRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CheckMd5DuplicationRequest.

        文件大小

        :param size: The size of this CheckMd5DuplicationRequest.
        :type size: int
        """
        self._size = size

    @property
    def md5(self):
        """Gets the md5 of this CheckMd5DuplicationRequest.

        文件MD5。  建议参考[上传校验](https://support.huaweicloud.com/api-vod/vod_04_0212.html#vod_04_0212__section575102165412)生成对应的MD5值。

        :return: The md5 of this CheckMd5DuplicationRequest.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this CheckMd5DuplicationRequest.

        文件MD5。  建议参考[上传校验](https://support.huaweicloud.com/api-vod/vod_04_0212.html#vod_04_0212__section575102165412)生成对应的MD5值。

        :param md5: The md5 of this CheckMd5DuplicationRequest.
        :type md5: str
        """
        self._md5 = md5

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
        if not isinstance(other, CheckMd5DuplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
