# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOverviewDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'dimension_stats': 'list[AiOverviewDimensionStats]',
        'source_info': 'AiOverviewSourceInfo'
    }

    attribute_map = {
        'source': 'source',
        'dimension_stats': 'dimension_stats',
        'source_info': 'source_info'
    }

    def __init__(self, source=None, dimension_stats=None, source_info=None):
        r"""AiOverviewDataList

        The model defined in huaweicloud sdk

        :param source: **参数解释**： 产品类型 **取值范围**： - AgentArts - OfficeAce - OpenClaw 
        :type source: str
        :param dimension_stats: **参数解释**: 维度统计列表（type&#x3D;alarm/risk时返回） **取值范围**: 不涉及 
        :type dimension_stats: list[:class:`huaweicloudsdkhss.v5.AiOverviewDimensionStats`]
        :param source_info: 
        :type source_info: :class:`huaweicloudsdkhss.v5.AiOverviewSourceInfo`
        """
        
        

        self._source = None
        self._dimension_stats = None
        self._source_info = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if dimension_stats is not None:
            self.dimension_stats = dimension_stats
        if source_info is not None:
            self.source_info = source_info

    @property
    def source(self):
        r"""Gets the source of this AiOverviewDataList.

        **参数解释**： 产品类型 **取值范围**： - AgentArts - OfficeAce - OpenClaw 

        :return: The source of this AiOverviewDataList.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AiOverviewDataList.

        **参数解释**： 产品类型 **取值范围**： - AgentArts - OfficeAce - OpenClaw 

        :param source: The source of this AiOverviewDataList.
        :type source: str
        """
        self._source = source

    @property
    def dimension_stats(self):
        r"""Gets the dimension_stats of this AiOverviewDataList.

        **参数解释**: 维度统计列表（type=alarm/risk时返回） **取值范围**: 不涉及 

        :return: The dimension_stats of this AiOverviewDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AiOverviewDimensionStats`]
        """
        return self._dimension_stats

    @dimension_stats.setter
    def dimension_stats(self, dimension_stats):
        r"""Sets the dimension_stats of this AiOverviewDataList.

        **参数解释**: 维度统计列表（type=alarm/risk时返回） **取值范围**: 不涉及 

        :param dimension_stats: The dimension_stats of this AiOverviewDataList.
        :type dimension_stats: list[:class:`huaweicloudsdkhss.v5.AiOverviewDimensionStats`]
        """
        self._dimension_stats = dimension_stats

    @property
    def source_info(self):
        r"""Gets the source_info of this AiOverviewDataList.

        :return: The source_info of this AiOverviewDataList.
        :rtype: :class:`huaweicloudsdkhss.v5.AiOverviewSourceInfo`
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        r"""Sets the source_info of this AiOverviewDataList.

        :param source_info: The source_info of this AiOverviewDataList.
        :type source_info: :class:`huaweicloudsdkhss.v5.AiOverviewSourceInfo`
        """
        self._source_info = source_info

    def to_dict(self):
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
        if not isinstance(other, AiOverviewDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
