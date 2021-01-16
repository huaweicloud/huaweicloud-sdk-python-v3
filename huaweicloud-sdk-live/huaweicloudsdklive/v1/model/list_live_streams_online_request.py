# coding: utf-8

import pprint
import re

import six





class ListLiveStreamsOnlineRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'offset': 'int',
        'limit': 'int',
        'stream': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'offset': 'offset',
        'limit': 'limit',
        'stream': 'stream'
    }

    def __init__(self, publish_domain=None, app=None, offset=None, limit=10, stream=None):
        """ListLiveStreamsOnlineRequest - a model defined in huaweicloud sdk"""
        
        

        self._publish_domain = None
        self._app = None
        self._offset = None
        self._limit = None
        self._stream = None
        self.discriminator = None

        self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if stream is not None:
            self.stream = stream

    @property
    def publish_domain(self):
        """Gets the publish_domain of this ListLiveStreamsOnlineRequest.


        :return: The publish_domain of this ListLiveStreamsOnlineRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this ListLiveStreamsOnlineRequest.


        :param publish_domain: The publish_domain of this ListLiveStreamsOnlineRequest.
        :type: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this ListLiveStreamsOnlineRequest.


        :return: The app of this ListLiveStreamsOnlineRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListLiveStreamsOnlineRequest.


        :param app: The app of this ListLiveStreamsOnlineRequest.
        :type: str
        """
        self._app = app

    @property
    def offset(self):
        """Gets the offset of this ListLiveStreamsOnlineRequest.


        :return: The offset of this ListLiveStreamsOnlineRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLiveStreamsOnlineRequest.


        :param offset: The offset of this ListLiveStreamsOnlineRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLiveStreamsOnlineRequest.


        :return: The limit of this ListLiveStreamsOnlineRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLiveStreamsOnlineRequest.


        :param limit: The limit of this ListLiveStreamsOnlineRequest.
        :type: int
        """
        self._limit = limit

    @property
    def stream(self):
        """Gets the stream of this ListLiveStreamsOnlineRequest.


        :return: The stream of this ListLiveStreamsOnlineRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListLiveStreamsOnlineRequest.


        :param stream: The stream of this ListLiveStreamsOnlineRequest.
        :type: str
        """
        self._stream = stream

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
        if not isinstance(other, ListLiveStreamsOnlineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
