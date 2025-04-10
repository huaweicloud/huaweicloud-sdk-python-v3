# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplatesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_ids': 'list[str]',
        'platform_source': 'int'
    }

    attribute_map = {
        'template_ids': 'template_ids',
        'platform_source': 'platform_source'
    }

    def __init__(self, template_ids=None, platform_source=None):
        r"""TemplatesInfo

        The model defined in huaweicloud sdk

        :param template_ids: 模板ID列表。
        :type template_ids: list[str]
        :param platform_source: 平台来源： - 0：codelabs - 1：devstar 
        :type platform_source: int
        """
        
        

        self._template_ids = None
        self._platform_source = None
        self.discriminator = None

        self.template_ids = template_ids
        self.platform_source = platform_source

    @property
    def template_ids(self):
        r"""Gets the template_ids of this TemplatesInfo.

        模板ID列表。

        :return: The template_ids of this TemplatesInfo.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        r"""Sets the template_ids of this TemplatesInfo.

        模板ID列表。

        :param template_ids: The template_ids of this TemplatesInfo.
        :type template_ids: list[str]
        """
        self._template_ids = template_ids

    @property
    def platform_source(self):
        r"""Gets the platform_source of this TemplatesInfo.

        平台来源： - 0：codelabs - 1：devstar 

        :return: The platform_source of this TemplatesInfo.
        :rtype: int
        """
        return self._platform_source

    @platform_source.setter
    def platform_source(self, platform_source):
        r"""Sets the platform_source of this TemplatesInfo.

        平台来源： - 0：codelabs - 1：devstar 

        :param platform_source: The platform_source of this TemplatesInfo.
        :type platform_source: int
        """
        self._platform_source = platform_source

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
        if not isinstance(other, TemplatesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
