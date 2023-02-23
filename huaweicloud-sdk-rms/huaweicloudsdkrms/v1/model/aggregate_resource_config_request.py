# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateResourceConfigRequest:

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
        'resource_identifier': 'ResourceIdentifier'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'resource_identifier': 'resource_identifier'
    }

    def __init__(self, aggregator_id=None, resource_identifier=None):
        """AggregateResourceConfigRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param resource_identifier: 
        :type resource_identifier: :class:`huaweicloudsdkrms.v1.ResourceIdentifier`
        """
        
        

        self._aggregator_id = None
        self._resource_identifier = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        self.resource_identifier = resource_identifier

    @property
    def aggregator_id(self):
        """Gets the aggregator_id of this AggregateResourceConfigRequest.

        资源聚合器ID。

        :return: The aggregator_id of this AggregateResourceConfigRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        """Sets the aggregator_id of this AggregateResourceConfigRequest.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this AggregateResourceConfigRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def resource_identifier(self):
        """Gets the resource_identifier of this AggregateResourceConfigRequest.

        :return: The resource_identifier of this AggregateResourceConfigRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.ResourceIdentifier`
        """
        return self._resource_identifier

    @resource_identifier.setter
    def resource_identifier(self, resource_identifier):
        """Sets the resource_identifier of this AggregateResourceConfigRequest.

        :param resource_identifier: The resource_identifier of this AggregateResourceConfigRequest.
        :type resource_identifier: :class:`huaweicloudsdkrms.v1.ResourceIdentifier`
        """
        self._resource_identifier = resource_identifier

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
        if not isinstance(other, AggregateResourceConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
