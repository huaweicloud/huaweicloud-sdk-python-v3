# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimTemplateReportsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_reports': 'list[AIMTemplateReport]',
        'page_info': 'Page'
    }

    attribute_map = {
        'template_reports': 'template_reports',
        'page_info': 'page_info'
    }

    def __init__(self, template_reports=None, page_info=None):
        """ListAimTemplateReportsResponse

        The model defined in huaweicloud sdk

        :param template_reports: 查询模板报表结果集。
        :type template_reports: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateReport`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        super(ListAimTemplateReportsResponse, self).__init__()

        self._template_reports = None
        self._page_info = None
        self.discriminator = None

        if template_reports is not None:
            self.template_reports = template_reports
        if page_info is not None:
            self.page_info = page_info

    @property
    def template_reports(self):
        """Gets the template_reports of this ListAimTemplateReportsResponse.

        查询模板报表结果集。

        :return: The template_reports of this ListAimTemplateReportsResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateReport`]
        """
        return self._template_reports

    @template_reports.setter
    def template_reports(self, template_reports):
        """Sets the template_reports of this ListAimTemplateReportsResponse.

        查询模板报表结果集。

        :param template_reports: The template_reports of this ListAimTemplateReportsResponse.
        :type template_reports: list[:class:`huaweicloudsdkkoomessage.v1.AIMTemplateReport`]
        """
        self._template_reports = template_reports

    @property
    def page_info(self):
        """Gets the page_info of this ListAimTemplateReportsResponse.

        :return: The page_info of this ListAimTemplateReportsResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAimTemplateReportsResponse.

        :param page_info: The page_info of this ListAimTemplateReportsResponse.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAimTemplateReportsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
