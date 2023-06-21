# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVmsTemplateStatusResponseMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[VmsTemplateStatus]',
        'page_info': 'Page'
    }

    attribute_map = {
        'templates': 'templates',
        'page_info': 'page_info'
    }

    def __init__(self, templates=None, page_info=None):
        """ListVmsTemplateStatusResponseMode

        The model defined in huaweicloud sdk

        :param templates: 智能信息基础版模板列表。
        :type templates: list[:class:`huaweicloudsdkkoomessage.v1.VmsTemplateStatus`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        

        self._templates = None
        self._page_info = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if page_info is not None:
            self.page_info = page_info

    @property
    def templates(self):
        """Gets the templates of this ListVmsTemplateStatusResponseMode.

        智能信息基础版模板列表。

        :return: The templates of this ListVmsTemplateStatusResponseMode.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.VmsTemplateStatus`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListVmsTemplateStatusResponseMode.

        智能信息基础版模板列表。

        :param templates: The templates of this ListVmsTemplateStatusResponseMode.
        :type templates: list[:class:`huaweicloudsdkkoomessage.v1.VmsTemplateStatus`]
        """
        self._templates = templates

    @property
    def page_info(self):
        """Gets the page_info of this ListVmsTemplateStatusResponseMode.

        :return: The page_info of this ListVmsTemplateStatusResponseMode.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListVmsTemplateStatusResponseMode.

        :param page_info: The page_info of this ListVmsTemplateStatusResponseMode.
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
        if not isinstance(other, ListVmsTemplateStatusResponseMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
