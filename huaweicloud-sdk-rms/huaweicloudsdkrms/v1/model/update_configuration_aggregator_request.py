# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigurationAggregatorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregator_id': 'str',
        'body': 'ConfigurationAggregatorRequest'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'body': 'body'
    }

    def __init__(self, aggregator_id=None, body=None):
        """UpdateConfigurationAggregatorRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param body: Body of the UpdateConfigurationAggregatorRequest
        :type body: :class:`huaweicloudsdkrms.v1.ConfigurationAggregatorRequest`
        """
        
        

        self._aggregator_id = None
        self._body = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        if body is not None:
            self.body = body

    @property
    def aggregator_id(self):
        """Gets the aggregator_id of this UpdateConfigurationAggregatorRequest.

        资源聚合器ID。

        :return: The aggregator_id of this UpdateConfigurationAggregatorRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        """Sets the aggregator_id of this UpdateConfigurationAggregatorRequest.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this UpdateConfigurationAggregatorRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def body(self):
        """Gets the body of this UpdateConfigurationAggregatorRequest.

        :return: The body of this UpdateConfigurationAggregatorRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.ConfigurationAggregatorRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateConfigurationAggregatorRequest.

        :param body: The body of this UpdateConfigurationAggregatorRequest.
        :type body: :class:`huaweicloudsdkrms.v1.ConfigurationAggregatorRequest`
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
        if not isinstance(other, UpdateConfigurationAggregatorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
