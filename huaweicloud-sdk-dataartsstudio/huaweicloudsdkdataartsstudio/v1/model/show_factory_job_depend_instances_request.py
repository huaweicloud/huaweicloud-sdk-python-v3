# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryJobDependInstancesRequest:

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
        'job_name': 'str',
        'relation': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'job_name': 'job_name',
        'relation': 'relation'
    }

    def __init__(self, workspace=None, x_project_id=None, job_name=None, relation=None):
        r"""ShowFactoryJobDependInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param job_name: 作业名称。指定要查询上下游依赖关系的目标作业名称。 作业名称在创建作业时由用户指定，可通过\&quot;查询作业列表\&quot;接口获取。
        :type job_name: str
        :param relation: 查询的依赖方向。用于指定查询作业的直接上游、直接下游或同时查询上下游关系。 取值范围： - parent：查询直接上游作业，即当前作业依赖的作业。 - child：查询直接下游作业，即依赖当前作业的作业。 - both：同时查询直接上游和直接下游作业。 默认取值：both
        :type relation: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._job_name = None
        self._relation = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.job_name = job_name
        if relation is not None:
            self.relation = relation

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowFactoryJobDependInstancesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowFactoryJobDependInstancesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowFactoryJobDependInstancesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowFactoryJobDependInstancesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ShowFactoryJobDependInstancesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ShowFactoryJobDependInstancesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ShowFactoryJobDependInstancesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ShowFactoryJobDependInstancesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowFactoryJobDependInstancesRequest.

        作业名称。指定要查询上下游依赖关系的目标作业名称。 作业名称在创建作业时由用户指定，可通过\"查询作业列表\"接口获取。

        :return: The job_name of this ShowFactoryJobDependInstancesRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowFactoryJobDependInstancesRequest.

        作业名称。指定要查询上下游依赖关系的目标作业名称。 作业名称在创建作业时由用户指定，可通过\"查询作业列表\"接口获取。

        :param job_name: The job_name of this ShowFactoryJobDependInstancesRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def relation(self):
        r"""Gets the relation of this ShowFactoryJobDependInstancesRequest.

        查询的依赖方向。用于指定查询作业的直接上游、直接下游或同时查询上下游关系。 取值范围： - parent：查询直接上游作业，即当前作业依赖的作业。 - child：查询直接下游作业，即依赖当前作业的作业。 - both：同时查询直接上游和直接下游作业。 默认取值：both

        :return: The relation of this ShowFactoryJobDependInstancesRequest.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this ShowFactoryJobDependInstancesRequest.

        查询的依赖方向。用于指定查询作业的直接上游、直接下游或同时查询上下游关系。 取值范围： - parent：查询直接上游作业，即当前作业依赖的作业。 - child：查询直接下游作业，即依赖当前作业的作业。 - both：同时查询直接上游和直接下游作业。 默认取值：both

        :param relation: The relation of this ShowFactoryJobDependInstancesRequest.
        :type relation: str
        """
        self._relation = relation

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
        if not isinstance(other, ShowFactoryJobDependInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
