# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandStructureDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'compressed': 'bool',
        'data': 'str'
    }

    attribute_map = {
        'format': 'format',
        'compressed': 'compressed',
        'data': 'data'
    }

    def __init__(self, format=None, compressed=None, data=None):
        r"""LigandStructureDto

        The model defined in huaweicloud sdk

        :param format: 配体格式，即文件后缀名
        :type format: str
        :param compressed: 是否压缩
        :type compressed: bool
        :param data: 结构数据，如压缩则需要解码、解压处理（ASCII Encode -&gt; Base64 Decode -&gt; GZip Inflate -&gt; UTF-8 Decode）以得到原始字符串；如未压缩则为原始字符串
        :type data: str
        """
        
        

        self._format = None
        self._compressed = None
        self._data = None
        self.discriminator = None

        self.format = format
        if compressed is not None:
            self.compressed = compressed
        self.data = data

    @property
    def format(self):
        r"""Gets the format of this LigandStructureDto.

        配体格式，即文件后缀名

        :return: The format of this LigandStructureDto.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this LigandStructureDto.

        配体格式，即文件后缀名

        :param format: The format of this LigandStructureDto.
        :type format: str
        """
        self._format = format

    @property
    def compressed(self):
        r"""Gets the compressed of this LigandStructureDto.

        是否压缩

        :return: The compressed of this LigandStructureDto.
        :rtype: bool
        """
        return self._compressed

    @compressed.setter
    def compressed(self, compressed):
        r"""Sets the compressed of this LigandStructureDto.

        是否压缩

        :param compressed: The compressed of this LigandStructureDto.
        :type compressed: bool
        """
        self._compressed = compressed

    @property
    def data(self):
        r"""Gets the data of this LigandStructureDto.

        结构数据，如压缩则需要解码、解压处理（ASCII Encode -> Base64 Decode -> GZip Inflate -> UTF-8 Decode）以得到原始字符串；如未压缩则为原始字符串

        :return: The data of this LigandStructureDto.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this LigandStructureDto.

        结构数据，如压缩则需要解码、解压处理（ASCII Encode -> Base64 Decode -> GZip Inflate -> UTF-8 Decode）以得到原始字符串；如未压缩则为原始字符串

        :param data: The data of this LigandStructureDto.
        :type data: str
        """
        self._data = data

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
        if not isinstance(other, LigandStructureDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
