# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarIdcardRequestBody:

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
        'convert_unicode': 'bool',
        'return_confidence': 'bool',
        'return_portrait_image': 'bool',
        'return_portrait_location': 'bool',
        'return_idcard_type': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'convert_unicode': 'convert_unicode',
        'return_confidence': 'return_confidence',
        'return_portrait_image': 'return_portrait_image',
        'return_portrait_location': 'return_portrait_location',
        'return_idcard_type': 'return_idcard_type'
    }

    def __init__(self, image=None, url=None, convert_unicode=None, return_confidence=None, return_portrait_image=None, return_portrait_location=None, return_idcard_type=None):
        """MyanmarIdcardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param convert_unicode: - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 
        :type convert_unicode: bool
        :param return_confidence: 是否返回置信度的开关，可选值如下所示。 - true：返回置信度 - false：不返回置信度 如果无该参数，系统默认不返回置信度。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_confidence: bool
        :param return_portrait_image: 是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 
        :type return_portrait_image: bool
        :param return_portrait_location: 是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 
        :type return_portrait_location: bool
        :param return_idcard_type: 是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 
        :type return_idcard_type: bool
        """
        
        

        self._image = None
        self._url = None
        self._convert_unicode = None
        self._return_confidence = None
        self._return_portrait_image = None
        self._return_portrait_location = None
        self._return_idcard_type = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if convert_unicode is not None:
            self.convert_unicode = convert_unicode
        if return_confidence is not None:
            self.return_confidence = return_confidence
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image
        if return_portrait_location is not None:
            self.return_portrait_location = return_portrait_location
        if return_idcard_type is not None:
            self.return_idcard_type = return_idcard_type

    @property
    def image(self):
        """Gets the image of this MyanmarIdcardRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :return: The image of this MyanmarIdcardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MyanmarIdcardRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :param image: The image of this MyanmarIdcardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this MyanmarIdcardRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this MyanmarIdcardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MyanmarIdcardRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this MyanmarIdcardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def convert_unicode(self):
        """Gets the convert_unicode of this MyanmarIdcardRequestBody.

        - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 

        :return: The convert_unicode of this MyanmarIdcardRequestBody.
        :rtype: bool
        """
        return self._convert_unicode

    @convert_unicode.setter
    def convert_unicode(self, convert_unicode):
        """Sets the convert_unicode of this MyanmarIdcardRequestBody.

        - true：输出为unicode格式 - false：输出为zawgyi格式 如果参数值为空或无该参数，默认输出为zawgyi格式。 

        :param convert_unicode: The convert_unicode of this MyanmarIdcardRequestBody.
        :type convert_unicode: bool
        """
        self._convert_unicode = convert_unicode

    @property
    def return_confidence(self):
        """Gets the return_confidence of this MyanmarIdcardRequestBody.

        是否返回置信度的开关，可选值如下所示。 - true：返回置信度 - false：不返回置信度 如果无该参数，系统默认不返回置信度。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_confidence of this MyanmarIdcardRequestBody.
        :rtype: bool
        """
        return self._return_confidence

    @return_confidence.setter
    def return_confidence(self, return_confidence):
        """Sets the return_confidence of this MyanmarIdcardRequestBody.

        是否返回置信度的开关，可选值如下所示。 - true：返回置信度 - false：不返回置信度 如果无该参数，系统默认不返回置信度。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_confidence: The return_confidence of this MyanmarIdcardRequestBody.
        :type return_confidence: bool
        """
        self._return_confidence = return_confidence

    @property
    def return_portrait_image(self):
        """Gets the return_portrait_image of this MyanmarIdcardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 

        :return: The return_portrait_image of this MyanmarIdcardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        """Sets the return_portrait_image of this MyanmarIdcardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 

        :param return_portrait_image: The return_portrait_image of this MyanmarIdcardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

    @property
    def return_portrait_location(self):
        """Gets the return_portrait_location of this MyanmarIdcardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 

        :return: The return_portrait_location of this MyanmarIdcardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_location

    @return_portrait_location.setter
    def return_portrait_location(self, return_portrait_location):
        """Sets the return_portrait_location of this MyanmarIdcardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 

        :param return_portrait_location: The return_portrait_location of this MyanmarIdcardRequestBody.
        :type return_portrait_location: bool
        """
        self._return_portrait_location = return_portrait_location

    @property
    def return_idcard_type(self):
        """Gets the return_idcard_type of this MyanmarIdcardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 

        :return: The return_idcard_type of this MyanmarIdcardRequestBody.
        :rtype: bool
        """
        return self._return_idcard_type

    @return_idcard_type.setter
    def return_idcard_type(self, return_idcard_type):
        """Sets the return_idcard_type of this MyanmarIdcardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 

        :param return_idcard_type: The return_idcard_type of this MyanmarIdcardRequestBody.
        :type return_idcard_type: bool
        """
        self._return_idcard_type = return_idcard_type

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
        if not isinstance(other, MyanmarIdcardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
