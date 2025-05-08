# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'template_id': 'str',
        'input': 'ObsInfo',
        'image_watermark': 'ImageWatermark',
        'text_context': 'str',
        'text_watermark': 'TextWatermark',
        'svg_context': 'str',
        'svg_watermark': 'SVGWatermark'
    }

    attribute_map = {
        'template_id': 'template_id',
        'input': 'input',
        'image_watermark': 'image_watermark',
        'text_context': 'text_context',
        'text_watermark': 'text_watermark',
        'svg_context': 'svg_context',
        'svg_watermark': 'svg_watermark'
    }

    def __init__(self, template_id=None, input=None, image_watermark=None, text_context=None, text_watermark=None, svg_context=None, svg_watermark=None):
        r"""WatermarkRequest

        The model defined in huaweicloud sdk

        :param template_id: 水印模板ID 
        :type template_id: str
        :param input: 
        :type input: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param image_watermark: 
        :type image_watermark: :class:`huaweicloudsdkvod.v1.ImageWatermark`
        :param text_context: 文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空 
        :type text_context: str
        :param text_watermark: 
        :type text_watermark: :class:`huaweicloudsdkvod.v1.TextWatermark`
        :param svg_context: svg水印的内容 
        :type svg_context: str
        :param svg_watermark: 
        :type svg_watermark: :class:`huaweicloudsdkvod.v1.SVGWatermark`
        """
        
        

        self._template_id = None
        self._input = None
        self._image_watermark = None
        self._text_context = None
        self._text_watermark = None
        self._svg_context = None
        self._svg_watermark = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if input is not None:
            self.input = input
        if image_watermark is not None:
            self.image_watermark = image_watermark
        if text_context is not None:
            self.text_context = text_context
        if text_watermark is not None:
            self.text_watermark = text_watermark
        if svg_context is not None:
            self.svg_context = svg_context
        if svg_watermark is not None:
            self.svg_watermark = svg_watermark

    @property
    def template_id(self):
        r"""Gets the template_id of this WatermarkRequest.

        水印模板ID 

        :return: The template_id of this WatermarkRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this WatermarkRequest.

        水印模板ID 

        :param template_id: The template_id of this WatermarkRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def input(self):
        r"""Gets the input of this WatermarkRequest.

        :return: The input of this WatermarkRequest.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this WatermarkRequest.

        :param input: The input of this WatermarkRequest.
        :type input: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._input = input

    @property
    def image_watermark(self):
        r"""Gets the image_watermark of this WatermarkRequest.

        :return: The image_watermark of this WatermarkRequest.
        :rtype: :class:`huaweicloudsdkvod.v1.ImageWatermark`
        """
        return self._image_watermark

    @image_watermark.setter
    def image_watermark(self, image_watermark):
        r"""Sets the image_watermark of this WatermarkRequest.

        :param image_watermark: The image_watermark of this WatermarkRequest.
        :type image_watermark: :class:`huaweicloudsdkvod.v1.ImageWatermark`
        """
        self._image_watermark = image_watermark

    @property
    def text_context(self):
        r"""Gets the text_context of this WatermarkRequest.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空 

        :return: The text_context of this WatermarkRequest.
        :rtype: str
        """
        return self._text_context

    @text_context.setter
    def text_context(self, text_context):
        r"""Sets the text_context of this WatermarkRequest.

        文字水印内容，内容需做Base64编码，若类型为文字水印 (type字段为Text)，则此配置项不能为空 

        :param text_context: The text_context of this WatermarkRequest.
        :type text_context: str
        """
        self._text_context = text_context

    @property
    def text_watermark(self):
        r"""Gets the text_watermark of this WatermarkRequest.

        :return: The text_watermark of this WatermarkRequest.
        :rtype: :class:`huaweicloudsdkvod.v1.TextWatermark`
        """
        return self._text_watermark

    @text_watermark.setter
    def text_watermark(self, text_watermark):
        r"""Sets the text_watermark of this WatermarkRequest.

        :param text_watermark: The text_watermark of this WatermarkRequest.
        :type text_watermark: :class:`huaweicloudsdkvod.v1.TextWatermark`
        """
        self._text_watermark = text_watermark

    @property
    def svg_context(self):
        r"""Gets the svg_context of this WatermarkRequest.

        svg水印的内容 

        :return: The svg_context of this WatermarkRequest.
        :rtype: str
        """
        return self._svg_context

    @svg_context.setter
    def svg_context(self, svg_context):
        r"""Sets the svg_context of this WatermarkRequest.

        svg水印的内容 

        :param svg_context: The svg_context of this WatermarkRequest.
        :type svg_context: str
        """
        self._svg_context = svg_context

    @property
    def svg_watermark(self):
        r"""Gets the svg_watermark of this WatermarkRequest.

        :return: The svg_watermark of this WatermarkRequest.
        :rtype: :class:`huaweicloudsdkvod.v1.SVGWatermark`
        """
        return self._svg_watermark

    @svg_watermark.setter
    def svg_watermark(self, svg_watermark):
        r"""Sets the svg_watermark of this WatermarkRequest.

        :param svg_watermark: The svg_watermark of this WatermarkRequest.
        :type svg_watermark: :class:`huaweicloudsdkvod.v1.SVGWatermark`
        """
        self._svg_watermark = svg_watermark

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
        if not isinstance(other, WatermarkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
