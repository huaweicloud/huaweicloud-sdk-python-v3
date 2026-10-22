# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2EndpointsMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[V2EndpointMetrics]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, data=None, x_request_id=None):
        r"""ShowV2EndpointsMetricsResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetrics`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def data(self):
        r"""Gets the data of this ShowV2EndpointsMetricsResponse.

        :return: The data of this ShowV2EndpointsMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetrics`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowV2EndpointsMetricsResponse.

        :param data: The data of this ShowV2EndpointsMetricsResponse.
        :type data: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointMetrics`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowV2EndpointsMetricsResponse.

        :return: The x_request_id of this ShowV2EndpointsMetricsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowV2EndpointsMetricsResponse.

        :param x_request_id: The x_request_id of this ShowV2EndpointsMetricsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowV2EndpointsMetricsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowV2EndpointsMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
