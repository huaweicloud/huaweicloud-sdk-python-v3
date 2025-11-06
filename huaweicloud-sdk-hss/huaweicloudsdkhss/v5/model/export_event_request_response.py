# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportEventRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_total_num': 'int',
        'task_id': 'str'
    }

    attribute_map = {
        'record_total_num': 'record_total_num',
        'task_id': 'task_id'
    }

    def __init__(self, record_total_num=None, task_id=None):
        r"""ExportEventRequestResponse

        The model defined in huaweicloud sdk

        :param record_total_num: **参数解释**： 导出记录总数 **取值范围**： 不涉及
        :type record_total_num: int
        :param task_id: **参数解释**： 导出任务ID **取值范围**： 不涉及
        :type task_id: str
        """
        
        super().__init__()

        self._record_total_num = None
        self._task_id = None
        self.discriminator = None

        if record_total_num is not None:
            self.record_total_num = record_total_num
        if task_id is not None:
            self.task_id = task_id

    @property
    def record_total_num(self):
        r"""Gets the record_total_num of this ExportEventRequestResponse.

        **参数解释**： 导出记录总数 **取值范围**： 不涉及

        :return: The record_total_num of this ExportEventRequestResponse.
        :rtype: int
        """
        return self._record_total_num

    @record_total_num.setter
    def record_total_num(self, record_total_num):
        r"""Sets the record_total_num of this ExportEventRequestResponse.

        **参数解释**： 导出记录总数 **取值范围**： 不涉及

        :param record_total_num: The record_total_num of this ExportEventRequestResponse.
        :type record_total_num: int
        """
        self._record_total_num = record_total_num

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportEventRequestResponse.

        **参数解释**： 导出任务ID **取值范围**： 不涉及

        :return: The task_id of this ExportEventRequestResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportEventRequestResponse.

        **参数解释**： 导出任务ID **取值范围**： 不涉及

        :param task_id: The task_id of this ExportEventRequestResponse.
        :type task_id: str
        """
        self._task_id = task_id

    def to_dict(self):
        import warnings
        warnings.warn("ExportEventRequestResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExportEventRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
