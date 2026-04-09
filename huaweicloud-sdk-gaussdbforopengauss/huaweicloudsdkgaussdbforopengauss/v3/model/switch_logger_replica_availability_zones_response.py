# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchLoggerReplicaAvailabilityZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_infos': 'list[AzInformationResult]'
    }

    attribute_map = {
        'availability_zone_infos': 'availability_zone_infos'
    }

    def __init__(self, availability_zone_infos=None):
        r"""SwitchLoggerReplicaAvailabilityZonesResponse

        The model defined in huaweicloud sdk

        :param availability_zone_infos: **参数解释**: 选择日志节点AZ列表。
        :type availability_zone_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AzInformationResult`]
        """
        
        super().__init__()

        self._availability_zone_infos = None
        self.discriminator = None

        if availability_zone_infos is not None:
            self.availability_zone_infos = availability_zone_infos

    @property
    def availability_zone_infos(self):
        r"""Gets the availability_zone_infos of this SwitchLoggerReplicaAvailabilityZonesResponse.

        **参数解释**: 选择日志节点AZ列表。

        :return: The availability_zone_infos of this SwitchLoggerReplicaAvailabilityZonesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AzInformationResult`]
        """
        return self._availability_zone_infos

    @availability_zone_infos.setter
    def availability_zone_infos(self, availability_zone_infos):
        r"""Sets the availability_zone_infos of this SwitchLoggerReplicaAvailabilityZonesResponse.

        **参数解释**: 选择日志节点AZ列表。

        :param availability_zone_infos: The availability_zone_infos of this SwitchLoggerReplicaAvailabilityZonesResponse.
        :type availability_zone_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AzInformationResult`]
        """
        self._availability_zone_infos = availability_zone_infos

    def to_dict(self):
        import warnings
        warnings.warn("SwitchLoggerReplicaAvailabilityZonesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SwitchLoggerReplicaAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
