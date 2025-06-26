# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceSignatureExecutionSubtasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_tasks': 'list[SignatureExecutionSubTask]',
        'total': 'int'
    }

    attribute_map = {
        'sub_tasks': 'sub_tasks',
        'total': 'total'
    }

    def __init__(self, sub_tasks=None, total=None):
        r"""ListInstanceSignatureExecutionSubtasksResponse

        The model defined in huaweicloud sdk

        :param sub_tasks: 签名策略执行记录子任务列表
        :type sub_tasks: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionSubTask`]
        :param total: 签名策略执行记录子任务总数
        :type total: int
        """
        
        super(ListInstanceSignatureExecutionSubtasksResponse, self).__init__()

        self._sub_tasks = None
        self._total = None
        self.discriminator = None

        if sub_tasks is not None:
            self.sub_tasks = sub_tasks
        if total is not None:
            self.total = total

    @property
    def sub_tasks(self):
        r"""Gets the sub_tasks of this ListInstanceSignatureExecutionSubtasksResponse.

        签名策略执行记录子任务列表

        :return: The sub_tasks of this ListInstanceSignatureExecutionSubtasksResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionSubTask`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        r"""Sets the sub_tasks of this ListInstanceSignatureExecutionSubtasksResponse.

        签名策略执行记录子任务列表

        :param sub_tasks: The sub_tasks of this ListInstanceSignatureExecutionSubtasksResponse.
        :type sub_tasks: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionSubTask`]
        """
        self._sub_tasks = sub_tasks

    @property
    def total(self):
        r"""Gets the total of this ListInstanceSignatureExecutionSubtasksResponse.

        签名策略执行记录子任务总数

        :return: The total of this ListInstanceSignatureExecutionSubtasksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceSignatureExecutionSubtasksResponse.

        签名策略执行记录子任务总数

        :param total: The total of this ListInstanceSignatureExecutionSubtasksResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceSignatureExecutionSubtasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
