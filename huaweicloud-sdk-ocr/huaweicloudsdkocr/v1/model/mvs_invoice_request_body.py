# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MvsInvoiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'return_text_location': 'bool',
        'return_confidence': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_text_location': 'return_text_location',
        'return_confidence': 'return_confidence',
        'type': 'type'
    }

    def __init__(self, image=None, url=None, return_text_location=None, return_confidence=None, type=None):
        """MvsInvoiceRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_text_location: 如果为True，返回体中会包含text_location对象，内容是各字段的检测框四点坐标。如果是False或者没有这个key，则返回体中不包含text_location对象。 
        :type return_text_location: bool
        :param return_confidence: 如果为True，返回体中会包含confidence对象，内容是各字段的置信度。如果是False或者没有这个key，则返回体中不包含confidence对象。 
        :type return_confidence: bool
        :param type: 如果没有type字段则默认返回原机动车销售发票出参； 若存在type字段但是不属于 auto、new或者used三个枚举值，API返回AIS.0101入参错误； 如果type为auto，API自动判断发票类型，并在返回参数中添加type出参以指明发票类型； 如果type为new，API在检测出的类型为机动车发票时返回原版机动车发票出参并添加type出参（机动车销售统一发票），不一致时报错AIS.0104图像质量差； 如果type为used，API在检测出的类型为二手车时返回二手车发票出参，并添加type出参（二手车销售统一发票），不一致时报错AIS.0104图像质量差。 
        :type type: str
        """
        
        

        self._image = None
        self._url = None
        self._return_text_location = None
        self._return_confidence = None
        self._type = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_text_location is not None:
            self.return_text_location = return_text_location
        if return_confidence is not None:
            self.return_confidence = return_confidence
        if type is not None:
            self.type = type

    @property
    def image(self):
        """Gets the image of this MvsInvoiceRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this MvsInvoiceRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MvsInvoiceRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this MvsInvoiceRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this MvsInvoiceRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this MvsInvoiceRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MvsInvoiceRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this MvsInvoiceRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_text_location(self):
        """Gets the return_text_location of this MvsInvoiceRequestBody.

        如果为True，返回体中会包含text_location对象，内容是各字段的检测框四点坐标。如果是False或者没有这个key，则返回体中不包含text_location对象。 

        :return: The return_text_location of this MvsInvoiceRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this MvsInvoiceRequestBody.

        如果为True，返回体中会包含text_location对象，内容是各字段的检测框四点坐标。如果是False或者没有这个key，则返回体中不包含text_location对象。 

        :param return_text_location: The return_text_location of this MvsInvoiceRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

    @property
    def return_confidence(self):
        """Gets the return_confidence of this MvsInvoiceRequestBody.

        如果为True，返回体中会包含confidence对象，内容是各字段的置信度。如果是False或者没有这个key，则返回体中不包含confidence对象。 

        :return: The return_confidence of this MvsInvoiceRequestBody.
        :rtype: bool
        """
        return self._return_confidence

    @return_confidence.setter
    def return_confidence(self, return_confidence):
        """Sets the return_confidence of this MvsInvoiceRequestBody.

        如果为True，返回体中会包含confidence对象，内容是各字段的置信度。如果是False或者没有这个key，则返回体中不包含confidence对象。 

        :param return_confidence: The return_confidence of this MvsInvoiceRequestBody.
        :type return_confidence: bool
        """
        self._return_confidence = return_confidence

    @property
    def type(self):
        """Gets the type of this MvsInvoiceRequestBody.

        如果没有type字段则默认返回原机动车销售发票出参； 若存在type字段但是不属于 auto、new或者used三个枚举值，API返回AIS.0101入参错误； 如果type为auto，API自动判断发票类型，并在返回参数中添加type出参以指明发票类型； 如果type为new，API在检测出的类型为机动车发票时返回原版机动车发票出参并添加type出参（机动车销售统一发票），不一致时报错AIS.0104图像质量差； 如果type为used，API在检测出的类型为二手车时返回二手车发票出参，并添加type出参（二手车销售统一发票），不一致时报错AIS.0104图像质量差。 

        :return: The type of this MvsInvoiceRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MvsInvoiceRequestBody.

        如果没有type字段则默认返回原机动车销售发票出参； 若存在type字段但是不属于 auto、new或者used三个枚举值，API返回AIS.0101入参错误； 如果type为auto，API自动判断发票类型，并在返回参数中添加type出参以指明发票类型； 如果type为new，API在检测出的类型为机动车发票时返回原版机动车发票出参并添加type出参（机动车销售统一发票），不一致时报错AIS.0104图像质量差； 如果type为used，API在检测出的类型为二手车时返回二手车发票出参，并添加type出参（二手车销售统一发票），不一致时报错AIS.0104图像质量差。 

        :param type: The type of this MvsInvoiceRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MvsInvoiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
