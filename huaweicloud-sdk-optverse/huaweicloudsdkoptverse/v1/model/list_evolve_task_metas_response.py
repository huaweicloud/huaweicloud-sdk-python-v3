# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEvolveTaskMetasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[EvolveTaskRsp]',
        'total_records': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'total_records': 'total_records'
    }

    def __init__(self, tasks=None, total_records=None):
        r"""ListEvolveTaskMetasResponse

        The model defined in huaweicloud sdk

        :param tasks: 演化任务结构体列表
        :type tasks: list[:class:`huaweicloudsdkoptverse.v1.EvolveTaskRsp`]
        :param total_records: 查询列表总数
        :type total_records: int
        """
        
        super().__init__()

        self._tasks = None
        self._total_records = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if total_records is not None:
            self.total_records = total_records

    @property
    def tasks(self):
        r"""Gets the tasks of this ListEvolveTaskMetasResponse.

        演化任务结构体列表

        :return: The tasks of this ListEvolveTaskMetasResponse.
        :rtype: list[:class:`huaweicloudsdkoptverse.v1.EvolveTaskRsp`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListEvolveTaskMetasResponse.

        演化任务结构体列表

        :param tasks: The tasks of this ListEvolveTaskMetasResponse.
        :type tasks: list[:class:`huaweicloudsdkoptverse.v1.EvolveTaskRsp`]
        """
        self._tasks = tasks

    @property
    def total_records(self):
        r"""Gets the total_records of this ListEvolveTaskMetasResponse.

        查询列表总数

        :return: The total_records of this ListEvolveTaskMetasResponse.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        r"""Sets the total_records of this ListEvolveTaskMetasResponse.

        查询列表总数

        :param total_records: The total_records of this ListEvolveTaskMetasResponse.
        :type total_records: int
        """
        self._total_records = total_records

    def to_dict(self):
        import warnings
        warnings.warn("ListEvolveTaskMetasResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListEvolveTaskMetasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
