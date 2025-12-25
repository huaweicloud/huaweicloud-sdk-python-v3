# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeMappingDetail:

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
        'project_id': 'str',
        'workspace_id': 'str',
        'dataclass_id': 'str',
        'dataclass_name': 'str',
        'mapper_type_id': 'str',
        'dpe_info': 'DpeInfo',
        'create_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'update_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'mapper_field_list': 'list[DpeMappingFieldDetail]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_id': 'dataclass_id',
        'dataclass_name': 'dataclass_name',
        'mapper_type_id': 'mapper_type_id',
        'dpe_info': 'dpe_info',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'mapper_field_list': 'mapper_field_list'
    }

    def __init__(self, id=None, name=None, project_id=None, workspace_id=None, dataclass_id=None, dataclass_name=None, mapper_type_id=None, dpe_info=None, create_time=None, creator_id=None, creator_name=None, update_time=None, modifier_id=None, modifier_name=None, mapper_field_list=None):
        r"""DpeMappingDetail

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param name: 名称
        :type name: str
        :param project_id: 映射id
        :type project_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param dataclass_id: 映射id
        :type dataclass_id: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param mapper_type_id: 映射id
        :type mapper_type_id: str
        :param dpe_info: 
        :type dpe_info: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者id
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param update_time: 更新时间
        :type update_time: str
        :param modifier_id: 修改者id
        :type modifier_id: str
        :param modifier_name: 修改者名称
        :type modifier_name: str
        :param mapper_field_list: 映射集合
        :type mapper_field_list: list[:class:`huaweicloudsdksecmaster.v1.DpeMappingFieldDetail`]
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._workspace_id = None
        self._dataclass_id = None
        self._dataclass_name = None
        self._mapper_type_id = None
        self._dpe_info = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._update_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._mapper_field_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if mapper_type_id is not None:
            self.mapper_type_id = mapper_type_id
        if dpe_info is not None:
            self.dpe_info = dpe_info
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if mapper_field_list is not None:
            self.mapper_field_list = mapper_field_list

    @property
    def id(self):
        r"""Gets the id of this DpeMappingDetail.

        映射id

        :return: The id of this DpeMappingDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DpeMappingDetail.

        映射id

        :param id: The id of this DpeMappingDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DpeMappingDetail.

        名称

        :return: The name of this DpeMappingDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DpeMappingDetail.

        名称

        :param name: The name of this DpeMappingDetail.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this DpeMappingDetail.

        映射id

        :return: The project_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DpeMappingDetail.

        映射id

        :param project_id: The project_id of this DpeMappingDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DpeMappingDetail.

        映射id

        :return: The workspace_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DpeMappingDetail.

        映射id

        :param workspace_id: The workspace_id of this DpeMappingDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this DpeMappingDetail.

        映射id

        :return: The dataclass_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this DpeMappingDetail.

        映射id

        :param dataclass_id: The dataclass_id of this DpeMappingDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this DpeMappingDetail.

        数据类名称

        :return: The dataclass_name of this DpeMappingDetail.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this DpeMappingDetail.

        数据类名称

        :param dataclass_name: The dataclass_name of this DpeMappingDetail.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def mapper_type_id(self):
        r"""Gets the mapper_type_id of this DpeMappingDetail.

        映射id

        :return: The mapper_type_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._mapper_type_id

    @mapper_type_id.setter
    def mapper_type_id(self, mapper_type_id):
        r"""Sets the mapper_type_id of this DpeMappingDetail.

        映射id

        :param mapper_type_id: The mapper_type_id of this DpeMappingDetail.
        :type mapper_type_id: str
        """
        self._mapper_type_id = mapper_type_id

    @property
    def dpe_info(self):
        r"""Gets the dpe_info of this DpeMappingDetail.

        :return: The dpe_info of this DpeMappingDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        """
        return self._dpe_info

    @dpe_info.setter
    def dpe_info(self, dpe_info):
        r"""Sets the dpe_info of this DpeMappingDetail.

        :param dpe_info: The dpe_info of this DpeMappingDetail.
        :type dpe_info: :class:`huaweicloudsdksecmaster.v1.DpeInfo`
        """
        self._dpe_info = dpe_info

    @property
    def create_time(self):
        r"""Gets the create_time of this DpeMappingDetail.

        创建时间

        :return: The create_time of this DpeMappingDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DpeMappingDetail.

        创建时间

        :param create_time: The create_time of this DpeMappingDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this DpeMappingDetail.

        创建者id

        :return: The creator_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this DpeMappingDetail.

        创建者id

        :param creator_id: The creator_id of this DpeMappingDetail.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this DpeMappingDetail.

        创建者名称

        :return: The creator_name of this DpeMappingDetail.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this DpeMappingDetail.

        创建者名称

        :param creator_name: The creator_name of this DpeMappingDetail.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this DpeMappingDetail.

        更新时间

        :return: The update_time of this DpeMappingDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DpeMappingDetail.

        更新时间

        :param update_time: The update_time of this DpeMappingDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this DpeMappingDetail.

        修改者id

        :return: The modifier_id of this DpeMappingDetail.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this DpeMappingDetail.

        修改者id

        :param modifier_id: The modifier_id of this DpeMappingDetail.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this DpeMappingDetail.

        修改者名称

        :return: The modifier_name of this DpeMappingDetail.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this DpeMappingDetail.

        修改者名称

        :param modifier_name: The modifier_name of this DpeMappingDetail.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def mapper_field_list(self):
        r"""Gets the mapper_field_list of this DpeMappingDetail.

        映射集合

        :return: The mapper_field_list of this DpeMappingDetail.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DpeMappingFieldDetail`]
        """
        return self._mapper_field_list

    @mapper_field_list.setter
    def mapper_field_list(self, mapper_field_list):
        r"""Sets the mapper_field_list of this DpeMappingDetail.

        映射集合

        :param mapper_field_list: The mapper_field_list of this DpeMappingDetail.
        :type mapper_field_list: list[:class:`huaweicloudsdksecmaster.v1.DpeMappingFieldDetail`]
        """
        self._mapper_field_list = mapper_field_list

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
        if not isinstance(other, DpeMappingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
