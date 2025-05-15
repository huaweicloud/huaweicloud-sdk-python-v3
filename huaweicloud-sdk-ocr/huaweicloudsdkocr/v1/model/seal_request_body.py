# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SealRequestBody:

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
        'return_seal_image': 'bool',
        'return_erased_seal_image': 'bool',
        'pdf_page_number': 'int'
    }

    attribute_map = {
        'data': 'data',
        'url': 'url',
        'return_seal_image': 'return_seal_image',
        'return_erased_seal_image': 'return_erased_seal_image',
        'pdf_page_number': 'pdf_page_number'
    }

    def __init__(self, data=None, url=None, return_seal_image=None, return_erased_seal_image=None, pdf_page_number=None):
        r"""SealRequestBody

        The model defined in huaweicloud sdk

        :param data: 该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 
        :type data: str
        :param url: 与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_seal_image: 是否返回提取的印章base64编码图片，可选值如下所示： - true：返回提取的印章图片base64编码 - false：不返回提取的印章图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_seal_image: bool
        :param return_erased_seal_image: 是否返回印章擦除后的base64编码图片，可选值包括： - true：返回印章擦除后的图片base64编码 - false：不返回印章擦除后的图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 
        :type return_erased_seal_image: bool
        :param pdf_page_number: 指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 
        :type pdf_page_number: int
        """
        
        

        self._data = None
        self._url = None
        self._return_seal_image = None
        self._return_erased_seal_image = None
        self._pdf_page_number = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if url is not None:
            self.url = url
        if return_seal_image is not None:
            self.return_seal_image = return_seal_image
        if return_erased_seal_image is not None:
            self.return_erased_seal_image = return_erased_seal_image
        if pdf_page_number is not None:
            self.pdf_page_number = pdf_page_number

    @property
    def data(self):
        r"""Gets the data of this SealRequestBody.

        该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 

        :return: The data of this SealRequestBody.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this SealRequestBody.

        该参数与url二选一。  图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 

        :param data: The data of this SealRequestBody.
        :type data: str
        """
        self._data = data

    @property
    def url(self):
        r"""Gets the url of this SealRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this SealRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SealRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最短边不小于15px，最长边不超过8192px。支持JPEG、JPG、PNG、BMP、GIF、TIFF、WEBP、PCX、ICO、PSD、PDF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this SealRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_seal_image(self):
        r"""Gets the return_seal_image of this SealRequestBody.

        是否返回提取的印章base64编码图片，可选值如下所示： - true：返回提取的印章图片base64编码 - false：不返回提取的印章图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_seal_image of this SealRequestBody.
        :rtype: bool
        """
        return self._return_seal_image

    @return_seal_image.setter
    def return_seal_image(self, return_seal_image):
        r"""Sets the return_seal_image of this SealRequestBody.

        是否返回提取的印章base64编码图片，可选值如下所示： - true：返回提取的印章图片base64编码 - false：不返回提取的印章图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_seal_image: The return_seal_image of this SealRequestBody.
        :type return_seal_image: bool
        """
        self._return_seal_image = return_seal_image

    @property
    def return_erased_seal_image(self):
        r"""Gets the return_erased_seal_image of this SealRequestBody.

        是否返回印章擦除后的base64编码图片，可选值包括： - true：返回印章擦除后的图片base64编码 - false：不返回印章擦除后的图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :return: The return_erased_seal_image of this SealRequestBody.
        :rtype: bool
        """
        return self._return_erased_seal_image

    @return_erased_seal_image.setter
    def return_erased_seal_image(self, return_erased_seal_image):
        r"""Sets the return_erased_seal_image of this SealRequestBody.

        是否返回印章擦除后的base64编码图片，可选值包括： - true：返回印章擦除后的图片base64编码 - false：不返回印章擦除后的图片base64编码  如果无该参数，系统默认不返回印章擦除后的图片。如果输入参数不是Boolean类型，则会报非法参数错误。 

        :param return_erased_seal_image: The return_erased_seal_image of this SealRequestBody.
        :type return_erased_seal_image: bool
        """
        self._return_erased_seal_image = return_erased_seal_image

    @property
    def pdf_page_number(self):
        r"""Gets the pdf_page_number of this SealRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :return: The pdf_page_number of this SealRequestBody.
        :rtype: int
        """
        return self._pdf_page_number

    @pdf_page_number.setter
    def pdf_page_number(self, pdf_page_number):
        r"""Sets the pdf_page_number of this SealRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :param pdf_page_number: The pdf_page_number of this SealRequestBody.
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
        if not isinstance(other, SealRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
