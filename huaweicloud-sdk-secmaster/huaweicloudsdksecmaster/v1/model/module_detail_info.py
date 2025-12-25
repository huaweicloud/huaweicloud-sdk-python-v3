# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModuleDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'cloud_pack_version': 'str',
        'create_time': 'str',
        'creator_id': 'str',
        'description': 'str',
        'en_description': 'str',
        'id': 'str',
        'module_json': 'str',
        'name': 'str',
        'en_name': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'update_time': 'str',
        'thumbnail': 'str',
        'module_type': 'str',
        'tag': 'str',
        'is_built_in': 'bool',
        'data_query': 'str',
        'boa_version': 'str',
        'version': 'str'
    }

    attribute_map = {
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'cloud_pack_version': 'cloud_pack_version',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'description': 'description',
        'en_description': 'en_description',
        'id': 'id',
        'module_json': 'module_json',
        'name': 'name',
        'en_name': 'en_name',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'update_time': 'update_time',
        'thumbnail': 'thumbnail',
        'module_type': 'module_type',
        'tag': 'tag',
        'is_built_in': 'is_built_in',
        'data_query': 'data_query',
        'boa_version': 'boa_version',
        'version': 'version'
    }

    def __init__(self, cloud_pack_id=None, cloud_pack_name=None, cloud_pack_version=None, create_time=None, creator_id=None, description=None, en_description=None, id=None, module_json=None, name=None, en_name=None, project_id=None, workspace_id=None, update_time=None, thumbnail=None, module_type=None, tag=None, is_built_in=None, data_query=None, boa_version=None, version=None):
        r"""ModuleDetailInfo

        The model defined in huaweicloud sdk

        :param cloud_pack_id: 订阅包id
        :type cloud_pack_id: str
        :param cloud_pack_name: 订阅包名称
        :type cloud_pack_name: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param description: 描述信息
        :type description: str
        :param en_description: 英文描述
        :type en_description: str
        :param id: 模块ID
        :type id: str
        :param module_json: 模块相关信息，当module为指标卡片时，items中的字段id也为指标id
        :type module_json: str
        :param name: 名称
        :type name: str
        :param en_name: 英文名称
        :type en_name: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param update_time: 更新时间
        :type update_time: str
        :param thumbnail: 模块缩略图
        :type thumbnail: str
        :param module_type: 模块类型,tab/section
        :type module_type: str
        :param tag: 模块标签
        :type tag: str
        :param is_built_in: 是否为系统模块
        :type is_built_in: bool
        :param data_query: 数据查询方式
        :type data_query: str
        :param boa_version: BOA底座版本
        :type boa_version: str
        :param version: 安全云脑版本
        :type version: str
        """
        
        

        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._cloud_pack_version = None
        self._create_time = None
        self._creator_id = None
        self._description = None
        self._en_description = None
        self._id = None
        self._module_json = None
        self._name = None
        self._en_name = None
        self._project_id = None
        self._workspace_id = None
        self._update_time = None
        self._thumbnail = None
        self._module_type = None
        self._tag = None
        self._is_built_in = None
        self._data_query = None
        self._boa_version = None
        self._version = None
        self.discriminator = None

        if cloud_pack_id is not None:
            self.cloud_pack_id = cloud_pack_id
        if cloud_pack_name is not None:
            self.cloud_pack_name = cloud_pack_name
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if description is not None:
            self.description = description
        if en_description is not None:
            self.en_description = en_description
        if id is not None:
            self.id = id
        if module_json is not None:
            self.module_json = module_json
        if name is not None:
            self.name = name
        if en_name is not None:
            self.en_name = en_name
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if update_time is not None:
            self.update_time = update_time
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if module_type is not None:
            self.module_type = module_type
        if tag is not None:
            self.tag = tag
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if data_query is not None:
            self.data_query = data_query
        if boa_version is not None:
            self.boa_version = boa_version
        if version is not None:
            self.version = version

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this ModuleDetailInfo.

        订阅包id

        :return: The cloud_pack_id of this ModuleDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this ModuleDetailInfo.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this ModuleDetailInfo.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this ModuleDetailInfo.

        订阅包名称

        :return: The cloud_pack_name of this ModuleDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this ModuleDetailInfo.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this ModuleDetailInfo.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this ModuleDetailInfo.

        订阅包版本

        :return: The cloud_pack_version of this ModuleDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this ModuleDetailInfo.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this ModuleDetailInfo.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def create_time(self):
        r"""Gets the create_time of this ModuleDetailInfo.

        创建时间

        :return: The create_time of this ModuleDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModuleDetailInfo.

        创建时间

        :param create_time: The create_time of this ModuleDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ModuleDetailInfo.

        创建者ID

        :return: The creator_id of this ModuleDetailInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ModuleDetailInfo.

        创建者ID

        :param creator_id: The creator_id of this ModuleDetailInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def description(self):
        r"""Gets the description of this ModuleDetailInfo.

        描述信息

        :return: The description of this ModuleDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModuleDetailInfo.

        描述信息

        :param description: The description of this ModuleDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def en_description(self):
        r"""Gets the en_description of this ModuleDetailInfo.

        英文描述

        :return: The en_description of this ModuleDetailInfo.
        :rtype: str
        """
        return self._en_description

    @en_description.setter
    def en_description(self, en_description):
        r"""Sets the en_description of this ModuleDetailInfo.

        英文描述

        :param en_description: The en_description of this ModuleDetailInfo.
        :type en_description: str
        """
        self._en_description = en_description

    @property
    def id(self):
        r"""Gets the id of this ModuleDetailInfo.

        模块ID

        :return: The id of this ModuleDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModuleDetailInfo.

        模块ID

        :param id: The id of this ModuleDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def module_json(self):
        r"""Gets the module_json of this ModuleDetailInfo.

        模块相关信息，当module为指标卡片时，items中的字段id也为指标id

        :return: The module_json of this ModuleDetailInfo.
        :rtype: str
        """
        return self._module_json

    @module_json.setter
    def module_json(self, module_json):
        r"""Sets the module_json of this ModuleDetailInfo.

        模块相关信息，当module为指标卡片时，items中的字段id也为指标id

        :param module_json: The module_json of this ModuleDetailInfo.
        :type module_json: str
        """
        self._module_json = module_json

    @property
    def name(self):
        r"""Gets the name of this ModuleDetailInfo.

        名称

        :return: The name of this ModuleDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModuleDetailInfo.

        名称

        :param name: The name of this ModuleDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def en_name(self):
        r"""Gets the en_name of this ModuleDetailInfo.

        英文名称

        :return: The en_name of this ModuleDetailInfo.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this ModuleDetailInfo.

        英文名称

        :param en_name: The en_name of this ModuleDetailInfo.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ModuleDetailInfo.

        租户ID

        :return: The project_id of this ModuleDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ModuleDetailInfo.

        租户ID

        :param project_id: The project_id of this ModuleDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ModuleDetailInfo.

        工作空间ID

        :return: The workspace_id of this ModuleDetailInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ModuleDetailInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this ModuleDetailInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ModuleDetailInfo.

        更新时间

        :return: The update_time of this ModuleDetailInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModuleDetailInfo.

        更新时间

        :param update_time: The update_time of this ModuleDetailInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this ModuleDetailInfo.

        模块缩略图

        :return: The thumbnail of this ModuleDetailInfo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this ModuleDetailInfo.

        模块缩略图

        :param thumbnail: The thumbnail of this ModuleDetailInfo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def module_type(self):
        r"""Gets the module_type of this ModuleDetailInfo.

        模块类型,tab/section

        :return: The module_type of this ModuleDetailInfo.
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this ModuleDetailInfo.

        模块类型,tab/section

        :param module_type: The module_type of this ModuleDetailInfo.
        :type module_type: str
        """
        self._module_type = module_type

    @property
    def tag(self):
        r"""Gets the tag of this ModuleDetailInfo.

        模块标签

        :return: The tag of this ModuleDetailInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ModuleDetailInfo.

        模块标签

        :param tag: The tag of this ModuleDetailInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this ModuleDetailInfo.

        是否为系统模块

        :return: The is_built_in of this ModuleDetailInfo.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this ModuleDetailInfo.

        是否为系统模块

        :param is_built_in: The is_built_in of this ModuleDetailInfo.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def data_query(self):
        r"""Gets the data_query of this ModuleDetailInfo.

        数据查询方式

        :return: The data_query of this ModuleDetailInfo.
        :rtype: str
        """
        return self._data_query

    @data_query.setter
    def data_query(self, data_query):
        r"""Sets the data_query of this ModuleDetailInfo.

        数据查询方式

        :param data_query: The data_query of this ModuleDetailInfo.
        :type data_query: str
        """
        self._data_query = data_query

    @property
    def boa_version(self):
        r"""Gets the boa_version of this ModuleDetailInfo.

        BOA底座版本

        :return: The boa_version of this ModuleDetailInfo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this ModuleDetailInfo.

        BOA底座版本

        :param boa_version: The boa_version of this ModuleDetailInfo.
        :type boa_version: str
        """
        self._boa_version = boa_version

    @property
    def version(self):
        r"""Gets the version of this ModuleDetailInfo.

        安全云脑版本

        :return: The version of this ModuleDetailInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ModuleDetailInfo.

        安全云脑版本

        :param version: The version of this ModuleDetailInfo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ModuleDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
