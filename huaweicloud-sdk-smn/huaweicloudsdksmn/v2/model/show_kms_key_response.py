# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKmsKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'status': 'str',
        'id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'status': 'status',
        'id': 'id',
        'request_id': 'request_id'
    }

    def __init__(self, key_id=None, status=None, id=None, request_id=None):
        r"""ShowKmsKeyResponse

        The model defined in huaweicloud sdk

        :param key_id: 在DEW服务上创建的用户主密钥对应的密钥ID，具体参考在DEW服务上创建密钥章节。
        :type key_id: str
        :param status: 密钥的状态字段，为枚举类型。 - ENABLED状态为密钥启用状态，此时发布的消息均使用该主密钥创建的数据密钥进行加解密。 - TO_BE_ACTIVATED状态为密钥待激活状态，当密钥未激活时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DISABLED状态为密钥禁用状态，当密钥已被禁用时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - PENDING_DELETION状态为密钥计划删除状态，当密钥已被计划删除时，发布主题消息仍能正常使用该密钥。 - PENDING_IMPORT状态为密钥计划导入状态，当密钥计划导入时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DELETED状态为密钥已删除状态，当密钥已删除后，SMN无法从DEW服务处获取有效的密钥，此时发布主题消息会返回失败，请重新在主题下配置可用的密钥。
        :type status: str
        :param id: 密钥对应的资源ID，该ID由SMN服务生成。
        :type id: str
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        """
        
        super().__init__()

        self._key_id = None
        self._status = None
        self._id = None
        self._request_id = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if request_id is not None:
            self.request_id = request_id

    @property
    def key_id(self):
        r"""Gets the key_id of this ShowKmsKeyResponse.

        在DEW服务上创建的用户主密钥对应的密钥ID，具体参考在DEW服务上创建密钥章节。

        :return: The key_id of this ShowKmsKeyResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ShowKmsKeyResponse.

        在DEW服务上创建的用户主密钥对应的密钥ID，具体参考在DEW服务上创建密钥章节。

        :param key_id: The key_id of this ShowKmsKeyResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def status(self):
        r"""Gets the status of this ShowKmsKeyResponse.

        密钥的状态字段，为枚举类型。 - ENABLED状态为密钥启用状态，此时发布的消息均使用该主密钥创建的数据密钥进行加解密。 - TO_BE_ACTIVATED状态为密钥待激活状态，当密钥未激活时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DISABLED状态为密钥禁用状态，当密钥已被禁用时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - PENDING_DELETION状态为密钥计划删除状态，当密钥已被计划删除时，发布主题消息仍能正常使用该密钥。 - PENDING_IMPORT状态为密钥计划导入状态，当密钥计划导入时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DELETED状态为密钥已删除状态，当密钥已删除后，SMN无法从DEW服务处获取有效的密钥，此时发布主题消息会返回失败，请重新在主题下配置可用的密钥。

        :return: The status of this ShowKmsKeyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowKmsKeyResponse.

        密钥的状态字段，为枚举类型。 - ENABLED状态为密钥启用状态，此时发布的消息均使用该主密钥创建的数据密钥进行加解密。 - TO_BE_ACTIVATED状态为密钥待激活状态，当密钥未激活时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DISABLED状态为密钥禁用状态，当密钥已被禁用时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - PENDING_DELETION状态为密钥计划删除状态，当密钥已被计划删除时，发布主题消息仍能正常使用该密钥。 - PENDING_IMPORT状态为密钥计划导入状态，当密钥计划导入时，发布主题消息会返回失败，请前往DEW服务对密钥进行操作。 - DELETED状态为密钥已删除状态，当密钥已删除后，SMN无法从DEW服务处获取有效的密钥，此时发布主题消息会返回失败，请重新在主题下配置可用的密钥。

        :param status: The status of this ShowKmsKeyResponse.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this ShowKmsKeyResponse.

        密钥对应的资源ID，该ID由SMN服务生成。

        :return: The id of this ShowKmsKeyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowKmsKeyResponse.

        密钥对应的资源ID，该ID由SMN服务生成。

        :param id: The id of this ShowKmsKeyResponse.
        :type id: str
        """
        self._id = id

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowKmsKeyResponse.

        请求的唯一标识ID。

        :return: The request_id of this ShowKmsKeyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowKmsKeyResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ShowKmsKeyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowKmsKeyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowKmsKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
