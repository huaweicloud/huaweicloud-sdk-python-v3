# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2JobTypeObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, uid=None, creation_timestamp=None, update_timestamp=None):
        r"""V2JobTypeObject

        The model defined in huaweicloud sdk

        :param uid: **参数解释**： Job UUID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type uid: str
        :param creation_timestamp: **参数解释**： Job 创建时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type creation_timestamp: str
        :param update_timestamp: **参数解释**： Job 最后更新时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type update_timestamp: str
        """
        
        

        self._uid = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def uid(self):
        r"""Gets the uid of this V2JobTypeObject.

        **参数解释**： Job UUID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The uid of this V2JobTypeObject.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this V2JobTypeObject.

        **参数解释**： Job UUID **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param uid: The uid of this V2JobTypeObject.
        :type uid: str
        """
        self._uid = uid

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this V2JobTypeObject.

        **参数解释**： Job 创建时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The creation_timestamp of this V2JobTypeObject.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this V2JobTypeObject.

        **参数解释**： Job 创建时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param creation_timestamp: The creation_timestamp of this V2JobTypeObject.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this V2JobTypeObject.

        **参数解释**： Job 最后更新时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The update_timestamp of this V2JobTypeObject.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this V2JobTypeObject.

        **参数解释**： Job 最后更新时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param update_timestamp: The update_timestamp of this V2JobTypeObject.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, V2JobTypeObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
