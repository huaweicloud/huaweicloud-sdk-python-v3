# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListEventByTimelineResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'requests': 'list[StatisticListInfoRequests]',
        'attacks': 'list[StatisticListInfoRequests]'
    }

    attribute_map = {
        'requests': 'requests',
        'attacks': 'attacks'
    }

    def __init__(self, requests=None, attacks=None):
        """ListEventByTimelineResponse - a model defined in huaweicloud sdk"""
        
        super(ListEventByTimelineResponse, self).__init__()

        self._requests = None
        self._attacks = None
        self.discriminator = None

        if requests is not None:
            self.requests = requests
        if attacks is not None:
            self.attacks = attacks

    @property
    def requests(self):
        """Gets the requests of this ListEventByTimelineResponse.

        请求个数列表

        :return: The requests of this ListEventByTimelineResponse.
        :rtype: list[StatisticListInfoRequests]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this ListEventByTimelineResponse.

        请求个数列表

        :param requests: The requests of this ListEventByTimelineResponse.
        :type: list[StatisticListInfoRequests]
        """
        self._requests = requests

    @property
    def attacks(self):
        """Gets the attacks of this ListEventByTimelineResponse.

        攻击个数列表

        :return: The attacks of this ListEventByTimelineResponse.
        :rtype: list[StatisticListInfoRequests]
        """
        return self._attacks

    @attacks.setter
    def attacks(self, attacks):
        """Sets the attacks of this ListEventByTimelineResponse.

        攻击个数列表

        :param attacks: The attacks of this ListEventByTimelineResponse.
        :type: list[StatisticListInfoRequests]
        """
        self._attacks = attacks

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEventByTimelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
