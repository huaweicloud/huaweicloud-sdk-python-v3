# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteKmsKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'id': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'id': 'id'
    }

    def __init__(self, topic_urn=None, id=None):
        r"""DeleteKmsKeyRequest

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。
        :type topic_urn: str
        :param id: 当前已绑定密钥的资源ID。
        :type id: str
        """
        
        

        self._topic_urn = None
        self._id = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.id = id

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this DeleteKmsKeyRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :return: The topic_urn of this DeleteKmsKeyRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this DeleteKmsKeyRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](smn_api_51004.xml)获取该标识。

        :param topic_urn: The topic_urn of this DeleteKmsKeyRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def id(self):
        r"""Gets the id of this DeleteKmsKeyRequest.

        当前已绑定密钥的资源ID。

        :return: The id of this DeleteKmsKeyRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteKmsKeyRequest.

        当前已绑定密钥的资源ID。

        :param id: The id of this DeleteKmsKeyRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DeleteKmsKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
