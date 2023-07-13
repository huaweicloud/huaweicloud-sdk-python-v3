# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxSearchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'int',
        'region': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'env_id': 'int',
        'request_id': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'business_id': 'business_id',
        'region': 'region',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'env_id': 'env_id',
        'request_id': 'request_id',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, business_id=None, region=None, start_time=None, end_time=None, env_id=None, request_id=None, page_no=None, page_size=None):
        """TxSearchRequest

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param region: region英文名称。
        :type region: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param env_id: 环境id。
        :type env_id: int
        :param request_id: 上次请求的id。
        :type request_id: str
        :param page_no: 页码。
        :type page_no: int
        :param page_size: 每页数量。
        :type page_size: int
        """
        
        

        self._business_id = None
        self._region = None
        self._start_time = None
        self._end_time = None
        self._env_id = None
        self._request_id = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        self.business_id = business_id
        self.region = region
        self.start_time = start_time
        self.end_time = end_time
        if env_id is not None:
            self.env_id = env_id
        if request_id is not None:
            self.request_id = request_id
        self.page_no = page_no
        self.page_size = page_size

    @property
    def business_id(self):
        """Gets the business_id of this TxSearchRequest.

        应用id。

        :return: The business_id of this TxSearchRequest.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TxSearchRequest.

        应用id。

        :param business_id: The business_id of this TxSearchRequest.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def region(self):
        """Gets the region of this TxSearchRequest.

        region英文名称。

        :return: The region of this TxSearchRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TxSearchRequest.

        region英文名称。

        :param region: The region of this TxSearchRequest.
        :type region: str
        """
        self._region = region

    @property
    def start_time(self):
        """Gets the start_time of this TxSearchRequest.

        开始时间。

        :return: The start_time of this TxSearchRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TxSearchRequest.

        开始时间。

        :param start_time: The start_time of this TxSearchRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TxSearchRequest.

        结束时间。

        :return: The end_time of this TxSearchRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TxSearchRequest.

        结束时间。

        :param end_time: The end_time of this TxSearchRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def env_id(self):
        """Gets the env_id of this TxSearchRequest.

        环境id。

        :return: The env_id of this TxSearchRequest.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TxSearchRequest.

        环境id。

        :param env_id: The env_id of this TxSearchRequest.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def request_id(self):
        """Gets the request_id of this TxSearchRequest.

        上次请求的id。

        :return: The request_id of this TxSearchRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TxSearchRequest.

        上次请求的id。

        :param request_id: The request_id of this TxSearchRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_no(self):
        """Gets the page_no of this TxSearchRequest.

        页码。

        :return: The page_no of this TxSearchRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this TxSearchRequest.

        页码。

        :param page_no: The page_no of this TxSearchRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this TxSearchRequest.

        每页数量。

        :return: The page_size of this TxSearchRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TxSearchRequest.

        每页数量。

        :param page_size: The page_size of this TxSearchRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, TxSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
