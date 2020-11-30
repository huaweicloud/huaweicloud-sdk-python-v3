# coding: utf-8

import pprint
import re

import six





class ShowUpBandwidthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_domains': 'list[str]',
        'app': 'str',
        'stream': 'str',
        'region': 'list[str]',
        'isp': 'list[str]',
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domains': 'publish_domains',
        'app': 'app',
        'stream': 'stream',
        'region': 'region',
        'isp': 'isp',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domains=None, app=None, stream=None, region=None, isp=None, interval=None, start_time=None, end_time=None):
        """ShowUpBandwidthRequest - a model defined in huaweicloud sdk"""
        
        

        self._publish_domains = None
        self._app = None
        self._stream = None
        self._region = None
        self._isp = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domains = publish_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domains(self):
        """Gets the publish_domains of this ShowUpBandwidthRequest.


        :return: The publish_domains of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._publish_domains

    @publish_domains.setter
    def publish_domains(self, publish_domains):
        """Sets the publish_domains of this ShowUpBandwidthRequest.


        :param publish_domains: The publish_domains of this ShowUpBandwidthRequest.
        :type: list[str]
        """
        self._publish_domains = publish_domains

    @property
    def app(self):
        """Gets the app of this ShowUpBandwidthRequest.


        :return: The app of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ShowUpBandwidthRequest.


        :param app: The app of this ShowUpBandwidthRequest.
        :type: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ShowUpBandwidthRequest.


        :return: The stream of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ShowUpBandwidthRequest.


        :param stream: The stream of this ShowUpBandwidthRequest.
        :type: str
        """
        self._stream = stream

    @property
    def region(self):
        """Gets the region of this ShowUpBandwidthRequest.


        :return: The region of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowUpBandwidthRequest.


        :param region: The region of this ShowUpBandwidthRequest.
        :type: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ShowUpBandwidthRequest.


        :return: The isp of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowUpBandwidthRequest.


        :param isp: The isp of this ShowUpBandwidthRequest.
        :type: list[str]
        """
        self._isp = isp

    @property
    def interval(self):
        """Gets the interval of this ShowUpBandwidthRequest.


        :return: The interval of this ShowUpBandwidthRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowUpBandwidthRequest.


        :param interval: The interval of this ShowUpBandwidthRequest.
        :type: int
        """
        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ShowUpBandwidthRequest.


        :return: The start_time of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowUpBandwidthRequest.


        :param start_time: The start_time of this ShowUpBandwidthRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowUpBandwidthRequest.


        :return: The end_time of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowUpBandwidthRequest.


        :param end_time: The end_time of this ShowUpBandwidthRequest.
        :type: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowUpBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
