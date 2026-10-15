# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataFilterRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'general_filtering_list': 'list[GeneralTransformationReq]',
        'advanced_setting_list': 'list[DataFilteringAdvancedSetting]',
        'source': 'str',
        'data_filter_type': 'str'
    }

    attribute_map = {
        'general_filtering_list': 'general_filtering_list',
        'advanced_setting_list': 'advanced_setting_list',
        'source': 'source',
        'data_filter_type': 'data_filter_type'
    }

    def __init__(self, general_filtering_list=None, advanced_setting_list=None, source=None, data_filter_type=None):
        r"""DataFilterRuleReq

        The model defined in huaweicloud sdk

        :param general_filtering_list: 数据过滤条件列表。包含需要校验的数据过滤规则信息，当data_filter_type为common（简单条件过滤）时，此参数为必填项。列表中的每个元素代表一组过滤条件，包含过滤对象列表和源库过滤条件SQL。包含以下关键字段：filter_object_list（过滤对象列表）/source_filter_condition（源库过滤条件SQL）。适用条件：data_filter_type&#x3D;common时必填。
        :type general_filtering_list: list[:class:`huaweicloudsdkdrs.v5.GeneralTransformationReq`]
        :param advanced_setting_list: 数据过滤高级设置列表。用于配置关联表场景下的高级过滤规则，包含数据库名、表名、列名、索引等详细过滤配置。当前Mysql-Mysql、Mysql-TaurusDB、TaurusDB-TaurusDB、TaurusDB-Mysql、Mysql-MariaDB、MariaDB-Mysql、MariaDB-TaurusDBL链路支持此功能。适用条件：data_filter_type&#x3D;config时必填。
        :type advanced_setting_list: list[:class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`]
        :param source: 校验请求的来源场景。用于区分数据过滤规则校验是来自数据同步任务执行场景，还是来自数据对比任务执行场景。 取值：job（数据同步任务执行时的过滤规则校验）/compare（数据对比任务执行时的过滤规则校验）
        :type source: str
        :param data_filter_type: 数据过滤类型。用于指定数据过滤规则的模式，common表示简单条件过滤（单表过滤条件），config表示关联表过滤（多表关联条件过滤）。 取值：common（简单条件过滤）/config（关联表过滤）。 约束：当简单条件过滤是子查询时，需要先校验关联条件，关联条件校验成功之后，需要保存关联条件。
        :type data_filter_type: str
        """
        
        

        self._general_filtering_list = None
        self._advanced_setting_list = None
        self._source = None
        self._data_filter_type = None
        self.discriminator = None

        if general_filtering_list is not None:
            self.general_filtering_list = general_filtering_list
        if advanced_setting_list is not None:
            self.advanced_setting_list = advanced_setting_list
        if source is not None:
            self.source = source
        if data_filter_type is not None:
            self.data_filter_type = data_filter_type

    @property
    def general_filtering_list(self):
        r"""Gets the general_filtering_list of this DataFilterRuleReq.

        数据过滤条件列表。包含需要校验的数据过滤规则信息，当data_filter_type为common（简单条件过滤）时，此参数为必填项。列表中的每个元素代表一组过滤条件，包含过滤对象列表和源库过滤条件SQL。包含以下关键字段：filter_object_list（过滤对象列表）/source_filter_condition（源库过滤条件SQL）。适用条件：data_filter_type=common时必填。

        :return: The general_filtering_list of this DataFilterRuleReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.GeneralTransformationReq`]
        """
        return self._general_filtering_list

    @general_filtering_list.setter
    def general_filtering_list(self, general_filtering_list):
        r"""Sets the general_filtering_list of this DataFilterRuleReq.

        数据过滤条件列表。包含需要校验的数据过滤规则信息，当data_filter_type为common（简单条件过滤）时，此参数为必填项。列表中的每个元素代表一组过滤条件，包含过滤对象列表和源库过滤条件SQL。包含以下关键字段：filter_object_list（过滤对象列表）/source_filter_condition（源库过滤条件SQL）。适用条件：data_filter_type=common时必填。

        :param general_filtering_list: The general_filtering_list of this DataFilterRuleReq.
        :type general_filtering_list: list[:class:`huaweicloudsdkdrs.v5.GeneralTransformationReq`]
        """
        self._general_filtering_list = general_filtering_list

    @property
    def advanced_setting_list(self):
        r"""Gets the advanced_setting_list of this DataFilterRuleReq.

        数据过滤高级设置列表。用于配置关联表场景下的高级过滤规则，包含数据库名、表名、列名、索引等详细过滤配置。当前Mysql-Mysql、Mysql-TaurusDB、TaurusDB-TaurusDB、TaurusDB-Mysql、Mysql-MariaDB、MariaDB-Mysql、MariaDB-TaurusDBL链路支持此功能。适用条件：data_filter_type=config时必填。

        :return: The advanced_setting_list of this DataFilterRuleReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`]
        """
        return self._advanced_setting_list

    @advanced_setting_list.setter
    def advanced_setting_list(self, advanced_setting_list):
        r"""Sets the advanced_setting_list of this DataFilterRuleReq.

        数据过滤高级设置列表。用于配置关联表场景下的高级过滤规则，包含数据库名、表名、列名、索引等详细过滤配置。当前Mysql-Mysql、Mysql-TaurusDB、TaurusDB-TaurusDB、TaurusDB-Mysql、Mysql-MariaDB、MariaDB-Mysql、MariaDB-TaurusDBL链路支持此功能。适用条件：data_filter_type=config时必填。

        :param advanced_setting_list: The advanced_setting_list of this DataFilterRuleReq.
        :type advanced_setting_list: list[:class:`huaweicloudsdkdrs.v5.DataFilteringAdvancedSetting`]
        """
        self._advanced_setting_list = advanced_setting_list

    @property
    def source(self):
        r"""Gets the source of this DataFilterRuleReq.

        校验请求的来源场景。用于区分数据过滤规则校验是来自数据同步任务执行场景，还是来自数据对比任务执行场景。 取值：job（数据同步任务执行时的过滤规则校验）/compare（数据对比任务执行时的过滤规则校验）

        :return: The source of this DataFilterRuleReq.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this DataFilterRuleReq.

        校验请求的来源场景。用于区分数据过滤规则校验是来自数据同步任务执行场景，还是来自数据对比任务执行场景。 取值：job（数据同步任务执行时的过滤规则校验）/compare（数据对比任务执行时的过滤规则校验）

        :param source: The source of this DataFilterRuleReq.
        :type source: str
        """
        self._source = source

    @property
    def data_filter_type(self):
        r"""Gets the data_filter_type of this DataFilterRuleReq.

        数据过滤类型。用于指定数据过滤规则的模式，common表示简单条件过滤（单表过滤条件），config表示关联表过滤（多表关联条件过滤）。 取值：common（简单条件过滤）/config（关联表过滤）。 约束：当简单条件过滤是子查询时，需要先校验关联条件，关联条件校验成功之后，需要保存关联条件。

        :return: The data_filter_type of this DataFilterRuleReq.
        :rtype: str
        """
        return self._data_filter_type

    @data_filter_type.setter
    def data_filter_type(self, data_filter_type):
        r"""Sets the data_filter_type of this DataFilterRuleReq.

        数据过滤类型。用于指定数据过滤规则的模式，common表示简单条件过滤（单表过滤条件），config表示关联表过滤（多表关联条件过滤）。 取值：common（简单条件过滤）/config（关联表过滤）。 约束：当简单条件过滤是子查询时，需要先校验关联条件，关联条件校验成功之后，需要保存关联条件。

        :param data_filter_type: The data_filter_type of this DataFilterRuleReq.
        :type data_filter_type: str
        """
        self._data_filter_type = data_filter_type

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
        if not isinstance(other, DataFilterRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
