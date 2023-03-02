# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignCombineReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'canvas_w': 'int',
        'canvas_h': 'int',
        'layers': 'list[ImageWisedesignCombineBody]'
    }

    attribute_map = {
        'canvas_w': 'canvas_w',
        'canvas_h': 'canvas_h',
        'layers': 'layers'
    }

    def __init__(self, canvas_w=None, canvas_h=None, layers=None):
        """ImageWisedesignCombineReq

        The model defined in huaweicloud sdk

        :param canvas_w: 画布的宽度
        :type canvas_w: int
        :param canvas_h: 画布的高度
        :type canvas_h: int
        :param layers: 图片合成的层级详细信息
        :type layers: list[:class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBody`]
        """
        
        

        self._canvas_w = None
        self._canvas_h = None
        self._layers = None
        self.discriminator = None

        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        self.layers = layers

    @property
    def canvas_w(self):
        """Gets the canvas_w of this ImageWisedesignCombineReq.

        画布的宽度

        :return: The canvas_w of this ImageWisedesignCombineReq.
        :rtype: int
        """
        return self._canvas_w

    @canvas_w.setter
    def canvas_w(self, canvas_w):
        """Sets the canvas_w of this ImageWisedesignCombineReq.

        画布的宽度

        :param canvas_w: The canvas_w of this ImageWisedesignCombineReq.
        :type canvas_w: int
        """
        self._canvas_w = canvas_w

    @property
    def canvas_h(self):
        """Gets the canvas_h of this ImageWisedesignCombineReq.

        画布的高度

        :return: The canvas_h of this ImageWisedesignCombineReq.
        :rtype: int
        """
        return self._canvas_h

    @canvas_h.setter
    def canvas_h(self, canvas_h):
        """Sets the canvas_h of this ImageWisedesignCombineReq.

        画布的高度

        :param canvas_h: The canvas_h of this ImageWisedesignCombineReq.
        :type canvas_h: int
        """
        self._canvas_h = canvas_h

    @property
    def layers(self):
        """Gets the layers of this ImageWisedesignCombineReq.

        图片合成的层级详细信息

        :return: The layers of this ImageWisedesignCombineReq.
        :rtype: list[:class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBody`]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this ImageWisedesignCombineReq.

        图片合成的层级详细信息

        :param layers: The layers of this ImageWisedesignCombineReq.
        :type layers: list[:class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBody`]
        """
        self._layers = layers

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
        if not isinstance(other, ImageWisedesignCombineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
