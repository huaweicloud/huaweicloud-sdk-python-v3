# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'es_result': 'EsMonitorBody',
        'result': 'list[dict(str, object)]'
    }

    attribute_map = {
        'es_result': 'es_result',
        'result': 'result'
    }

    def __init__(self, es_result=None, result=None):
        r"""ShowMonitorStatsResponse

        The model defined in huaweicloud sdk

        :param es_result: 
        :type es_result: :class:`huaweicloudsdksecmaster.v2.EsMonitorBody`
        :param result: pulsar返回的结果列表
        :type result: list[dict(str, object)]
        """
        
        super().__init__()

        self._es_result = None
        self._result = None
        self.discriminator = None

        if es_result is not None:
            self.es_result = es_result
        if result is not None:
            self.result = result

    @property
    def es_result(self):
        r"""Gets the es_result of this ShowMonitorStatsResponse.

        :return: The es_result of this ShowMonitorStatsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.EsMonitorBody`
        """
        return self._es_result

    @es_result.setter
    def es_result(self, es_result):
        r"""Sets the es_result of this ShowMonitorStatsResponse.

        :param es_result: The es_result of this ShowMonitorStatsResponse.
        :type es_result: :class:`huaweicloudsdksecmaster.v2.EsMonitorBody`
        """
        self._es_result = es_result

    @property
    def result(self):
        r"""Gets the result of this ShowMonitorStatsResponse.

        pulsar返回的结果列表

        :return: The result of this ShowMonitorStatsResponse.
        :rtype: list[dict(str, object)]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowMonitorStatsResponse.

        pulsar返回的结果列表

        :param result: The result of this ShowMonitorStatsResponse.
        :type result: list[dict(str, object)]
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowMonitorStatsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMonitorStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
