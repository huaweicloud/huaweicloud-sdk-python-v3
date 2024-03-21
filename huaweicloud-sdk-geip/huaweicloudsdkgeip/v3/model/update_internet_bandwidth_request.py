# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternetBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'internet_bandwidth_id': 'str',
        'body': 'UpdateInternetBandwidthRequestBody'
    }

    attribute_map = {
        'internet_bandwidth_id': 'internet_bandwidth_id',
        'body': 'body'
    }

    def __init__(self, internet_bandwidth_id=None, body=None):
        """UpdateInternetBandwidthRequest

        The model defined in huaweicloud sdk

        :param internet_bandwidth_id: 
        :type internet_bandwidth_id: str
        :param body: Body of the UpdateInternetBandwidthRequest
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidthRequestBody`
        """
        
        

        self._internet_bandwidth_id = None
        self._body = None
        self.discriminator = None

        self.internet_bandwidth_id = internet_bandwidth_id
        if body is not None:
            self.body = body

    @property
    def internet_bandwidth_id(self):
        """Gets the internet_bandwidth_id of this UpdateInternetBandwidthRequest.

        :return: The internet_bandwidth_id of this UpdateInternetBandwidthRequest.
        :rtype: str
        """
        return self._internet_bandwidth_id

    @internet_bandwidth_id.setter
    def internet_bandwidth_id(self, internet_bandwidth_id):
        """Sets the internet_bandwidth_id of this UpdateInternetBandwidthRequest.

        :param internet_bandwidth_id: The internet_bandwidth_id of this UpdateInternetBandwidthRequest.
        :type internet_bandwidth_id: str
        """
        self._internet_bandwidth_id = internet_bandwidth_id

    @property
    def body(self):
        """Gets the body of this UpdateInternetBandwidthRequest.

        :return: The body of this UpdateInternetBandwidthRequest.
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidthRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateInternetBandwidthRequest.

        :param body: The body of this UpdateInternetBandwidthRequest.
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidthRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateInternetBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
