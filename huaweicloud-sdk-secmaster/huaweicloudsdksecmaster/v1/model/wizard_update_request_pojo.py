# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WizardUpdateRequestPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'creator_id': 'str',
        'description': 'str',
        'id': 'str',
        'wizard_json': 'str',
        'name': 'str',
        'update_time': 'str',
        'layout_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'is_binding': 'bool',
        'binding_button': 'list[WizardUpdateRequestPojoBindingButton]',
        'boa_version': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'description': 'description',
        'id': 'id',
        'wizard_json': 'wizard_json',
        'name': 'name',
        'update_time': 'update_time',
        'layout_id': 'layout_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'is_binding': 'is_binding',
        'binding_button': 'binding_button',
        'boa_version': 'boa_version'
    }

    def __init__(self, create_time=None, creator_id=None, description=None, id=None, wizard_json=None, name=None, update_time=None, layout_id=None, project_id=None, workspace_id=None, is_binding=None, binding_button=None, boa_version=None):
        r"""WizardUpdateRequestPojo

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param description: 描述信息
        :type description: str
        :param id: 页面ID
        :type id: str
        :param wizard_json: 布局页面相关信息
        :type wizard_json: str
        :param name: 页面名称
        :type name: str
        :param update_time: 更新时间
        :type update_time: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param is_binding: 是否已绑定按钮
        :type is_binding: bool
        :param binding_button: 绑定按钮
        :type binding_button: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojoBindingButton`]
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._create_time = None
        self._creator_id = None
        self._description = None
        self._id = None
        self._wizard_json = None
        self._name = None
        self._update_time = None
        self._layout_id = None
        self._project_id = None
        self._workspace_id = None
        self._is_binding = None
        self._binding_button = None
        self._boa_version = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if wizard_json is not None:
            self.wizard_json = wizard_json
        if name is not None:
            self.name = name
        if update_time is not None:
            self.update_time = update_time
        if layout_id is not None:
            self.layout_id = layout_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if is_binding is not None:
            self.is_binding = is_binding
        if binding_button is not None:
            self.binding_button = binding_button
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def create_time(self):
        r"""Gets the create_time of this WizardUpdateRequestPojo.

        创建时间

        :return: The create_time of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WizardUpdateRequestPojo.

        创建时间

        :param create_time: The create_time of this WizardUpdateRequestPojo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this WizardUpdateRequestPojo.

        创建者ID

        :return: The creator_id of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this WizardUpdateRequestPojo.

        创建者ID

        :param creator_id: The creator_id of this WizardUpdateRequestPojo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def description(self):
        r"""Gets the description of this WizardUpdateRequestPojo.

        描述信息

        :return: The description of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WizardUpdateRequestPojo.

        描述信息

        :param description: The description of this WizardUpdateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this WizardUpdateRequestPojo.

        页面ID

        :return: The id of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WizardUpdateRequestPojo.

        页面ID

        :param id: The id of this WizardUpdateRequestPojo.
        :type id: str
        """
        self._id = id

    @property
    def wizard_json(self):
        r"""Gets the wizard_json of this WizardUpdateRequestPojo.

        布局页面相关信息

        :return: The wizard_json of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._wizard_json

    @wizard_json.setter
    def wizard_json(self, wizard_json):
        r"""Sets the wizard_json of this WizardUpdateRequestPojo.

        布局页面相关信息

        :param wizard_json: The wizard_json of this WizardUpdateRequestPojo.
        :type wizard_json: str
        """
        self._wizard_json = wizard_json

    @property
    def name(self):
        r"""Gets the name of this WizardUpdateRequestPojo.

        页面名称

        :return: The name of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WizardUpdateRequestPojo.

        页面名称

        :param name: The name of this WizardUpdateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def update_time(self):
        r"""Gets the update_time of this WizardUpdateRequestPojo.

        更新时间

        :return: The update_time of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WizardUpdateRequestPojo.

        更新时间

        :param update_time: The update_time of this WizardUpdateRequestPojo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def layout_id(self):
        r"""Gets the layout_id of this WizardUpdateRequestPojo.

        布局ID

        :return: The layout_id of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this WizardUpdateRequestPojo.

        布局ID

        :param layout_id: The layout_id of this WizardUpdateRequestPojo.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def project_id(self):
        r"""Gets the project_id of this WizardUpdateRequestPojo.

        租户ID

        :return: The project_id of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this WizardUpdateRequestPojo.

        租户ID

        :param project_id: The project_id of this WizardUpdateRequestPojo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this WizardUpdateRequestPojo.

        工作空间ID

        :return: The workspace_id of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this WizardUpdateRequestPojo.

        工作空间ID

        :param workspace_id: The workspace_id of this WizardUpdateRequestPojo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def is_binding(self):
        r"""Gets the is_binding of this WizardUpdateRequestPojo.

        是否已绑定按钮

        :return: The is_binding of this WizardUpdateRequestPojo.
        :rtype: bool
        """
        return self._is_binding

    @is_binding.setter
    def is_binding(self, is_binding):
        r"""Sets the is_binding of this WizardUpdateRequestPojo.

        是否已绑定按钮

        :param is_binding: The is_binding of this WizardUpdateRequestPojo.
        :type is_binding: bool
        """
        self._is_binding = is_binding

    @property
    def binding_button(self):
        r"""Gets the binding_button of this WizardUpdateRequestPojo.

        绑定按钮

        :return: The binding_button of this WizardUpdateRequestPojo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojoBindingButton`]
        """
        return self._binding_button

    @binding_button.setter
    def binding_button(self, binding_button):
        r"""Sets the binding_button of this WizardUpdateRequestPojo.

        绑定按钮

        :param binding_button: The binding_button of this WizardUpdateRequestPojo.
        :type binding_button: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojoBindingButton`]
        """
        self._binding_button = binding_button

    @property
    def boa_version(self):
        r"""Gets the boa_version of this WizardUpdateRequestPojo.

        BOA底座版本

        :return: The boa_version of this WizardUpdateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this WizardUpdateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this WizardUpdateRequestPojo.
        :type boa_version: str
        """
        self._boa_version = boa_version

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
        if not isinstance(other, WizardUpdateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
