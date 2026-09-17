# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesPageTagList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'name': 'str',
        'color': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'creator_id': 'str',
        'updater_id': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'name': 'name',
        'color': 'color',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'creator_id': 'creator_id',
        'updater_id': 'updater_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, tag_id=None, name=None, color=None, project_id=None, domain_id=None, creator_id=None, updater_id=None, create_time=None, update_time=None):
        r"""ListPipelinesPageTagList

        The model defined in huaweicloud sdk

        :param tag_id: **参数解释**： 标签ID。 **取值范围**： 不涉及。 
        :type tag_id: str
        :param name: **参数解释**： 标签名称。 **取值范围**： 不涉及。 
        :type name: str
        :param color: **参数解释**： 标签颜色。 **取值范围**： 不涉及。 
        :type color: str
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 不涉及。 
        :type project_id: str
        :param domain_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。 
        :type domain_id: str
        :param creator_id: **参数解释**： 创建人ID。 **取值范围**： 不涉及。 
        :type creator_id: str
        :param updater_id: **参数解释**： 更新人ID。 **取值范围**： 不涉及。 
        :type updater_id: str
        :param create_time: **参数解释**： 创建时间。 **取值范围**： 不涉及。 
        :type create_time: int
        :param update_time: **参数解释**： 更新时间。 **取值范围**： 不涉及。 
        :type update_time: int
        """
        
        

        self._tag_id = None
        self._name = None
        self._color = None
        self._project_id = None
        self._domain_id = None
        self._creator_id = None
        self._updater_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def tag_id(self):
        r"""Gets the tag_id of this ListPipelinesPageTagList.

        **参数解释**： 标签ID。 **取值范围**： 不涉及。 

        :return: The tag_id of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this ListPipelinesPageTagList.

        **参数解释**： 标签ID。 **取值范围**： 不涉及。 

        :param tag_id: The tag_id of this ListPipelinesPageTagList.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def name(self):
        r"""Gets the name of this ListPipelinesPageTagList.

        **参数解释**： 标签名称。 **取值范围**： 不涉及。 

        :return: The name of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPipelinesPageTagList.

        **参数解释**： 标签名称。 **取值范围**： 不涉及。 

        :param name: The name of this ListPipelinesPageTagList.
        :type name: str
        """
        self._name = name

    @property
    def color(self):
        r"""Gets the color of this ListPipelinesPageTagList.

        **参数解释**： 标签颜色。 **取值范围**： 不涉及。 

        :return: The color of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this ListPipelinesPageTagList.

        **参数解释**： 标签颜色。 **取值范围**： 不涉及。 

        :param color: The color of this ListPipelinesPageTagList.
        :type color: str
        """
        self._color = color

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPipelinesPageTagList.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。 

        :return: The project_id of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPipelinesPageTagList.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。 

        :param project_id: The project_id of this ListPipelinesPageTagList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListPipelinesPageTagList.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。 

        :return: The domain_id of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListPipelinesPageTagList.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。 

        :param domain_id: The domain_id of this ListPipelinesPageTagList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ListPipelinesPageTagList.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。 

        :return: The creator_id of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ListPipelinesPageTagList.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。 

        :param creator_id: The creator_id of this ListPipelinesPageTagList.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def updater_id(self):
        r"""Gets the updater_id of this ListPipelinesPageTagList.

        **参数解释**： 更新人ID。 **取值范围**： 不涉及。 

        :return: The updater_id of this ListPipelinesPageTagList.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        r"""Sets the updater_id of this ListPipelinesPageTagList.

        **参数解释**： 更新人ID。 **取值范围**： 不涉及。 

        :param updater_id: The updater_id of this ListPipelinesPageTagList.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListPipelinesPageTagList.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :return: The create_time of this ListPipelinesPageTagList.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListPipelinesPageTagList.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :param create_time: The create_time of this ListPipelinesPageTagList.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListPipelinesPageTagList.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。 

        :return: The update_time of this ListPipelinesPageTagList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListPipelinesPageTagList.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。 

        :param update_time: The update_time of this ListPipelinesPageTagList.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ListPipelinesPageTagList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
