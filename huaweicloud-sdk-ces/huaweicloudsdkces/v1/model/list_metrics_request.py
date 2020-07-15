# coding: utf-8

import pprint
import re

import six





class ListMetricsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dim0': 'str',
        'dim1': 'str',
        'dim2': 'str',
        'limit': 'int',
        'metric_name': 'str',
        'namespace': 'str',
        'order': 'str',
        'start': 'str'
    }

    attribute_map = {
        'dim0': 'dim.0',
        'dim1': 'dim.1',
        'dim2': 'dim.2',
        'limit': 'limit',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'order': 'order',
        'start': 'start'
    }

    def __init__(self, dim0=None, dim1=None, dim2=None, limit=None, metric_name=None, namespace=None, order=None, start=None):
        """ListMetricsRequest - a model defined in huaweicloud sdk"""
        
        

        self._dim0 = None
        self._dim1 = None
        self._dim2 = None
        self._limit = None
        self._metric_name = None
        self._namespace = None
        self._order = None
        self._start = None
        self.discriminator = None

        if dim0 is not None:
            self.dim0 = dim0
        if dim1 is not None:
            self.dim1 = dim1
        if dim2 is not None:
            self.dim2 = dim2
        if limit is not None:
            self.limit = limit
        if metric_name is not None:
            self.metric_name = metric_name
        if namespace is not None:
            self.namespace = namespace
        if order is not None:
            self.order = order
        if start is not None:
            self.start = start

    @property
    def dim0(self):
        """Gets the dim0 of this ListMetricsRequest.


        :return: The dim0 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim0

    @dim0.setter
    def dim0(self, dim0):
        """Sets the dim0 of this ListMetricsRequest.


        :param dim0: The dim0 of this ListMetricsRequest.
        :type: str
        """
        self._dim0 = dim0

    @property
    def dim1(self):
        """Gets the dim1 of this ListMetricsRequest.


        :return: The dim1 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim1

    @dim1.setter
    def dim1(self, dim1):
        """Sets the dim1 of this ListMetricsRequest.


        :param dim1: The dim1 of this ListMetricsRequest.
        :type: str
        """
        self._dim1 = dim1

    @property
    def dim2(self):
        """Gets the dim2 of this ListMetricsRequest.


        :return: The dim2 of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim2

    @dim2.setter
    def dim2(self, dim2):
        """Sets the dim2 of this ListMetricsRequest.


        :param dim2: The dim2 of this ListMetricsRequest.
        :type: str
        """
        self._dim2 = dim2

    @property
    def limit(self):
        """Gets the limit of this ListMetricsRequest.


        :return: The limit of this ListMetricsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMetricsRequest.


        :param limit: The limit of this ListMetricsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def metric_name(self):
        """Gets the metric_name of this ListMetricsRequest.


        :return: The metric_name of this ListMetricsRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ListMetricsRequest.


        :param metric_name: The metric_name of this ListMetricsRequest.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this ListMetricsRequest.


        :return: The namespace of this ListMetricsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListMetricsRequest.


        :param namespace: The namespace of this ListMetricsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def order(self):
        """Gets the order of this ListMetricsRequest.


        :return: The order of this ListMetricsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListMetricsRequest.


        :param order: The order of this ListMetricsRequest.
        :type: str
        """
        self._order = order

    @property
    def start(self):
        """Gets the start of this ListMetricsRequest.


        :return: The start of this ListMetricsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListMetricsRequest.


        :param start: The start of this ListMetricsRequest.
        :type: str
        """
        self._start = start

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
        if not isinstance(other, ListMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
