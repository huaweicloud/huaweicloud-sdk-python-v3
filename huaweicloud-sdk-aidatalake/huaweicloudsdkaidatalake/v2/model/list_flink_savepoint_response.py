# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkSavepointResponse(SdkResponse):

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
        'savepoints': 'list[FlinkSavepointSummary]'
    }

    attribute_map = {
        'count': 'count',
        'savepoints': 'savepoints'
    }

    def __init__(self, count=None, savepoints=None):
        r"""ListFlinkSavepointResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**：Savepoint总数。 **取值范围**：0~2147483647。 
        :type count: int
        :param savepoints: **参数解释**：Savepoint摘要信息列表。可显示0~1000个FlinkSavepointSummary对象。 
        :type savepoints: list[:class:`huaweicloudsdkaidatalake.v2.FlinkSavepointSummary`]
        """
        
        super().__init__()

        self._count = None
        self._savepoints = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if savepoints is not None:
            self.savepoints = savepoints

    @property
    def count(self):
        r"""Gets the count of this ListFlinkSavepointResponse.

        **参数解释**：Savepoint总数。 **取值范围**：0~2147483647。 

        :return: The count of this ListFlinkSavepointResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFlinkSavepointResponse.

        **参数解释**：Savepoint总数。 **取值范围**：0~2147483647。 

        :param count: The count of this ListFlinkSavepointResponse.
        :type count: int
        """
        self._count = count

    @property
    def savepoints(self):
        r"""Gets the savepoints of this ListFlinkSavepointResponse.

        **参数解释**：Savepoint摘要信息列表。可显示0~1000个FlinkSavepointSummary对象。 

        :return: The savepoints of this ListFlinkSavepointResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.FlinkSavepointSummary`]
        """
        return self._savepoints

    @savepoints.setter
    def savepoints(self, savepoints):
        r"""Sets the savepoints of this ListFlinkSavepointResponse.

        **参数解释**：Savepoint摘要信息列表。可显示0~1000个FlinkSavepointSummary对象。 

        :param savepoints: The savepoints of this ListFlinkSavepointResponse.
        :type savepoints: list[:class:`huaweicloudsdkaidatalake.v2.FlinkSavepointSummary`]
        """
        self._savepoints = savepoints

    def to_dict(self):
        import warnings
        warnings.warn("ListFlinkSavepointResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFlinkSavepointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
