# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAvailableVpcsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpcs': 'list[Vpc]',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'vpcs': 'vpcs',
        'x_trace_id': 'X-TRACE-ID'
    }

    def __init__(self, vpcs=None, x_trace_id=None):
        r"""GetAvailableVpcsResponse

        The model defined in huaweicloud sdk

        :param vpcs: 可用的VPC列表
        :type vpcs: list[:class:`huaweicloudsdkrds.v3.Vpc`]
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._vpcs = None
        self._x_trace_id = None
        self.discriminator = None

        if vpcs is not None:
            self.vpcs = vpcs
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def vpcs(self):
        r"""Gets the vpcs of this GetAvailableVpcsResponse.

        可用的VPC列表

        :return: The vpcs of this GetAvailableVpcsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Vpc`]
        """
        return self._vpcs

    @vpcs.setter
    def vpcs(self, vpcs):
        r"""Sets the vpcs of this GetAvailableVpcsResponse.

        可用的VPC列表

        :param vpcs: The vpcs of this GetAvailableVpcsResponse.
        :type vpcs: list[:class:`huaweicloudsdkrds.v3.Vpc`]
        """
        self._vpcs = vpcs

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this GetAvailableVpcsResponse.

        :return: The x_trace_id of this GetAvailableVpcsResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this GetAvailableVpcsResponse.

        :param x_trace_id: The x_trace_id of this GetAvailableVpcsResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("GetAvailableVpcsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetAvailableVpcsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
