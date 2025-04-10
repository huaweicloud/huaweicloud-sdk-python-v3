# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInternetBandwidthRequest:

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
        'fields': 'list[str]'
    }

    attribute_map = {
        'internet_bandwidth_id': 'internet_bandwidth_id',
        'fields': 'fields'
    }

    def __init__(self, internet_bandwidth_id=None, fields=None):
        r"""ShowInternetBandwidthRequest

        The model defined in huaweicloud sdk

        :param internet_bandwidth_id: 
        :type internet_bandwidth_id: str
        :param fields: 
        :type fields: list[str]
        """
        
        

        self._internet_bandwidth_id = None
        self._fields = None
        self.discriminator = None

        self.internet_bandwidth_id = internet_bandwidth_id
        if fields is not None:
            self.fields = fields

    @property
    def internet_bandwidth_id(self):
        r"""Gets the internet_bandwidth_id of this ShowInternetBandwidthRequest.

        :return: The internet_bandwidth_id of this ShowInternetBandwidthRequest.
        :rtype: str
        """
        return self._internet_bandwidth_id

    @internet_bandwidth_id.setter
    def internet_bandwidth_id(self, internet_bandwidth_id):
        r"""Sets the internet_bandwidth_id of this ShowInternetBandwidthRequest.

        :param internet_bandwidth_id: The internet_bandwidth_id of this ShowInternetBandwidthRequest.
        :type internet_bandwidth_id: str
        """
        self._internet_bandwidth_id = internet_bandwidth_id

    @property
    def fields(self):
        r"""Gets the fields of this ShowInternetBandwidthRequest.

        :return: The fields of this ShowInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowInternetBandwidthRequest.

        :param fields: The fields of this ShowInternetBandwidthRequest.
        :type fields: list[str]
        """
        self._fields = fields

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
        if not isinstance(other, ShowInternetBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
