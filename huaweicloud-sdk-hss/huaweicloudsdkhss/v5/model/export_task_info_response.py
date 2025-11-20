# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTaskInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id'
    }

    def __init__(self, task_id=None):
        r"""ExportTaskInfoResponse

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**： 导出任务ID **取值范围**： 字符长度0-128位 
        :type task_id: str
        """
        
        super().__init__()

        self._task_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportTaskInfoResponse.

        **参数解释**： 导出任务ID **取值范围**： 字符长度0-128位 

        :return: The task_id of this ExportTaskInfoResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportTaskInfoResponse.

        **参数解释**： 导出任务ID **取值范围**： 字符长度0-128位 

        :param task_id: The task_id of this ExportTaskInfoResponse.
        :type task_id: str
        """
        self._task_id = task_id

    def to_dict(self):
        import warnings
        warnings.warn("ExportTaskInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExportTaskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
