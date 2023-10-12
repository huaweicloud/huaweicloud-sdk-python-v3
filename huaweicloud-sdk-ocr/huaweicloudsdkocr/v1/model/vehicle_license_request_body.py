# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleLicenseRequestBody:

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
        'return_issuing_authority': 'bool',
        'return_text_location': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side',
        'return_issuing_authority': 'return_issuing_authority',
        'return_text_location': 'return_text_location'
    }

    def __init__(self, image=None, url=None, side=None, return_issuing_authority=None, return_text_location=None):
        """VehicleLicenseRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param side:  - front：行驶证主页  - back：行驶证副页  - double_side：行驶证双页信息  &gt; 说明： 如果参数值为空或无该参数，系统默认识别主页，建议填写，准确率更高。 
        :type side: str
        :param return_issuing_authority: 是否返回发证机关的开关，可选值包括： - true：返回发证机关 - false：不返回发证机关  &gt; 说明： - 如果无该参数，系统默认不返回发证机关。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_issuing_authority: bool
        :param return_text_location: 识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。:: 
        :type return_text_location: bool
        """
        
        

        self._image = None
        self._url = None
        self._side = None
        self._return_issuing_authority = None
        self._return_text_location = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if side is not None:
            self.side = side
        if return_issuing_authority is not None:
            self.return_issuing_authority = return_issuing_authority
        if return_text_location is not None:
            self.return_text_location = return_text_location

    @property
    def image(self):
        """Gets the image of this VehicleLicenseRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this VehicleLicenseRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VehicleLicenseRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8000px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this VehicleLicenseRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this VehicleLicenseRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this VehicleLicenseRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VehicleLicenseRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this VehicleLicenseRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def side(self):
        """Gets the side of this VehicleLicenseRequestBody.

         - front：行驶证主页  - back：行驶证副页  - double_side：行驶证双页信息  > 说明： 如果参数值为空或无该参数，系统默认识别主页，建议填写，准确率更高。 

        :return: The side of this VehicleLicenseRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this VehicleLicenseRequestBody.

         - front：行驶证主页  - back：行驶证副页  - double_side：行驶证双页信息  > 说明： 如果参数值为空或无该参数，系统默认识别主页，建议填写，准确率更高。 

        :param side: The side of this VehicleLicenseRequestBody.
        :type side: str
        """
        self._side = side

    @property
    def return_issuing_authority(self):
        """Gets the return_issuing_authority of this VehicleLicenseRequestBody.

        是否返回发证机关的开关，可选值包括： - true：返回发证机关 - false：不返回发证机关  > 说明： - 如果无该参数，系统默认不返回发证机关。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_issuing_authority of this VehicleLicenseRequestBody.
        :rtype: bool
        """
        return self._return_issuing_authority

    @return_issuing_authority.setter
    def return_issuing_authority(self, return_issuing_authority):
        """Sets the return_issuing_authority of this VehicleLicenseRequestBody.

        是否返回发证机关的开关，可选值包括： - true：返回发证机关 - false：不返回发证机关  > 说明： - 如果无该参数，系统默认不返回发证机关。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_issuing_authority: The return_issuing_authority of this VehicleLicenseRequestBody.
        :type return_issuing_authority: bool
        """
        self._return_issuing_authority = return_issuing_authority

    @property
    def return_text_location(self):
        """Gets the return_text_location of this VehicleLicenseRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。:: 

        :return: The return_text_location of this VehicleLicenseRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this VehicleLicenseRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。:: 

        :param return_text_location: The return_text_location of this VehicleLicenseRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

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
        if not isinstance(other, VehicleLicenseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
