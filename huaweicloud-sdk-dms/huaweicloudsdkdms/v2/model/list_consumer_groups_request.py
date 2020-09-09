# coding: utf-8

import pprint
import re

import six





class ListConsumerGroupsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_id': 'str',
        'include_deadletter': 'bool',
        'include_messages_num': 'bool',
        'page_size': 'int',
        'current_page': 'int'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'include_deadletter': 'include_deadletter',
        'include_messages_num': 'include_messages_num',
        'page_size': 'page_size',
        'current_page': 'current_page'
    }

    def __init__(self, queue_id=None, include_deadletter=None, include_messages_num=None, page_size=None, current_page=None):
        """ListConsumerGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._queue_id = None
        self._include_deadletter = None
        self._include_messages_num = None
        self._page_size = None
        self._current_page = None
        self.discriminator = None

        self.queue_id = queue_id
        if include_deadletter is not None:
            self.include_deadletter = include_deadletter
        if include_messages_num is not None:
            self.include_messages_num = include_messages_num
        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page

    @property
    def queue_id(self):
        """Gets the queue_id of this ListConsumerGroupsRequest.


        :return: The queue_id of this ListConsumerGroupsRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ListConsumerGroupsRequest.


        :param queue_id: The queue_id of this ListConsumerGroupsRequest.
        :type: str
        """
        self._queue_id = queue_id

    @property
    def include_deadletter(self):
        """Gets the include_deadletter of this ListConsumerGroupsRequest.


        :return: The include_deadletter of this ListConsumerGroupsRequest.
        :rtype: bool
        """
        return self._include_deadletter

    @include_deadletter.setter
    def include_deadletter(self, include_deadletter):
        """Sets the include_deadletter of this ListConsumerGroupsRequest.


        :param include_deadletter: The include_deadletter of this ListConsumerGroupsRequest.
        :type: bool
        """
        self._include_deadletter = include_deadletter

    @property
    def include_messages_num(self):
        """Gets the include_messages_num of this ListConsumerGroupsRequest.


        :return: The include_messages_num of this ListConsumerGroupsRequest.
        :rtype: bool
        """
        return self._include_messages_num

    @include_messages_num.setter
    def include_messages_num(self, include_messages_num):
        """Sets the include_messages_num of this ListConsumerGroupsRequest.


        :param include_messages_num: The include_messages_num of this ListConsumerGroupsRequest.
        :type: bool
        """
        self._include_messages_num = include_messages_num

    @property
    def page_size(self):
        """Gets the page_size of this ListConsumerGroupsRequest.


        :return: The page_size of this ListConsumerGroupsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListConsumerGroupsRequest.


        :param page_size: The page_size of this ListConsumerGroupsRequest.
        :type: int
        """
        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this ListConsumerGroupsRequest.


        :return: The current_page of this ListConsumerGroupsRequest.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListConsumerGroupsRequest.


        :param current_page: The current_page of this ListConsumerGroupsRequest.
        :type: int
        """
        self._current_page = current_page

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListConsumerGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
