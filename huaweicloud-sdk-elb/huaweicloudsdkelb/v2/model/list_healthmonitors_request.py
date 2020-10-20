# coding: utf-8

import pprint
import re

import six





class ListHealthmonitorsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'delay': 'int',
        'max_retries': 'int',
        'admin_state_up': 'bool',
        'timeout': 'int',
        'type': 'str',
        'monitor_port': 'int',
        'expected_codes': 'str',
        'domain_name': 'str',
        'url_path': 'str',
        'http_method': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'delay': 'delay',
        'max_retries': 'max_retries',
        'admin_state_up': 'admin_state_up',
        'timeout': 'timeout',
        'type': 'type',
        'monitor_port': 'monitor_port',
        'expected_codes': 'expected_codes',
        'domain_name': 'domain_name',
        'url_path': 'url_path',
        'http_method': 'http_method'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, delay=None, max_retries=None, admin_state_up=None, timeout=None, type=None, monitor_port=None, expected_codes=None, domain_name=None, url_path=None, http_method=None):
        """ListHealthmonitorsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._delay = None
        self._max_retries = None
        self._admin_state_up = None
        self._timeout = None
        self._type = None
        self._monitor_port = None
        self._expected_codes = None
        self._domain_name = None
        self._url_path = None
        self._http_method = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if delay is not None:
            self.delay = delay
        if max_retries is not None:
            self.max_retries = max_retries
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if domain_name is not None:
            self.domain_name = domain_name
        if url_path is not None:
            self.url_path = url_path
        if http_method is not None:
            self.http_method = http_method

    @property
    def limit(self):
        """Gets the limit of this ListHealthmonitorsRequest.


        :return: The limit of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHealthmonitorsRequest.


        :param limit: The limit of this ListHealthmonitorsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListHealthmonitorsRequest.


        :return: The marker of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHealthmonitorsRequest.


        :param marker: The marker of this ListHealthmonitorsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListHealthmonitorsRequest.


        :return: The page_reverse of this ListHealthmonitorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListHealthmonitorsRequest.


        :param page_reverse: The page_reverse of this ListHealthmonitorsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListHealthmonitorsRequest.


        :return: The id of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHealthmonitorsRequest.


        :param id: The id of this ListHealthmonitorsRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListHealthmonitorsRequest.


        :return: The name of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHealthmonitorsRequest.


        :param name: The name of this ListHealthmonitorsRequest.
        :type: str
        """
        self._name = name

    @property
    def delay(self):
        """Gets the delay of this ListHealthmonitorsRequest.


        :return: The delay of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ListHealthmonitorsRequest.


        :param delay: The delay of this ListHealthmonitorsRequest.
        :type: int
        """
        self._delay = delay

    @property
    def max_retries(self):
        """Gets the max_retries of this ListHealthmonitorsRequest.


        :return: The max_retries of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this ListHealthmonitorsRequest.


        :param max_retries: The max_retries of this ListHealthmonitorsRequest.
        :type: int
        """
        self._max_retries = max_retries

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListHealthmonitorsRequest.


        :return: The admin_state_up of this ListHealthmonitorsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListHealthmonitorsRequest.


        :param admin_state_up: The admin_state_up of this ListHealthmonitorsRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def timeout(self):
        """Gets the timeout of this ListHealthmonitorsRequest.


        :return: The timeout of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ListHealthmonitorsRequest.


        :param timeout: The timeout of this ListHealthmonitorsRequest.
        :type: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ListHealthmonitorsRequest.


        :return: The type of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListHealthmonitorsRequest.


        :param type: The type of this ListHealthmonitorsRequest.
        :type: str
        """
        self._type = type

    @property
    def monitor_port(self):
        """Gets the monitor_port of this ListHealthmonitorsRequest.


        :return: The monitor_port of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this ListHealthmonitorsRequest.


        :param monitor_port: The monitor_port of this ListHealthmonitorsRequest.
        :type: int
        """
        self._monitor_port = monitor_port

    @property
    def expected_codes(self):
        """Gets the expected_codes of this ListHealthmonitorsRequest.


        :return: The expected_codes of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this ListHealthmonitorsRequest.


        :param expected_codes: The expected_codes of this ListHealthmonitorsRequest.
        :type: str
        """
        self._expected_codes = expected_codes

    @property
    def domain_name(self):
        """Gets the domain_name of this ListHealthmonitorsRequest.


        :return: The domain_name of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListHealthmonitorsRequest.


        :param domain_name: The domain_name of this ListHealthmonitorsRequest.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def url_path(self):
        """Gets the url_path of this ListHealthmonitorsRequest.


        :return: The url_path of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this ListHealthmonitorsRequest.


        :param url_path: The url_path of this ListHealthmonitorsRequest.
        :type: str
        """
        self._url_path = url_path

    @property
    def http_method(self):
        """Gets the http_method of this ListHealthmonitorsRequest.


        :return: The http_method of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ListHealthmonitorsRequest.


        :param http_method: The http_method of this ListHealthmonitorsRequest.
        :type: str
        """
        self._http_method = http_method

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
        if not isinstance(other, ListHealthmonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
