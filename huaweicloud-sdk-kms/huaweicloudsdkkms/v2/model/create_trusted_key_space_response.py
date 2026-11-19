# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrustedKeySpaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyspace_id': 'str'
    }

    attribute_map = {
        'keyspace_id': 'keyspace_id'
    }

    def __init__(self, keyspace_id=None):
        r"""CreateTrustedKeySpaceResponse

        The model defined in huaweicloud sdk

        :param keyspace_id: **参数解释：** 创建的密钥空间ID **取值范围：** 不涉及
        :type keyspace_id: str
        """
        
        super().__init__()

        self._keyspace_id = None
        self.discriminator = None

        if keyspace_id is not None:
            self.keyspace_id = keyspace_id

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this CreateTrustedKeySpaceResponse.

        **参数解释：** 创建的密钥空间ID **取值范围：** 不涉及

        :return: The keyspace_id of this CreateTrustedKeySpaceResponse.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this CreateTrustedKeySpaceResponse.

        **参数解释：** 创建的密钥空间ID **取值范围：** 不涉及

        :param keyspace_id: The keyspace_id of this CreateTrustedKeySpaceResponse.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateTrustedKeySpaceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateTrustedKeySpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
