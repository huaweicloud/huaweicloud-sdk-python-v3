# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowSqlTemplatesDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_sql_templates': 'list[SlowSqlTemplate]',
        'total_count': 'int'
    }

    attribute_map = {
        'slow_sql_templates': 'slow_sql_templates',
        'total_count': 'total_count'
    }

    def __init__(self, slow_sql_templates=None, total_count=None):
        r"""ExportSlowSqlTemplatesDetailsResponse

        The model defined in huaweicloud sdk

        :param slow_sql_templates: 慢日志模板数据列表。
        :type slow_sql_templates: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        :param total_count: 慢日志模板总数。
        :type total_count: int
        """
        
        super(ExportSlowSqlTemplatesDetailsResponse, self).__init__()

        self._slow_sql_templates = None
        self._total_count = None
        self.discriminator = None

        if slow_sql_templates is not None:
            self.slow_sql_templates = slow_sql_templates
        if total_count is not None:
            self.total_count = total_count

    @property
    def slow_sql_templates(self):
        r"""Gets the slow_sql_templates of this ExportSlowSqlTemplatesDetailsResponse.

        慢日志模板数据列表。

        :return: The slow_sql_templates of this ExportSlowSqlTemplatesDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        return self._slow_sql_templates

    @slow_sql_templates.setter
    def slow_sql_templates(self, slow_sql_templates):
        r"""Sets the slow_sql_templates of this ExportSlowSqlTemplatesDetailsResponse.

        慢日志模板数据列表。

        :param slow_sql_templates: The slow_sql_templates of this ExportSlowSqlTemplatesDetailsResponse.
        :type slow_sql_templates: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        self._slow_sql_templates = slow_sql_templates

    @property
    def total_count(self):
        r"""Gets the total_count of this ExportSlowSqlTemplatesDetailsResponse.

        慢日志模板总数。

        :return: The total_count of this ExportSlowSqlTemplatesDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ExportSlowSqlTemplatesDetailsResponse.

        慢日志模板总数。

        :param total_count: The total_count of this ExportSlowSqlTemplatesDetailsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ExportSlowSqlTemplatesDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
