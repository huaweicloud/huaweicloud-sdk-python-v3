# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BankReceiptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'url': 'str',
        'page_num': 'int',
        'single_orientation_mode': 'bool',
        'erase_seal': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'url': 'url',
        'page_num': 'page_num',
        'single_orientation_mode': 'single_orientation_mode',
        'erase_seal': 'erase_seal'
    }

    def __init__(self, data=None, url=None, page_num=None, single_orientation_mode=None, erase_seal=None):
        r"""BankReceiptRequestBody

        The model defined in huaweicloud sdk

        :param data: 该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 PDF以200dpi的分辨率转为图像进行识别，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 
        :type data: str
        :param url: 与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param page_num: 指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页，该参数仅在文件为PDF格式时有效。 
        :type page_num: int
        :param single_orientation_mode: 单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\&quot;true\&quot;，既默认图片中的文字方向为单朝向。 
        :type single_orientation_mode: bool
        :param erase_seal: 是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 
        :type erase_seal: bool
        """
        
        

        self._data = None
        self._url = None
        self._page_num = None
        self._single_orientation_mode = None
        self._erase_seal = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if url is not None:
            self.url = url
        if page_num is not None:
            self.page_num = page_num
        if single_orientation_mode is not None:
            self.single_orientation_mode = single_orientation_mode
        if erase_seal is not None:
            self.erase_seal = erase_seal

    @property
    def data(self):
        r"""Gets the data of this BankReceiptRequestBody.

        该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 PDF以200dpi的分辨率转为图像进行识别，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 

        :return: The data of this BankReceiptRequestBody.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this BankReceiptRequestBody.

        该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 PDF以200dpi的分辨率转为图像进行识别，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 

        :param data: The data of this BankReceiptRequestBody.
        :type data: str
        """
        self._data = data

    @property
    def url(self):
        r"""Gets the url of this BankReceiptRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this BankReceiptRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this BankReceiptRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过8192像素，支持JPG/PNG/BMP/TIFF/PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this BankReceiptRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def page_num(self):
        r"""Gets the page_num of this BankReceiptRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页，该参数仅在文件为PDF格式时有效。 

        :return: The page_num of this BankReceiptRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this BankReceiptRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页，该参数仅在文件为PDF格式时有效。 

        :param page_num: The page_num of this BankReceiptRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def single_orientation_mode(self):
        r"""Gets the single_orientation_mode of this BankReceiptRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\"true\"，既默认图片中的文字方向为单朝向。 

        :return: The single_orientation_mode of this BankReceiptRequestBody.
        :rtype: bool
        """
        return self._single_orientation_mode

    @single_orientation_mode.setter
    def single_orientation_mode(self, single_orientation_mode):
        r"""Sets the single_orientation_mode of this BankReceiptRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\"true\"，既默认图片中的文字方向为单朝向。 

        :param single_orientation_mode: The single_orientation_mode of this BankReceiptRequestBody.
        :type single_orientation_mode: bool
        """
        self._single_orientation_mode = single_orientation_mode

    @property
    def erase_seal(self):
        r"""Gets the erase_seal of this BankReceiptRequestBody.

        是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 

        :return: The erase_seal of this BankReceiptRequestBody.
        :rtype: bool
        """
        return self._erase_seal

    @erase_seal.setter
    def erase_seal(self, erase_seal):
        r"""Sets the erase_seal of this BankReceiptRequestBody.

        是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 

        :param erase_seal: The erase_seal of this BankReceiptRequestBody.
        :type erase_seal: bool
        """
        self._erase_seal = erase_seal

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
        if not isinstance(other, BankReceiptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
