# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageHighresolutionMattingInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'return_type': 'str',
        'coord': 'list[int]'
    }

    attribute_map = {
        'return_type': 'return_type',
        'coord': 'coord'
    }

    def __init__(self, return_type=None, coord=None):
        """ImageHighresolutionMattingInference

        The model defined in huaweicloud sdk

        :param return_type: 是否只返回处理结果的alpha通道，\&quot;foreground\&quot;代表返回带alpha通道的前景图片，\&quot;alpha\&quot;字符串代表仅返回alpha通道
        :type return_type: str
        :param coord: 指定抠图区域坐标，默认全图，示例：[x_min,y_min,x_max,y_max]
        :type coord: list[int]
        """
        
        

        self._return_type = None
        self._coord = None
        self.discriminator = None

        self.return_type = return_type
        if coord is not None:
            self.coord = coord

    @property
    def return_type(self):
        """Gets the return_type of this ImageHighresolutionMattingInference.

        是否只返回处理结果的alpha通道，\"foreground\"代表返回带alpha通道的前景图片，\"alpha\"字符串代表仅返回alpha通道

        :return: The return_type of this ImageHighresolutionMattingInference.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this ImageHighresolutionMattingInference.

        是否只返回处理结果的alpha通道，\"foreground\"代表返回带alpha通道的前景图片，\"alpha\"字符串代表仅返回alpha通道

        :param return_type: The return_type of this ImageHighresolutionMattingInference.
        :type return_type: str
        """
        self._return_type = return_type

    @property
    def coord(self):
        """Gets the coord of this ImageHighresolutionMattingInference.

        指定抠图区域坐标，默认全图，示例：[x_min,y_min,x_max,y_max]

        :return: The coord of this ImageHighresolutionMattingInference.
        :rtype: list[int]
        """
        return self._coord

    @coord.setter
    def coord(self, coord):
        """Sets the coord of this ImageHighresolutionMattingInference.

        指定抠图区域坐标，默认全图，示例：[x_min,y_min,x_max,y_max]

        :param coord: The coord of this ImageHighresolutionMattingInference.
        :type coord: list[int]
        """
        self._coord = coord

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
        if not isinstance(other, ImageHighresolutionMattingInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
