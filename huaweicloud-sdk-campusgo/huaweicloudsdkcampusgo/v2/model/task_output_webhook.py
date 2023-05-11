# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutputWebhook:

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
        'headers': 'object',
        'data_category': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'headers': 'headers',
        'data_category': 'data_category'
    }

    def __init__(self, url=None, headers=None, data_category=None):
        """TaskOutputWebhook

        The model defined in huaweicloud sdk

        :param url: 结果回调地址
        :type url: str
        :param headers: 结果回调时需要携带的请求头
        :type headers: object
        :param data_category: 作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要
        :type data_category: list[str]
        """
        
        

        self._url = None
        self._headers = None
        self._data_category = None
        self.discriminator = None

        self.url = url
        self.headers = headers
        if data_category is not None:
            self.data_category = data_category

    @property
    def url(self):
        """Gets the url of this TaskOutputWebhook.

        结果回调地址

        :return: The url of this TaskOutputWebhook.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TaskOutputWebhook.

        结果回调地址

        :param url: The url of this TaskOutputWebhook.
        :type url: str
        """
        self._url = url

    @property
    def headers(self):
        """Gets the headers of this TaskOutputWebhook.

        结果回调时需要携带的请求头

        :return: The headers of this TaskOutputWebhook.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this TaskOutputWebhook.

        结果回调时需要携带的请求头

        :param headers: The headers of this TaskOutputWebhook.
        :type headers: object
        """
        self._headers = headers

    @property
    def data_category(self):
        """Gets the data_category of this TaskOutputWebhook.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :return: The data_category of this TaskOutputWebhook.
        :rtype: list[str]
        """
        return self._data_category

    @data_category.setter
    def data_category(self, data_category):
        """Sets the data_category of this TaskOutputWebhook.

        作业输出数据类别的列表，当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据，部分服务需要

        :param data_category: The data_category of this TaskOutputWebhook.
        :type data_category: list[str]
        """
        self._data_category = data_category

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
        if not isinstance(other, TaskOutputWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
