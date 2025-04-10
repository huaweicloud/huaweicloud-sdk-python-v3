# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBatchSyncReqUrls:

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
        'data_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'data_id': 'data_id'
    }

    def __init__(self, url=None, data_id=None):
        r"""ImageBatchSyncReqUrls

        The model defined in huaweicloud sdk

        :param url: 图片url，目前支持：公网HTTP/HTTPS URL。
        :type url: str
        :param data_id: 图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。
        :type data_id: str
        """
        
        

        self._url = None
        self._data_id = None
        self.discriminator = None

        self.url = url
        self.data_id = data_id

    @property
    def url(self):
        r"""Gets the url of this ImageBatchSyncReqUrls.

        图片url，目前支持：公网HTTP/HTTPS URL。

        :return: The url of this ImageBatchSyncReqUrls.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageBatchSyncReqUrls.

        图片url，目前支持：公网HTTP/HTTPS URL。

        :param url: The url of this ImageBatchSyncReqUrls.
        :type url: str
        """
        self._url = url

    @property
    def data_id(self):
        r"""Gets the data_id of this ImageBatchSyncReqUrls.

        图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。

        :return: The data_id of this ImageBatchSyncReqUrls.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        r"""Sets the data_id of this ImageBatchSyncReqUrls.

        图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。

        :param data_id: The data_id of this ImageBatchSyncReqUrls.
        :type data_id: str
        """
        self._data_id = data_id

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
        if not isinstance(other, ImageBatchSyncReqUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
