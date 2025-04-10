# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_num': 'int',
        'templates': 'list[ConfigTemplatesListInfo]'
    }

    attribute_map = {
        'template_num': 'template_num',
        'templates': 'templates'
    }

    def __init__(self, template_num=None, templates=None):
        r"""ListConfigTemplatesResponse

        The model defined in huaweicloud sdk

        :param template_num: 模板个数。
        :type template_num: int
        :param templates: 模板的详情数组。
        :type templates: list[:class:`huaweicloudsdkdcs.v2.ConfigTemplatesListInfo`]
        """
        
        super(ListConfigTemplatesResponse, self).__init__()

        self._template_num = None
        self._templates = None
        self.discriminator = None

        if template_num is not None:
            self.template_num = template_num
        if templates is not None:
            self.templates = templates

    @property
    def template_num(self):
        r"""Gets the template_num of this ListConfigTemplatesResponse.

        模板个数。

        :return: The template_num of this ListConfigTemplatesResponse.
        :rtype: int
        """
        return self._template_num

    @template_num.setter
    def template_num(self, template_num):
        r"""Sets the template_num of this ListConfigTemplatesResponse.

        模板个数。

        :param template_num: The template_num of this ListConfigTemplatesResponse.
        :type template_num: int
        """
        self._template_num = template_num

    @property
    def templates(self):
        r"""Gets the templates of this ListConfigTemplatesResponse.

        模板的详情数组。

        :return: The templates of this ListConfigTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ConfigTemplatesListInfo`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListConfigTemplatesResponse.

        模板的详情数组。

        :param templates: The templates of this ListConfigTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkdcs.v2.ConfigTemplatesListInfo`]
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
        if not isinstance(other, ListConfigTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
