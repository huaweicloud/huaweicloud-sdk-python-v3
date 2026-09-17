# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVariableGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_variable_groups': 'list[ListVariableGroupsRespPipelineVariableGroups]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'pipeline_variable_groups': 'pipeline_variable_groups',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, pipeline_variable_groups=None, offset=None, limit=None, total=None):
        r"""ListVariableGroupsResponse

        The model defined in huaweicloud sdk

        :param pipeline_variable_groups: 详情列表
        :type pipeline_variable_groups: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespPipelineVariableGroups`]
        :param offset: 偏移量
        :type offset: int
        :param limit: 单页条数·
        :type limit: int
        :param total: **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 
        :type total: int
        """
        
        super().__init__()

        self._pipeline_variable_groups = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if pipeline_variable_groups is not None:
            self.pipeline_variable_groups = pipeline_variable_groups
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def pipeline_variable_groups(self):
        r"""Gets the pipeline_variable_groups of this ListVariableGroupsResponse.

        详情列表

        :return: The pipeline_variable_groups of this ListVariableGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespPipelineVariableGroups`]
        """
        return self._pipeline_variable_groups

    @pipeline_variable_groups.setter
    def pipeline_variable_groups(self, pipeline_variable_groups):
        r"""Sets the pipeline_variable_groups of this ListVariableGroupsResponse.

        详情列表

        :param pipeline_variable_groups: The pipeline_variable_groups of this ListVariableGroupsResponse.
        :type pipeline_variable_groups: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListVariableGroupsRespPipelineVariableGroups`]
        """
        self._pipeline_variable_groups = pipeline_variable_groups

    @property
    def offset(self):
        r"""Gets the offset of this ListVariableGroupsResponse.

        偏移量

        :return: The offset of this ListVariableGroupsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVariableGroupsResponse.

        偏移量

        :param offset: The offset of this ListVariableGroupsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVariableGroupsResponse.

        单页条数·

        :return: The limit of this ListVariableGroupsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVariableGroupsResponse.

        单页条数·

        :param limit: The limit of this ListVariableGroupsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListVariableGroupsResponse.

        **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 

        :return: The total of this ListVariableGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListVariableGroupsResponse.

        **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 

        :param total: The total of this ListVariableGroupsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListVariableGroupsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListVariableGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
