# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CambodianIdCardRequestBody:

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
        'return_portrait_image': 'bool',
        'return_portrait_location': 'bool',
        'return_idcard_type': 'bool',
        'detect_border_integrity': 'bool',
        'detect_blocking_within_border': 'bool',
        'detect_blur': 'bool',
        'detect_glare': 'bool',
        'return_adjusted_image': 'bool',
        'detect_tampering': 'bool',
        'detect_reproduce': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_portrait_image': 'return_portrait_image',
        'return_portrait_location': 'return_portrait_location',
        'return_idcard_type': 'return_idcard_type',
        'detect_border_integrity': 'detect_border_integrity',
        'detect_blocking_within_border': 'detect_blocking_within_border',
        'detect_blur': 'detect_blur',
        'detect_glare': 'detect_glare',
        'return_adjusted_image': 'return_adjusted_image',
        'detect_tampering': 'detect_tampering',
        'detect_reproduce': 'detect_reproduce'
    }

    def __init__(self, image=None, url=None, return_portrait_image=None, return_portrait_location=None, return_idcard_type=None, detect_border_integrity=None, detect_blocking_within_border=None, detect_blur=None, detect_glare=None, return_adjusted_image=None, detect_tampering=None, detect_reproduce=None):
        r"""CambodianIdCardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_portrait_image: 是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 
        :type return_portrait_image: bool
        :param return_portrait_location: 是否返回头像坐标的开关，可选值如下所示： - true: 返回身份证头像的位置坐标 - false: 不返回身份证头像的位置坐标 未传入该参数时默认为“false”，即不返回身份证的头像坐标。 
        :type return_portrait_location: bool
        :param return_idcard_type: 是否返回身份证类型的开关，可选值如下所示： - true:返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 
        :type return_idcard_type: bool
        :param detect_border_integrity: 返回身份证边框完整性的告警结果的开关，可选值如下所示 - true：打开身份证图像边框完整性告警功能  - false：关闭身份证图像边框完整性告警功能 
        :type detect_border_integrity: bool
        :param detect_blocking_within_border: 返回身份证内部是否有被遮挡的告警结果的开关，可选值如下所示 - true：打开身份证内部是否有被遮挡的告警功能  - false：关闭身份证内部是否有被遮挡的告警功能 
        :type detect_blocking_within_border: bool
        :param detect_blur: 返回身份证模糊告警结果的开关，可选值如下所示 - true:打开身份证是否模糊的告警功能 - false：关闭身份证是否模糊的告警功能 
        :type detect_blur: bool
        :param detect_glare: 返回身份证是否反光的告警结果的开关，可选值如下所示 - true：打开身份证是否反光的告警功能  - false：关闭身份证是否反光的告警功能 
        :type detect_glare: bool
        :param return_adjusted_image: 返回身份证四点原图的base64编码 - true: 返回身份证原图的base64编码  - false：不返回身份证原图的base64编码 
        :type return_adjusted_image: bool
        :param detect_tampering: 返回身份证人像是否被篡改的告警结果的开关，可选值如下所示 - true:  打开身份证人像是否被篡改的告警功能  - false：关闭身份证人像被篡改的告警功能 不支持精细化的P图 
        :type detect_tampering: bool
        :param detect_reproduce: 返回判断身份证图像是否经过翻拍告警的开关，可选值如下所示 - true:打开判断身份证图像是否经过翻拍告警的功能  - false:关闭判断身份证图像是否经过翻拍告警的功能 
        :type detect_reproduce: bool
        """
        
        

        self._image = None
        self._url = None
        self._return_portrait_image = None
        self._return_portrait_location = None
        self._return_idcard_type = None
        self._detect_border_integrity = None
        self._detect_blocking_within_border = None
        self._detect_blur = None
        self._detect_glare = None
        self._return_adjusted_image = None
        self._detect_tampering = None
        self._detect_reproduce = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image
        if return_portrait_location is not None:
            self.return_portrait_location = return_portrait_location
        if return_idcard_type is not None:
            self.return_idcard_type = return_idcard_type
        if detect_border_integrity is not None:
            self.detect_border_integrity = detect_border_integrity
        if detect_blocking_within_border is not None:
            self.detect_blocking_within_border = detect_blocking_within_border
        if detect_blur is not None:
            self.detect_blur = detect_blur
        if detect_glare is not None:
            self.detect_glare = detect_glare
        if return_adjusted_image is not None:
            self.return_adjusted_image = return_adjusted_image
        if detect_tampering is not None:
            self.detect_tampering = detect_tampering
        if detect_reproduce is not None:
            self.detect_reproduce = detect_reproduce

    @property
    def image(self):
        r"""Gets the image of this CambodianIdCardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 

        :return: The image of this CambodianIdCardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CambodianIdCardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 

        :param image: The image of this CambodianIdCardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this CambodianIdCardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this CambodianIdCardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CambodianIdCardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIF格式。 图片的url路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this CambodianIdCardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_portrait_image(self):
        r"""Gets the return_portrait_image of this CambodianIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 

        :return: The return_portrait_image of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        r"""Sets the return_portrait_image of this CambodianIdCardRequestBody.

        是否返回头像内容开关，可选值如下所示： - true: 返回身份证头像照片的 base64 编码 - false: 不返回身份证头像照片的 base64 编码 未传入该参数时默认为“false”，即不返回身份证头像照片的 base64 编码。 

        :param return_portrait_image: The return_portrait_image of this CambodianIdCardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

    @property
    def return_portrait_location(self):
        r"""Gets the return_portrait_location of this CambodianIdCardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true: 返回身份证头像的位置坐标 - false: 不返回身份证头像的位置坐标 未传入该参数时默认为“false”，即不返回身份证的头像坐标。 

        :return: The return_portrait_location of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_location

    @return_portrait_location.setter
    def return_portrait_location(self, return_portrait_location):
        r"""Sets the return_portrait_location of this CambodianIdCardRequestBody.

        是否返回头像坐标的开关，可选值如下所示： - true: 返回身份证头像的位置坐标 - false: 不返回身份证头像的位置坐标 未传入该参数时默认为“false”，即不返回身份证的头像坐标。 

        :param return_portrait_location: The return_portrait_location of this CambodianIdCardRequestBody.
        :type return_portrait_location: bool
        """
        self._return_portrait_location = return_portrait_location

    @property
    def return_idcard_type(self):
        r"""Gets the return_idcard_type of this CambodianIdCardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true:返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 

        :return: The return_idcard_type of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._return_idcard_type

    @return_idcard_type.setter
    def return_idcard_type(self, return_idcard_type):
        r"""Sets the return_idcard_type of this CambodianIdCardRequestBody.

        是否返回身份证类型的开关，可选值如下所示： - true:返回身份证的类型，类型包括身份证原件以及身份证复印件 - false：不返回身份证的类型 

        :param return_idcard_type: The return_idcard_type of this CambodianIdCardRequestBody.
        :type return_idcard_type: bool
        """
        self._return_idcard_type = return_idcard_type

    @property
    def detect_border_integrity(self):
        r"""Gets the detect_border_integrity of this CambodianIdCardRequestBody.

        返回身份证边框完整性的告警结果的开关，可选值如下所示 - true：打开身份证图像边框完整性告警功能  - false：关闭身份证图像边框完整性告警功能 

        :return: The detect_border_integrity of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_border_integrity

    @detect_border_integrity.setter
    def detect_border_integrity(self, detect_border_integrity):
        r"""Sets the detect_border_integrity of this CambodianIdCardRequestBody.

        返回身份证边框完整性的告警结果的开关，可选值如下所示 - true：打开身份证图像边框完整性告警功能  - false：关闭身份证图像边框完整性告警功能 

        :param detect_border_integrity: The detect_border_integrity of this CambodianIdCardRequestBody.
        :type detect_border_integrity: bool
        """
        self._detect_border_integrity = detect_border_integrity

    @property
    def detect_blocking_within_border(self):
        r"""Gets the detect_blocking_within_border of this CambodianIdCardRequestBody.

        返回身份证内部是否有被遮挡的告警结果的开关，可选值如下所示 - true：打开身份证内部是否有被遮挡的告警功能  - false：关闭身份证内部是否有被遮挡的告警功能 

        :return: The detect_blocking_within_border of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_blocking_within_border

    @detect_blocking_within_border.setter
    def detect_blocking_within_border(self, detect_blocking_within_border):
        r"""Sets the detect_blocking_within_border of this CambodianIdCardRequestBody.

        返回身份证内部是否有被遮挡的告警结果的开关，可选值如下所示 - true：打开身份证内部是否有被遮挡的告警功能  - false：关闭身份证内部是否有被遮挡的告警功能 

        :param detect_blocking_within_border: The detect_blocking_within_border of this CambodianIdCardRequestBody.
        :type detect_blocking_within_border: bool
        """
        self._detect_blocking_within_border = detect_blocking_within_border

    @property
    def detect_blur(self):
        r"""Gets the detect_blur of this CambodianIdCardRequestBody.

        返回身份证模糊告警结果的开关，可选值如下所示 - true:打开身份证是否模糊的告警功能 - false：关闭身份证是否模糊的告警功能 

        :return: The detect_blur of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_blur

    @detect_blur.setter
    def detect_blur(self, detect_blur):
        r"""Sets the detect_blur of this CambodianIdCardRequestBody.

        返回身份证模糊告警结果的开关，可选值如下所示 - true:打开身份证是否模糊的告警功能 - false：关闭身份证是否模糊的告警功能 

        :param detect_blur: The detect_blur of this CambodianIdCardRequestBody.
        :type detect_blur: bool
        """
        self._detect_blur = detect_blur

    @property
    def detect_glare(self):
        r"""Gets the detect_glare of this CambodianIdCardRequestBody.

        返回身份证是否反光的告警结果的开关，可选值如下所示 - true：打开身份证是否反光的告警功能  - false：关闭身份证是否反光的告警功能 

        :return: The detect_glare of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_glare

    @detect_glare.setter
    def detect_glare(self, detect_glare):
        r"""Sets the detect_glare of this CambodianIdCardRequestBody.

        返回身份证是否反光的告警结果的开关，可选值如下所示 - true：打开身份证是否反光的告警功能  - false：关闭身份证是否反光的告警功能 

        :param detect_glare: The detect_glare of this CambodianIdCardRequestBody.
        :type detect_glare: bool
        """
        self._detect_glare = detect_glare

    @property
    def return_adjusted_image(self):
        r"""Gets the return_adjusted_image of this CambodianIdCardRequestBody.

        返回身份证四点原图的base64编码 - true: 返回身份证原图的base64编码  - false：不返回身份证原图的base64编码 

        :return: The return_adjusted_image of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._return_adjusted_image

    @return_adjusted_image.setter
    def return_adjusted_image(self, return_adjusted_image):
        r"""Sets the return_adjusted_image of this CambodianIdCardRequestBody.

        返回身份证四点原图的base64编码 - true: 返回身份证原图的base64编码  - false：不返回身份证原图的base64编码 

        :param return_adjusted_image: The return_adjusted_image of this CambodianIdCardRequestBody.
        :type return_adjusted_image: bool
        """
        self._return_adjusted_image = return_adjusted_image

    @property
    def detect_tampering(self):
        r"""Gets the detect_tampering of this CambodianIdCardRequestBody.

        返回身份证人像是否被篡改的告警结果的开关，可选值如下所示 - true:  打开身份证人像是否被篡改的告警功能  - false：关闭身份证人像被篡改的告警功能 不支持精细化的P图 

        :return: The detect_tampering of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_tampering

    @detect_tampering.setter
    def detect_tampering(self, detect_tampering):
        r"""Sets the detect_tampering of this CambodianIdCardRequestBody.

        返回身份证人像是否被篡改的告警结果的开关，可选值如下所示 - true:  打开身份证人像是否被篡改的告警功能  - false：关闭身份证人像被篡改的告警功能 不支持精细化的P图 

        :param detect_tampering: The detect_tampering of this CambodianIdCardRequestBody.
        :type detect_tampering: bool
        """
        self._detect_tampering = detect_tampering

    @property
    def detect_reproduce(self):
        r"""Gets the detect_reproduce of this CambodianIdCardRequestBody.

        返回判断身份证图像是否经过翻拍告警的开关，可选值如下所示 - true:打开判断身份证图像是否经过翻拍告警的功能  - false:关闭判断身份证图像是否经过翻拍告警的功能 

        :return: The detect_reproduce of this CambodianIdCardRequestBody.
        :rtype: bool
        """
        return self._detect_reproduce

    @detect_reproduce.setter
    def detect_reproduce(self, detect_reproduce):
        r"""Sets the detect_reproduce of this CambodianIdCardRequestBody.

        返回判断身份证图像是否经过翻拍告警的开关，可选值如下所示 - true:打开判断身份证图像是否经过翻拍告警的功能  - false:关闭判断身份证图像是否经过翻拍告警的功能 

        :param detect_reproduce: The detect_reproduce of this CambodianIdCardRequestBody.
        :type detect_reproduce: bool
        """
        self._detect_reproduce = detect_reproduce

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
        if not isinstance(other, CambodianIdCardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
