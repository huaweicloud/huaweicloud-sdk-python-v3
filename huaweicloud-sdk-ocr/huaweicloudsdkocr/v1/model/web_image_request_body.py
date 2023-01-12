# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebImageRequestBody:

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
        'extract_type': 'list[str]',
        'detect_font': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'detect_direction': 'detect_direction',
        'extract_type': 'extract_type',
        'detect_font': 'detect_font'
    }

    def __init__(self, image=None, url=None, detect_direction=None, extract_type=None, detect_font=None):
        """WebImageRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过30000px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 
        :type url: str
        :param detect_direction: 图片朝向检测开关，可选值包括： - true：检测图片朝向; - false：不检测图片朝向。  &gt; 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 
        :type detect_direction: bool
        :param extract_type: 结构化数据提取参数列表，目前只支持联系人信息、图像宽高，其入参值分别为\&quot;contact_info\&quot;，\&quot;image_size\&quot;，若该字段为空列表或缺失该字段，默认不提取。 
        :type extract_type: list[str]
        :param detect_font: 为Boolean类型，若不传该字段，默认不检测切片字体，为True时，将检测切片的字体类型，并返回最相似的5种字体名称。 
        :type detect_font: bool
        """
        
        

        self._image = None
        self._url = None
        self._detect_direction = None
        self._extract_type = None
        self._detect_font = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if detect_direction is not None:
            self.detect_direction = detect_direction
        if extract_type is not None:
            self.extract_type = extract_type
        if detect_font is not None:
            self.detect_font = detect_font

    @property
    def image(self):
        """Gets the image of this WebImageRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过30000px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this WebImageRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this WebImageRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过30000px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this WebImageRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this WebImageRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :return: The url of this WebImageRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebImageRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 

        :param url: The url of this WebImageRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def detect_direction(self):
        """Gets the detect_direction of this WebImageRequestBody.

        图片朝向检测开关，可选值包括： - true：检测图片朝向; - false：不检测图片朝向。  > 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :return: The detect_direction of this WebImageRequestBody.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        """Sets the detect_direction of this WebImageRequestBody.

        图片朝向检测开关，可选值包括： - true：检测图片朝向; - false：不检测图片朝向。  > 说明： - 支持任意角度的图片朝向检测。未传入该参数时默认为false，即不检测图片朝向。 

        :param detect_direction: The detect_direction of this WebImageRequestBody.
        :type detect_direction: bool
        """
        self._detect_direction = detect_direction

    @property
    def extract_type(self):
        """Gets the extract_type of this WebImageRequestBody.

        结构化数据提取参数列表，目前只支持联系人信息、图像宽高，其入参值分别为\"contact_info\"，\"image_size\"，若该字段为空列表或缺失该字段，默认不提取。 

        :return: The extract_type of this WebImageRequestBody.
        :rtype: list[str]
        """
        return self._extract_type

    @extract_type.setter
    def extract_type(self, extract_type):
        """Sets the extract_type of this WebImageRequestBody.

        结构化数据提取参数列表，目前只支持联系人信息、图像宽高，其入参值分别为\"contact_info\"，\"image_size\"，若该字段为空列表或缺失该字段，默认不提取。 

        :param extract_type: The extract_type of this WebImageRequestBody.
        :type extract_type: list[str]
        """
        self._extract_type = extract_type

    @property
    def detect_font(self):
        """Gets the detect_font of this WebImageRequestBody.

        为Boolean类型，若不传该字段，默认不检测切片字体，为True时，将检测切片的字体类型，并返回最相似的5种字体名称。 

        :return: The detect_font of this WebImageRequestBody.
        :rtype: bool
        """
        return self._detect_font

    @detect_font.setter
    def detect_font(self, detect_font):
        """Sets the detect_font of this WebImageRequestBody.

        为Boolean类型，若不传该字段，默认不检测切片字体，为True时，将检测切片的字体类型，并返回最相似的5种字体名称。 

        :param detect_font: The detect_font of this WebImageRequestBody.
        :type detect_font: bool
        """
        self._detect_font = detect_font

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
        if not isinstance(other, WebImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
