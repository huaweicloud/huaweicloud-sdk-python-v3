# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'results': 'list[ModifyJobResp]'
    }

    attribute_map = {
        'count': 'count',
        'results': 'results'
    }

    def __init__(self, count=None, results=None):
        r"""BatchUpdateJobResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**：  返回的任务信息总数，表示本次修改成功返回的任务数量，与results数组的长度一致。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type count: int
        :param results: **参数解释**：  批量修改任务返回列表，包含每个任务的修改结果，详情请参见ModifyJobResp对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type results: list[:class:`huaweicloudsdkdrs.v3.ModifyJobResp`]
        """
        
        super().__init__()

        self._count = None
        self._results = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if results is not None:
            self.results = results

    @property
    def count(self):
        r"""Gets the count of this BatchUpdateJobResponse.

        **参数解释**：  返回的任务信息总数，表示本次修改成功返回的任务数量，与results数组的长度一致。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The count of this BatchUpdateJobResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this BatchUpdateJobResponse.

        **参数解释**：  返回的任务信息总数，表示本次修改成功返回的任务数量，与results数组的长度一致。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param count: The count of this BatchUpdateJobResponse.
        :type count: int
        """
        self._count = count

    @property
    def results(self):
        r"""Gets the results of this BatchUpdateJobResponse.

        **参数解释**：  批量修改任务返回列表，包含每个任务的修改结果，详情请参见ModifyJobResp对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The results of this BatchUpdateJobResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ModifyJobResp`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this BatchUpdateJobResponse.

        **参数解释**：  批量修改任务返回列表，包含每个任务的修改结果，详情请参见ModifyJobResp对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param results: The results of this BatchUpdateJobResponse.
        :type results: list[:class:`huaweicloudsdkdrs.v3.ModifyJobResp`]
        """
        self._results = results

    def to_dict(self):
        import warnings
        warnings.warn("BatchUpdateJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchUpdateJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
