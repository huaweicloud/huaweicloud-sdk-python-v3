# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_basic_info': 'TaskEntity',
        'task_additional_info': 'TaskAdditionalInfo'
    }

    attribute_map = {
        'task_basic_info': 'task_basic_info',
        'task_additional_info': 'task_additional_info'
    }

    def __init__(self, task_basic_info=None, task_additional_info=None):
        r"""ShowTaskResponse

        The model defined in huaweicloud sdk

        :param task_basic_info: 
        :type task_basic_info: :class:`huaweicloudsdkbcc.v1.TaskEntity`
        :param task_additional_info: 
        :type task_additional_info: :class:`huaweicloudsdkbcc.v1.TaskAdditionalInfo`
        """
        
        super().__init__()

        self._task_basic_info = None
        self._task_additional_info = None
        self.discriminator = None

        if task_basic_info is not None:
            self.task_basic_info = task_basic_info
        if task_additional_info is not None:
            self.task_additional_info = task_additional_info

    @property
    def task_basic_info(self):
        r"""Gets the task_basic_info of this ShowTaskResponse.

        :return: The task_basic_info of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.TaskEntity`
        """
        return self._task_basic_info

    @task_basic_info.setter
    def task_basic_info(self, task_basic_info):
        r"""Sets the task_basic_info of this ShowTaskResponse.

        :param task_basic_info: The task_basic_info of this ShowTaskResponse.
        :type task_basic_info: :class:`huaweicloudsdkbcc.v1.TaskEntity`
        """
        self._task_basic_info = task_basic_info

    @property
    def task_additional_info(self):
        r"""Gets the task_additional_info of this ShowTaskResponse.

        :return: The task_additional_info of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.TaskAdditionalInfo`
        """
        return self._task_additional_info

    @task_additional_info.setter
    def task_additional_info(self, task_additional_info):
        r"""Sets the task_additional_info of this ShowTaskResponse.

        :param task_additional_info: The task_additional_info of this ShowTaskResponse.
        :type task_additional_info: :class:`huaweicloudsdkbcc.v1.TaskAdditionalInfo`
        """
        self._task_additional_info = task_additional_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
