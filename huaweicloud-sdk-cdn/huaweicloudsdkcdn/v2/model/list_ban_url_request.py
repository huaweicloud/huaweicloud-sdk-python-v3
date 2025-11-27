# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBanUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'page_size': 'int',
        'page_number': 'int',
        'url': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'url': 'url'
    }

    def __init__(self, start_time=None, end_time=None, page_size=None, page_number=None, url=None):
        r"""ListBanUrlRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间戳（毫秒），需与结束时间戳同时指定。
        :type start_time: int
        :param end_time: 查询结束时间戳（毫秒），需与开始时间戳同时指定。
        :type end_time: int
        :param page_size: 封禁的url所显示单页最大数量，取值范围为1-50。page_size和page_number必须同时传值。默认值10.
        :type page_size: int
        :param page_number: 封禁的url当前查询为第几页，取值范围为1-65535。默认值1
        :type page_number: int
        :param url: 封禁的url地址。
        :type url: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._page_size = None
        self._page_number = None
        self._url = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if url is not None:
            self.url = url

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBanUrlRequest.

        查询起始时间戳（毫秒），需与结束时间戳同时指定。

        :return: The start_time of this ListBanUrlRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBanUrlRequest.

        查询起始时间戳（毫秒），需与结束时间戳同时指定。

        :param start_time: The start_time of this ListBanUrlRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBanUrlRequest.

        查询结束时间戳（毫秒），需与开始时间戳同时指定。

        :return: The end_time of this ListBanUrlRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBanUrlRequest.

        查询结束时间戳（毫秒），需与开始时间戳同时指定。

        :param end_time: The end_time of this ListBanUrlRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_size(self):
        r"""Gets the page_size of this ListBanUrlRequest.

        封禁的url所显示单页最大数量，取值范围为1-50。page_size和page_number必须同时传值。默认值10.

        :return: The page_size of this ListBanUrlRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListBanUrlRequest.

        封禁的url所显示单页最大数量，取值范围为1-50。page_size和page_number必须同时传值。默认值10.

        :param page_size: The page_size of this ListBanUrlRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ListBanUrlRequest.

        封禁的url当前查询为第几页，取值范围为1-65535。默认值1

        :return: The page_number of this ListBanUrlRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListBanUrlRequest.

        封禁的url当前查询为第几页，取值范围为1-65535。默认值1

        :param page_number: The page_number of this ListBanUrlRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def url(self):
        r"""Gets the url of this ListBanUrlRequest.

        封禁的url地址。

        :return: The url of this ListBanUrlRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ListBanUrlRequest.

        封禁的url地址。

        :param url: The url of this ListBanUrlRequest.
        :type url: str
        """
        self._url = url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBanUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
