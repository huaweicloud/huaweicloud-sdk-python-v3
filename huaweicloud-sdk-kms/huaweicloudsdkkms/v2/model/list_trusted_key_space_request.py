# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrustedKeySpaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'keyspace_id': 'str',
        'type': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'keyspace_id': 'keyspace_id',
        'type': 'type'
    }

    def __init__(self, limit=None, marker=None, keyspace_id=None, type=None):
        r"""ListTrustedKeySpaceRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 分页参数，每一页显示的记录数 **约束限制：** 数字类型 **取值范围：** 1-100 **默认取值：** 50
        :type limit: str
        :param marker: **参数解释：** 分页参数，下一页的标志 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type marker: str
        :param keyspace_id: **参数解释：** 密钥空间ID，用于过滤 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type keyspace_id: str
        :param type: **参数解释：** 密钥空间类型，用于过滤 **约束限制：** 数字类型 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: int
        """
        
        

        self._limit = None
        self._marker = None
        self._keyspace_id = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if keyspace_id is not None:
            self.keyspace_id = keyspace_id
        if type is not None:
            self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListTrustedKeySpaceRequest.

        **参数解释：** 分页参数，每一页显示的记录数 **约束限制：** 数字类型 **取值范围：** 1-100 **默认取值：** 50

        :return: The limit of this ListTrustedKeySpaceRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrustedKeySpaceRequest.

        **参数解释：** 分页参数，每一页显示的记录数 **约束限制：** 数字类型 **取值范围：** 1-100 **默认取值：** 50

        :param limit: The limit of this ListTrustedKeySpaceRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTrustedKeySpaceRequest.

        **参数解释：** 分页参数，下一页的标志 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The marker of this ListTrustedKeySpaceRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTrustedKeySpaceRequest.

        **参数解释：** 分页参数，下一页的标志 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param marker: The marker of this ListTrustedKeySpaceRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this ListTrustedKeySpaceRequest.

        **参数解释：** 密钥空间ID，用于过滤 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The keyspace_id of this ListTrustedKeySpaceRequest.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this ListTrustedKeySpaceRequest.

        **参数解释：** 密钥空间ID，用于过滤 **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param keyspace_id: The keyspace_id of this ListTrustedKeySpaceRequest.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def type(self):
        r"""Gets the type of this ListTrustedKeySpaceRequest.

        **参数解释：** 密钥空间类型，用于过滤 **约束限制：** 数字类型 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this ListTrustedKeySpaceRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListTrustedKeySpaceRequest.

        **参数解释：** 密钥空间类型，用于过滤 **约束限制：** 数字类型 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this ListTrustedKeySpaceRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ListTrustedKeySpaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
