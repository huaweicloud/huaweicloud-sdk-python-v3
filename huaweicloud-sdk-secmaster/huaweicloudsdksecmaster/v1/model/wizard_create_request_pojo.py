# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WizardCreateRequestPojo:

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
        'description': 'str',
        'layout_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'wizard_json': 'str',
        'is_binding': 'bool',
        'binding_button': 'list[WizardDetailInfoBindingButton]',
        'boa_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'layout_id': 'layout_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'wizard_json': 'wizard_json',
        'is_binding': 'is_binding',
        'binding_button': 'binding_button',
        'boa_version': 'boa_version'
    }

    def __init__(self, id=None, name=None, description=None, layout_id=None, project_id=None, workspace_id=None, wizard_json=None, is_binding=None, binding_button=None, boa_version=None):
        r"""WizardCreateRequestPojo

        The model defined in huaweicloud sdk

        :param id: 页面ID
        :type id: str
        :param name: 页面名称
        :type name: str
        :param description: 描述
        :type description: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param wizard_json: 布局页面相关信息
        :type wizard_json: str
        :param is_binding: 是否已绑定按钮
        :type is_binding: bool
        :param binding_button: 绑定按钮
        :type binding_button: list[:class:`huaweicloudsdksecmaster.v1.WizardDetailInfoBindingButton`]
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._layout_id = None
        self._project_id = None
        self._workspace_id = None
        self._wizard_json = None
        self._is_binding = None
        self._binding_button = None
        self._boa_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if layout_id is not None:
            self.layout_id = layout_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if wizard_json is not None:
            self.wizard_json = wizard_json
        if is_binding is not None:
            self.is_binding = is_binding
        if binding_button is not None:
            self.binding_button = binding_button
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def id(self):
        r"""Gets the id of this WizardCreateRequestPojo.

        页面ID

        :return: The id of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WizardCreateRequestPojo.

        页面ID

        :param id: The id of this WizardCreateRequestPojo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WizardCreateRequestPojo.

        页面名称

        :return: The name of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WizardCreateRequestPojo.

        页面名称

        :param name: The name of this WizardCreateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WizardCreateRequestPojo.

        描述

        :return: The description of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WizardCreateRequestPojo.

        描述

        :param description: The description of this WizardCreateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def layout_id(self):
        r"""Gets the layout_id of this WizardCreateRequestPojo.

        布局ID

        :return: The layout_id of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this WizardCreateRequestPojo.

        布局ID

        :param layout_id: The layout_id of this WizardCreateRequestPojo.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def project_id(self):
        r"""Gets the project_id of this WizardCreateRequestPojo.

        租户ID

        :return: The project_id of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this WizardCreateRequestPojo.

        租户ID

        :param project_id: The project_id of this WizardCreateRequestPojo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this WizardCreateRequestPojo.

        工作空间ID

        :return: The workspace_id of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this WizardCreateRequestPojo.

        工作空间ID

        :param workspace_id: The workspace_id of this WizardCreateRequestPojo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def wizard_json(self):
        r"""Gets the wizard_json of this WizardCreateRequestPojo.

        布局页面相关信息

        :return: The wizard_json of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._wizard_json

    @wizard_json.setter
    def wizard_json(self, wizard_json):
        r"""Sets the wizard_json of this WizardCreateRequestPojo.

        布局页面相关信息

        :param wizard_json: The wizard_json of this WizardCreateRequestPojo.
        :type wizard_json: str
        """
        self._wizard_json = wizard_json

    @property
    def is_binding(self):
        r"""Gets the is_binding of this WizardCreateRequestPojo.

        是否已绑定按钮

        :return: The is_binding of this WizardCreateRequestPojo.
        :rtype: bool
        """
        return self._is_binding

    @is_binding.setter
    def is_binding(self, is_binding):
        r"""Sets the is_binding of this WizardCreateRequestPojo.

        是否已绑定按钮

        :param is_binding: The is_binding of this WizardCreateRequestPojo.
        :type is_binding: bool
        """
        self._is_binding = is_binding

    @property
    def binding_button(self):
        r"""Gets the binding_button of this WizardCreateRequestPojo.

        绑定按钮

        :return: The binding_button of this WizardCreateRequestPojo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.WizardDetailInfoBindingButton`]
        """
        return self._binding_button

    @binding_button.setter
    def binding_button(self, binding_button):
        r"""Sets the binding_button of this WizardCreateRequestPojo.

        绑定按钮

        :param binding_button: The binding_button of this WizardCreateRequestPojo.
        :type binding_button: list[:class:`huaweicloudsdksecmaster.v1.WizardDetailInfoBindingButton`]
        """
        self._binding_button = binding_button

    @property
    def boa_version(self):
        r"""Gets the boa_version of this WizardCreateRequestPojo.

        BOA底座版本

        :return: The boa_version of this WizardCreateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this WizardCreateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this WizardCreateRequestPojo.
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
        if not isinstance(other, WizardCreateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
