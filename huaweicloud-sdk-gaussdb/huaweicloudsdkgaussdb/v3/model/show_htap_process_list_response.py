# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHtapProcessListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_list': 'list[HtapProcessInfo]'
    }

    attribute_map = {
        'process_list': 'process_list'
    }

    def __init__(self, process_list=None):
        r"""ShowHtapProcessListResponse

        The model defined in huaweicloud sdk

        :param process_list: **参数解释**：  HTAP标准版查询的会话信息。  **默认值**：  不涉及。
        :type process_list: list[:class:`huaweicloudsdkgaussdb.v3.HtapProcessInfo`]
        """
        
        super().__init__()

        self._process_list = None
        self.discriminator = None

        if process_list is not None:
            self.process_list = process_list

    @property
    def process_list(self):
        r"""Gets the process_list of this ShowHtapProcessListResponse.

        **参数解释**：  HTAP标准版查询的会话信息。  **默认值**：  不涉及。

        :return: The process_list of this ShowHtapProcessListResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.HtapProcessInfo`]
        """
        return self._process_list

    @process_list.setter
    def process_list(self, process_list):
        r"""Sets the process_list of this ShowHtapProcessListResponse.

        **参数解释**：  HTAP标准版查询的会话信息。  **默认值**：  不涉及。

        :param process_list: The process_list of this ShowHtapProcessListResponse.
        :type process_list: list[:class:`huaweicloudsdkgaussdb.v3.HtapProcessInfo`]
        """
        self._process_list = process_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowHtapProcessListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowHtapProcessListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
