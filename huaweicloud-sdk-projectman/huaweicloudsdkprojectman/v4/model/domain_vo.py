# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'title': 'str',
        'project_id': 'str',
        'parent_id': 'str',
        'category': 'str',
        'created_by': 'str',
        'model_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'title': 'title',
        'project_id': 'project_id',
        'parent_id': 'parent_id',
        'category': 'category',
        'created_by': 'created_by',
        'model_id': 'model_id'
    }

    def __init__(self, id=None, name=None, title=None, project_id=None, parent_id=None, category=None, created_by=None, model_id=None):
        r"""DomainVO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  项目空间的唯一Id。 **取值范围：**  不涉及。
        :type id: str
        :param name: **参数解释：**  项目空间名称。 **取值范围：**  不涉及。
        :type name: str
        :param title: **参数解释：**  项目空间名称。 **取值范围：**  不涉及。
        :type title: str
        :param project_id: **参数解释：**  项目空间对应的32位UUId。 **取值范围：**  不涉及。
        :type project_id: str
        :param parent_id: **参数解释：**  项目空间的父项目空间Id，仅在项目群中使用。 **取值范围：**  不涉及。
        :type parent_id: str
        :param category: **参数解释：**  项目空间类型。 **取值范围：**  -  Project：项目 - Group：项目群
        :type category: str
        :param created_by: **参数解释：**  项目空间创建人Id。 **取值范围：**  不涉及。
        :type created_by: str
        :param model_id: **参数解释：**  项目空间对应的模型Id。 **取值范围：**  不涉及。 - 10001：系统设备类 - 10002：独立软件类 - 10003：自营软件/云服务类
        :type model_id: str
        """
        
        

        self._id = None
        self._name = None
        self._title = None
        self._project_id = None
        self._parent_id = None
        self._category = None
        self._created_by = None
        self._model_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if category is not None:
            self.category = category
        if created_by is not None:
            self.created_by = created_by
        if model_id is not None:
            self.model_id = model_id

    @property
    def id(self):
        r"""Gets the id of this DomainVO.

        **参数解释：**  项目空间的唯一Id。 **取值范围：**  不涉及。

        :return: The id of this DomainVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DomainVO.

        **参数解释：**  项目空间的唯一Id。 **取值范围：**  不涉及。

        :param id: The id of this DomainVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DomainVO.

        **参数解释：**  项目空间名称。 **取值范围：**  不涉及。

        :return: The name of this DomainVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DomainVO.

        **参数解释：**  项目空间名称。 **取值范围：**  不涉及。

        :param name: The name of this DomainVO.
        :type name: str
        """
        self._name = name

    @property
    def title(self):
        r"""Gets the title of this DomainVO.

        **参数解释：**  项目空间名称。 **取值范围：**  不涉及。

        :return: The title of this DomainVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DomainVO.

        **参数解释：**  项目空间名称。 **取值范围：**  不涉及。

        :param title: The title of this DomainVO.
        :type title: str
        """
        self._title = title

    @property
    def project_id(self):
        r"""Gets the project_id of this DomainVO.

        **参数解释：**  项目空间对应的32位UUId。 **取值范围：**  不涉及。

        :return: The project_id of this DomainVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DomainVO.

        **参数解释：**  项目空间对应的32位UUId。 **取值范围：**  不涉及。

        :param project_id: The project_id of this DomainVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DomainVO.

        **参数解释：**  项目空间的父项目空间Id，仅在项目群中使用。 **取值范围：**  不涉及。

        :return: The parent_id of this DomainVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DomainVO.

        **参数解释：**  项目空间的父项目空间Id，仅在项目群中使用。 **取值范围：**  不涉及。

        :param parent_id: The parent_id of this DomainVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def category(self):
        r"""Gets the category of this DomainVO.

        **参数解释：**  项目空间类型。 **取值范围：**  -  Project：项目 - Group：项目群

        :return: The category of this DomainVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this DomainVO.

        **参数解释：**  项目空间类型。 **取值范围：**  -  Project：项目 - Group：项目群

        :param category: The category of this DomainVO.
        :type category: str
        """
        self._category = category

    @property
    def created_by(self):
        r"""Gets the created_by of this DomainVO.

        **参数解释：**  项目空间创建人Id。 **取值范围：**  不涉及。

        :return: The created_by of this DomainVO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this DomainVO.

        **参数解释：**  项目空间创建人Id。 **取值范围：**  不涉及。

        :param created_by: The created_by of this DomainVO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def model_id(self):
        r"""Gets the model_id of this DomainVO.

        **参数解释：**  项目空间对应的模型Id。 **取值范围：**  不涉及。 - 10001：系统设备类 - 10002：独立软件类 - 10003：自营软件/云服务类

        :return: The model_id of this DomainVO.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this DomainVO.

        **参数解释：**  项目空间对应的模型Id。 **取值范围：**  不涉及。 - 10001：系统设备类 - 10002：独立软件类 - 10003：自营软件/云服务类

        :param model_id: The model_id of this DomainVO.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, DomainVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
