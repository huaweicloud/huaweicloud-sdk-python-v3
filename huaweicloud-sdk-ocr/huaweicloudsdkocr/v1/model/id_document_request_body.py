# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdDocumentRequestBody:

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
        'country_region': 'list[str]',
        'id_type': 'list[str]',
        'return_portrait_image': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'country_region': 'country_region',
        'id_type': 'id_type',
        'return_portrait_image': 'return_portrait_image'
    }

    def __init__(self, image=None, url=None, country_region=None, id_type=None, return_portrait_image=None):
        """IdDocumentRequestBody

        The model defined in huaweicloud sdk

        :param image: 该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF。
        :type image: str
        :param url: 该参数与image二选一。图片的url路径，目前支持： Image URL. Currently, the following URLs are supported: - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。 &gt; 说明: - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param country_region: 证件签发国家或地区代码，命名遵循ISO-3166 3位代码。可选值。支持填写1个或多个国家/地区。指定参数后，服务只识别指定国家/地区的卡证，如留空，则识别所有地区卡证。建议国家/地区固定或有限范围的情况下填写。支持国家/地区列表见表1国家/地区和证件列表。 
        :type country_region: list[str]
        :param id_type: 证件类型。可选值。支持填写1种或多种证件。指定参数后，服务只识别指定类型的卡证，如留空，默认识别所有类型卡证，建议已知证件类型的情况下填写。支持证件类型如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 
        :type id_type: list[str]
        :param return_portrait_image: 控制是否返回portrait_image（证件中的人像图片），True代表需要返回，False代表不需要。 
        :type return_portrait_image: bool
        """
        
        

        self._image = None
        self._url = None
        self._country_region = None
        self._id_type = None
        self._return_portrait_image = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if country_region is not None:
            self.country_region = country_region
        if id_type is not None:
            self.id_type = id_type
        if return_portrait_image is not None:
            self.return_portrait_image = return_portrait_image

    @property
    def image(self):
        """Gets the image of this IdDocumentRequestBody.

        该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF。

        :return: The image of this IdDocumentRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IdDocumentRequestBody.

        该参数与url二选一。图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于100px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF。

        :param image: The image of this IdDocumentRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this IdDocumentRequestBody.

        该参数与image二选一。图片的url路径，目前支持： Image URL. Currently, the following URLs are supported: - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。 > 说明: - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this IdDocumentRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IdDocumentRequestBody.

        该参数与image二选一。图片的url路径，目前支持： Image URL. Currently, the following URLs are supported: - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。 > 说明: - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this IdDocumentRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def country_region(self):
        """Gets the country_region of this IdDocumentRequestBody.

        证件签发国家或地区代码，命名遵循ISO-3166 3位代码。可选值。支持填写1个或多个国家/地区。指定参数后，服务只识别指定国家/地区的卡证，如留空，则识别所有地区卡证。建议国家/地区固定或有限范围的情况下填写。支持国家/地区列表见表1国家/地区和证件列表。 

        :return: The country_region of this IdDocumentRequestBody.
        :rtype: list[str]
        """
        return self._country_region

    @country_region.setter
    def country_region(self, country_region):
        """Sets the country_region of this IdDocumentRequestBody.

        证件签发国家或地区代码，命名遵循ISO-3166 3位代码。可选值。支持填写1个或多个国家/地区。指定参数后，服务只识别指定国家/地区的卡证，如留空，则识别所有地区卡证。建议国家/地区固定或有限范围的情况下填写。支持国家/地区列表见表1国家/地区和证件列表。 

        :param country_region: The country_region of this IdDocumentRequestBody.
        :type country_region: list[str]
        """
        self._country_region = country_region

    @property
    def id_type(self):
        """Gets the id_type of this IdDocumentRequestBody.

        证件类型。可选值。支持填写1种或多种证件。指定参数后，服务只识别指定类型的卡证，如留空，默认识别所有类型卡证，建议已知证件类型的情况下填写。支持证件类型如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 

        :return: The id_type of this IdDocumentRequestBody.
        :rtype: list[str]
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this IdDocumentRequestBody.

        证件类型。可选值。支持填写1种或多种证件。指定参数后，服务只识别指定类型的卡证，如留空，默认识别所有类型卡证，建议已知证件类型的情况下填写。支持证件类型如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 

        :param id_type: The id_type of this IdDocumentRequestBody.
        :type id_type: list[str]
        """
        self._id_type = id_type

    @property
    def return_portrait_image(self):
        """Gets the return_portrait_image of this IdDocumentRequestBody.

        控制是否返回portrait_image（证件中的人像图片），True代表需要返回，False代表不需要。 

        :return: The return_portrait_image of this IdDocumentRequestBody.
        :rtype: bool
        """
        return self._return_portrait_image

    @return_portrait_image.setter
    def return_portrait_image(self, return_portrait_image):
        """Sets the return_portrait_image of this IdDocumentRequestBody.

        控制是否返回portrait_image（证件中的人像图片），True代表需要返回，False代表不需要。 

        :param return_portrait_image: The return_portrait_image of this IdDocumentRequestBody.
        :type return_portrait_image: bool
        """
        self._return_portrait_image = return_portrait_image

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
        if not isinstance(other, IdDocumentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
