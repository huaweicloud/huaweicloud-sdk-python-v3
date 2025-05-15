# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoIdDocClassificationRequestBody:

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
        'alarm': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'url': 'url',
        'alarm': 'alarm'
    }

    def __init__(self, data=None, url=None, alarm=None):
        r"""AutoIdDocClassificationRequestBody

        The model defined in huaweicloud sdk

        :param data: 该参数与url二选一。  图片的Base64编码，单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议图片大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 
        :type data: str
        :param url: 与data二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param alarm: 证件告警检测功能的开关，默认false，取值范围如下：  - true：开启证件图像告警功能。 - false：关闭证件图像告警功能。 
        :type alarm: bool
        """
        
        

        self._data = None
        self._url = None
        self._alarm = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if url is not None:
            self.url = url
        if alarm is not None:
            self.alarm = alarm

    @property
    def data(self):
        r"""Gets the data of this AutoIdDocClassificationRequestBody.

        该参数与url二选一。  图片的Base64编码，单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议图片大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 

        :return: The data of this AutoIdDocClassificationRequestBody.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this AutoIdDocClassificationRequestBody.

        该参数与url二选一。  图片的Base64编码，单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议图片大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片Base64编码示例如/9j/4AAQSkZJRgABAg...，带有多余前缀会产生The image format is not supported报错。 

        :param data: The data of this AutoIdDocClassificationRequestBody.
        :type data: str
        """
        self._data = data

    @property
    def url(self):
        r"""Gets the url of this AutoIdDocClassificationRequestBody.

        与data二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this AutoIdDocClassificationRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AutoIdDocClassificationRequestBody.

        与data二选一。  单个图片其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片尺寸不小于15px，最长边不超过8192px，支持JPEG/JPG/PNG/BMP/TIFF格式。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this AutoIdDocClassificationRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def alarm(self):
        r"""Gets the alarm of this AutoIdDocClassificationRequestBody.

        证件告警检测功能的开关，默认false，取值范围如下：  - true：开启证件图像告警功能。 - false：关闭证件图像告警功能。 

        :return: The alarm of this AutoIdDocClassificationRequestBody.
        :rtype: bool
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        r"""Sets the alarm of this AutoIdDocClassificationRequestBody.

        证件告警检测功能的开关，默认false，取值范围如下：  - true：开启证件图像告警功能。 - false：关闭证件图像告警功能。 

        :param alarm: The alarm of this AutoIdDocClassificationRequestBody.
        :type alarm: bool
        """
        self._alarm = alarm

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
        if not isinstance(other, AutoIdDocClassificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
