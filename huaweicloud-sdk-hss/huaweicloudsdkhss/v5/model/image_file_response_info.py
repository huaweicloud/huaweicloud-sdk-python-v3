# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageFileResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_path': 'str',
        'size': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_path': 'file_path',
        'size': 'size'
    }

    def __init__(self, file_name=None, file_path=None, size=None):
        r"""ImageFileResponseInfo

        The model defined in huaweicloud sdk

        :param file_name: **参数解释**: 文件名称 **取值范围**: 字符长度0-256 
        :type file_name: str
        :param file_path: **参数解释**: 文件路径 **取值范围**: 字符长度0-256 
        :type file_path: str
        :param size: **参数解释**: 文件大小 **取值范围**: 最小值0，最大值65535 
        :type size: int
        """
        
        

        self._file_name = None
        self._file_path = None
        self._size = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if size is not None:
            self.size = size

    @property
    def file_name(self):
        r"""Gets the file_name of this ImageFileResponseInfo.

        **参数解释**: 文件名称 **取值范围**: 字符长度0-256 

        :return: The file_name of this ImageFileResponseInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ImageFileResponseInfo.

        **参数解释**: 文件名称 **取值范围**: 字符长度0-256 

        :param file_name: The file_name of this ImageFileResponseInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ImageFileResponseInfo.

        **参数解释**: 文件路径 **取值范围**: 字符长度0-256 

        :return: The file_path of this ImageFileResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ImageFileResponseInfo.

        **参数解释**: 文件路径 **取值范围**: 字符长度0-256 

        :param file_path: The file_path of this ImageFileResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def size(self):
        r"""Gets the size of this ImageFileResponseInfo.

        **参数解释**: 文件大小 **取值范围**: 最小值0，最大值65535 

        :return: The size of this ImageFileResponseInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ImageFileResponseInfo.

        **参数解释**: 文件大小 **取值范围**: 最小值0，最大值65535 

        :param size: The size of this ImageFileResponseInfo.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ImageFileResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
