# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassResponseBody:

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
        'create_time': 'str',
        'update_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'cloud_pack_version': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'business_code': 'str',
        'description': 'str',
        'is_built_in': 'bool',
        'parent_id': 'str',
        'type_num': 'float'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'cloud_pack_version': 'cloud_pack_version',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'business_code': 'business_code',
        'description': 'description',
        'is_built_in': 'is_built_in',
        'parent_id': 'parent_id',
        'type_num': 'type_num'
    }

    def __init__(self, id=None, create_time=None, update_time=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, cloud_pack_version=None, region_id=None, project_id=None, workspace_id=None, domain_id=None, name=None, business_code=None, description=None, is_built_in=None, parent_id=None, type_num=None):
        r"""DataClassResponseBody

        The model defined in huaweicloud sdk

        :param id: 数据类ID
        :type id: str
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
        :param modifier_name: 修改这名称
        :type modifier_name: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param region_id: 区域ID
        :type region_id: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param domain_id: domain id
        :type domain_id: str
        :param name: 数据类名称
        :type name: str
        :param business_code: 数据类业务编码
        :type business_code: str
        :param description: 数据类描述
        :type description: str
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
        :param parent_id: 父级id
        :type parent_id: str
        :param type_num: 子类型数量
        :type type_num: float
        """
        
        

        self._id = None
        self._create_time = None
        self._update_time = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._cloud_pack_version = None
        self._region_id = None
        self._project_id = None
        self._workspace_id = None
        self._domain_id = None
        self._name = None
        self._business_code = None
        self._description = None
        self._is_built_in = None
        self._parent_id = None
        self._type_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if business_code is not None:
            self.business_code = business_code
        if description is not None:
            self.description = description
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if parent_id is not None:
            self.parent_id = parent_id
        if type_num is not None:
            self.type_num = type_num

    @property
    def id(self):
        r"""Gets the id of this DataClassResponseBody.

        数据类ID

        :return: The id of this DataClassResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataClassResponseBody.

        数据类ID

        :param id: The id of this DataClassResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this DataClassResponseBody.

        创建时间

        :return: The create_time of this DataClassResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DataClassResponseBody.

        创建时间

        :param create_time: The create_time of this DataClassResponseBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DataClassResponseBody.

        更新时间

        :return: The update_time of this DataClassResponseBody.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DataClassResponseBody.

        更新时间

        :param update_time: The update_time of this DataClassResponseBody.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this DataClassResponseBody.

        创建者ID

        :return: The creator_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this DataClassResponseBody.

        创建者ID

        :param creator_id: The creator_id of this DataClassResponseBody.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this DataClassResponseBody.

        创建者名称

        :return: The creator_name of this DataClassResponseBody.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this DataClassResponseBody.

        创建者名称

        :param creator_name: The creator_name of this DataClassResponseBody.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this DataClassResponseBody.

        修改者ID

        :return: The modifier_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this DataClassResponseBody.

        修改者ID

        :param modifier_id: The modifier_id of this DataClassResponseBody.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this DataClassResponseBody.

        修改这名称

        :return: The modifier_name of this DataClassResponseBody.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this DataClassResponseBody.

        修改这名称

        :param modifier_name: The modifier_name of this DataClassResponseBody.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this DataClassResponseBody.

        订阅包版本

        :return: The cloud_pack_version of this DataClassResponseBody.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this DataClassResponseBody.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this DataClassResponseBody.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def region_id(self):
        r"""Gets the region_id of this DataClassResponseBody.

        区域ID

        :return: The region_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this DataClassResponseBody.

        区域ID

        :param region_id: The region_id of this DataClassResponseBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this DataClassResponseBody.

        租户ID

        :return: The project_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DataClassResponseBody.

        租户ID

        :param project_id: The project_id of this DataClassResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DataClassResponseBody.

        工作空间ID

        :return: The workspace_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DataClassResponseBody.

        工作空间ID

        :param workspace_id: The workspace_id of this DataClassResponseBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DataClassResponseBody.

        domain id

        :return: The domain_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DataClassResponseBody.

        domain id

        :param domain_id: The domain_id of this DataClassResponseBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this DataClassResponseBody.

        数据类名称

        :return: The name of this DataClassResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataClassResponseBody.

        数据类名称

        :param name: The name of this DataClassResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def business_code(self):
        r"""Gets the business_code of this DataClassResponseBody.

        数据类业务编码

        :return: The business_code of this DataClassResponseBody.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        r"""Sets the business_code of this DataClassResponseBody.

        数据类业务编码

        :param business_code: The business_code of this DataClassResponseBody.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def description(self):
        r"""Gets the description of this DataClassResponseBody.

        数据类描述

        :return: The description of this DataClassResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataClassResponseBody.

        数据类描述

        :param description: The description of this DataClassResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this DataClassResponseBody.

        是否内置，true内置，false非内置

        :return: The is_built_in of this DataClassResponseBody.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this DataClassResponseBody.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this DataClassResponseBody.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DataClassResponseBody.

        父级id

        :return: The parent_id of this DataClassResponseBody.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DataClassResponseBody.

        父级id

        :param parent_id: The parent_id of this DataClassResponseBody.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def type_num(self):
        r"""Gets the type_num of this DataClassResponseBody.

        子类型数量

        :return: The type_num of this DataClassResponseBody.
        :rtype: float
        """
        return self._type_num

    @type_num.setter
    def type_num(self, type_num):
        r"""Sets the type_num of this DataClassResponseBody.

        子类型数量

        :param type_num: The type_num of this DataClassResponseBody.
        :type type_num: float
        """
        self._type_num = type_num

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
        if not isinstance(other, DataClassResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
