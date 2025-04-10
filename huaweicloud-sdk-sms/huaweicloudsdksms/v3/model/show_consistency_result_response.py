# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsistencyResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_list': 'list[ConsistencyResultRequestBodyResultList]',
        'task_id': 'str'
    }

    attribute_map = {
        'result_list': 'result_list',
        'task_id': 'task_id'
    }

    def __init__(self, result_list=None, task_id=None):
        r"""ShowConsistencyResultResponse

        The model defined in huaweicloud sdk

        :param result_list: 一致性校验结果列表
        :type result_list: list[:class:`huaweicloudsdksms.v3.ConsistencyResultRequestBodyResultList`]
        :param task_id: 任务id
        :type task_id: str
        """
        
        super(ShowConsistencyResultResponse, self).__init__()

        self._result_list = None
        self._task_id = None
        self.discriminator = None

        if result_list is not None:
            self.result_list = result_list
        if task_id is not None:
            self.task_id = task_id

    @property
    def result_list(self):
        r"""Gets the result_list of this ShowConsistencyResultResponse.

        一致性校验结果列表

        :return: The result_list of this ShowConsistencyResultResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.ConsistencyResultRequestBodyResultList`]
        """
        return self._result_list

    @result_list.setter
    def result_list(self, result_list):
        r"""Sets the result_list of this ShowConsistencyResultResponse.

        一致性校验结果列表

        :param result_list: The result_list of this ShowConsistencyResultResponse.
        :type result_list: list[:class:`huaweicloudsdksms.v3.ConsistencyResultRequestBodyResultList`]
        """
        self._result_list = result_list

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowConsistencyResultResponse.

        任务id

        :return: The task_id of this ShowConsistencyResultResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowConsistencyResultResponse.

        任务id

        :param task_id: The task_id of this ShowConsistencyResultResponse.
        :type task_id: str
        """
        self._task_id = task_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowConsistencyResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
