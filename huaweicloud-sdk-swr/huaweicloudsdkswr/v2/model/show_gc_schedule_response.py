# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGcScheduleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule': 'ScheduleDetails',
        'parameters': 'GcParameters'
    }

    attribute_map = {
        'schedule': 'schedule',
        'parameters': 'parameters'
    }

    def __init__(self, schedule=None, parameters=None):
        r"""ShowGcScheduleResponse

        The model defined in huaweicloud sdk

        :param schedule: 
        :type schedule: :class:`huaweicloudsdkswr.v2.ScheduleDetails`
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkswr.v2.GcParameters`
        """
        
        super().__init__()

        self._schedule = None
        self._parameters = None
        self.discriminator = None

        if schedule is not None:
            self.schedule = schedule
        if parameters is not None:
            self.parameters = parameters

    @property
    def schedule(self):
        r"""Gets the schedule of this ShowGcScheduleResponse.

        :return: The schedule of this ShowGcScheduleResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.ScheduleDetails`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this ShowGcScheduleResponse.

        :param schedule: The schedule of this ShowGcScheduleResponse.
        :type schedule: :class:`huaweicloudsdkswr.v2.ScheduleDetails`
        """
        self._schedule = schedule

    @property
    def parameters(self):
        r"""Gets the parameters of this ShowGcScheduleResponse.

        :return: The parameters of this ShowGcScheduleResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.GcParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ShowGcScheduleResponse.

        :param parameters: The parameters of this ShowGcScheduleResponse.
        :type parameters: :class:`huaweicloudsdkswr.v2.GcParameters`
        """
        self._parameters = parameters

    def to_dict(self):
        import warnings
        warnings.warn("ShowGcScheduleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowGcScheduleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
