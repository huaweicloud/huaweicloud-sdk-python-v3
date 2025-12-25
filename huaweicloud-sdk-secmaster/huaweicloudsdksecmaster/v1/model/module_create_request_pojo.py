# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModuleCreateRequestPojo:

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
        'project_id': 'str',
        'workspace_id': 'str',
        'module_json': 'str',
        'module_type': 'str',
        'metric_ids': 'str',
        'thumbnail': 'str',
        'data_query': 'str',
        'boa_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'module_json': 'module_json',
        'module_type': 'module_type',
        'metric_ids': 'metric_ids',
        'thumbnail': 'thumbnail',
        'data_query': 'data_query',
        'boa_version': 'boa_version'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, workspace_id=None, module_json=None, module_type=None, metric_ids=None, thumbnail=None, data_query=None, boa_version=None):
        r"""ModuleCreateRequestPojo

        The model defined in huaweicloud sdk

        :param id: 模块ID
        :type id: str
        :param name: 名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param module_json: 模块相关信息
        :type module_json: str
        :param module_type: 模块类型,tab/section
        :type module_type: str
        :param metric_ids: section类模块关联的指标id
        :type metric_ids: str
        :param thumbnail: 模块缩略图
        :type thumbnail: str
        :param data_query: 数据查询方式
        :type data_query: str
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._workspace_id = None
        self._module_json = None
        self._module_type = None
        self._metric_ids = None
        self._thumbnail = None
        self._data_query = None
        self._boa_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if module_json is not None:
            self.module_json = module_json
        if module_type is not None:
            self.module_type = module_type
        if metric_ids is not None:
            self.metric_ids = metric_ids
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if data_query is not None:
            self.data_query = data_query
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def id(self):
        r"""Gets the id of this ModuleCreateRequestPojo.

        模块ID

        :return: The id of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModuleCreateRequestPojo.

        模块ID

        :param id: The id of this ModuleCreateRequestPojo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModuleCreateRequestPojo.

        名称

        :return: The name of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModuleCreateRequestPojo.

        名称

        :param name: The name of this ModuleCreateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModuleCreateRequestPojo.

        描述信息

        :return: The description of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModuleCreateRequestPojo.

        描述信息

        :param description: The description of this ModuleCreateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this ModuleCreateRequestPojo.

        租户ID

        :return: The project_id of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ModuleCreateRequestPojo.

        租户ID

        :param project_id: The project_id of this ModuleCreateRequestPojo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ModuleCreateRequestPojo.

        工作空间ID

        :return: The workspace_id of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ModuleCreateRequestPojo.

        工作空间ID

        :param workspace_id: The workspace_id of this ModuleCreateRequestPojo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def module_json(self):
        r"""Gets the module_json of this ModuleCreateRequestPojo.

        模块相关信息

        :return: The module_json of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._module_json

    @module_json.setter
    def module_json(self, module_json):
        r"""Sets the module_json of this ModuleCreateRequestPojo.

        模块相关信息

        :param module_json: The module_json of this ModuleCreateRequestPojo.
        :type module_json: str
        """
        self._module_json = module_json

    @property
    def module_type(self):
        r"""Gets the module_type of this ModuleCreateRequestPojo.

        模块类型,tab/section

        :return: The module_type of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this ModuleCreateRequestPojo.

        模块类型,tab/section

        :param module_type: The module_type of this ModuleCreateRequestPojo.
        :type module_type: str
        """
        self._module_type = module_type

    @property
    def metric_ids(self):
        r"""Gets the metric_ids of this ModuleCreateRequestPojo.

        section类模块关联的指标id

        :return: The metric_ids of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._metric_ids

    @metric_ids.setter
    def metric_ids(self, metric_ids):
        r"""Sets the metric_ids of this ModuleCreateRequestPojo.

        section类模块关联的指标id

        :param metric_ids: The metric_ids of this ModuleCreateRequestPojo.
        :type metric_ids: str
        """
        self._metric_ids = metric_ids

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this ModuleCreateRequestPojo.

        模块缩略图

        :return: The thumbnail of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this ModuleCreateRequestPojo.

        模块缩略图

        :param thumbnail: The thumbnail of this ModuleCreateRequestPojo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def data_query(self):
        r"""Gets the data_query of this ModuleCreateRequestPojo.

        数据查询方式

        :return: The data_query of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._data_query

    @data_query.setter
    def data_query(self, data_query):
        r"""Sets the data_query of this ModuleCreateRequestPojo.

        数据查询方式

        :param data_query: The data_query of this ModuleCreateRequestPojo.
        :type data_query: str
        """
        self._data_query = data_query

    @property
    def boa_version(self):
        r"""Gets the boa_version of this ModuleCreateRequestPojo.

        BOA底座版本

        :return: The boa_version of this ModuleCreateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this ModuleCreateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this ModuleCreateRequestPojo.
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
        if not isinstance(other, ModuleCreateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
