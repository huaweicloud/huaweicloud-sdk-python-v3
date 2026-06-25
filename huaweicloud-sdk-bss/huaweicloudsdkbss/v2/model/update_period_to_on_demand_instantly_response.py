# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePeriodToOnDemandInstantlyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'to_ondemand_service_results': 'list[ToOndemandServiceResult]'
    }

    attribute_map = {
        'to_ondemand_service_results': 'to_ondemand_service_results'
    }

    def __init__(self, to_ondemand_service_results=None):
        r"""UpdatePeriodToOnDemandInstantlyResponse

        The model defined in huaweicloud sdk

        :param to_ondemand_service_results: |参数名称：包年包月即时转按需结果| |参数约束以及描述：包年包月即时转按需结果。HTTP 200的时候返回该字段，具体参见ToOndemandServiceResult。|
        :type to_ondemand_service_results: list[:class:`huaweicloudsdkbss.v2.ToOndemandServiceResult`]
        """
        
        super().__init__()

        self._to_ondemand_service_results = None
        self.discriminator = None

        if to_ondemand_service_results is not None:
            self.to_ondemand_service_results = to_ondemand_service_results

    @property
    def to_ondemand_service_results(self):
        r"""Gets the to_ondemand_service_results of this UpdatePeriodToOnDemandInstantlyResponse.

        |参数名称：包年包月即时转按需结果| |参数约束以及描述：包年包月即时转按需结果。HTTP 200的时候返回该字段，具体参见ToOndemandServiceResult。|

        :return: The to_ondemand_service_results of this UpdatePeriodToOnDemandInstantlyResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ToOndemandServiceResult`]
        """
        return self._to_ondemand_service_results

    @to_ondemand_service_results.setter
    def to_ondemand_service_results(self, to_ondemand_service_results):
        r"""Sets the to_ondemand_service_results of this UpdatePeriodToOnDemandInstantlyResponse.

        |参数名称：包年包月即时转按需结果| |参数约束以及描述：包年包月即时转按需结果。HTTP 200的时候返回该字段，具体参见ToOndemandServiceResult。|

        :param to_ondemand_service_results: The to_ondemand_service_results of this UpdatePeriodToOnDemandInstantlyResponse.
        :type to_ondemand_service_results: list[:class:`huaweicloudsdkbss.v2.ToOndemandServiceResult`]
        """
        self._to_ondemand_service_results = to_ondemand_service_results

    def to_dict(self):
        import warnings
        warnings.warn("UpdatePeriodToOnDemandInstantlyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdatePeriodToOnDemandInstantlyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
