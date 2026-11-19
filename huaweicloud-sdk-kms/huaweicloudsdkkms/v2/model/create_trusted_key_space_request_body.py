# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrustedKeySpaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyspace_name': 'str',
        'type': 'str',
        'keystore_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'keyspace_name': 'keyspace_name',
        'type': 'type',
        'keystore_id': 'keystore_id',
        'description': 'description'
    }

    def __init__(self, keyspace_name=None, type=None, keystore_id=None, description=None):
        r"""CreateTrustedKeySpaceRequestBody

        The model defined in huaweicloud sdk

        :param keyspace_name: **参数解释：** 密钥空间名称 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及
        :type keyspace_name: str
        :param type: **参数解释：** 密钥空间类型 **约束限制：** 不涉及 **取值范围：** - 1 默认密钥空间 - 2 专属加密集群密钥空间 - 3 外部密钥存储密钥空间 **默认取值：** 1
        :type type: str
        :param keystore_id: **参数解释：** 密钥空间关联的密钥库ID,仅type为2或3时必填，关联的密钥库ID需要和类型匹配 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type keystore_id: str
        :param description: **参数解释：** 密钥空间描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        """
        
        

        self._keyspace_name = None
        self._type = None
        self._keystore_id = None
        self._description = None
        self.discriminator = None

        self.keyspace_name = keyspace_name
        if type is not None:
            self.type = type
        if keystore_id is not None:
            self.keystore_id = keystore_id
        if description is not None:
            self.description = description

    @property
    def keyspace_name(self):
        r"""Gets the keyspace_name of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间名称 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及

        :return: The keyspace_name of this CreateTrustedKeySpaceRequestBody.
        :rtype: str
        """
        return self._keyspace_name

    @keyspace_name.setter
    def keyspace_name(self, keyspace_name):
        r"""Sets the keyspace_name of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间名称 **约束限制：** 不涉及 **取值范围：** 1-255 **默认取值：** 不涉及

        :param keyspace_name: The keyspace_name of this CreateTrustedKeySpaceRequestBody.
        :type keyspace_name: str
        """
        self._keyspace_name = keyspace_name

    @property
    def type(self):
        r"""Gets the type of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间类型 **约束限制：** 不涉及 **取值范围：** - 1 默认密钥空间 - 2 专属加密集群密钥空间 - 3 外部密钥存储密钥空间 **默认取值：** 1

        :return: The type of this CreateTrustedKeySpaceRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间类型 **约束限制：** 不涉及 **取值范围：** - 1 默认密钥空间 - 2 专属加密集群密钥空间 - 3 外部密钥存储密钥空间 **默认取值：** 1

        :param type: The type of this CreateTrustedKeySpaceRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间关联的密钥库ID,仅type为2或3时必填，关联的密钥库ID需要和类型匹配 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The keystore_id of this CreateTrustedKeySpaceRequestBody.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间关联的密钥库ID,仅type为2或3时必填，关联的密钥库ID需要和类型匹配 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param keystore_id: The keystore_id of this CreateTrustedKeySpaceRequestBody.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def description(self):
        r"""Gets the description of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateTrustedKeySpaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateTrustedKeySpaceRequestBody.

        **参数解释：** 密钥空间描述信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateTrustedKeySpaceRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateTrustedKeySpaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
