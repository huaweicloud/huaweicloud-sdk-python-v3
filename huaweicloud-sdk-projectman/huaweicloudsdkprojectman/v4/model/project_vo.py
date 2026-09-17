# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'name': 'str',
        'id': 'int',
        'project_type': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'id': 'id',
        'project_type': 'project_type'
    }

    def __init__(self, identifier=None, name=None, id=None, project_type=None):
        r"""ProjectVO

        The model defined in huaweicloud sdk

        :param identifier: **参数解释：** 项目uuid **取值范围：** 不涉及。
        :type identifier: str
        :param name: **参数解释：** 项目名称 **取值范围：** 不涉及。
        :type name: str
        :param id: **参数解释：** 项目数字id **取值范围：** 不涉及。
        :type id: int
        :param project_type: **参数解释：** 项目类型 **取值范围：** scrum。
        :type project_type: str
        """
        
        

        self._identifier = None
        self._name = None
        self._id = None
        self._project_type = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if project_type is not None:
            self.project_type = project_type

    @property
    def identifier(self):
        r"""Gets the identifier of this ProjectVO.

        **参数解释：** 项目uuid **取值范围：** 不涉及。

        :return: The identifier of this ProjectVO.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this ProjectVO.

        **参数解释：** 项目uuid **取值范围：** 不涉及。

        :param identifier: The identifier of this ProjectVO.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def name(self):
        r"""Gets the name of this ProjectVO.

        **参数解释：** 项目名称 **取值范围：** 不涉及。

        :return: The name of this ProjectVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectVO.

        **参数解释：** 项目名称 **取值范围：** 不涉及。

        :param name: The name of this ProjectVO.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ProjectVO.

        **参数解释：** 项目数字id **取值范围：** 不涉及。

        :return: The id of this ProjectVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectVO.

        **参数解释：** 项目数字id **取值范围：** 不涉及。

        :param id: The id of this ProjectVO.
        :type id: int
        """
        self._id = id

    @property
    def project_type(self):
        r"""Gets the project_type of this ProjectVO.

        **参数解释：** 项目类型 **取值范围：** scrum。

        :return: The project_type of this ProjectVO.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this ProjectVO.

        **参数解释：** 项目类型 **取值范围：** scrum。

        :param project_type: The project_type of this ProjectVO.
        :type project_type: str
        """
        self._project_type = project_type

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
        if not isinstance(other, ProjectVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
