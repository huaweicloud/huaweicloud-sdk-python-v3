# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryDependInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'instance_id': 'int',
        'relation': 'str',
        'depth': 'int',
        'latest': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'instance_id': 'instance_id',
        'relation': 'relation',
        'depth': 'depth',
        'latest': 'latest'
    }

    def __init__(self, workspace=None, x_project_id=None, instance_id=None, relation=None, depth=None, latest=None):
        r"""ShowFactoryDependInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param instance_id: 作业实例id，可通过作业实例列表接口获取。
        :type instance_id: int
        :param relation: 支持选择查询实例的直接上游、直接下游或者是直接上下游，取值为 parent、child、both，默认为both。 - parent：直接上游实例 - child：直接下游实例 - both：直接上下游实例
        :type relation: str
        :param depth: 默认值为1, depth是上下游依赖查询的层级深度，例如 depth&#x3D;1 只查直接依赖，depth&#x3D;2 查到依赖的依赖。单次查询可返回的最大深度为50层。
        :type depth: int
        :param latest: 默认值为true, 当latest&#x3D;true的时候，控制是否只返回每个依赖任务的最新实例，true 时只返回endTime 最晚的执行记录，false 时返回所有历史实例。
        :type latest: bool
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._instance_id = None
        self._relation = None
        self._depth = None
        self._latest = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.instance_id = instance_id
        if relation is not None:
            self.relation = relation
        if depth is not None:
            self.depth = depth
        if latest is not None:
            self.latest = latest

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowFactoryDependInstancesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowFactoryDependInstancesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowFactoryDependInstancesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowFactoryDependInstancesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ShowFactoryDependInstancesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ShowFactoryDependInstancesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ShowFactoryDependInstancesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ShowFactoryDependInstancesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowFactoryDependInstancesRequest.

        作业实例id，可通过作业实例列表接口获取。

        :return: The instance_id of this ShowFactoryDependInstancesRequest.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowFactoryDependInstancesRequest.

        作业实例id，可通过作业实例列表接口获取。

        :param instance_id: The instance_id of this ShowFactoryDependInstancesRequest.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def relation(self):
        r"""Gets the relation of this ShowFactoryDependInstancesRequest.

        支持选择查询实例的直接上游、直接下游或者是直接上下游，取值为 parent、child、both，默认为both。 - parent：直接上游实例 - child：直接下游实例 - both：直接上下游实例

        :return: The relation of this ShowFactoryDependInstancesRequest.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this ShowFactoryDependInstancesRequest.

        支持选择查询实例的直接上游、直接下游或者是直接上下游，取值为 parent、child、both，默认为both。 - parent：直接上游实例 - child：直接下游实例 - both：直接上下游实例

        :param relation: The relation of this ShowFactoryDependInstancesRequest.
        :type relation: str
        """
        self._relation = relation

    @property
    def depth(self):
        r"""Gets the depth of this ShowFactoryDependInstancesRequest.

        默认值为1, depth是上下游依赖查询的层级深度，例如 depth=1 只查直接依赖，depth=2 查到依赖的依赖。单次查询可返回的最大深度为50层。

        :return: The depth of this ShowFactoryDependInstancesRequest.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this ShowFactoryDependInstancesRequest.

        默认值为1, depth是上下游依赖查询的层级深度，例如 depth=1 只查直接依赖，depth=2 查到依赖的依赖。单次查询可返回的最大深度为50层。

        :param depth: The depth of this ShowFactoryDependInstancesRequest.
        :type depth: int
        """
        self._depth = depth

    @property
    def latest(self):
        r"""Gets the latest of this ShowFactoryDependInstancesRequest.

        默认值为true, 当latest=true的时候，控制是否只返回每个依赖任务的最新实例，true 时只返回endTime 最晚的执行记录，false 时返回所有历史实例。

        :return: The latest of this ShowFactoryDependInstancesRequest.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        r"""Sets the latest of this ShowFactoryDependInstancesRequest.

        默认值为true, 当latest=true的时候，控制是否只返回每个依赖任务的最新实例，true 时只返回endTime 最晚的执行记录，false 时返回所有历史实例。

        :param latest: The latest of this ShowFactoryDependInstancesRequest.
        :type latest: bool
        """
        self._latest = latest

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
        if not isinstance(other, ShowFactoryDependInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
