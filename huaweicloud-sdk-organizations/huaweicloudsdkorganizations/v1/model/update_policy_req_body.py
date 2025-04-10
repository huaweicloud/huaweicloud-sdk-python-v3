# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'content': 'content',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, content=None, description=None, name=None):
        r"""UpdatePolicyReqBody

        The model defined in huaweicloud sdk

        :param content: 要添加到新策略的策略文本内容。
        :type content: str
        :param description: 要分配给策略的可选说明。
        :type description: str
        :param name: 要分配给策略的名称。
        :type name: str
        """
        
        

        self._content = None
        self._description = None
        self._name = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def content(self):
        r"""Gets the content of this UpdatePolicyReqBody.

        要添加到新策略的策略文本内容。

        :return: The content of this UpdatePolicyReqBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this UpdatePolicyReqBody.

        要添加到新策略的策略文本内容。

        :param content: The content of this UpdatePolicyReqBody.
        :type content: str
        """
        self._content = content

    @property
    def description(self):
        r"""Gets the description of this UpdatePolicyReqBody.

        要分配给策略的可选说明。

        :return: The description of this UpdatePolicyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePolicyReqBody.

        要分配给策略的可选说明。

        :param description: The description of this UpdatePolicyReqBody.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdatePolicyReqBody.

        要分配给策略的名称。

        :return: The name of this UpdatePolicyReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdatePolicyReqBody.

        要分配给策略的名称。

        :param name: The name of this UpdatePolicyReqBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, UpdatePolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
