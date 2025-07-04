# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimSimulationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'next': 'str',
        'previous': 'str',
        'results': 'list[SimulationSrlz]'
    }

    attribute_map = {
        'count': 'count',
        'next': 'next',
        'previous': 'previous',
        'results': 'results'
    }

    def __init__(self, count=None, next=None, previous=None, results=None):
        r"""ListSimSimulationsResponse

        The model defined in huaweicloud sdk

        :param count: 返回子任务总数
        :type count: int
        :param next: 
        :type next: str
        :param previous: 
        :type previous: str
        :param results: 
        :type results: list[:class:`huaweicloudsdkoctopus.v2.SimulationSrlz`]
        """
        
        super(ListSimSimulationsResponse, self).__init__()

        self._count = None
        self._next = None
        self._previous = None
        self._results = None
        self.discriminator = None

        if count is not None:
            self.count = count
        self.next = next
        self.previous = previous
        if results is not None:
            self.results = results

    @property
    def count(self):
        r"""Gets the count of this ListSimSimulationsResponse.

        返回子任务总数

        :return: The count of this ListSimSimulationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSimSimulationsResponse.

        返回子任务总数

        :param count: The count of this ListSimSimulationsResponse.
        :type count: int
        """
        self._count = count

    @property
    def next(self):
        r"""Gets the next of this ListSimSimulationsResponse.

        :return: The next of this ListSimSimulationsResponse.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        r"""Sets the next of this ListSimSimulationsResponse.

        :param next: The next of this ListSimSimulationsResponse.
        :type next: str
        """
        self._next = next

    @property
    def previous(self):
        r"""Gets the previous of this ListSimSimulationsResponse.

        :return: The previous of this ListSimSimulationsResponse.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        r"""Sets the previous of this ListSimSimulationsResponse.

        :param previous: The previous of this ListSimSimulationsResponse.
        :type previous: str
        """
        self._previous = previous

    @property
    def results(self):
        r"""Gets the results of this ListSimSimulationsResponse.

        :return: The results of this ListSimSimulationsResponse.
        :rtype: list[:class:`huaweicloudsdkoctopus.v2.SimulationSrlz`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this ListSimSimulationsResponse.

        :param results: The results of this ListSimSimulationsResponse.
        :type results: list[:class:`huaweicloudsdkoctopus.v2.SimulationSrlz`]
        """
        self._results = results

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
        if not isinstance(other, ListSimSimulationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
