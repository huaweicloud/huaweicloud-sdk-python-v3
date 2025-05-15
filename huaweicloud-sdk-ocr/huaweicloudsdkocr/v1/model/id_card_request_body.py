# coding: utf-8

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
        'detect_copy': 'bool',
        'return_portrait_location': 'bool',
        'return_portrait_image': 'bool',
        'return_adjusted_image': 'bool',
        'detect_tampering': 'bool',
        'detect_border_integrity': 'bool',
        'detect_blocking_within_border': 'bool',
        'detect_blur': 'bool',
        'detect_interim': 'bool',
        'detect_glare': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'side': 'side',
        'return_verification': 'return_verification',
        'return_text_location': 'return_text_location',
        'detect_reproduce': 'detect_reproduce',
        'detect_copy': 'detect_copy',
        'return_portrait_location': 'return_portrait_location',
        'return_portrait_image': 'return_portrait_image',
        'return_adjusted_image': 'return_adjusted_image',
        'detect_tampering': 'detect_tampering',
        'detect_border_integrity': 'detect_border_integrity',
        'detect_blocking_within_border': 'detect_blocking_within_border',
        'detect_blur': 'detect_blur',
        'detect_interim': 'detect_interim',
        'detect_glare': 'detect_glare'
    }

    def __init__(self, image=None, url=None, side=None, return_verification=None, return_text_location=None, detect_reproduce=None, detect_copy=None, return_portrait_location=None, return_portrait_image=None, return_adjusted_image=None, detect_tampering=None, detect_border_integrity=None, detect_blocking_within_border=None, detect_blur=None, detect_interim=None, detect_glare=None):
        r"""IdCardRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param side:  - front：身份证人像面。 - back：身份证国徽面。 - double_side：身份证双面信息 &gt; 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 
        :type side: str
        :param return_verification: 返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 
        :type return_verification: bool
        :param return_text_location: 识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_text_location: bool
        :param detect_reproduce: 返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否经过翻拍功能  - false：关闭判断身份证图像是否经过翻拍功能 
        :type detect_reproduce: bool
        :param detect_copy: 返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否是复印件功能  - false : 关闭身份证图像是否是复印件功能 
        :type detect_copy: bool
        :param return_portrait_location: 返回头像位置信息的开关，默认false，可选值如下所示：  - true ：开启返回头像位置信息的功能 - false : 关闭返回头像位置信息的功能 
        :type return_portrait_location: bool
        :param return_portrait_image: 返回头像图片信息（base64码）的开关，默认false，可选值如下所示：  - true ：开启头像图片信息（base64码）的功能 - false : 关闭头像图片信息（base64码）的功能 
        :type return_portrait_image: bool
        :param return_adjusted_image: 返回身份证卡面（base64码）的开关，默认false，可选值如下所示：  - true ：开启身份证卡面（base64码）的功能 - false : 关闭身份证卡面（base64码）的功能 
        :type return_adjusted_image: bool
        :param detect_tampering: 身份证图像PS告警功能开关，默认false，可选值如下：  - true ：开启身份证图像PS告警功能 - false : 关闭身份证图像告警功能 
        :type detect_tampering: bool
        :param detect_border_integrity: 身份证图像边框完整性告警功能开关，默认false，可选值如下：  - true ：打开身份证图像边框完整性告警功能 - false : 关闭身份证图像边框完整性告警功能 
        :type detect_border_integrity: bool
        :param detect_blocking_within_border: 身份证图像边框内部是否有异物遮挡的告警功能开关，默认false，可选值如下：  - true ：开启身份证边框内部异物遮挡告警功能 - false : 关闭身份证边框内部异物遮挡告警功能 
        :type detect_blocking_within_border: bool
        :param detect_blur: 身份证图像模糊告警功能的开关，默认false，可选值如下：  - true ：开启身份证图像模糊告警功能 - false : 关闭身份证图像模糊告警功能 
        :type detect_blur: bool
        :param detect_interim: 临时身份证告警功能开关，默认false，可选值如下：  - true ：开启临时身份证告警功能 - false : 关闭临时身份证告警功能 
        :type detect_interim: bool
        :param detect_glare: 身份证反光告警功能开关，默认false，可选值如下：  - true ：开启身份证反光告警功能  - false : 关闭身份证反光告警功能 
        :type detect_glare: bool
        """
        
        

        self._image = None
        self._url = None
        self._side = None
        self._return_verification = None
        self._return_text_location = None
        self._detect_reproduce = None
        self._detect_copy = None
        self._return_portrait_location = None
        self._return_portrait_image = None
        self._return_adjusted_image = None
        self._detect_tampering = None
        self._detect_border_integrity = None
        self._detect_blocking_within_border = None
        self._detect_blur = None
        self._detect_interim = None
        self._detect_glare = None
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
        if return_portrait_location is not None:
            self.return_portrait_location = return_portrait_location
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image
        if return_adjusted_image is not None:
            self.return_adjusted_image = return_adjusted_image
        if detect_tampering is not None:
            self.detect_tampering = detect_tampering
        if detect_border_integrity is not None:
            self.detect_border_integrity = detect_border_integrity
        if detect_blocking_within_border is not None:
            self.detect_blocking_within_border = detect_blocking_within_border
        if detect_blur is not None:
            self.detect_blur = detect_blur
        if detect_interim is not None:
            self.detect_interim = detect_interim
        if detect_glare is not None:
            self.detect_glare = detect_glare

    @property
    def image(self):
        r"""Gets the image of this IdCardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this IdCardRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this IdCardRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this IdCardRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this IdCardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this IdCardRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this IdCardRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this IdCardRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def side(self):
        r"""Gets the side of this IdCardRequestBody.

         - front：身份证人像面。 - back：身份证国徽面。 - double_side：身份证双面信息 > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :return: The side of this IdCardRequestBody.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        r"""Sets the side of this IdCardRequestBody.

         - front：身份证人像面。 - back：身份证国徽面。 - double_side：身份证双面信息 > 说明： 如果参数值为空或无该参数，系统自动识别，建议填写，准确率更高。 

        :param side: The side of this IdCardRequestBody.
        :type side: str
        """
        self._side = side

    @property
    def return_verification(self):
        r"""Gets the return_verification of this IdCardRequestBody.

        返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 

        :return: The return_verification of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_verification

    @return_verification.setter
    def return_verification(self, return_verification):
        r"""Sets the return_verification of this IdCardRequestBody.

        返回校验身份证号等信息的开关，默认false，可选值如下所示：  - true：返回校验信息  - false：不返回校验信息 

        :param return_verification: The return_verification of this IdCardRequestBody.
        :type return_verification: bool
        """
        self._return_verification = return_verification

    @property
    def return_text_location(self):
        r"""Gets the return_text_location of this IdCardRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_text_location of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        r"""Sets the return_text_location of this IdCardRequestBody.

        识别到的文字块的区域位置信息。可选值包括：  - true：返回各个文字块区域  - false：不返回各个文字块区域  如果无该参数，系统默认不返回文字块区域。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_text_location: The return_text_location of this IdCardRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

    @property
    def detect_reproduce(self):
        r"""Gets the detect_reproduce of this IdCardRequestBody.

        返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否经过翻拍功能  - false：关闭判断身份证图像是否经过翻拍功能 

        :return: The detect_reproduce of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_reproduce

    @detect_reproduce.setter
    def detect_reproduce(self, detect_reproduce):
        r"""Sets the detect_reproduce of this IdCardRequestBody.

        返回判断身份证图像是否经过翻拍的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否经过翻拍功能  - false：关闭判断身份证图像是否经过翻拍功能 

        :param detect_reproduce: The detect_reproduce of this IdCardRequestBody.
        :type detect_reproduce: bool
        """
        self._detect_reproduce = detect_reproduce

    @property
    def detect_copy(self):
        r"""Gets the detect_copy of this IdCardRequestBody.

        返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否是复印件功能  - false : 关闭身份证图像是否是复印件功能 

        :return: The detect_copy of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_copy

    @detect_copy.setter
    def detect_copy(self, detect_copy):
        r"""Sets the detect_copy of this IdCardRequestBody.

        返回判断身份证图像是否是黑白复印件的开关，默认false，可选值如下所示：  - true ：开启判断身份证图像是否是复印件功能  - false : 关闭身份证图像是否是复印件功能 

        :param detect_copy: The detect_copy of this IdCardRequestBody.
        :type detect_copy: bool
        """
        self._detect_copy = detect_copy

    @property
    def return_portrait_location(self):
        r"""Gets the return_portrait_location of this IdCardRequestBody.

        返回头像位置信息的开关，默认false，可选值如下所示：  - true ：开启返回头像位置信息的功能 - false : 关闭返回头像位置信息的功能 

        :return: The return_portrait_location of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_location

    @return_portrait_location.setter
    def return_portrait_location(self, return_portrait_location):
        r"""Sets the return_portrait_location of this IdCardRequestBody.

        返回头像位置信息的开关，默认false，可选值如下所示：  - true ：开启返回头像位置信息的功能 - false : 关闭返回头像位置信息的功能 

        :param return_portrait_location: The return_portrait_location of this IdCardRequestBody.
        :type return_portrait_location: bool
        """
        self._return_portrait_location = return_portrait_location

    @property
    def return_portrait_image(self):
        r"""Gets the return_portrait_image of this IdCardRequestBody.

        返回头像图片信息（base64码）的开关，默认false，可选值如下所示：  - true ：开启头像图片信息（base64码）的功能 - false : 关闭头像图片信息（base64码）的功能 

        :return: The return_portrait_image of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        r"""Sets the return_portrait_image of this IdCardRequestBody.

        返回头像图片信息（base64码）的开关，默认false，可选值如下所示：  - true ：开启头像图片信息（base64码）的功能 - false : 关闭头像图片信息（base64码）的功能 

        :param return_portrait_image: The return_portrait_image of this IdCardRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

    @property
    def return_adjusted_image(self):
        r"""Gets the return_adjusted_image of this IdCardRequestBody.

        返回身份证卡面（base64码）的开关，默认false，可选值如下所示：  - true ：开启身份证卡面（base64码）的功能 - false : 关闭身份证卡面（base64码）的功能 

        :return: The return_adjusted_image of this IdCardRequestBody.
        :rtype: bool
        """
        return self._return_adjusted_image

    @return_adjusted_image.setter
    def return_adjusted_image(self, return_adjusted_image):
        r"""Sets the return_adjusted_image of this IdCardRequestBody.

        返回身份证卡面（base64码）的开关，默认false，可选值如下所示：  - true ：开启身份证卡面（base64码）的功能 - false : 关闭身份证卡面（base64码）的功能 

        :param return_adjusted_image: The return_adjusted_image of this IdCardRequestBody.
        :type return_adjusted_image: bool
        """
        self._return_adjusted_image = return_adjusted_image

    @property
    def detect_tampering(self):
        r"""Gets the detect_tampering of this IdCardRequestBody.

        身份证图像PS告警功能开关，默认false，可选值如下：  - true ：开启身份证图像PS告警功能 - false : 关闭身份证图像告警功能 

        :return: The detect_tampering of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_tampering

    @detect_tampering.setter
    def detect_tampering(self, detect_tampering):
        r"""Sets the detect_tampering of this IdCardRequestBody.

        身份证图像PS告警功能开关，默认false，可选值如下：  - true ：开启身份证图像PS告警功能 - false : 关闭身份证图像告警功能 

        :param detect_tampering: The detect_tampering of this IdCardRequestBody.
        :type detect_tampering: bool
        """
        self._detect_tampering = detect_tampering

    @property
    def detect_border_integrity(self):
        r"""Gets the detect_border_integrity of this IdCardRequestBody.

        身份证图像边框完整性告警功能开关，默认false，可选值如下：  - true ：打开身份证图像边框完整性告警功能 - false : 关闭身份证图像边框完整性告警功能 

        :return: The detect_border_integrity of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_border_integrity

    @detect_border_integrity.setter
    def detect_border_integrity(self, detect_border_integrity):
        r"""Sets the detect_border_integrity of this IdCardRequestBody.

        身份证图像边框完整性告警功能开关，默认false，可选值如下：  - true ：打开身份证图像边框完整性告警功能 - false : 关闭身份证图像边框完整性告警功能 

        :param detect_border_integrity: The detect_border_integrity of this IdCardRequestBody.
        :type detect_border_integrity: bool
        """
        self._detect_border_integrity = detect_border_integrity

    @property
    def detect_blocking_within_border(self):
        r"""Gets the detect_blocking_within_border of this IdCardRequestBody.

        身份证图像边框内部是否有异物遮挡的告警功能开关，默认false，可选值如下：  - true ：开启身份证边框内部异物遮挡告警功能 - false : 关闭身份证边框内部异物遮挡告警功能 

        :return: The detect_blocking_within_border of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_blocking_within_border

    @detect_blocking_within_border.setter
    def detect_blocking_within_border(self, detect_blocking_within_border):
        r"""Sets the detect_blocking_within_border of this IdCardRequestBody.

        身份证图像边框内部是否有异物遮挡的告警功能开关，默认false，可选值如下：  - true ：开启身份证边框内部异物遮挡告警功能 - false : 关闭身份证边框内部异物遮挡告警功能 

        :param detect_blocking_within_border: The detect_blocking_within_border of this IdCardRequestBody.
        :type detect_blocking_within_border: bool
        """
        self._detect_blocking_within_border = detect_blocking_within_border

    @property
    def detect_blur(self):
        r"""Gets the detect_blur of this IdCardRequestBody.

        身份证图像模糊告警功能的开关，默认false，可选值如下：  - true ：开启身份证图像模糊告警功能 - false : 关闭身份证图像模糊告警功能 

        :return: The detect_blur of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_blur

    @detect_blur.setter
    def detect_blur(self, detect_blur):
        r"""Sets the detect_blur of this IdCardRequestBody.

        身份证图像模糊告警功能的开关，默认false，可选值如下：  - true ：开启身份证图像模糊告警功能 - false : 关闭身份证图像模糊告警功能 

        :param detect_blur: The detect_blur of this IdCardRequestBody.
        :type detect_blur: bool
        """
        self._detect_blur = detect_blur

    @property
    def detect_interim(self):
        r"""Gets the detect_interim of this IdCardRequestBody.

        临时身份证告警功能开关，默认false，可选值如下：  - true ：开启临时身份证告警功能 - false : 关闭临时身份证告警功能 

        :return: The detect_interim of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_interim

    @detect_interim.setter
    def detect_interim(self, detect_interim):
        r"""Sets the detect_interim of this IdCardRequestBody.

        临时身份证告警功能开关，默认false，可选值如下：  - true ：开启临时身份证告警功能 - false : 关闭临时身份证告警功能 

        :param detect_interim: The detect_interim of this IdCardRequestBody.
        :type detect_interim: bool
        """
        self._detect_interim = detect_interim

    @property
    def detect_glare(self):
        r"""Gets the detect_glare of this IdCardRequestBody.

        身份证反光告警功能开关，默认false，可选值如下：  - true ：开启身份证反光告警功能  - false : 关闭身份证反光告警功能 

        :return: The detect_glare of this IdCardRequestBody.
        :rtype: bool
        """
        return self._detect_glare

    @detect_glare.setter
    def detect_glare(self, detect_glare):
        r"""Sets the detect_glare of this IdCardRequestBody.

        身份证反光告警功能开关，默认false，可选值如下：  - true ：开启身份证反光告警功能  - false : 关闭身份证反光告警功能 

        :param detect_glare: The detect_glare of this IdCardRequestBody.
        :type detect_glare: bool
        """
        self._detect_glare = detect_glare

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
