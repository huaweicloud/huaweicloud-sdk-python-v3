# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSqlJobTemplateList:

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
        'templates': 'list[FlinkSqlJobTemplate]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'templates': 'templates'
    }

    def __init__(self, total_count=None, templates=None):
        r"""FlinkSqlJobTemplateList

        The model defined in huaweicloud sdk

        :param total_count: 模板总数。
        :type total_count: int
        :param templates: 模板详细信息
        :type templates: list[:class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplate`]
        """
        
        

        self._total_count = None
        self._templates = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if templates is not None:
            self.templates = templates

    @property
    def total_count(self):
        r"""Gets the total_count of this FlinkSqlJobTemplateList.

        模板总数。

        :return: The total_count of this FlinkSqlJobTemplateList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this FlinkSqlJobTemplateList.

        模板总数。

        :param total_count: The total_count of this FlinkSqlJobTemplateList.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def templates(self):
        r"""Gets the templates of this FlinkSqlJobTemplateList.

        模板详细信息

        :return: The templates of this FlinkSqlJobTemplateList.
        :rtype: list[:class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplate`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this FlinkSqlJobTemplateList.

        模板详细信息

        :param templates: The templates of this FlinkSqlJobTemplateList.
        :type templates: list[:class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplate`]
        """
        self._templates = templates

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
        if not isinstance(other, FlinkSqlJobTemplateList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
