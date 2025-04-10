# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvisioningTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[ProvisioningTemplateSimple]',
        'page': 'Page'
    }

    attribute_map = {
        'templates': 'templates',
        'page': 'page'
    }

    def __init__(self, templates=None, page=None):
        r"""ListProvisioningTemplatesResponse

        The model defined in huaweicloud sdk

        :param templates: **参数说明**：预调配模板详情。
        :type templates: list[:class:`huaweicloudsdkiotda.v5.ProvisioningTemplateSimple`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListProvisioningTemplatesResponse, self).__init__()

        self._templates = None
        self._page = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if page is not None:
            self.page = page

    @property
    def templates(self):
        r"""Gets the templates of this ListProvisioningTemplatesResponse.

        **参数说明**：预调配模板详情。

        :return: The templates of this ListProvisioningTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ProvisioningTemplateSimple`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListProvisioningTemplatesResponse.

        **参数说明**：预调配模板详情。

        :param templates: The templates of this ListProvisioningTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkiotda.v5.ProvisioningTemplateSimple`]
        """
        self._templates = templates

    @property
    def page(self):
        r"""Gets the page of this ListProvisioningTemplatesResponse.

        :return: The page of this ListProvisioningTemplatesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListProvisioningTemplatesResponse.

        :param page: The page of this ListProvisioningTemplatesResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListProvisioningTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
