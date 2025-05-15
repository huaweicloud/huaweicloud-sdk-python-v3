# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTextRequestBody:

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
        'detect_direction': 'bool',
        'quick_mode': 'bool',
        'character_mode': 'bool',
        'language': 'str',
        'single_orientation_mode': 'bool',
        'pdf_page_number': 'int'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'detect_direction': 'detect_direction',
        'quick_mode': 'quick_mode',
        'character_mode': 'character_mode',
        'language': 'language',
        'single_orientation_mode': 'single_orientation_mode',
        'pdf_page_number': 'pdf_page_number'
    }

    def __init__(self, image=None, url=None, detect_direction=None, quick_mode=None, character_mode=None, language=None, single_orientation_mode=None, pdf_page_number=None):
        r"""GeneralTextRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。  图片文件Base64编码字符串，[点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)](tag:hc)[点击[这里](https://support.huaweicloud.com/intl/zh-cn/ocr_faq/ocr_01_0032.html)](tag:hk)查看详细获取方式。     
        :type image: str
        :param url: 与image二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param detect_direction: 图片朝向检测开关，可选值包括： - true：打开检测图片朝向功能。 - false：关闭检测图片朝向功能。  &gt; 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 
        :type detect_direction: bool
        :param quick_mode: 快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括： - true：打开快速识别模式。 - false：关闭快速识别模式。  &gt; 说明： - 未传入该参数时默认为false，即关闭快速模式。 
        :type quick_mode: bool
        :param character_mode: 单字符模式开关。可选值包括： - true：打开单字符模式。 - false：关闭单字符模式。  未传入该参数时默认为false，即不返回单个文本行的单字符信息。 
        :type character_mode: bool
        :param language: 语种选择，取值范围可参考表1中英文列。未传入该参数时默认为中英文识别模式。 **表1* 语种选择说明 | 英文 |     中文     | | :--: | :----------: | | auto | 自动语种分类 | |  ms  |    马来语    | |  uk  |   乌克兰语   | |  hi  |    印地语    | |  ru  |     俄语     | |  vi  |    越南语    | |  id  |    印尼语    | |  th  |     泰语     | |  zh  |    中英文    | |  ar  |   阿拉伯语   | |  de  |     德语     | |  la  |    拉丁语    | |  fr  |     法语     | |  it  |   意大利语   | |  es  |   西班牙语   | |  pt  |   葡萄牙语   | |  ro  |  罗马尼亚语  | |  pl  |    波兰语    | |  am  |  阿姆哈拉语  | |  ja  |     日语     | |  ko  |     韩语     | |  tr  |   土耳其语   | |  no  |   挪威语     | |  da  |   丹麦语     | |  sv  |   瑞典语     | |  km  |   柬埔寨语   | |  he  |   希伯来语   | 
        :type language: str
        :param single_orientation_mode: 单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。 图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为false，即默认图片中的文字朝向为多朝向。 
        :type single_orientation_mode: bool
        :param pdf_page_number: 指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 
        :type pdf_page_number: int
        """
        
        

        self._image = None
        self._url = None
        self._detect_direction = None
        self._quick_mode = None
        self._character_mode = None
        self._language = None
        self._single_orientation_mode = None
        self._pdf_page_number = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if detect_direction is not None:
            self.detect_direction = detect_direction
        if quick_mode is not None:
            self.quick_mode = quick_mode
        if character_mode is not None:
            self.character_mode = character_mode
        if language is not None:
            self.language = language
        if single_orientation_mode is not None:
            self.single_orientation_mode = single_orientation_mode
        if pdf_page_number is not None:
            self.pdf_page_number = pdf_page_number

    @property
    def image(self):
        r"""Gets the image of this GeneralTextRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。  图片文件Base64编码字符串，[点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)](tag:hc)[点击[这里](https://support.huaweicloud.com/intl/zh-cn/ocr_faq/ocr_01_0032.html)](tag:hk)查看详细获取方式。     

        :return: The image of this GeneralTextRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this GeneralTextRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。  图片文件Base64编码字符串，[点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)](tag:hc)[点击[这里](https://support.huaweicloud.com/intl/zh-cn/ocr_faq/ocr_01_0032.html)](tag:hk)查看详细获取方式。     

        :param image: The image of this GeneralTextRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this GeneralTextRequestBody.

        与image二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this GeneralTextRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this GeneralTextRequestBody.

        与image二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过30000px。图片分辨率不能大于1.6亿px。 支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，[详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。](tag:hc)[详情参见[配置OBS访问权限](https://support.huaweicloud.com/intl/zh-cn/api-ocr/ocr_03_0132.html)。](tag:hk)  > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this GeneralTextRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def detect_direction(self):
        r"""Gets the detect_direction of this GeneralTextRequestBody.

        图片朝向检测开关，可选值包括： - true：打开检测图片朝向功能。 - false：关闭检测图片朝向功能。  > 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :return: The detect_direction of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        r"""Sets the detect_direction of this GeneralTextRequestBody.

        图片朝向检测开关，可选值包括： - true：打开检测图片朝向功能。 - false：关闭检测图片朝向功能。  > 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :param detect_direction: The detect_direction of this GeneralTextRequestBody.
        :type detect_direction: bool
        """
        self._detect_direction = detect_direction

    @property
    def quick_mode(self):
        r"""Gets the quick_mode of this GeneralTextRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括： - true：打开快速识别模式。 - false：关闭快速识别模式。  > 说明： - 未传入该参数时默认为false，即关闭快速模式。 

        :return: The quick_mode of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._quick_mode

    @quick_mode.setter
    def quick_mode(self, quick_mode):
        r"""Sets the quick_mode of this GeneralTextRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别。可选值包括： - true：打开快速识别模式。 - false：关闭快速识别模式。  > 说明： - 未传入该参数时默认为false，即关闭快速模式。 

        :param quick_mode: The quick_mode of this GeneralTextRequestBody.
        :type quick_mode: bool
        """
        self._quick_mode = quick_mode

    @property
    def character_mode(self):
        r"""Gets the character_mode of this GeneralTextRequestBody.

        单字符模式开关。可选值包括： - true：打开单字符模式。 - false：关闭单字符模式。  未传入该参数时默认为false，即不返回单个文本行的单字符信息。 

        :return: The character_mode of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._character_mode

    @character_mode.setter
    def character_mode(self, character_mode):
        r"""Sets the character_mode of this GeneralTextRequestBody.

        单字符模式开关。可选值包括： - true：打开单字符模式。 - false：关闭单字符模式。  未传入该参数时默认为false，即不返回单个文本行的单字符信息。 

        :param character_mode: The character_mode of this GeneralTextRequestBody.
        :type character_mode: bool
        """
        self._character_mode = character_mode

    @property
    def language(self):
        r"""Gets the language of this GeneralTextRequestBody.

        语种选择，取值范围可参考表1中英文列。未传入该参数时默认为中英文识别模式。 **表1* 语种选择说明 | 英文 |     中文     | | :--: | :----------: | | auto | 自动语种分类 | |  ms  |    马来语    | |  uk  |   乌克兰语   | |  hi  |    印地语    | |  ru  |     俄语     | |  vi  |    越南语    | |  id  |    印尼语    | |  th  |     泰语     | |  zh  |    中英文    | |  ar  |   阿拉伯语   | |  de  |     德语     | |  la  |    拉丁语    | |  fr  |     法语     | |  it  |   意大利语   | |  es  |   西班牙语   | |  pt  |   葡萄牙语   | |  ro  |  罗马尼亚语  | |  pl  |    波兰语    | |  am  |  阿姆哈拉语  | |  ja  |     日语     | |  ko  |     韩语     | |  tr  |   土耳其语   | |  no  |   挪威语     | |  da  |   丹麦语     | |  sv  |   瑞典语     | |  km  |   柬埔寨语   | |  he  |   希伯来语   | 

        :return: The language of this GeneralTextRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this GeneralTextRequestBody.

        语种选择，取值范围可参考表1中英文列。未传入该参数时默认为中英文识别模式。 **表1* 语种选择说明 | 英文 |     中文     | | :--: | :----------: | | auto | 自动语种分类 | |  ms  |    马来语    | |  uk  |   乌克兰语   | |  hi  |    印地语    | |  ru  |     俄语     | |  vi  |    越南语    | |  id  |    印尼语    | |  th  |     泰语     | |  zh  |    中英文    | |  ar  |   阿拉伯语   | |  de  |     德语     | |  la  |    拉丁语    | |  fr  |     法语     | |  it  |   意大利语   | |  es  |   西班牙语   | |  pt  |   葡萄牙语   | |  ro  |  罗马尼亚语  | |  pl  |    波兰语    | |  am  |  阿姆哈拉语  | |  ja  |     日语     | |  ko  |     韩语     | |  tr  |   土耳其语   | |  no  |   挪威语     | |  da  |   丹麦语     | |  sv  |   瑞典语     | |  km  |   柬埔寨语   | |  he  |   希伯来语   | 

        :param language: The language of this GeneralTextRequestBody.
        :type language: str
        """
        self._language = language

    @property
    def single_orientation_mode(self):
        r"""Gets the single_orientation_mode of this GeneralTextRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。 图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为false，即默认图片中的文字朝向为多朝向。 

        :return: The single_orientation_mode of this GeneralTextRequestBody.
        :rtype: bool
        """
        return self._single_orientation_mode

    @single_orientation_mode.setter
    def single_orientation_mode(self, single_orientation_mode):
        r"""Sets the single_orientation_mode of this GeneralTextRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。 图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为false，即默认图片中的文字朝向为多朝向。 

        :param single_orientation_mode: The single_orientation_mode of this GeneralTextRequestBody.
        :type single_orientation_mode: bool
        """
        self._single_orientation_mode = single_orientation_mode

    @property
    def pdf_page_number(self):
        r"""Gets the pdf_page_number of this GeneralTextRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :return: The pdf_page_number of this GeneralTextRequestBody.
        :rtype: int
        """
        return self._pdf_page_number

    @pdf_page_number.setter
    def pdf_page_number(self, pdf_page_number):
        r"""Sets the pdf_page_number of this GeneralTextRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :param pdf_page_number: The pdf_page_number of this GeneralTextRequestBody.
        :type pdf_page_number: int
        """
        self._pdf_page_number = pdf_page_number

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
        if not isinstance(other, GeneralTextRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
