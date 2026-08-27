# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRunningDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta_start_at': 'int',
        'meta_finish_at': 'int'
    }

    attribute_map = {
        'meta_start_at': 'meta_start_at',
        'meta_finish_at': 'meta_finish_at'
    }

    def __init__(self, meta_start_at=None, meta_finish_at=None):
        r"""ShowTaskRunningDetailsResponse

        The model defined in huaweicloud sdk

        :param meta_start_at: **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type meta_start_at: int
        :param meta_finish_at: **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type meta_finish_at: int
        """
        
        super().__init__()

        self._meta_start_at = None
        self._meta_finish_at = None
        self.discriminator = None

        if meta_start_at is not None:
            self.meta_start_at = meta_start_at
        if meta_finish_at is not None:
            self.meta_finish_at = meta_finish_at

    @property
    def meta_start_at(self):
        r"""Gets the meta_start_at of this ShowTaskRunningDetailsResponse.

        **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The meta_start_at of this ShowTaskRunningDetailsResponse.
        :rtype: int
        """
        return self._meta_start_at

    @meta_start_at.setter
    def meta_start_at(self, meta_start_at):
        r"""Sets the meta_start_at of this ShowTaskRunningDetailsResponse.

        **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param meta_start_at: The meta_start_at of this ShowTaskRunningDetailsResponse.
        :type meta_start_at: int
        """
        self._meta_start_at = meta_start_at

    @property
    def meta_finish_at(self):
        r"""Gets the meta_finish_at of this ShowTaskRunningDetailsResponse.

        **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The meta_finish_at of this ShowTaskRunningDetailsResponse.
        :rtype: int
        """
        return self._meta_finish_at

    @meta_finish_at.setter
    def meta_finish_at(self, meta_finish_at):
        r"""Sets the meta_finish_at of this ShowTaskRunningDetailsResponse.

        **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param meta_finish_at: The meta_finish_at of this ShowTaskRunningDetailsResponse.
        :type meta_finish_at: int
        """
        self._meta_finish_at = meta_finish_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskRunningDetailsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTaskRunningDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
