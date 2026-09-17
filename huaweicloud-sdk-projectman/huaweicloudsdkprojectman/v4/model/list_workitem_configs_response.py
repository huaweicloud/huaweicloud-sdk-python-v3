# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkitemConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'closed_workitem_readonly_mode': 'bool'
    }

    attribute_map = {
        'closed_workitem_readonly_mode': 'closed_workitem_readonly_mode'
    }

    def __init__(self, closed_workitem_readonly_mode=None):
        r"""ListWorkitemConfigsResponse

        The model defined in huaweicloud sdk

        :param closed_workitem_readonly_mode: **参数解释：** 已关闭工作项只读模式。 **取值范围：** true：无法进行编辑或修改。 false：可以进行编辑或修改。
        :type closed_workitem_readonly_mode: bool
        """
        
        super().__init__()

        self._closed_workitem_readonly_mode = None
        self.discriminator = None

        if closed_workitem_readonly_mode is not None:
            self.closed_workitem_readonly_mode = closed_workitem_readonly_mode

    @property
    def closed_workitem_readonly_mode(self):
        r"""Gets the closed_workitem_readonly_mode of this ListWorkitemConfigsResponse.

        **参数解释：** 已关闭工作项只读模式。 **取值范围：** true：无法进行编辑或修改。 false：可以进行编辑或修改。

        :return: The closed_workitem_readonly_mode of this ListWorkitemConfigsResponse.
        :rtype: bool
        """
        return self._closed_workitem_readonly_mode

    @closed_workitem_readonly_mode.setter
    def closed_workitem_readonly_mode(self, closed_workitem_readonly_mode):
        r"""Sets the closed_workitem_readonly_mode of this ListWorkitemConfigsResponse.

        **参数解释：** 已关闭工作项只读模式。 **取值范围：** true：无法进行编辑或修改。 false：可以进行编辑或修改。

        :param closed_workitem_readonly_mode: The closed_workitem_readonly_mode of this ListWorkitemConfigsResponse.
        :type closed_workitem_readonly_mode: bool
        """
        self._closed_workitem_readonly_mode = closed_workitem_readonly_mode

    def to_dict(self):
        import warnings
        warnings.warn("ListWorkitemConfigsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWorkitemConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
