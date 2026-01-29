# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInfo:

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
        'dev_language': 'str',
        'dev_language_version': 'str',
        'alliance_id': 'str',
        'alliance_name': 'str',
        'description': 'str',
        'logo': 'str',
        'label': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'operation_history': 'list[ComponentInfoOperationHistory]',
        'versions': 'list[ComponentVersionInfo]',
        'component_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dev_language': 'dev_language',
        'dev_language_version': 'dev_language_version',
        'alliance_id': 'alliance_id',
        'alliance_name': 'alliance_name',
        'description': 'description',
        'logo': 'logo',
        'label': 'label',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'operation_history': 'operation_history',
        'versions': 'versions',
        'component_type': 'component_type'
    }

    def __init__(self, id=None, name=None, dev_language=None, dev_language_version=None, alliance_id=None, alliance_name=None, description=None, logo=None, label=None, create_time=None, update_time=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, operation_history=None, versions=None, component_type=None):
        r"""ComponentInfo

        The model defined in huaweicloud sdk

        :param id: 插件ID
        :type id: str
        :param name: 插件名称
        :type name: str
        :param dev_language: 插件的实现语言
        :type dev_language: str
        :param dev_language_version: 插件的实现语言版本
        :type dev_language_version: str
        :param alliance_id: 插件集ID
        :type alliance_id: str
        :param alliance_name: 插件集名称
        :type alliance_name: str
        :param description: 插件描述
        :type description: str
        :param logo: 插件图标
        :type logo: str
        :param label: 插件的标签信息
        :type label: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param modifier_id: 修改者ID
        :type modifier_id: str
        :param modifier_name: 修改者名称
        :type modifier_name: str
        :param operation_history: 插件操作历史
        :type operation_history: list[:class:`huaweicloudsdksecmaster.v1.ComponentInfoOperationHistory`]
        :param versions: 插件版本信息，兼容之前java的以插件为粒度的版本
        :type versions: list[:class:`huaweicloudsdksecmaster.v1.ComponentVersionInfo`]
        :param component_type: 插件类型，subscribe/custom/system，对应订阅/自定义开发/系统内置
        :type component_type: str
        """
        
        

        self._id = None
        self._name = None
        self._dev_language = None
        self._dev_language_version = None
        self._alliance_id = None
        self._alliance_name = None
        self._description = None
        self._logo = None
        self._label = None
        self._create_time = None
        self._update_time = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._operation_history = None
        self._versions = None
        self._component_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if dev_language is not None:
            self.dev_language = dev_language
        if dev_language_version is not None:
            self.dev_language_version = dev_language_version
        if alliance_id is not None:
            self.alliance_id = alliance_id
        if alliance_name is not None:
            self.alliance_name = alliance_name
        if description is not None:
            self.description = description
        if logo is not None:
            self.logo = logo
        if label is not None:
            self.label = label
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if operation_history is not None:
            self.operation_history = operation_history
        if versions is not None:
            self.versions = versions
        if component_type is not None:
            self.component_type = component_type

    @property
    def id(self):
        r"""Gets the id of this ComponentInfo.

        插件ID

        :return: The id of this ComponentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentInfo.

        插件ID

        :param id: The id of this ComponentInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ComponentInfo.

        插件名称

        :return: The name of this ComponentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentInfo.

        插件名称

        :param name: The name of this ComponentInfo.
        :type name: str
        """
        self._name = name

    @property
    def dev_language(self):
        r"""Gets the dev_language of this ComponentInfo.

        插件的实现语言

        :return: The dev_language of this ComponentInfo.
        :rtype: str
        """
        return self._dev_language

    @dev_language.setter
    def dev_language(self, dev_language):
        r"""Sets the dev_language of this ComponentInfo.

        插件的实现语言

        :param dev_language: The dev_language of this ComponentInfo.
        :type dev_language: str
        """
        self._dev_language = dev_language

    @property
    def dev_language_version(self):
        r"""Gets the dev_language_version of this ComponentInfo.

        插件的实现语言版本

        :return: The dev_language_version of this ComponentInfo.
        :rtype: str
        """
        return self._dev_language_version

    @dev_language_version.setter
    def dev_language_version(self, dev_language_version):
        r"""Sets the dev_language_version of this ComponentInfo.

        插件的实现语言版本

        :param dev_language_version: The dev_language_version of this ComponentInfo.
        :type dev_language_version: str
        """
        self._dev_language_version = dev_language_version

    @property
    def alliance_id(self):
        r"""Gets the alliance_id of this ComponentInfo.

        插件集ID

        :return: The alliance_id of this ComponentInfo.
        :rtype: str
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        r"""Sets the alliance_id of this ComponentInfo.

        插件集ID

        :param alliance_id: The alliance_id of this ComponentInfo.
        :type alliance_id: str
        """
        self._alliance_id = alliance_id

    @property
    def alliance_name(self):
        r"""Gets the alliance_name of this ComponentInfo.

        插件集名称

        :return: The alliance_name of this ComponentInfo.
        :rtype: str
        """
        return self._alliance_name

    @alliance_name.setter
    def alliance_name(self, alliance_name):
        r"""Sets the alliance_name of this ComponentInfo.

        插件集名称

        :param alliance_name: The alliance_name of this ComponentInfo.
        :type alliance_name: str
        """
        self._alliance_name = alliance_name

    @property
    def description(self):
        r"""Gets the description of this ComponentInfo.

        插件描述

        :return: The description of this ComponentInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentInfo.

        插件描述

        :param description: The description of this ComponentInfo.
        :type description: str
        """
        self._description = description

    @property
    def logo(self):
        r"""Gets the logo of this ComponentInfo.

        插件图标

        :return: The logo of this ComponentInfo.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        r"""Sets the logo of this ComponentInfo.

        插件图标

        :param logo: The logo of this ComponentInfo.
        :type logo: str
        """
        self._logo = logo

    @property
    def label(self):
        r"""Gets the label of this ComponentInfo.

        插件的标签信息

        :return: The label of this ComponentInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ComponentInfo.

        插件的标签信息

        :param label: The label of this ComponentInfo.
        :type label: str
        """
        self._label = label

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentInfo.

        创建时间

        :return: The create_time of this ComponentInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentInfo.

        创建时间

        :param create_time: The create_time of this ComponentInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentInfo.

        更新时间

        :return: The update_time of this ComponentInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentInfo.

        更新时间

        :param update_time: The update_time of this ComponentInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ComponentInfo.

        创建者ID

        :return: The creator_id of this ComponentInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ComponentInfo.

        创建者ID

        :param creator_id: The creator_id of this ComponentInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ComponentInfo.

        创建者名称

        :return: The creator_name of this ComponentInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ComponentInfo.

        创建者名称

        :param creator_name: The creator_name of this ComponentInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this ComponentInfo.

        修改者ID

        :return: The modifier_id of this ComponentInfo.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this ComponentInfo.

        修改者ID

        :param modifier_id: The modifier_id of this ComponentInfo.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this ComponentInfo.

        修改者名称

        :return: The modifier_name of this ComponentInfo.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this ComponentInfo.

        修改者名称

        :param modifier_name: The modifier_name of this ComponentInfo.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def operation_history(self):
        r"""Gets the operation_history of this ComponentInfo.

        插件操作历史

        :return: The operation_history of this ComponentInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentInfoOperationHistory`]
        """
        return self._operation_history

    @operation_history.setter
    def operation_history(self, operation_history):
        r"""Sets the operation_history of this ComponentInfo.

        插件操作历史

        :param operation_history: The operation_history of this ComponentInfo.
        :type operation_history: list[:class:`huaweicloudsdksecmaster.v1.ComponentInfoOperationHistory`]
        """
        self._operation_history = operation_history

    @property
    def versions(self):
        r"""Gets the versions of this ComponentInfo.

        插件版本信息，兼容之前java的以插件为粒度的版本

        :return: The versions of this ComponentInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentVersionInfo`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ComponentInfo.

        插件版本信息，兼容之前java的以插件为粒度的版本

        :param versions: The versions of this ComponentInfo.
        :type versions: list[:class:`huaweicloudsdksecmaster.v1.ComponentVersionInfo`]
        """
        self._versions = versions

    @property
    def component_type(self):
        r"""Gets the component_type of this ComponentInfo.

        插件类型，subscribe/custom/system，对应订阅/自定义开发/系统内置

        :return: The component_type of this ComponentInfo.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        r"""Sets the component_type of this ComponentInfo.

        插件类型，subscribe/custom/system，对应订阅/自定义开发/系统内置

        :param component_type: The component_type of this ComponentInfo.
        :type component_type: str
        """
        self._component_type = component_type

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
        if not isinstance(other, ComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
