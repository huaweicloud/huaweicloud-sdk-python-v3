# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompressRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compress_type': 'str',
        'compress_file_type': 'str'
    }

    attribute_map = {
        'compress_type': 'compress_type',
        'compress_file_type': 'compress_file_type'
    }

    def __init__(self, compress_type=None, compress_file_type=None):
        """CompressRules

        The model defined in huaweicloud sdk

        :param compress_type: GZIP压缩类型（目前只支持 gzip）
        :type compress_type: str
        :param compress_file_type: GZIP压缩文件类型（文件后缀竖线分割，如：.js|.html|.css|.xml）
        :type compress_file_type: str
        """
        
        

        self._compress_type = None
        self._compress_file_type = None
        self.discriminator = None

        if compress_type is not None:
            self.compress_type = compress_type
        if compress_file_type is not None:
            self.compress_file_type = compress_file_type

    @property
    def compress_type(self):
        """Gets the compress_type of this CompressRules.

        GZIP压缩类型（目前只支持 gzip）

        :return: The compress_type of this CompressRules.
        :rtype: str
        """
        return self._compress_type

    @compress_type.setter
    def compress_type(self, compress_type):
        """Sets the compress_type of this CompressRules.

        GZIP压缩类型（目前只支持 gzip）

        :param compress_type: The compress_type of this CompressRules.
        :type compress_type: str
        """
        self._compress_type = compress_type

    @property
    def compress_file_type(self):
        """Gets the compress_file_type of this CompressRules.

        GZIP压缩文件类型（文件后缀竖线分割，如：.js|.html|.css|.xml）

        :return: The compress_file_type of this CompressRules.
        :rtype: str
        """
        return self._compress_file_type

    @compress_file_type.setter
    def compress_file_type(self, compress_file_type):
        """Sets the compress_file_type of this CompressRules.

        GZIP压缩文件类型（文件后缀竖线分割，如：.js|.html|.css|.xml）

        :param compress_file_type: The compress_file_type of this CompressRules.
        :type compress_file_type: str
        """
        self._compress_file_type = compress_file_type

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
        if not isinstance(other, CompressRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
