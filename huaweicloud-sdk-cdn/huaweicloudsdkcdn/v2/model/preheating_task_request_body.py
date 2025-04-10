# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreheatingTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zh_url_encode': 'bool',
        'urls': 'list[str]'
    }

    attribute_map = {
        'zh_url_encode': 'zh_url_encode',
        'urls': 'urls'
    }

    def __init__(self, zh_url_encode=None, urls=None):
        r"""PreheatingTaskRequestBody

        The model defined in huaweicloud sdk

        :param zh_url_encode: 是否对url中的中文字符进行编码后预热，false代表不开启，true代表开启，开启后仅预热转码后的URL。
        :type zh_url_encode: bool
        :param urls: 需要预热的URL必须带有“http://”或“https://”，多个URL用逗号分隔（\&quot;url1\&quot;, \&quot;url2\&quot;），目前不支持对目录的预热，单个url的长度限制为4096字符,单次最多输入1000个url。
        :type urls: list[str]
        """
        
        

        self._zh_url_encode = None
        self._urls = None
        self.discriminator = None

        if zh_url_encode is not None:
            self.zh_url_encode = zh_url_encode
        self.urls = urls

    @property
    def zh_url_encode(self):
        r"""Gets the zh_url_encode of this PreheatingTaskRequestBody.

        是否对url中的中文字符进行编码后预热，false代表不开启，true代表开启，开启后仅预热转码后的URL。

        :return: The zh_url_encode of this PreheatingTaskRequestBody.
        :rtype: bool
        """
        return self._zh_url_encode

    @zh_url_encode.setter
    def zh_url_encode(self, zh_url_encode):
        r"""Sets the zh_url_encode of this PreheatingTaskRequestBody.

        是否对url中的中文字符进行编码后预热，false代表不开启，true代表开启，开启后仅预热转码后的URL。

        :param zh_url_encode: The zh_url_encode of this PreheatingTaskRequestBody.
        :type zh_url_encode: bool
        """
        self._zh_url_encode = zh_url_encode

    @property
    def urls(self):
        r"""Gets the urls of this PreheatingTaskRequestBody.

        需要预热的URL必须带有“http://”或“https://”，多个URL用逗号分隔（\"url1\", \"url2\"），目前不支持对目录的预热，单个url的长度限制为4096字符,单次最多输入1000个url。

        :return: The urls of this PreheatingTaskRequestBody.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this PreheatingTaskRequestBody.

        需要预热的URL必须带有“http://”或“https://”，多个URL用逗号分隔（\"url1\", \"url2\"），目前不支持对目录的预热，单个url的长度限制为4096字符,单次最多输入1000个url。

        :param urls: The urls of this PreheatingTaskRequestBody.
        :type urls: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, PreheatingTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
