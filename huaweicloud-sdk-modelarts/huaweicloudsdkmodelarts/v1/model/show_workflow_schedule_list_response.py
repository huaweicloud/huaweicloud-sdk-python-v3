# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowScheduleListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedules': 'list[WorkflowScheduleResp]'
    }

    attribute_map = {
        'schedules': 'schedules'
    }

    def __init__(self, schedules=None):
        r"""ShowWorkflowScheduleListResponse

        The model defined in huaweicloud sdk

        :param schedules: **参数解释**：工作流定时调度列表
        :type schedules: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowScheduleResp`]
        """
        
        super().__init__()

        self._schedules = None
        self.discriminator = None

        if schedules is not None:
            self.schedules = schedules

    @property
    def schedules(self):
        r"""Gets the schedules of this ShowWorkflowScheduleListResponse.

        **参数解释**：工作流定时调度列表

        :return: The schedules of this ShowWorkflowScheduleListResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowScheduleResp`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        r"""Sets the schedules of this ShowWorkflowScheduleListResponse.

        **参数解释**：工作流定时调度列表

        :param schedules: The schedules of this ShowWorkflowScheduleListResponse.
        :type schedules: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowScheduleResp`]
        """
        self._schedules = schedules

    def to_dict(self):
        import warnings
        warnings.warn("ShowWorkflowScheduleListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowWorkflowScheduleListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
