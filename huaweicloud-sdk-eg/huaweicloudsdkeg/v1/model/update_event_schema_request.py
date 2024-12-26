# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEventSchemaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_id': 'str',
        'body': 'CustomizeSchemaUpdateReq'
    }

    attribute_map = {
        'schema_id': 'schema_id',
        'body': 'body'
    }

    def __init__(self, schema_id=None, body=None):
        """UpdateEventSchemaRequest

        The model defined in huaweicloud sdk

        :param schema_id: 指定查询的事件模型ID
        :type schema_id: str
        :param body: Body of the UpdateEventSchemaRequest
        :type body: :class:`huaweicloudsdkeg.v1.CustomizeSchemaUpdateReq`
        """
        
        

        self._schema_id = None
        self._body = None
        self.discriminator = None

        self.schema_id = schema_id
        if body is not None:
            self.body = body

    @property
    def schema_id(self):
        """Gets the schema_id of this UpdateEventSchemaRequest.

        指定查询的事件模型ID

        :return: The schema_id of this UpdateEventSchemaRequest.
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this UpdateEventSchemaRequest.

        指定查询的事件模型ID

        :param schema_id: The schema_id of this UpdateEventSchemaRequest.
        :type schema_id: str
        """
        self._schema_id = schema_id

    @property
    def body(self):
        """Gets the body of this UpdateEventSchemaRequest.

        :return: The body of this UpdateEventSchemaRequest.
        :rtype: :class:`huaweicloudsdkeg.v1.CustomizeSchemaUpdateReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEventSchemaRequest.

        :param body: The body of this UpdateEventSchemaRequest.
        :type body: :class:`huaweicloudsdkeg.v1.CustomizeSchemaUpdateReq`
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
        if not isinstance(other, UpdateEventSchemaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
