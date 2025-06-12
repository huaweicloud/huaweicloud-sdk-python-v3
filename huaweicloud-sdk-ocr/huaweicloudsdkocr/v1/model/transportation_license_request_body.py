# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransportationLicenseRequestBody:

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
        'return_image_location': 'bool',
        'return_adjusted_image': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_image_location': 'return_image_location',
        'return_adjusted_image': 'return_adjusted_image'
    }

    def __init__(self, image=None, url=None, return_image_location=None, return_adjusted_image=None):
        r"""TransportationLicenseRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_image_location: 返回道路运输证在原图中的坐标位置的开关，默认false，取值范围包括：  - true: 开启返回坐标位置的功能。 - false: 关闭返回坐标位置的功能。 
        :type return_image_location: bool
        :param return_adjusted_image: 返回道路运输证（base64）的开关，默认false，取值范围包括：  - true: 开启道路运输证（base64）的功能。 - false: 关闭道路运输证（base64）的功能。 
        :type return_adjusted_image: bool
        """
        
        

        self._image = None
        self._url = None
        self._return_image_location = None
        self._return_adjusted_image = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_image_location is not None:
            self.return_image_location = return_image_location
        if return_adjusted_image is not None:
            self.return_adjusted_image = return_adjusted_image

    @property
    def image(self):
        r"""Gets the image of this TransportationLicenseRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this TransportationLicenseRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this TransportationLicenseRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this TransportationLicenseRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this TransportationLicenseRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this TransportationLicenseRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this TransportationLicenseRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过4096px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this TransportationLicenseRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_image_location(self):
        r"""Gets the return_image_location of this TransportationLicenseRequestBody.

        返回道路运输证在原图中的坐标位置的开关，默认false，取值范围包括：  - true: 开启返回坐标位置的功能。 - false: 关闭返回坐标位置的功能。 

        :return: The return_image_location of this TransportationLicenseRequestBody.
        :rtype: bool
        """
        return self._return_image_location

    @return_image_location.setter
    def return_image_location(self, return_image_location):
        r"""Sets the return_image_location of this TransportationLicenseRequestBody.

        返回道路运输证在原图中的坐标位置的开关，默认false，取值范围包括：  - true: 开启返回坐标位置的功能。 - false: 关闭返回坐标位置的功能。 

        :param return_image_location: The return_image_location of this TransportationLicenseRequestBody.
        :type return_image_location: bool
        """
        self._return_image_location = return_image_location

    @property
    def return_adjusted_image(self):
        r"""Gets the return_adjusted_image of this TransportationLicenseRequestBody.

        返回道路运输证（base64）的开关，默认false，取值范围包括：  - true: 开启道路运输证（base64）的功能。 - false: 关闭道路运输证（base64）的功能。 

        :return: The return_adjusted_image of this TransportationLicenseRequestBody.
        :rtype: bool
        """
        return self._return_adjusted_image

    @return_adjusted_image.setter
    def return_adjusted_image(self, return_adjusted_image):
        r"""Sets the return_adjusted_image of this TransportationLicenseRequestBody.

        返回道路运输证（base64）的开关，默认false，取值范围包括：  - true: 开启道路运输证（base64）的功能。 - false: 关闭道路运输证（base64）的功能。 

        :param return_adjusted_image: The return_adjusted_image of this TransportationLicenseRequestBody.
        :type return_adjusted_image: bool
        """
        self._return_adjusted_image = return_adjusted_image

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
        if not isinstance(other, TransportationLicenseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
