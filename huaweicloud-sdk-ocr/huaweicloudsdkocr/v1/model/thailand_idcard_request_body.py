# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThailandIdcardRequestBody:

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
        'return_portrait_image': 'bool',
        'return_portrait_location': 'bool',
        'return_idcard_type': 'bool',
        'return_text_location': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side',
        'return_portrait_image': 'return_portrait_image',
        'return_portrait_location': 'return_portrait_location',
        'return_idcard_type': 'return_idcard_type',
        'return_text_location': 'return_text_location'
    }

    def __init__(self, image=None, url=None, side=None, return_portrait_image=None, return_portrait_location=None, return_idcard_type=None, return_text_location=None):
        r"""ThailandIdcardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param side: - front：身份证正面 - back：身份证背面 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 
        :type side: str
        :param return_portrait_image: 是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 
        :type return_portrait_image: bool
        :param return_portrait_location: 是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 
        :type return_portrait_location: bool
        :param return_idcard_type: 是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件、身份证复印件和屏幕翻拍 - false：不返回身份证的类型 
        :type return_idcard_type: bool
        :param return_text_location: 识别到的文字块的区域位置信息。可选值包括： - true：返回各个文字块区域 - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_text_location: bool
        """
        
        

        self._image = None
        self._url = None
        self._side = None
        self._return_portrait_image = None
        self._return_portrait_location = None
        self._return_idcard_type = None
        self._return_text_location = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if side is not None:
            self.side = side
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image
        if return_portrait_location is not None:
            self.return_portrait_location = return_portrait_location
        if return_idcard_type is not None:
            self.return_idcard_type = return_idcard_type
        if return_text_location is not None:
            self.return_text_location = return_text_location

    @property
    def image(self):
        r"""Gets the image of this ThailandIdcardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :return: The image of this ThailandIdcardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ThailandIdcardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。

        :param image: The image of this ThailandIdcardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this ThailandIdcardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this ThailandIdcardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ThailandIdcardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this ThailandIdcardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def side(self):
        r"""Gets the side of this ThailandIdcardRequestBody.

        - front：身份证正面 - back：身份证背面 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :return: The side of this ThailandIdcardRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        r"""Sets the side of this ThailandIdcardRequestBody.

        - front：身份证正面 - back：身份证背面 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :param side: The side of this ThailandIdcardRequestBody.
        :type side: str
        """
        self._side = side

    @property
    def return_portrait_image(self):
        r"""Gets the return_portrait_image of this ThailandIdcardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 

        :return: The return_portrait_image of this ThailandIdcardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        r"""Sets the return_portrait_image of this ThailandIdcardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true：返回身份证头像照片的 base64 编码 - false：不返回身份证头像照片的 base64 编码 未传入该参数时默认为false，即不返回身份证头像照片的 base64 编码。 

        :param return_portrait_image: The return_portrait_image of this ThailandIdcardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

    @property
    def return_portrait_location(self):
        r"""Gets the return_portrait_location of this ThailandIdcardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 

        :return: The return_portrait_location of this ThailandIdcardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_location

    @return_portrait_location.setter
    def return_portrait_location(self, return_portrait_location):
        r"""Sets the return_portrait_location of this ThailandIdcardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true：返回身份证头像的位置 - false：不返回身份证头像的位置 

        :param return_portrait_location: The return_portrait_location of this ThailandIdcardRequestBody.
        :type return_portrait_location: bool
        """
        self._return_portrait_location = return_portrait_location

    @property
    def return_idcard_type(self):
        r"""Gets the return_idcard_type of this ThailandIdcardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件、身份证复印件和屏幕翻拍 - false：不返回身份证的类型 

        :return: The return_idcard_type of this ThailandIdcardRequestBody.
        :rtype: bool
        """
        return self._return_idcard_type

    @return_idcard_type.setter
    def return_idcard_type(self, return_idcard_type):
        r"""Sets the return_idcard_type of this ThailandIdcardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true：返回身份证的类型，类型包括身份证原件、身份证复印件和屏幕翻拍 - false：不返回身份证的类型 

        :param return_idcard_type: The return_idcard_type of this ThailandIdcardRequestBody.
        :type return_idcard_type: bool
        """
        self._return_idcard_type = return_idcard_type

    @property
    def return_text_location(self):
        r"""Gets the return_text_location of this ThailandIdcardRequestBody.

        识别到的文字块的区域位置信息。可选值包括： - true：返回各个文字块区域 - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_text_location of this ThailandIdcardRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        r"""Sets the return_text_location of this ThailandIdcardRequestBody.

        识别到的文字块的区域位置信息。可选值包括： - true：返回各个文字块区域 - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_text_location: The return_text_location of this ThailandIdcardRequestBody.
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
        if not isinstance(other, ThailandIdcardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
