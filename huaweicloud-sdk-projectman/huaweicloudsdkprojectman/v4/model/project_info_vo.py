# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectInfoVO:

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
        'project_type': 'str',
        'domain_id': 'str',
        'model_id': 'str',
        'accept_rr': 'int',
        'category': 'str',
        'created_by_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_type': 'project_type',
        'domain_id': 'domain_id',
        'model_id': 'model_id',
        'accept_rr': 'accept_rr',
        'category': 'category',
        'created_by_name': 'created_by_name'
    }

    def __init__(self, id=None, name=None, project_type=None, domain_id=None, model_id=None, accept_rr=None, category=None, created_by_name=None):
        r"""ProjectInfoVO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 项目ID。 **取值范围**： 不涉及
        :type id: str
        :param name: **参数解释**： 项目名称。 **取值范围**： 不涉及
        :type name: str
        :param project_type: **参数解释**： 项目类型。 **取值范围**： - ipd：IPD项目 - scrum：scrum项目 - xboard：看板项目
        :type project_type: str
        :param domain_id: **参数解释**： 项目空间ID。 **取值范围**： 不涉及
        :type domain_id: str
        :param model_id: **参数解释**： IPD项目模型Id。 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型）
        :type model_id: str
        :param accept_rr: **参数解释**： 该项目是否接受外部RR（原始需求）。 **取值范围**： - 0：不接受外部RR - 1：接受外部RR
        :type accept_rr: int
        :param category: **参数解释**： 项目类型，用于区分项目和项目群。 **取值范围**： - Project：项目 - Group：项目群
        :type category: str
        :param created_by_name: **参数解释**： 项目创建人名称。 **取值范围**： 不涉及。
        :type created_by_name: str
        """
        
        

        self._id = None
        self._name = None
        self._project_type = None
        self._domain_id = None
        self._model_id = None
        self._accept_rr = None
        self._category = None
        self._created_by_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_type is not None:
            self.project_type = project_type
        if domain_id is not None:
            self.domain_id = domain_id
        if model_id is not None:
            self.model_id = model_id
        if accept_rr is not None:
            self.accept_rr = accept_rr
        if category is not None:
            self.category = category
        if created_by_name is not None:
            self.created_by_name = created_by_name

    @property
    def id(self):
        r"""Gets the id of this ProjectInfoVO.

        **参数解释**： 项目ID。 **取值范围**： 不涉及

        :return: The id of this ProjectInfoVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectInfoVO.

        **参数解释**： 项目ID。 **取值范围**： 不涉及

        :param id: The id of this ProjectInfoVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ProjectInfoVO.

        **参数解释**： 项目名称。 **取值范围**： 不涉及

        :return: The name of this ProjectInfoVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectInfoVO.

        **参数解释**： 项目名称。 **取值范围**： 不涉及

        :param name: The name of this ProjectInfoVO.
        :type name: str
        """
        self._name = name

    @property
    def project_type(self):
        r"""Gets the project_type of this ProjectInfoVO.

        **参数解释**： 项目类型。 **取值范围**： - ipd：IPD项目 - scrum：scrum项目 - xboard：看板项目

        :return: The project_type of this ProjectInfoVO.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this ProjectInfoVO.

        **参数解释**： 项目类型。 **取值范围**： - ipd：IPD项目 - scrum：scrum项目 - xboard：看板项目

        :param project_type: The project_type of this ProjectInfoVO.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProjectInfoVO.

        **参数解释**： 项目空间ID。 **取值范围**： 不涉及

        :return: The domain_id of this ProjectInfoVO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProjectInfoVO.

        **参数解释**： 项目空间ID。 **取值范围**： 不涉及

        :param domain_id: The domain_id of this ProjectInfoVO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ProjectInfoVO.

        **参数解释**： IPD项目模型Id。 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型）

        :return: The model_id of this ProjectInfoVO.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ProjectInfoVO.

        **参数解释**： IPD项目模型Id。 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型）

        :param model_id: The model_id of this ProjectInfoVO.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def accept_rr(self):
        r"""Gets the accept_rr of this ProjectInfoVO.

        **参数解释**： 该项目是否接受外部RR（原始需求）。 **取值范围**： - 0：不接受外部RR - 1：接受外部RR

        :return: The accept_rr of this ProjectInfoVO.
        :rtype: int
        """
        return self._accept_rr

    @accept_rr.setter
    def accept_rr(self, accept_rr):
        r"""Sets the accept_rr of this ProjectInfoVO.

        **参数解释**： 该项目是否接受外部RR（原始需求）。 **取值范围**： - 0：不接受外部RR - 1：接受外部RR

        :param accept_rr: The accept_rr of this ProjectInfoVO.
        :type accept_rr: int
        """
        self._accept_rr = accept_rr

    @property
    def category(self):
        r"""Gets the category of this ProjectInfoVO.

        **参数解释**： 项目类型，用于区分项目和项目群。 **取值范围**： - Project：项目 - Group：项目群

        :return: The category of this ProjectInfoVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ProjectInfoVO.

        **参数解释**： 项目类型，用于区分项目和项目群。 **取值范围**： - Project：项目 - Group：项目群

        :param category: The category of this ProjectInfoVO.
        :type category: str
        """
        self._category = category

    @property
    def created_by_name(self):
        r"""Gets the created_by_name of this ProjectInfoVO.

        **参数解释**： 项目创建人名称。 **取值范围**： 不涉及。

        :return: The created_by_name of this ProjectInfoVO.
        :rtype: str
        """
        return self._created_by_name

    @created_by_name.setter
    def created_by_name(self, created_by_name):
        r"""Sets the created_by_name of this ProjectInfoVO.

        **参数解释**： 项目创建人名称。 **取值范围**： 不涉及。

        :param created_by_name: The created_by_name of this ProjectInfoVO.
        :type created_by_name: str
        """
        self._created_by_name = created_by_name

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
        if not isinstance(other, ProjectInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
