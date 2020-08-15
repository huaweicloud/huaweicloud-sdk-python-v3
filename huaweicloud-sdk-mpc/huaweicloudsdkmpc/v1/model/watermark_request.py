# coding: utf-8

import pprint
import re

import six





class WatermarkRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'template_id': 'str',
        'text_context': 'str',
        'image_watermark': 'ImageWatermark',
        'text_watermark': 'TextWatermark'
    }

    attribute_map = {
        'input': 'input',
        'template_id': 'template_id',
        'text_context': 'text_context',
        'image_watermark': 'image_watermark',
        'text_watermark': 'text_watermark'
    }

    def __init__(self, input=None, template_id=None, text_context=None, image_watermark=None, text_watermark=None):
        """WatermarkRequest - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._template_id = None
        self._text_context = None
        self._image_watermark = None
        self._text_watermark = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if template_id is not None:
            self.template_id = template_id
        if text_context is not None:
            self.text_context = text_context
        if image_watermark is not None:
            self.image_watermark = image_watermark
        if text_watermark is not None:
            self.text_watermark = text_watermark

    @property
    def input(self):
        """Gets the input of this WatermarkRequest.


        :return: The input of this WatermarkRequest.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this WatermarkRequest.


        :param input: The input of this WatermarkRequest.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def template_id(self):
        """Gets the template_id of this WatermarkRequest.

        水印模板。可通过新建水印模板接口创建水印模板。

        :return: The template_id of this WatermarkRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WatermarkRequest.

        水印模板。可通过新建水印模板接口创建水印模板。

        :param template_id: The template_id of this WatermarkRequest.
        :type: str
        """
        self._template_id = template_id

    @property
    def text_context(self):
        """Gets the text_context of this WatermarkRequest.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空  示例：若想添加文字水印“测试文字水印”，那么Content的值为：5rWL6K+V5paH5a2X5rC05Y2w 

        :return: The text_context of this WatermarkRequest.
        :rtype: str
        """
        return self._text_context

    @text_context.setter
    def text_context(self, text_context):
        """Sets the text_context of this WatermarkRequest.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空  示例：若想添加文字水印“测试文字水印”，那么Content的值为：5rWL6K+V5paH5a2X5rC05Y2w 

        :param text_context: The text_context of this WatermarkRequest.
        :type: str
        """
        self._text_context = text_context

    @property
    def image_watermark(self):
        """Gets the image_watermark of this WatermarkRequest.


        :return: The image_watermark of this WatermarkRequest.
        :rtype: ImageWatermark
        """
        return self._image_watermark

    @image_watermark.setter
    def image_watermark(self, image_watermark):
        """Sets the image_watermark of this WatermarkRequest.


        :param image_watermark: The image_watermark of this WatermarkRequest.
        :type: ImageWatermark
        """
        self._image_watermark = image_watermark

    @property
    def text_watermark(self):
        """Gets the text_watermark of this WatermarkRequest.


        :return: The text_watermark of this WatermarkRequest.
        :rtype: TextWatermark
        """
        return self._text_watermark

    @text_watermark.setter
    def text_watermark(self, text_watermark):
        """Sets the text_watermark of this WatermarkRequest.


        :param text_watermark: The text_watermark of this WatermarkRequest.
        :type: TextWatermark
        """
        self._text_watermark = text_watermark

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WatermarkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
