# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdCardRequestBody:

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
        'side': 'str',
        'return_verification': 'bool',
        'return_text_location': 'bool',
        'detect_reproduce': 'bool',
        'detect_copy': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side',
        'return_verification': 'return_verification',
        'return_text_location': 'return_text_location',
        'detect_reproduce': 'detect_reproduce',
        'detect_copy': 'detect_copy'
    }

    def __init__(self, image=None, url=None, side=None, return_verification=None, return_text_location=None, detect_reproduce=None, detect_copy=None):
        """IdCardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  &gt; 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param side:  - front：身份证正面。  - back：身份证背面。  &gt; 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 
        :type side: str
        :param return_verification: 返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 
        :type return_verification: bool
        :param return_text_location: 识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_text_location: bool
        :param detect_reproduce: 返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否经过翻拍  - false：不返回身份证图像是否经过翻拍 
        :type detect_reproduce: bool
        :param detect_copy: 返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否是复印件  - false : 不返回身份证图像是否是复印件             
        :type detect_copy: bool
        """
        
        

        self._image = None
        self._url = None
        self._side = None
        self._return_verification = None
        self._return_text_location = None
        self._detect_reproduce = None
        self._detect_copy = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if side is not None:
            self.side = side
        if return_verification is not None:
            self.return_verification = return_verification
        if return_text_location is not None:
            self.return_text_location = return_text_location
        if detect_reproduce is not None:
            self.detect_reproduce = detect_reproduce
        if detect_copy is not None:
            self.detect_copy = detect_copy

    @property
    def image(self):
        """Gets the image of this IdCardRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this IdCardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IdCardRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this IdCardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this IdCardRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this IdCardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdCardRequestBody.

        与image二选一  图片的URL路径，目前支持：  - 公网http/https url  - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this IdCardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def side(self):
        """Gets the side of this IdCardRequestBody.

         - front：身份证正面。  - back：身份证背面。  > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :return: The side of this IdCardRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this IdCardRequestBody.

         - front：身份证正面。  - back：身份证背面。  > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :param side: The side of this IdCardRequestBody.
        :type side: str
        """
        self._side = side

    @property
    def return_verification(self):
        """Gets the return_verification of this IdCardRequestBody.

        返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 

        :return: The return_verification of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_verification

    @return_verification.setter
    def return_verification(self, return_verification):
        """Sets the return_verification of this IdCardRequestBody.

        返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 

        :param return_verification: The return_verification of this IdCardRequestBody.
        :type return_verification: bool
        """
        self._return_verification = return_verification

    @property
    def return_text_location(self):
        """Gets the return_text_location of this IdCardRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_text_location of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this IdCardRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_text_location: The return_text_location of this IdCardRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

    @property
    def detect_reproduce(self):
        """Gets the detect_reproduce of this IdCardRequestBody.

        返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否经过翻拍  - false：不返回身份证图像是否经过翻拍 

        :return: The detect_reproduce of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_reproduce

    @detect_reproduce.setter
    def detect_reproduce(self, detect_reproduce):
        """Sets the detect_reproduce of this IdCardRequestBody.

        返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否经过翻拍  - false：不返回身份证图像是否经过翻拍 

        :param detect_reproduce: The detect_reproduce of this IdCardRequestBody.
        :type detect_reproduce: bool
        """
        self._detect_reproduce = detect_reproduce

    @property
    def detect_copy(self):
        """Gets the detect_copy of this IdCardRequestBody.

        返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否是复印件  - false : 不返回身份证图像是否是复印件             

        :return: The detect_copy of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_copy

    @detect_copy.setter
    def detect_copy(self, detect_copy):
        """Sets the detect_copy of this IdCardRequestBody.

        返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：返回身份证图像是否是复印件  - false : 不返回身份证图像是否是复印件             

        :param detect_copy: The detect_copy of this IdCardRequestBody.
        :type detect_copy: bool
        """
        self._detect_copy = detect_copy

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
        if not isinstance(other, IdCardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
