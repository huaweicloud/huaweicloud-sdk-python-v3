# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandwritingRequestBody:

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
        'quick_mode': 'bool',
        'char_set': 'str',
        'detect_direction': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'quick_mode': 'quick_mode',
        'char_set': 'char_set',
        'detect_direction': 'detect_direction'
    }

    def __init__(self, image=None, url=None, quick_mode=None, char_set=None, detect_direction=None):
        r"""HandwritingRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param quick_mode: 快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别内容。可选值包括： - true：打开快速模式； - false：关闭快速模式。  &gt; 说明： - 未传入该参数时默认为false，即关闭快速模式 
        :type quick_mode: bool
        :param char_set: 字符集设置，用户可以根据实际需要限定输出字符集范围。可选值如下所示。  - \&quot;digit\&quot;: 数字模式；  - \&quot;letter\&quot;: 大小写字母模式；  - \&quot;digit_letter\&quot;: 数字+字母模式；  - \&quot;general\&quot;: 数字+字母+中文模式；  &gt; 说明： - 未传入该参数时，默认为“general”模式。 
        :type char_set: str
        :param detect_direction: 校正图片的倾斜角度开关，可选值如下所示。 - true：校正图片的倾斜角度； - false：不校正图片的倾斜角度。  &gt; 说明： - 支持任意角度的校正，未传入该参数时默认为“false”。 
        :type detect_direction: bool
        """
        
        

        self._image = None
        self._url = None
        self._quick_mode = None
        self._char_set = None
        self._detect_direction = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if quick_mode is not None:
            self.quick_mode = quick_mode
        if char_set is not None:
            self.char_set = char_set
        if detect_direction is not None:
            self.detect_direction = detect_direction

    @property
    def image(self):
        r"""Gets the image of this HandwritingRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this HandwritingRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this HandwritingRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this HandwritingRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this HandwritingRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this HandwritingRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this HandwritingRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于8px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this HandwritingRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def quick_mode(self):
        r"""Gets the quick_mode of this HandwritingRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别内容。可选值包括： - true：打开快速模式； - false：关闭快速模式。  > 说明： - 未传入该参数时默认为false，即关闭快速模式 

        :return: The quick_mode of this HandwritingRequestBody.
        :rtype: bool
        """
        return self._quick_mode

    @quick_mode.setter
    def quick_mode(self, quick_mode):
        r"""Sets the quick_mode of this HandwritingRequestBody.

        快速模式开关，针对单行文字图片（要求图片只包含一行文字，且文字区域占比超过50%），打开时可以更快返回识别内容。可选值包括： - true：打开快速模式； - false：关闭快速模式。  > 说明： - 未传入该参数时默认为false，即关闭快速模式 

        :param quick_mode: The quick_mode of this HandwritingRequestBody.
        :type quick_mode: bool
        """
        self._quick_mode = quick_mode

    @property
    def char_set(self):
        r"""Gets the char_set of this HandwritingRequestBody.

        字符集设置，用户可以根据实际需要限定输出字符集范围。可选值如下所示。  - \"digit\": 数字模式；  - \"letter\": 大小写字母模式；  - \"digit_letter\": 数字+字母模式；  - \"general\": 数字+字母+中文模式；  > 说明： - 未传入该参数时，默认为“general”模式。 

        :return: The char_set of this HandwritingRequestBody.
        :rtype: str
        """
        return self._char_set

    @char_set.setter
    def char_set(self, char_set):
        r"""Sets the char_set of this HandwritingRequestBody.

        字符集设置，用户可以根据实际需要限定输出字符集范围。可选值如下所示。  - \"digit\": 数字模式；  - \"letter\": 大小写字母模式；  - \"digit_letter\": 数字+字母模式；  - \"general\": 数字+字母+中文模式；  > 说明： - 未传入该参数时，默认为“general”模式。 

        :param char_set: The char_set of this HandwritingRequestBody.
        :type char_set: str
        """
        self._char_set = char_set

    @property
    def detect_direction(self):
        r"""Gets the detect_direction of this HandwritingRequestBody.

        校正图片的倾斜角度开关，可选值如下所示。 - true：校正图片的倾斜角度； - false：不校正图片的倾斜角度。  > 说明： - 支持任意角度的校正，未传入该参数时默认为“false”。 

        :return: The detect_direction of this HandwritingRequestBody.
        :rtype: bool
        """
        return self._detect_direction

    @detect_direction.setter
    def detect_direction(self, detect_direction):
        r"""Sets the detect_direction of this HandwritingRequestBody.

        校正图片的倾斜角度开关，可选值如下所示。 - true：校正图片的倾斜角度； - false：不校正图片的倾斜角度。  > 说明： - 支持任意角度的校正，未传入该参数时默认为“false”。 

        :param detect_direction: The detect_direction of this HandwritingRequestBody.
        :type detect_direction: bool
        """
        self._detect_direction = detect_direction

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
        if not isinstance(other, HandwritingRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
