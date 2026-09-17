# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueNewAssignedTo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'first_name': 'str',
        'last_name': 'str',
        'identifier': 'str',
        'image_id': 'str',
        'assigned_nick_name': 'str',
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'identifier': 'identifier',
        'image_id': 'image_id',
        'assigned_nick_name': 'assignedNickName',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, first_name=None, last_name=None, identifier=None, image_id=None, assigned_nick_name=None, name=None, id=None):
        r"""IssueNewAssignedTo

        The model defined in huaweicloud sdk

        :param first_name: **参数解释：** 用户名。 **取值范围：** 不涉及。
        :type first_name: str
        :param last_name: **参数解释：** 用户姓名。 **取值范围：** 不涉及。
        :type last_name: str
        :param identifier: **参数解释：** 用户32位uuid。 **取值范围：** 不涉及。
        :type identifier: str
        :param image_id: **参数解释：** 用户头像id。 **取值范围：** 不涉及。
        :type image_id: str
        :param assigned_nick_name: **参数解释：** 用户昵称。 **取值范围：** 不涉及。
        :type assigned_nick_name: str
        :param name: **参数解释：** 用户名。 **取值范围：** 不涉及。
        :type name: str
        :param id: **参数解释：** 用户数字id。 **取值范围：** 不涉及。
        :type id: int
        """
        
        

        self._first_name = None
        self._last_name = None
        self._identifier = None
        self._image_id = None
        self._assigned_nick_name = None
        self._name = None
        self._id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if identifier is not None:
            self.identifier = identifier
        if image_id is not None:
            self.image_id = image_id
        if assigned_nick_name is not None:
            self.assigned_nick_name = assigned_nick_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def first_name(self):
        r"""Gets the first_name of this IssueNewAssignedTo.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :return: The first_name of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        r"""Sets the first_name of this IssueNewAssignedTo.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :param first_name: The first_name of this IssueNewAssignedTo.
        :type first_name: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        r"""Gets the last_name of this IssueNewAssignedTo.

        **参数解释：** 用户姓名。 **取值范围：** 不涉及。

        :return: The last_name of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        r"""Sets the last_name of this IssueNewAssignedTo.

        **参数解释：** 用户姓名。 **取值范围：** 不涉及。

        :param last_name: The last_name of this IssueNewAssignedTo.
        :type last_name: str
        """
        self._last_name = last_name

    @property
    def identifier(self):
        r"""Gets the identifier of this IssueNewAssignedTo.

        **参数解释：** 用户32位uuid。 **取值范围：** 不涉及。

        :return: The identifier of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this IssueNewAssignedTo.

        **参数解释：** 用户32位uuid。 **取值范围：** 不涉及。

        :param identifier: The identifier of this IssueNewAssignedTo.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def image_id(self):
        r"""Gets the image_id of this IssueNewAssignedTo.

        **参数解释：** 用户头像id。 **取值范围：** 不涉及。

        :return: The image_id of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this IssueNewAssignedTo.

        **参数解释：** 用户头像id。 **取值范围：** 不涉及。

        :param image_id: The image_id of this IssueNewAssignedTo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def assigned_nick_name(self):
        r"""Gets the assigned_nick_name of this IssueNewAssignedTo.

        **参数解释：** 用户昵称。 **取值范围：** 不涉及。

        :return: The assigned_nick_name of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._assigned_nick_name

    @assigned_nick_name.setter
    def assigned_nick_name(self, assigned_nick_name):
        r"""Sets the assigned_nick_name of this IssueNewAssignedTo.

        **参数解释：** 用户昵称。 **取值范围：** 不涉及。

        :param assigned_nick_name: The assigned_nick_name of this IssueNewAssignedTo.
        :type assigned_nick_name: str
        """
        self._assigned_nick_name = assigned_nick_name

    @property
    def name(self):
        r"""Gets the name of this IssueNewAssignedTo.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :return: The name of this IssueNewAssignedTo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IssueNewAssignedTo.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :param name: The name of this IssueNewAssignedTo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this IssueNewAssignedTo.

        **参数解释：** 用户数字id。 **取值范围：** 不涉及。

        :return: The id of this IssueNewAssignedTo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueNewAssignedTo.

        **参数解释：** 用户数字id。 **取值范围：** 不涉及。

        :param id: The id of this IssueNewAssignedTo.
        :type id: int
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
        if not isinstance(other, IssueNewAssignedTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
