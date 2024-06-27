# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'shard_statics': 'list[ReplayShardStaticsResp]',
        'slow_sqls': 'list[ReplaySlowSqlResp]',
        'slow_sql_templates': 'list[ReplaySlowSqlTemplateResp]',
        'error_sqls': 'list[ReplayErrorSqlResp]',
        'error_sql_templates': 'list[ReplayErrorSqlTemplateResp]',
        'replaying_sqls': 'list[ReplayingSqlResp]',
        'error_classifications': 'list[ReplayErrorClassification]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'shard_statics': 'shard_statics',
        'slow_sqls': 'slow_sqls',
        'slow_sql_templates': 'slow_sql_templates',
        'error_sqls': 'error_sqls',
        'error_sql_templates': 'error_sql_templates',
        'replaying_sqls': 'replaying_sqls',
        'error_classifications': 'error_classifications'
    }

    def __init__(self, total_count=None, shard_statics=None, slow_sqls=None, slow_sql_templates=None, error_sqls=None, error_sql_templates=None, replaying_sqls=None, error_classifications=None):
        """ShowReplayResultsResponse

        The model defined in huaweicloud sdk

        :param total_count: 数据总量
        :type total_count: int
        :param shard_statics: 回放基于时间统计详细信息列表，在type为shard_statistics时返回
        :type shard_statics: list[:class:`huaweicloudsdkdrs.v5.ReplayShardStaticsResp`]
        :param slow_sqls: 慢SQL信息列表，在type为slow_sql时返回
        :type slow_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlResp`]
        :param slow_sql_templates: 慢SQL统计信息列表，在type为slow_sql_template时返回
        :type slow_sql_templates: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlTemplateResp`]
        :param error_sqls: 异常SQL信息列表，在type为error_sql时返回
        :type error_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlResp`]
        :param error_sql_templates: 异常SQL统计信息列表，在type为error_sql_template时返回
        :type error_sql_templates: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlTemplateResp`]
        :param replaying_sqls: 正在回放SQL信息列表，在type为replaying_sql时返回
        :type replaying_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplayingSqlResp`]
        :param error_classifications: 回放异常SQL分类信息，在type为error_classification时返回
        :type error_classifications: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorClassification`]
        """
        
        super(ShowReplayResultsResponse, self).__init__()

        self._total_count = None
        self._shard_statics = None
        self._slow_sqls = None
        self._slow_sql_templates = None
        self._error_sqls = None
        self._error_sql_templates = None
        self._replaying_sqls = None
        self._error_classifications = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if shard_statics is not None:
            self.shard_statics = shard_statics
        if slow_sqls is not None:
            self.slow_sqls = slow_sqls
        if slow_sql_templates is not None:
            self.slow_sql_templates = slow_sql_templates
        if error_sqls is not None:
            self.error_sqls = error_sqls
        if error_sql_templates is not None:
            self.error_sql_templates = error_sql_templates
        if replaying_sqls is not None:
            self.replaying_sqls = replaying_sqls
        if error_classifications is not None:
            self.error_classifications = error_classifications

    @property
    def total_count(self):
        """Gets the total_count of this ShowReplayResultsResponse.

        数据总量

        :return: The total_count of this ShowReplayResultsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowReplayResultsResponse.

        数据总量

        :param total_count: The total_count of this ShowReplayResultsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def shard_statics(self):
        """Gets the shard_statics of this ShowReplayResultsResponse.

        回放基于时间统计详细信息列表，在type为shard_statistics时返回

        :return: The shard_statics of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplayShardStaticsResp`]
        """
        return self._shard_statics

    @shard_statics.setter
    def shard_statics(self, shard_statics):
        """Sets the shard_statics of this ShowReplayResultsResponse.

        回放基于时间统计详细信息列表，在type为shard_statistics时返回

        :param shard_statics: The shard_statics of this ShowReplayResultsResponse.
        :type shard_statics: list[:class:`huaweicloudsdkdrs.v5.ReplayShardStaticsResp`]
        """
        self._shard_statics = shard_statics

    @property
    def slow_sqls(self):
        """Gets the slow_sqls of this ShowReplayResultsResponse.

        慢SQL信息列表，在type为slow_sql时返回

        :return: The slow_sqls of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlResp`]
        """
        return self._slow_sqls

    @slow_sqls.setter
    def slow_sqls(self, slow_sqls):
        """Sets the slow_sqls of this ShowReplayResultsResponse.

        慢SQL信息列表，在type为slow_sql时返回

        :param slow_sqls: The slow_sqls of this ShowReplayResultsResponse.
        :type slow_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlResp`]
        """
        self._slow_sqls = slow_sqls

    @property
    def slow_sql_templates(self):
        """Gets the slow_sql_templates of this ShowReplayResultsResponse.

        慢SQL统计信息列表，在type为slow_sql_template时返回

        :return: The slow_sql_templates of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlTemplateResp`]
        """
        return self._slow_sql_templates

    @slow_sql_templates.setter
    def slow_sql_templates(self, slow_sql_templates):
        """Sets the slow_sql_templates of this ShowReplayResultsResponse.

        慢SQL统计信息列表，在type为slow_sql_template时返回

        :param slow_sql_templates: The slow_sql_templates of this ShowReplayResultsResponse.
        :type slow_sql_templates: list[:class:`huaweicloudsdkdrs.v5.ReplaySlowSqlTemplateResp`]
        """
        self._slow_sql_templates = slow_sql_templates

    @property
    def error_sqls(self):
        """Gets the error_sqls of this ShowReplayResultsResponse.

        异常SQL信息列表，在type为error_sql时返回

        :return: The error_sqls of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlResp`]
        """
        return self._error_sqls

    @error_sqls.setter
    def error_sqls(self, error_sqls):
        """Sets the error_sqls of this ShowReplayResultsResponse.

        异常SQL信息列表，在type为error_sql时返回

        :param error_sqls: The error_sqls of this ShowReplayResultsResponse.
        :type error_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlResp`]
        """
        self._error_sqls = error_sqls

    @property
    def error_sql_templates(self):
        """Gets the error_sql_templates of this ShowReplayResultsResponse.

        异常SQL统计信息列表，在type为error_sql_template时返回

        :return: The error_sql_templates of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlTemplateResp`]
        """
        return self._error_sql_templates

    @error_sql_templates.setter
    def error_sql_templates(self, error_sql_templates):
        """Sets the error_sql_templates of this ShowReplayResultsResponse.

        异常SQL统计信息列表，在type为error_sql_template时返回

        :param error_sql_templates: The error_sql_templates of this ShowReplayResultsResponse.
        :type error_sql_templates: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorSqlTemplateResp`]
        """
        self._error_sql_templates = error_sql_templates

    @property
    def replaying_sqls(self):
        """Gets the replaying_sqls of this ShowReplayResultsResponse.

        正在回放SQL信息列表，在type为replaying_sql时返回

        :return: The replaying_sqls of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplayingSqlResp`]
        """
        return self._replaying_sqls

    @replaying_sqls.setter
    def replaying_sqls(self, replaying_sqls):
        """Sets the replaying_sqls of this ShowReplayResultsResponse.

        正在回放SQL信息列表，在type为replaying_sql时返回

        :param replaying_sqls: The replaying_sqls of this ShowReplayResultsResponse.
        :type replaying_sqls: list[:class:`huaweicloudsdkdrs.v5.ReplayingSqlResp`]
        """
        self._replaying_sqls = replaying_sqls

    @property
    def error_classifications(self):
        """Gets the error_classifications of this ShowReplayResultsResponse.

        回放异常SQL分类信息，在type为error_classification时返回

        :return: The error_classifications of this ShowReplayResultsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorClassification`]
        """
        return self._error_classifications

    @error_classifications.setter
    def error_classifications(self, error_classifications):
        """Sets the error_classifications of this ShowReplayResultsResponse.

        回放异常SQL分类信息，在type为error_classification时返回

        :param error_classifications: The error_classifications of this ShowReplayResultsResponse.
        :type error_classifications: list[:class:`huaweicloudsdkdrs.v5.ReplayErrorClassification`]
        """
        self._error_classifications = error_classifications

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowReplayResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
