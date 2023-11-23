# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueuePropertiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'page': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'page': 'page',
        'page_size': 'page_size'
    }

    def __init__(self, queue_name=None, page=None, page_size=None):
        """ListQueuePropertiesRequest

        The model defined in huaweicloud sdk

        :param queue_name: 队列名称
        :type queue_name: str
        :param page: 列表当前页
        :type page: int
        :param page_size: 每页显示条数
        :type page_size: int
        """
        
        

        self._queue_name = None
        self._page = None
        self._page_size = None
        self.discriminator = None

        self.queue_name = queue_name
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size

    @property
    def queue_name(self):
        """Gets the queue_name of this ListQueuePropertiesRequest.

        队列名称

        :return: The queue_name of this ListQueuePropertiesRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListQueuePropertiesRequest.

        队列名称

        :param queue_name: The queue_name of this ListQueuePropertiesRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def page(self):
        """Gets the page of this ListQueuePropertiesRequest.

        列表当前页

        :return: The page of this ListQueuePropertiesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListQueuePropertiesRequest.

        列表当前页

        :param page: The page of this ListQueuePropertiesRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ListQueuePropertiesRequest.

        每页显示条数

        :return: The page_size of this ListQueuePropertiesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListQueuePropertiesRequest.

        每页显示条数

        :param page_size: The page_size of this ListQueuePropertiesRequest.
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
        if not isinstance(other, ListQueuePropertiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
