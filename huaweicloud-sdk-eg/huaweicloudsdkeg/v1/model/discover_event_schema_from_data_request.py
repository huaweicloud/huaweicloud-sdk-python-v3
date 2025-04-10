# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscoverEventSchemaFromDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'object'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        r"""DiscoverEventSchemaFromDataRequest

        The model defined in huaweicloud sdk

        :param body: {   \&quot;description\&quot;: \&quot;通过事件数据发现事件模型的请求\&quot;,   \&quot;type\&quot;: \&quot;object\&quot;,   \&quot;required\&quot;: [     \&quot;event\&quot;   ],   \&quot;properties\&quot;: {     \&quot;event\&quot;: {       \&quot;description\&quot;: \&quot;事件数据内容\&quot;,       \&quot;type\&quot;: \&quot;string\&quot;,       \&quot;maxLength\&quot;: 1024,       \&quot;example\&quot;: \&quot;{\\\&quot;fileName\\\&quot;: \\\&quot;one.jpg\\\&quot;, \\\&quot;fileSize\\\&quot;: 1048576}\&quot;     },     \&quot;format\&quot;: {       \&quot;description\&quot;: \&quot;事件模型格式类型\&quot;,       \&quot;type\&quot;: \&quot;string\&quot;,       \&quot;default\&quot;: \&quot;JSON_SCHEMA_DRAFT_6\&quot;,       \&quot;enum\&quot;: [         \&quot;JSON_SCHEMA_DRAFT_6\&quot;       ]     }   } }
        :type body: object
        """
        
        

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        r"""Gets the body of this DiscoverEventSchemaFromDataRequest.

        {   \"description\": \"通过事件数据发现事件模型的请求\",   \"type\": \"object\",   \"required\": [     \"event\"   ],   \"properties\": {     \"event\": {       \"description\": \"事件数据内容\",       \"type\": \"string\",       \"maxLength\": 1024,       \"example\": \"{\\\"fileName\\\": \\\"one.jpg\\\", \\\"fileSize\\\": 1048576}\"     },     \"format\": {       \"description\": \"事件模型格式类型\",       \"type\": \"string\",       \"default\": \"JSON_SCHEMA_DRAFT_6\",       \"enum\": [         \"JSON_SCHEMA_DRAFT_6\"       ]     }   } }

        :return: The body of this DiscoverEventSchemaFromDataRequest.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DiscoverEventSchemaFromDataRequest.

        {   \"description\": \"通过事件数据发现事件模型的请求\",   \"type\": \"object\",   \"required\": [     \"event\"   ],   \"properties\": {     \"event\": {       \"description\": \"事件数据内容\",       \"type\": \"string\",       \"maxLength\": 1024,       \"example\": \"{\\\"fileName\\\": \\\"one.jpg\\\", \\\"fileSize\\\": 1048576}\"     },     \"format\": {       \"description\": \"事件模型格式类型\",       \"type\": \"string\",       \"default\": \"JSON_SCHEMA_DRAFT_6\",       \"enum\": [         \"JSON_SCHEMA_DRAFT_6\"       ]     }   } }

        :param body: The body of this DiscoverEventSchemaFromDataRequest.
        :type body: object
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
        if not isinstance(other, DiscoverEventSchemaFromDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
