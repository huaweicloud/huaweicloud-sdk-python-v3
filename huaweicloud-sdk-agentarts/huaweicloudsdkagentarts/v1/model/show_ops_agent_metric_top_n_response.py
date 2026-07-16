# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentMetricTopNResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_list': 'list[RowList]'
    }

    attribute_map = {
        'row_list': 'row_list'
    }

    def __init__(self, row_list=None):
        r"""ShowOpsAgentMetricTopNResponse

        The model defined in huaweicloud sdk

        :param row_list: 数据
        :type row_list: list[:class:`huaweicloudsdkagentarts.v1.RowList`]
        """
        
        super().__init__()

        self._row_list = None
        self.discriminator = None

        if row_list is not None:
            self.row_list = row_list

    @property
    def row_list(self):
        r"""Gets the row_list of this ShowOpsAgentMetricTopNResponse.

        数据

        :return: The row_list of this ShowOpsAgentMetricTopNResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.RowList`]
        """
        return self._row_list

    @row_list.setter
    def row_list(self, row_list):
        r"""Sets the row_list of this ShowOpsAgentMetricTopNResponse.

        数据

        :param row_list: The row_list of this ShowOpsAgentMetricTopNResponse.
        :type row_list: list[:class:`huaweicloudsdkagentarts.v1.RowList`]
        """
        self._row_list = row_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsAgentMetricTopNResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsAgentMetricTopNResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
