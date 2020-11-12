# coding: utf-8

import pprint
import re

import six





class ShowMetricDataRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'filter': 'str',
        '_from': 'int',
        'metric_name': 'str',
        'namespace': 'str',
        'period': 'int',
        'to': 'int'
    }

    attribute_map = {
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'filter': 'filter',
        '_from': 'from',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'period': 'period',
        'to': 'to'
    }

    def __init__(self, dim_0=None, dim_1=None, dim_2=None, filter=None, _from=None, metric_name=None, namespace=None, period=None, to=None):
        """ShowMetricDataRequest - a model defined in huaweicloud sdk"""
        
        

        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._filter = None
        self.__from = None
        self._metric_name = None
        self._namespace = None
        self._period = None
        self._to = None
        self.discriminator = None

        self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        self.filter = filter
        self._from = _from
        self.metric_name = metric_name
        self.namespace = namespace
        self.period = period
        self.to = to

    @property
    def dim_0(self):
        """Gets the dim_0 of this ShowMetricDataRequest.


        :return: The dim_0 of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        """Sets the dim_0 of this ShowMetricDataRequest.


        :param dim_0: The dim_0 of this ShowMetricDataRequest.
        :type: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        """Gets the dim_1 of this ShowMetricDataRequest.


        :return: The dim_1 of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        """Sets the dim_1 of this ShowMetricDataRequest.


        :param dim_1: The dim_1 of this ShowMetricDataRequest.
        :type: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        """Gets the dim_2 of this ShowMetricDataRequest.


        :return: The dim_2 of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        """Sets the dim_2 of this ShowMetricDataRequest.


        :param dim_2: The dim_2 of this ShowMetricDataRequest.
        :type: str
        """
        self._dim_2 = dim_2

    @property
    def filter(self):
        """Gets the filter of this ShowMetricDataRequest.


        :return: The filter of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ShowMetricDataRequest.


        :param filter: The filter of this ShowMetricDataRequest.
        :type: str
        """
        self._filter = filter

    @property
    def _from(self):
        """Gets the _from of this ShowMetricDataRequest.


        :return: The _from of this ShowMetricDataRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ShowMetricDataRequest.


        :param _from: The _from of this ShowMetricDataRequest.
        :type: int
        """
        self.__from = _from

    @property
    def metric_name(self):
        """Gets the metric_name of this ShowMetricDataRequest.


        :return: The metric_name of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ShowMetricDataRequest.


        :param metric_name: The metric_name of this ShowMetricDataRequest.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this ShowMetricDataRequest.


        :return: The namespace of this ShowMetricDataRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowMetricDataRequest.


        :param namespace: The namespace of this ShowMetricDataRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def period(self):
        """Gets the period of this ShowMetricDataRequest.


        :return: The period of this ShowMetricDataRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowMetricDataRequest.


        :param period: The period of this ShowMetricDataRequest.
        :type: int
        """
        self._period = period

    @property
    def to(self):
        """Gets the to of this ShowMetricDataRequest.


        :return: The to of this ShowMetricDataRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ShowMetricDataRequest.


        :param to: The to of this ShowMetricDataRequest.
        :type: int
        """
        self._to = to

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
        if not isinstance(other, ShowMetricDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
