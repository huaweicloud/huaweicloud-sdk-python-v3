# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageHighresolutionMattingInputData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'key': 'str'
    }

    attribute_map = {
        'url': 'url',
        'key': 'key'
    }

    def __init__(self, url=None, key=None):
        """ImageHighresolutionMattingInputData

        The model defined in huaweicloud sdk

        :param url: url输入源的地址，当输入为url类型时必填。 长度不超过1000。输入的图片大小不能大于20M，长边不能大于10000px。
        :type url: str
        :param key: 数据标识。多输入场景下必选，值由算法定义；单输入场景非必选。
        :type key: str
        """
        
        

        self._url = None
        self._key = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if key is not None:
            self.key = key

    @property
    def url(self):
        """Gets the url of this ImageHighresolutionMattingInputData.

        url输入源的地址，当输入为url类型时必填。 长度不超过1000。输入的图片大小不能大于20M，长边不能大于10000px。

        :return: The url of this ImageHighresolutionMattingInputData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageHighresolutionMattingInputData.

        url输入源的地址，当输入为url类型时必填。 长度不超过1000。输入的图片大小不能大于20M，长边不能大于10000px。

        :param url: The url of this ImageHighresolutionMattingInputData.
        :type url: str
        """
        self._url = url

    @property
    def key(self):
        """Gets the key of this ImageHighresolutionMattingInputData.

        数据标识。多输入场景下必选，值由算法定义；单输入场景非必选。

        :return: The key of this ImageHighresolutionMattingInputData.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ImageHighresolutionMattingInputData.

        数据标识。多输入场景下必选，值由算法定义；单输入场景非必选。

        :param key: The key of this ImageHighresolutionMattingInputData.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, ImageHighresolutionMattingInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
