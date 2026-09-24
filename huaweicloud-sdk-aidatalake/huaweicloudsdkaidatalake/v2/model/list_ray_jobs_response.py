# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRayJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'previous_marker': 'str',
        'current_count': 'int',
        'jobs': 'list[RayJobInfo]'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'previous_marker': 'previous_marker',
        'current_count': 'current_count',
        'jobs': 'jobs'
    }

    def __init__(self, next_marker=None, previous_marker=None, current_count=None, jobs=None):
        r"""ListRayJobsResponse

        The model defined in huaweicloud sdk

        :param next_marker: **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type next_marker: str
        :param previous_marker: **参数解释**：返回前一页查询地址，为空则表示是第一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type previous_marker: str
        :param current_count: **参数解释**：本次查询记录总数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type current_count: int
        :param jobs: **参数解释**：Ray作业信息列表，包含作业名称、状态、配置等详细信息。数组中的每个元素为一个RayJobInfo对象。 **约束限制**：0~100。
        :type jobs: list[:class:`huaweicloudsdkaidatalake.v2.RayJobInfo`]
        """
        
        super().__init__()

        self._next_marker = None
        self._previous_marker = None
        self._current_count = None
        self._jobs = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker
        if previous_marker is not None:
            self.previous_marker = previous_marker
        if current_count is not None:
            self.current_count = current_count
        if jobs is not None:
            self.jobs = jobs

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListRayJobsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The next_marker of this ListRayJobsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListRayJobsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param next_marker: The next_marker of this ListRayJobsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def previous_marker(self):
        r"""Gets the previous_marker of this ListRayJobsResponse.

        **参数解释**：返回前一页查询地址，为空则表示是第一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The previous_marker of this ListRayJobsResponse.
        :rtype: str
        """
        return self._previous_marker

    @previous_marker.setter
    def previous_marker(self, previous_marker):
        r"""Sets the previous_marker of this ListRayJobsResponse.

        **参数解释**：返回前一页查询地址，为空则表示是第一页。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param previous_marker: The previous_marker of this ListRayJobsResponse.
        :type previous_marker: str
        """
        self._previous_marker = previous_marker

    @property
    def current_count(self):
        r"""Gets the current_count of this ListRayJobsResponse.

        **参数解释**：本次查询记录总数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The current_count of this ListRayJobsResponse.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        r"""Sets the current_count of this ListRayJobsResponse.

        **参数解释**：本次查询记录总数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param current_count: The current_count of this ListRayJobsResponse.
        :type current_count: int
        """
        self._current_count = current_count

    @property
    def jobs(self):
        r"""Gets the jobs of this ListRayJobsResponse.

        **参数解释**：Ray作业信息列表，包含作业名称、状态、配置等详细信息。数组中的每个元素为一个RayJobInfo对象。 **约束限制**：0~100。

        :return: The jobs of this ListRayJobsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.RayJobInfo`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListRayJobsResponse.

        **参数解释**：Ray作业信息列表，包含作业名称、状态、配置等详细信息。数组中的每个元素为一个RayJobInfo对象。 **约束限制**：0~100。

        :param jobs: The jobs of this ListRayJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkaidatalake.v2.RayJobInfo`]
        """
        self._jobs = jobs

    def to_dict(self):
        import warnings
        warnings.warn("ListRayJobsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRayJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
