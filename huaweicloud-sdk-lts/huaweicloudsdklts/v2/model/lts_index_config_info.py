# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSIndexConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_text_index': 'LTSFullTextIndexInfo',
        'fields': 'list[LTSFieldsInfo]',
        'sql_analysis_enable': 'bool',
        'log_stream_id': 'str',
        'fast_analysis_sample_count': 'int'
    }

    attribute_map = {
        'full_text_index': 'fullTextIndex',
        'fields': 'fields',
        'sql_analysis_enable': 'sqlAnalysisEnable',
        'log_stream_id': 'logStreamId',
        'fast_analysis_sample_count': 'fastAnalysisSampleCount'
    }

    def __init__(self, full_text_index=None, fields=None, sql_analysis_enable=None, log_stream_id=None, fast_analysis_sample_count=None):
        r"""LTSIndexConfigInfo

        The model defined in huaweicloud sdk

        :param full_text_index: 
        :type full_text_index: :class:`huaweicloudsdklts.v2.LTSFullTextIndexInfo`
        :param fields: 字段索引配置
        :type fields: list[:class:`huaweicloudsdklts.v2.LTSFieldsInfo`]
        :param sql_analysis_enable: 是否开启可视化
        :type sql_analysis_enable: bool
        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param fast_analysis_sample_count: **参数解释：** 快速分析采样日志条数。 **约束限制：** 不涉及。 **取值范围：** 最小值：100000 最大值：10000000 **默认取值：** 100000
        :type fast_analysis_sample_count: int
        """
        
        

        self._full_text_index = None
        self._fields = None
        self._sql_analysis_enable = None
        self._log_stream_id = None
        self._fast_analysis_sample_count = None
        self.discriminator = None

        self.full_text_index = full_text_index
        if fields is not None:
            self.fields = fields
        if sql_analysis_enable is not None:
            self.sql_analysis_enable = sql_analysis_enable
        self.log_stream_id = log_stream_id
        if fast_analysis_sample_count is not None:
            self.fast_analysis_sample_count = fast_analysis_sample_count

    @property
    def full_text_index(self):
        r"""Gets the full_text_index of this LTSIndexConfigInfo.

        :return: The full_text_index of this LTSIndexConfigInfo.
        :rtype: :class:`huaweicloudsdklts.v2.LTSFullTextIndexInfo`
        """
        return self._full_text_index

    @full_text_index.setter
    def full_text_index(self, full_text_index):
        r"""Sets the full_text_index of this LTSIndexConfigInfo.

        :param full_text_index: The full_text_index of this LTSIndexConfigInfo.
        :type full_text_index: :class:`huaweicloudsdklts.v2.LTSFullTextIndexInfo`
        """
        self._full_text_index = full_text_index

    @property
    def fields(self):
        r"""Gets the fields of this LTSIndexConfigInfo.

        字段索引配置

        :return: The fields of this LTSIndexConfigInfo.
        :rtype: list[:class:`huaweicloudsdklts.v2.LTSFieldsInfo`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this LTSIndexConfigInfo.

        字段索引配置

        :param fields: The fields of this LTSIndexConfigInfo.
        :type fields: list[:class:`huaweicloudsdklts.v2.LTSFieldsInfo`]
        """
        self._fields = fields

    @property
    def sql_analysis_enable(self):
        r"""Gets the sql_analysis_enable of this LTSIndexConfigInfo.

        是否开启可视化

        :return: The sql_analysis_enable of this LTSIndexConfigInfo.
        :rtype: bool
        """
        return self._sql_analysis_enable

    @sql_analysis_enable.setter
    def sql_analysis_enable(self, sql_analysis_enable):
        r"""Sets the sql_analysis_enable of this LTSIndexConfigInfo.

        是否开启可视化

        :param sql_analysis_enable: The sql_analysis_enable of this LTSIndexConfigInfo.
        :type sql_analysis_enable: bool
        """
        self._sql_analysis_enable = sql_analysis_enable

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LTSIndexConfigInfo.

        日志流id

        :return: The log_stream_id of this LTSIndexConfigInfo.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LTSIndexConfigInfo.

        日志流id

        :param log_stream_id: The log_stream_id of this LTSIndexConfigInfo.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def fast_analysis_sample_count(self):
        r"""Gets the fast_analysis_sample_count of this LTSIndexConfigInfo.

        **参数解释：** 快速分析采样日志条数。 **约束限制：** 不涉及。 **取值范围：** 最小值：100000 最大值：10000000 **默认取值：** 100000

        :return: The fast_analysis_sample_count of this LTSIndexConfigInfo.
        :rtype: int
        """
        return self._fast_analysis_sample_count

    @fast_analysis_sample_count.setter
    def fast_analysis_sample_count(self, fast_analysis_sample_count):
        r"""Sets the fast_analysis_sample_count of this LTSIndexConfigInfo.

        **参数解释：** 快速分析采样日志条数。 **约束限制：** 不涉及。 **取值范围：** 最小值：100000 最大值：10000000 **默认取值：** 100000

        :param fast_analysis_sample_count: The fast_analysis_sample_count of this LTSIndexConfigInfo.
        :type fast_analysis_sample_count: int
        """
        self._fast_analysis_sample_count = fast_analysis_sample_count

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
        if not isinstance(other, LTSIndexConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
