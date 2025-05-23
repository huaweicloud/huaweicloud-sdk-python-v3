# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomTemplateRequestBody:

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
        'template_id': 'str',
        'classifier_id': 'str',
        'classifier_mode': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'template_id': 'template_id',
        'classifier_id': 'classifier_id',
        'classifier_mode': 'classifier_mode'
    }

    def __init__(self, image=None, url=None, template_id=None, classifier_id=None, classifier_mode=None):
        r"""CustomTemplateRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param template_id: 该参数与classifier_id二选一。 模板id，如果传入，启用单模板识别模式。 
        :type template_id: str
        :param classifier_id: 该参数与template_id二选一。 分类器id，如果传入，启用多模板识别模式。 
        :type classifier_id: str
        :param classifier_mode: 该参数与classifier_id参数配合使用，可选值如下所示： - true：仅返回模板分类结果 - false：正常返回多模板识别结果 &gt; 说明： - 如果未传入该参数时默认为false，即正常返回多模板识别结果。 
        :type classifier_mode: bool
        """
        
        

        self._image = None
        self._url = None
        self._template_id = None
        self._classifier_id = None
        self._classifier_mode = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if template_id is not None:
            self.template_id = template_id
        if classifier_id is not None:
            self.classifier_id = classifier_id
        if classifier_mode is not None:
            self.classifier_mode = classifier_mode

    @property
    def image(self):
        r"""Gets the image of this CustomTemplateRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this CustomTemplateRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CustomTemplateRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this CustomTemplateRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this CustomTemplateRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this CustomTemplateRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CustomTemplateRequestBody.

        与image二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、GIF、WEBP格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this CustomTemplateRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def template_id(self):
        r"""Gets the template_id of this CustomTemplateRequestBody.

        该参数与classifier_id二选一。 模板id，如果传入，启用单模板识别模式。 

        :return: The template_id of this CustomTemplateRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CustomTemplateRequestBody.

        该参数与classifier_id二选一。 模板id，如果传入，启用单模板识别模式。 

        :param template_id: The template_id of this CustomTemplateRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def classifier_id(self):
        r"""Gets the classifier_id of this CustomTemplateRequestBody.

        该参数与template_id二选一。 分类器id，如果传入，启用多模板识别模式。 

        :return: The classifier_id of this CustomTemplateRequestBody.
        :rtype: str
        """
        return self._classifier_id

    @classifier_id.setter
    def classifier_id(self, classifier_id):
        r"""Sets the classifier_id of this CustomTemplateRequestBody.

        该参数与template_id二选一。 分类器id，如果传入，启用多模板识别模式。 

        :param classifier_id: The classifier_id of this CustomTemplateRequestBody.
        :type classifier_id: str
        """
        self._classifier_id = classifier_id

    @property
    def classifier_mode(self):
        r"""Gets the classifier_mode of this CustomTemplateRequestBody.

        该参数与classifier_id参数配合使用，可选值如下所示： - true：仅返回模板分类结果 - false：正常返回多模板识别结果 > 说明： - 如果未传入该参数时默认为false，即正常返回多模板识别结果。 

        :return: The classifier_mode of this CustomTemplateRequestBody.
        :rtype: bool
        """
        return self._classifier_mode

    @classifier_mode.setter
    def classifier_mode(self, classifier_mode):
        r"""Sets the classifier_mode of this CustomTemplateRequestBody.

        该参数与classifier_id参数配合使用，可选值如下所示： - true：仅返回模板分类结果 - false：正常返回多模板识别结果 > 说明： - 如果未传入该参数时默认为false，即正常返回多模板识别结果。 

        :param classifier_mode: The classifier_mode of this CustomTemplateRequestBody.
        :type classifier_mode: bool
        """
        self._classifier_mode = classifier_mode

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
        if not isinstance(other, CustomTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
