# coding: utf-8

import pprint
import re

import six





class ListDevicesRequest:


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
        'product_id': 'str',
        'gateway_id': 'str',
        'is_cascade_query': 'bool',
        'node_id': 'str',
        'device_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'product_id': 'product_id',
        'gateway_id': 'gateway_id',
        'is_cascade_query': 'is_cascade_query',
        'node_id': 'node_id',
        'device_name': 'device_name',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'app_id': 'app_id'
    }

    def __init__(self, instance_id=None, product_id=None, gateway_id=None, is_cascade_query=False, node_id=None, device_name=None, limit=10, marker='ffffffffffffffffffffffff', offset=0, start_time=None, end_time=None, app_id=None):
        """ListDevicesRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._product_id = None
        self._gateway_id = None
        self._is_cascade_query = None
        self._node_id = None
        self._device_name = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self._app_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if product_id is not None:
            self.product_id = product_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if is_cascade_query is not None:
            self.is_cascade_query = is_cascade_query
        if node_id is not None:
            self.node_id = node_id
        if device_name is not None:
            self.device_name = device_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if app_id is not None:
            self.app_id = app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDevicesRequest.


        :return: The instance_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDevicesRequest.


        :param instance_id: The instance_id of this ListDevicesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this ListDevicesRequest.


        :return: The product_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListDevicesRequest.


        :param product_id: The product_id of this ListDevicesRequest.
        :type: str
        """
        self._product_id = product_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ListDevicesRequest.


        :return: The gateway_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ListDevicesRequest.


        :param gateway_id: The gateway_id of this ListDevicesRequest.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def is_cascade_query(self):
        """Gets the is_cascade_query of this ListDevicesRequest.


        :return: The is_cascade_query of this ListDevicesRequest.
        :rtype: bool
        """
        return self._is_cascade_query

    @is_cascade_query.setter
    def is_cascade_query(self, is_cascade_query):
        """Sets the is_cascade_query of this ListDevicesRequest.


        :param is_cascade_query: The is_cascade_query of this ListDevicesRequest.
        :type: bool
        """
        self._is_cascade_query = is_cascade_query

    @property
    def node_id(self):
        """Gets the node_id of this ListDevicesRequest.


        :return: The node_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListDevicesRequest.


        :param node_id: The node_id of this ListDevicesRequest.
        :type: str
        """
        self._node_id = node_id

    @property
    def device_name(self):
        """Gets the device_name of this ListDevicesRequest.


        :return: The device_name of this ListDevicesRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListDevicesRequest.


        :param device_name: The device_name of this ListDevicesRequest.
        :type: str
        """
        self._device_name = device_name

    @property
    def limit(self):
        """Gets the limit of this ListDevicesRequest.


        :return: The limit of this ListDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDevicesRequest.


        :param limit: The limit of this ListDevicesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDevicesRequest.


        :return: The marker of this ListDevicesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDevicesRequest.


        :param marker: The marker of this ListDevicesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListDevicesRequest.


        :return: The offset of this ListDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDevicesRequest.


        :param offset: The offset of this ListDevicesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this ListDevicesRequest.


        :return: The start_time of this ListDevicesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListDevicesRequest.


        :param start_time: The start_time of this ListDevicesRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListDevicesRequest.


        :return: The end_time of this ListDevicesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListDevicesRequest.


        :param end_time: The end_time of this ListDevicesRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def app_id(self):
        """Gets the app_id of this ListDevicesRequest.


        :return: The app_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListDevicesRequest.


        :param app_id: The app_id of this ListDevicesRequest.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ListDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
