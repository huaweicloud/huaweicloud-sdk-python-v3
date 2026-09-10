# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelServiceTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[ModelServiceTaskRsp]',
        'count': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'count': 'count'
    }

    def __init__(self, tasks=None, count=None):
        r"""ListModelServiceTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type tasks: list[:class:`huaweicloudsdkoptverse.v1.ModelServiceTaskRsp`]
        :param count: **参数解释**： 供应商模型个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        """
        
        super().__init__()

        self._tasks = None
        self._count = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if count is not None:
            self.count = count

    @property
    def tasks(self):
        r"""Gets the tasks of this ListModelServiceTasksResponse.

        **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The tasks of this ListModelServiceTasksResponse.
        :rtype: list[:class:`huaweicloudsdkoptverse.v1.ModelServiceTaskRsp`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListModelServiceTasksResponse.

        **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param tasks: The tasks of this ListModelServiceTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkoptverse.v1.ModelServiceTaskRsp`]
        """
        self._tasks = tasks

    @property
    def count(self):
        r"""Gets the count of this ListModelServiceTasksResponse.

        **参数解释**： 供应商模型个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListModelServiceTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListModelServiceTasksResponse.

        **参数解释**： 供应商模型个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListModelServiceTasksResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListModelServiceTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListModelServiceTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
