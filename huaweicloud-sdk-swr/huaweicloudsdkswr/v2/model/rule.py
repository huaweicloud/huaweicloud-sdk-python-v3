# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template': 'str',
        'params': 'object',
        'tag_selectors': 'list[TagSelector]'
    }

    attribute_map = {
        'template': 'template',
        'params': 'params',
        'tag_selectors': 'tag_selectors'
    }

    def __init__(self, template=None, params=None, tag_selectors=None):
        """Rule

        The model defined in huaweicloud sdk

        :param template: 回收类型，date_rule、tag_rule
        :type template: str
        :param params: template是date_rule时，设置params为{\&quot;days\&quot;: \&quot;xxx\&quot;} template是tag_rule时，设置params为{\&quot;num\&quot;: \&quot;xxx\&quot;} 
        :type params: object
        :param tag_selectors: 例外镜像
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.TagSelector`]
        """
        
        

        self._template = None
        self._params = None
        self._tag_selectors = None
        self.discriminator = None

        self.template = template
        self.params = params
        self.tag_selectors = tag_selectors

    @property
    def template(self):
        """Gets the template of this Rule.

        回收类型，date_rule、tag_rule

        :return: The template of this Rule.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Rule.

        回收类型，date_rule、tag_rule

        :param template: The template of this Rule.
        :type template: str
        """
        self._template = template

    @property
    def params(self):
        """Gets the params of this Rule.

        template是date_rule时，设置params为{\"days\": \"xxx\"} template是tag_rule时，设置params为{\"num\": \"xxx\"} 

        :return: The params of this Rule.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Rule.

        template是date_rule时，设置params为{\"days\": \"xxx\"} template是tag_rule时，设置params为{\"num\": \"xxx\"} 

        :param params: The params of this Rule.
        :type params: object
        """
        self._params = params

    @property
    def tag_selectors(self):
        """Gets the tag_selectors of this Rule.

        例外镜像

        :return: The tag_selectors of this Rule.
        :rtype: list[:class:`huaweicloudsdkswr.v2.TagSelector`]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        """Sets the tag_selectors of this Rule.

        例外镜像

        :param tag_selectors: The tag_selectors of this Rule.
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.TagSelector`]
        """
        self._tag_selectors = tag_selectors

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
