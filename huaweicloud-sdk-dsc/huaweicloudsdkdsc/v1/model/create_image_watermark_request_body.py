# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageWatermarkRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'blind_watermark': 'str'
    }

    attribute_map = {
        'file': 'file',
        'blind_watermark': 'blind_watermark'
    }

    def __init__(self, file=None, blind_watermark=None):
        """CreateImageWatermarkRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._file = None
        self._blind_watermark = None
        self.discriminator = None

        self.file = file
        self.blind_watermark = blind_watermark

    @property
    def file(self):
        """Gets the file of this CreateImageWatermarkRequestBody.

        要添加水印的图片文件，添加的图片短边尺寸需要超过512像素。

        :return: The file of this CreateImageWatermarkRequestBody.
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateImageWatermarkRequestBody.

        要添加水印的图片文件，添加的图片短边尺寸需要超过512像素。

        :param file: The file of this CreateImageWatermarkRequestBody.
        :type: file
        """
        self._file = file

    @property
    def blind_watermark(self):
        """Gets the blind_watermark of this CreateImageWatermarkRequestBody.

        嵌入暗水印的内容，长度不超过32个字符。当前仅支持数字及英文大小写。

        :return: The blind_watermark of this CreateImageWatermarkRequestBody.
        :rtype: str
        """
        return self._blind_watermark

    @blind_watermark.setter
    def blind_watermark(self, blind_watermark):
        """Sets the blind_watermark of this CreateImageWatermarkRequestBody.

        嵌入暗水印的内容，长度不超过32个字符。当前仅支持数字及英文大小写。

        :param blind_watermark: The blind_watermark of this CreateImageWatermarkRequestBody.
        :type: str
        """
        self._blind_watermark = blind_watermark

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
        if not isinstance(other, CreateImageWatermarkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
