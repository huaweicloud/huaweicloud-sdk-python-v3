# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMeshRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'body': 'Mesh'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'body': 'body'
    }

    def __init__(self, content_type=None, body=None):
        r"""CreateMeshRequest

        The model defined in huaweicloud sdk

        :param content_type: 消息体的类型（格式）。 取值范围： - application/json;charset&#x3D;utf-8：指定内容为JSON格式，并以UTF8字符编码进行编码 - application/json：指定内容为JSON格式
        :type content_type: str
        :param body: Body of the CreateMeshRequest
        :type body: :class:`huaweicloudsdkasm.v1.Mesh`
        """
        
        

        self._content_type = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        r"""Gets the content_type of this CreateMeshRequest.

        消息体的类型（格式）。 取值范围： - application/json;charset=utf-8：指定内容为JSON格式，并以UTF8字符编码进行编码 - application/json：指定内容为JSON格式

        :return: The content_type of this CreateMeshRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this CreateMeshRequest.

        消息体的类型（格式）。 取值范围： - application/json;charset=utf-8：指定内容为JSON格式，并以UTF8字符编码进行编码 - application/json：指定内容为JSON格式

        :param content_type: The content_type of this CreateMeshRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def body(self):
        r"""Gets the body of this CreateMeshRequest.

        :return: The body of this CreateMeshRequest.
        :rtype: :class:`huaweicloudsdkasm.v1.Mesh`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateMeshRequest.

        :param body: The body of this CreateMeshRequest.
        :type body: :class:`huaweicloudsdkasm.v1.Mesh`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMeshRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
