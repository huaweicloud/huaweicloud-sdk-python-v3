# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompliancePackageModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'name': 'str',
        'version': 'str',
        'owner': 'str',
        'spec_catalog_vo_list': 'list[BaselineCatalogModel]',
        'description': 'str',
        'classify': 'str',
        'areas': 'str',
        'region': 'str',
        'state': 'int',
        'type': 'int',
        'check_items_num': 'int',
        'has_auto_check_items': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'version': 'version',
        'owner': 'owner',
        'spec_catalog_vo_list': 'spec_catalog_vo_list',
        'description': 'description',
        'classify': 'classify',
        'areas': 'areas',
        'region': 'region',
        'state': 'state',
        'type': 'type',
        'check_items_num': 'check_items_num',
        'has_auto_check_items': 'has_auto_check_items'
    }

    def __init__(self, uuid=None, name=None, version=None, owner=None, spec_catalog_vo_list=None, description=None, classify=None, areas=None, region=None, state=None, type=None, check_items_num=None, has_auto_check_items=None):
        r"""CompliancePackageModel

        The model defined in huaweicloud sdk

        :param uuid: 遵从包的uuid
        :type uuid: str
        :param name: 遵从包的名称
        :type name: str
        :param version: 遵从包的版本号
        :type version: str
        :param owner: 遵从包的责任人
        :type owner: str
        :param spec_catalog_vo_list: 遵从包的目录列表
        :type spec_catalog_vo_list: list[:class:`huaweicloudsdksecmaster.v2.BaselineCatalogModel`]
        :param description: 对遵从包的描述
        :type description: str
        :param classify: 遵从包的分类
        :type classify: str
        :param areas: 遵从包适用的领域
        :type areas: str
        :param region: 遵从包适用的区域
        :type region: str
        :param state: 表示遵从包的状态 0：未启用 1: 启用
        :type state: int
        :param type: 表示遵从包的类型 0：内置 1: 自定义
        :type type: int
        :param check_items_num: 表示该遵从包包含的检查项个数
        :type check_items_num: int
        :param has_auto_check_items: 表示该遵从包是否包含自动检查项
        :type has_auto_check_items: bool
        """
        
        

        self._uuid = None
        self._name = None
        self._version = None
        self._owner = None
        self._spec_catalog_vo_list = None
        self._description = None
        self._classify = None
        self._areas = None
        self._region = None
        self._state = None
        self._type = None
        self._check_items_num = None
        self._has_auto_check_items = None
        self.discriminator = None

        self.uuid = uuid
        self.name = name
        if version is not None:
            self.version = version
        if owner is not None:
            self.owner = owner
        if spec_catalog_vo_list is not None:
            self.spec_catalog_vo_list = spec_catalog_vo_list
        self.description = description
        if classify is not None:
            self.classify = classify
        if areas is not None:
            self.areas = areas
        if region is not None:
            self.region = region
        self.state = state
        if type is not None:
            self.type = type
        if check_items_num is not None:
            self.check_items_num = check_items_num
        if has_auto_check_items is not None:
            self.has_auto_check_items = has_auto_check_items

    @property
    def uuid(self):
        r"""Gets the uuid of this CompliancePackageModel.

        遵从包的uuid

        :return: The uuid of this CompliancePackageModel.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this CompliancePackageModel.

        遵从包的uuid

        :param uuid: The uuid of this CompliancePackageModel.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def name(self):
        r"""Gets the name of this CompliancePackageModel.

        遵从包的名称

        :return: The name of this CompliancePackageModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CompliancePackageModel.

        遵从包的名称

        :param name: The name of this CompliancePackageModel.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this CompliancePackageModel.

        遵从包的版本号

        :return: The version of this CompliancePackageModel.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CompliancePackageModel.

        遵从包的版本号

        :param version: The version of this CompliancePackageModel.
        :type version: str
        """
        self._version = version

    @property
    def owner(self):
        r"""Gets the owner of this CompliancePackageModel.

        遵从包的责任人

        :return: The owner of this CompliancePackageModel.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CompliancePackageModel.

        遵从包的责任人

        :param owner: The owner of this CompliancePackageModel.
        :type owner: str
        """
        self._owner = owner

    @property
    def spec_catalog_vo_list(self):
        r"""Gets the spec_catalog_vo_list of this CompliancePackageModel.

        遵从包的目录列表

        :return: The spec_catalog_vo_list of this CompliancePackageModel.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.BaselineCatalogModel`]
        """
        return self._spec_catalog_vo_list

    @spec_catalog_vo_list.setter
    def spec_catalog_vo_list(self, spec_catalog_vo_list):
        r"""Sets the spec_catalog_vo_list of this CompliancePackageModel.

        遵从包的目录列表

        :param spec_catalog_vo_list: The spec_catalog_vo_list of this CompliancePackageModel.
        :type spec_catalog_vo_list: list[:class:`huaweicloudsdksecmaster.v2.BaselineCatalogModel`]
        """
        self._spec_catalog_vo_list = spec_catalog_vo_list

    @property
    def description(self):
        r"""Gets the description of this CompliancePackageModel.

        对遵从包的描述

        :return: The description of this CompliancePackageModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CompliancePackageModel.

        对遵从包的描述

        :param description: The description of this CompliancePackageModel.
        :type description: str
        """
        self._description = description

    @property
    def classify(self):
        r"""Gets the classify of this CompliancePackageModel.

        遵从包的分类

        :return: The classify of this CompliancePackageModel.
        :rtype: str
        """
        return self._classify

    @classify.setter
    def classify(self, classify):
        r"""Sets the classify of this CompliancePackageModel.

        遵从包的分类

        :param classify: The classify of this CompliancePackageModel.
        :type classify: str
        """
        self._classify = classify

    @property
    def areas(self):
        r"""Gets the areas of this CompliancePackageModel.

        遵从包适用的领域

        :return: The areas of this CompliancePackageModel.
        :rtype: str
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        r"""Sets the areas of this CompliancePackageModel.

        遵从包适用的领域

        :param areas: The areas of this CompliancePackageModel.
        :type areas: str
        """
        self._areas = areas

    @property
    def region(self):
        r"""Gets the region of this CompliancePackageModel.

        遵从包适用的区域

        :return: The region of this CompliancePackageModel.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CompliancePackageModel.

        遵从包适用的区域

        :param region: The region of this CompliancePackageModel.
        :type region: str
        """
        self._region = region

    @property
    def state(self):
        r"""Gets the state of this CompliancePackageModel.

        表示遵从包的状态 0：未启用 1: 启用

        :return: The state of this CompliancePackageModel.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CompliancePackageModel.

        表示遵从包的状态 0：未启用 1: 启用

        :param state: The state of this CompliancePackageModel.
        :type state: int
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this CompliancePackageModel.

        表示遵从包的类型 0：内置 1: 自定义

        :return: The type of this CompliancePackageModel.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CompliancePackageModel.

        表示遵从包的类型 0：内置 1: 自定义

        :param type: The type of this CompliancePackageModel.
        :type type: int
        """
        self._type = type

    @property
    def check_items_num(self):
        r"""Gets the check_items_num of this CompliancePackageModel.

        表示该遵从包包含的检查项个数

        :return: The check_items_num of this CompliancePackageModel.
        :rtype: int
        """
        return self._check_items_num

    @check_items_num.setter
    def check_items_num(self, check_items_num):
        r"""Sets the check_items_num of this CompliancePackageModel.

        表示该遵从包包含的检查项个数

        :param check_items_num: The check_items_num of this CompliancePackageModel.
        :type check_items_num: int
        """
        self._check_items_num = check_items_num

    @property
    def has_auto_check_items(self):
        r"""Gets the has_auto_check_items of this CompliancePackageModel.

        表示该遵从包是否包含自动检查项

        :return: The has_auto_check_items of this CompliancePackageModel.
        :rtype: bool
        """
        return self._has_auto_check_items

    @has_auto_check_items.setter
    def has_auto_check_items(self, has_auto_check_items):
        r"""Sets the has_auto_check_items of this CompliancePackageModel.

        表示该遵从包是否包含自动检查项

        :param has_auto_check_items: The has_auto_check_items of this CompliancePackageModel.
        :type has_auto_check_items: bool
        """
        self._has_auto_check_items = has_auto_check_items

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
        if not isinstance(other, CompliancePackageModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
