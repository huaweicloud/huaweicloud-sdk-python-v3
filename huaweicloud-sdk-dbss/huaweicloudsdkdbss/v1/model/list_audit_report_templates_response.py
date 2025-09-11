# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditReportTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_type': 'str',
        'templates': 'list[TemplateInfo]'
    }

    attribute_map = {
        'os_type': 'os_type',
        'templates': 'templates'
    }

    def __init__(self, os_type=None, templates=None):
        r"""ListAuditReportTemplatesResponse

        The model defined in huaweicloud sdk

        :param os_type: os类型
        :type os_type: str
        :param templates: 模板列表
        :type templates: list[:class:`huaweicloudsdkdbss.v1.TemplateInfo`]
        """
        
        super(ListAuditReportTemplatesResponse, self).__init__()

        self._os_type = None
        self._templates = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        if templates is not None:
            self.templates = templates

    @property
    def os_type(self):
        r"""Gets the os_type of this ListAuditReportTemplatesResponse.

        os类型

        :return: The os_type of this ListAuditReportTemplatesResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListAuditReportTemplatesResponse.

        os类型

        :param os_type: The os_type of this ListAuditReportTemplatesResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def templates(self):
        r"""Gets the templates of this ListAuditReportTemplatesResponse.

        模板列表

        :return: The templates of this ListAuditReportTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TemplateInfo`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListAuditReportTemplatesResponse.

        模板列表

        :param templates: The templates of this ListAuditReportTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkdbss.v1.TemplateInfo`]
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
        if not isinstance(other, ListAuditReportTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
