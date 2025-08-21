# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectCreatorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username'
    }

    def __init__(self, id=None, name=None, username=None):
        r"""ProjectCreatorDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标识id。
        :type id: int
        :param name: **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param username: **参数解释：** iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type username: str
        """
        
        

        self._id = None
        self._name = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username

    @property
    def id(self):
        r"""Gets the id of this ProjectCreatorDto.

        **参数解释：** 唯一标识id。

        :return: The id of this ProjectCreatorDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectCreatorDto.

        **参数解释：** 唯一标识id。

        :param id: The id of this ProjectCreatorDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ProjectCreatorDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this ProjectCreatorDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectCreatorDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this ProjectCreatorDto.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this ProjectCreatorDto.

        **参数解释：** iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The username of this ProjectCreatorDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ProjectCreatorDto.

        **参数解释：** iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param username: The username of this ProjectCreatorDto.
        :type username: str
        """
        self._username = username

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
        if not isinstance(other, ProjectCreatorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
