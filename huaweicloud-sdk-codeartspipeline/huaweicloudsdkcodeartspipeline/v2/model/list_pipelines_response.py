# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'current_system_time': 'int',
        'highest_confidentiality': 'ListPipelinesPageHighestConfidentiality',
        'number_of_hidden_data': 'int',
        'pipelines': 'list[ListPipelinesPagePipelines]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'current_system_time': 'current_system_time',
        'highest_confidentiality': 'highest_confidentiality',
        'number_of_hidden_data': 'number_of_hidden_data',
        'pipelines': 'pipelines'
    }

    def __init__(self, offset=None, limit=None, total=None, current_system_time=None, highest_confidentiality=None, number_of_hidden_data=None, pipelines=None):
        r"""ListPipelinesResponse

        The model defined in huaweicloud sdk

        :param offset: **参数解释**： 起始偏移。 **取值范围**： 不涉及。 
        :type offset: int
        :param limit: **参数解释**： 查询大小。 **取值范围**： 不涉及。 
        :type limit: int
        :param total: **参数解释**： 记录总数。 **取值范围**： 不涉及。 
        :type total: int
        :param current_system_time: **参数解释**： 当前系统时间。 **取值范围**： 不涉及。 
        :type current_system_time: int
        :param highest_confidentiality: 
        :type highest_confidentiality: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageHighestConfidentiality`
        :param number_of_hidden_data: **参数解释**： 隐藏数据数量。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 不涉及。 
        :type number_of_hidden_data: int
        :param pipelines: **参数解释**： 流水线。 **取值范围**： 不涉及。 
        :type pipelines: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPagePipelines`]
        """
        
        super().__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._current_system_time = None
        self._highest_confidentiality = None
        self._number_of_hidden_data = None
        self._pipelines = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if current_system_time is not None:
            self.current_system_time = current_system_time
        if highest_confidentiality is not None:
            self.highest_confidentiality = highest_confidentiality
        if number_of_hidden_data is not None:
            self.number_of_hidden_data = number_of_hidden_data
        if pipelines is not None:
            self.pipelines = pipelines

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelinesResponse.

        **参数解释**： 起始偏移。 **取值范围**： 不涉及。 

        :return: The offset of this ListPipelinesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelinesResponse.

        **参数解释**： 起始偏移。 **取值范围**： 不涉及。 

        :param offset: The offset of this ListPipelinesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelinesResponse.

        **参数解释**： 查询大小。 **取值范围**： 不涉及。 

        :return: The limit of this ListPipelinesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelinesResponse.

        **参数解释**： 查询大小。 **取值范围**： 不涉及。 

        :param limit: The limit of this ListPipelinesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListPipelinesResponse.

        **参数解释**： 记录总数。 **取值范围**： 不涉及。 

        :return: The total of this ListPipelinesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPipelinesResponse.

        **参数解释**： 记录总数。 **取值范围**： 不涉及。 

        :param total: The total of this ListPipelinesResponse.
        :type total: int
        """
        self._total = total

    @property
    def current_system_time(self):
        r"""Gets the current_system_time of this ListPipelinesResponse.

        **参数解释**： 当前系统时间。 **取值范围**： 不涉及。 

        :return: The current_system_time of this ListPipelinesResponse.
        :rtype: int
        """
        return self._current_system_time

    @current_system_time.setter
    def current_system_time(self, current_system_time):
        r"""Sets the current_system_time of this ListPipelinesResponse.

        **参数解释**： 当前系统时间。 **取值范围**： 不涉及。 

        :param current_system_time: The current_system_time of this ListPipelinesResponse.
        :type current_system_time: int
        """
        self._current_system_time = current_system_time

    @property
    def highest_confidentiality(self):
        r"""Gets the highest_confidentiality of this ListPipelinesResponse.

        :return: The highest_confidentiality of this ListPipelinesResponse.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageHighestConfidentiality`
        """
        return self._highest_confidentiality

    @highest_confidentiality.setter
    def highest_confidentiality(self, highest_confidentiality):
        r"""Sets the highest_confidentiality of this ListPipelinesResponse.

        :param highest_confidentiality: The highest_confidentiality of this ListPipelinesResponse.
        :type highest_confidentiality: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageHighestConfidentiality`
        """
        self._highest_confidentiality = highest_confidentiality

    @property
    def number_of_hidden_data(self):
        r"""Gets the number_of_hidden_data of this ListPipelinesResponse.

        **参数解释**： 隐藏数据数量。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 不涉及。 

        :return: The number_of_hidden_data of this ListPipelinesResponse.
        :rtype: int
        """
        return self._number_of_hidden_data

    @number_of_hidden_data.setter
    def number_of_hidden_data(self, number_of_hidden_data):
        r"""Sets the number_of_hidden_data of this ListPipelinesResponse.

        **参数解释**： 隐藏数据数量。 **约束限制**： 非涉密场景无该字段。 **取值范围**： 不涉及。 

        :param number_of_hidden_data: The number_of_hidden_data of this ListPipelinesResponse.
        :type number_of_hidden_data: int
        """
        self._number_of_hidden_data = number_of_hidden_data

    @property
    def pipelines(self):
        r"""Gets the pipelines of this ListPipelinesResponse.

        **参数解释**： 流水线。 **取值范围**： 不涉及。 

        :return: The pipelines of this ListPipelinesResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPagePipelines`]
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        r"""Sets the pipelines of this ListPipelinesResponse.

        **参数解释**： 流水线。 **取值范围**： 不涉及。 

        :param pipelines: The pipelines of this ListPipelinesResponse.
        :type pipelines: list[:class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPagePipelines`]
        """
        self._pipelines = pipelines

    def to_dict(self):
        import warnings
        warnings.warn("ListPipelinesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPipelinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
