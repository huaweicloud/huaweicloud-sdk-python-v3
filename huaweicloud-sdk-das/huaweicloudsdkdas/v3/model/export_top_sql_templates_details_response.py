# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTopSqlTemplatesDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_sql_templates': 'list[TopSqlTemplate]',
        'total_count': 'int'
    }

    attribute_map = {
        'top_sql_templates': 'top_sql_templates',
        'total_count': 'total_count'
    }

    def __init__(self, top_sql_templates=None, total_count=None):
        r"""ExportTopSqlTemplatesDetailsResponse

        The model defined in huaweicloud sdk

        :param top_sql_templates: SQL模板列表。
        :type top_sql_templates: list[:class:`huaweicloudsdkdas.v3.TopSqlTemplate`]
        :param total_count: SQL模板总数。
        :type total_count: int
        """
        
        super(ExportTopSqlTemplatesDetailsResponse, self).__init__()

        self._top_sql_templates = None
        self._total_count = None
        self.discriminator = None

        if top_sql_templates is not None:
            self.top_sql_templates = top_sql_templates
        if total_count is not None:
            self.total_count = total_count

    @property
    def top_sql_templates(self):
        r"""Gets the top_sql_templates of this ExportTopSqlTemplatesDetailsResponse.

        SQL模板列表。

        :return: The top_sql_templates of this ExportTopSqlTemplatesDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopSqlTemplate`]
        """
        return self._top_sql_templates

    @top_sql_templates.setter
    def top_sql_templates(self, top_sql_templates):
        r"""Sets the top_sql_templates of this ExportTopSqlTemplatesDetailsResponse.

        SQL模板列表。

        :param top_sql_templates: The top_sql_templates of this ExportTopSqlTemplatesDetailsResponse.
        :type top_sql_templates: list[:class:`huaweicloudsdkdas.v3.TopSqlTemplate`]
        """
        self._top_sql_templates = top_sql_templates

    @property
    def total_count(self):
        r"""Gets the total_count of this ExportTopSqlTemplatesDetailsResponse.

        SQL模板总数。

        :return: The total_count of this ExportTopSqlTemplatesDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ExportTopSqlTemplatesDetailsResponse.

        SQL模板总数。

        :param total_count: The total_count of this ExportTopSqlTemplatesDetailsResponse.
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
        if not isinstance(other, ExportTopSqlTemplatesDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
