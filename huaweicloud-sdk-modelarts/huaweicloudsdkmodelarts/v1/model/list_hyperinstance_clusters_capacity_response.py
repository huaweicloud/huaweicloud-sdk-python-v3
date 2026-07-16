# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHyperinstanceClustersCapacityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacities': 'list[ServerHpsClusterCapacity]'
    }

    attribute_map = {
        'capacities': 'capacities'
    }

    def __init__(self, capacities=None):
        r"""ListHyperinstanceClustersCapacityResponse

        The model defined in huaweicloud sdk

        :param capacities: 容量信息列表
        :type capacities: list[:class:`huaweicloudsdkmodelarts.v1.ServerHpsClusterCapacity`]
        """
        
        super().__init__()

        self._capacities = None
        self.discriminator = None

        if capacities is not None:
            self.capacities = capacities

    @property
    def capacities(self):
        r"""Gets the capacities of this ListHyperinstanceClustersCapacityResponse.

        容量信息列表

        :return: The capacities of this ListHyperinstanceClustersCapacityResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerHpsClusterCapacity`]
        """
        return self._capacities

    @capacities.setter
    def capacities(self, capacities):
        r"""Sets the capacities of this ListHyperinstanceClustersCapacityResponse.

        容量信息列表

        :param capacities: The capacities of this ListHyperinstanceClustersCapacityResponse.
        :type capacities: list[:class:`huaweicloudsdkmodelarts.v1.ServerHpsClusterCapacity`]
        """
        self._capacities = capacities

    def to_dict(self):
        import warnings
        warnings.warn("ListHyperinstanceClustersCapacityResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHyperinstanceClustersCapacityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
