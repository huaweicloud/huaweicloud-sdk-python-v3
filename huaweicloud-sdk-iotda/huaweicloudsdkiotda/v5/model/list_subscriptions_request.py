# coding: utf-8

import pprint
import re

import six





class ListSubscriptionsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'resource': 'str',
        'event': 'str',
        'callbackurl': 'str',
        'app_id': 'str',
        'channel': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'resource': 'resource',
        'event': 'event',
        'callbackurl': 'callbackurl',
        'app_id': 'app_id',
        'channel': 'channel',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, resource=None, event=None, callbackurl=None, app_id=None, channel=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """ListSubscriptionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._resource = None
        self._event = None
        self._callbackurl = None
        self._app_id = None
        self._channel = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if resource is not None:
            self.resource = resource
        if event is not None:
            self.event = event
        if callbackurl is not None:
            self.callbackurl = callbackurl
        if app_id is not None:
            self.app_id = app_id
        if channel is not None:
            self.channel = channel
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSubscriptionsRequest.


        :return: The instance_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSubscriptionsRequest.


        :param instance_id: The instance_id of this ListSubscriptionsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def resource(self):
        """Gets the resource of this ListSubscriptionsRequest.


        :return: The resource of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ListSubscriptionsRequest.


        :param resource: The resource of this ListSubscriptionsRequest.
        :type: str
        """
        self._resource = resource

    @property
    def event(self):
        """Gets the event of this ListSubscriptionsRequest.


        :return: The event of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this ListSubscriptionsRequest.


        :param event: The event of this ListSubscriptionsRequest.
        :type: str
        """
        self._event = event

    @property
    def callbackurl(self):
        """Gets the callbackurl of this ListSubscriptionsRequest.


        :return: The callbackurl of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._callbackurl

    @callbackurl.setter
    def callbackurl(self, callbackurl):
        """Sets the callbackurl of this ListSubscriptionsRequest.


        :param callbackurl: The callbackurl of this ListSubscriptionsRequest.
        :type: str
        """
        self._callbackurl = callbackurl

    @property
    def app_id(self):
        """Gets the app_id of this ListSubscriptionsRequest.


        :return: The app_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListSubscriptionsRequest.


        :param app_id: The app_id of this ListSubscriptionsRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def channel(self):
        """Gets the channel of this ListSubscriptionsRequest.


        :return: The channel of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ListSubscriptionsRequest.


        :param channel: The channel of this ListSubscriptionsRequest.
        :type: str
        """
        self._channel = channel

    @property
    def limit(self):
        """Gets the limit of this ListSubscriptionsRequest.


        :return: The limit of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubscriptionsRequest.


        :param limit: The limit of this ListSubscriptionsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSubscriptionsRequest.


        :return: The marker of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSubscriptionsRequest.


        :param marker: The marker of this ListSubscriptionsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListSubscriptionsRequest.


        :return: The offset of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubscriptionsRequest.


        :param offset: The offset of this ListSubscriptionsRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSubscriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
