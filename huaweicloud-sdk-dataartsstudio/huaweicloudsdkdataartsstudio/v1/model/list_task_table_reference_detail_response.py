# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskTableReferenceDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'task_table_detail_list': 'list[TaskTableReferenceDetailResponse]'
    }

    attribute_map = {
        'total': 'total',
        'task_table_detail_list': 'task_table_detail_list'
    }

    def __init__(self, total=None, task_table_detail_list=None):
        r"""ListTaskTableReferenceDetailResponse

        The model defined in huaweicloud sdk

        :param total: 引用的作业数量。
        :type total: int
        :param task_table_detail_list: 引用作业的详情。
        :type task_table_detail_list: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskTableReferenceDetailResponse`]
        """
        
        super().__init__()

        self._total = None
        self._task_table_detail_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if task_table_detail_list is not None:
            self.task_table_detail_list = task_table_detail_list

    @property
    def total(self):
        r"""Gets the total of this ListTaskTableReferenceDetailResponse.

        引用的作业数量。

        :return: The total of this ListTaskTableReferenceDetailResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTaskTableReferenceDetailResponse.

        引用的作业数量。

        :param total: The total of this ListTaskTableReferenceDetailResponse.
        :type total: int
        """
        self._total = total

    @property
    def task_table_detail_list(self):
        r"""Gets the task_table_detail_list of this ListTaskTableReferenceDetailResponse.

        引用作业的详情。

        :return: The task_table_detail_list of this ListTaskTableReferenceDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskTableReferenceDetailResponse`]
        """
        return self._task_table_detail_list

    @task_table_detail_list.setter
    def task_table_detail_list(self, task_table_detail_list):
        r"""Sets the task_table_detail_list of this ListTaskTableReferenceDetailResponse.

        引用作业的详情。

        :param task_table_detail_list: The task_table_detail_list of this ListTaskTableReferenceDetailResponse.
        :type task_table_detail_list: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskTableReferenceDetailResponse`]
        """
        self._task_table_detail_list = task_table_detail_list

    def to_dict(self):
        import warnings
        warnings.warn("ListTaskTableReferenceDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTaskTableReferenceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
