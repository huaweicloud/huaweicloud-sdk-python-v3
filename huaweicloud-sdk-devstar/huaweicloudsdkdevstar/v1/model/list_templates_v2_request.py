# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'action_id': 'str',
        'body': 'TemplateQueryV2'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'action_id': 'action_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, action_id=None, body=None):
        """ListTemplatesV2Request

        The model defined in huaweicloud sdk

        :param x_language: 语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 
        :type x_language: str
        :param action_id: 请填写固定值“query”。
        :type action_id: str
        :param body: Body of the ListTemplatesV2Request
        :type body: :class:`huaweicloudsdkdevstar.v1.TemplateQueryV2`
        """
        
        

        self._x_language = None
        self._action_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.action_id = action_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this ListTemplatesV2Request.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :return: The x_language of this ListTemplatesV2Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListTemplatesV2Request.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :param x_language: The x_language of this ListTemplatesV2Request.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def action_id(self):
        """Gets the action_id of this ListTemplatesV2Request.

        请填写固定值“query”。

        :return: The action_id of this ListTemplatesV2Request.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ListTemplatesV2Request.

        请填写固定值“query”。

        :param action_id: The action_id of this ListTemplatesV2Request.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def body(self):
        """Gets the body of this ListTemplatesV2Request.


        :return: The body of this ListTemplatesV2Request.
        :rtype: :class:`huaweicloudsdkdevstar.v1.TemplateQueryV2`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListTemplatesV2Request.


        :param body: The body of this ListTemplatesV2Request.
        :type body: :class:`huaweicloudsdkdevstar.v1.TemplateQueryV2`
        """
        self._body = body

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
        if not isinstance(other, ListTemplatesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
