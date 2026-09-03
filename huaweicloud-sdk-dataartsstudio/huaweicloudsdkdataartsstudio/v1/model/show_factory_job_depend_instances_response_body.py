# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryJobDependInstancesResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'job_path': 'str',
        'depend_layer': 'str',
        'workspace_name': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'job_path': 'job_path',
        'depend_layer': 'depend_layer',
        'workspace_name': 'workspace_name',
        'owner': 'owner'
    }

    def __init__(self, job_name=None, job_path=None, depend_layer=None, workspace_name=None, owner=None):
        r"""ShowFactoryJobDependInstancesResponseBody

        The model defined in huaweicloud sdk

        :param job_name: 依赖的作业名称。
        :type job_name: str
        :param job_path: 依赖的作业所在目录路径。作业在根目录下返回\&quot;/\&quot;。
        :type job_path: str
        :param depend_layer: 当前作业与查询目标作业的依赖关系方向。 取值范围： - parent：当前作业是查询目标作业的上游作业。 - child：当前作业是查询目标作业的下游作业。
        :type depend_layer: str
        :param workspace_name: 依赖的作业所在的工作空间名称。
        :type workspace_name: str
        :param owner: 作业责任人。创建作业时指定的作业负责人。
        :type owner: str
        """
        
        

        self._job_name = None
        self._job_path = None
        self._depend_layer = None
        self._workspace_name = None
        self._owner = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if job_path is not None:
            self.job_path = job_path
        if depend_layer is not None:
            self.depend_layer = depend_layer
        if workspace_name is not None:
            self.workspace_name = workspace_name
        if owner is not None:
            self.owner = owner

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业名称。

        :return: The job_name of this ShowFactoryJobDependInstancesResponseBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业名称。

        :param job_name: The job_name of this ShowFactoryJobDependInstancesResponseBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_path(self):
        r"""Gets the job_path of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业所在目录路径。作业在根目录下返回\"/\"。

        :return: The job_path of this ShowFactoryJobDependInstancesResponseBody.
        :rtype: str
        """
        return self._job_path

    @job_path.setter
    def job_path(self, job_path):
        r"""Sets the job_path of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业所在目录路径。作业在根目录下返回\"/\"。

        :param job_path: The job_path of this ShowFactoryJobDependInstancesResponseBody.
        :type job_path: str
        """
        self._job_path = job_path

    @property
    def depend_layer(self):
        r"""Gets the depend_layer of this ShowFactoryJobDependInstancesResponseBody.

        当前作业与查询目标作业的依赖关系方向。 取值范围： - parent：当前作业是查询目标作业的上游作业。 - child：当前作业是查询目标作业的下游作业。

        :return: The depend_layer of this ShowFactoryJobDependInstancesResponseBody.
        :rtype: str
        """
        return self._depend_layer

    @depend_layer.setter
    def depend_layer(self, depend_layer):
        r"""Sets the depend_layer of this ShowFactoryJobDependInstancesResponseBody.

        当前作业与查询目标作业的依赖关系方向。 取值范围： - parent：当前作业是查询目标作业的上游作业。 - child：当前作业是查询目标作业的下游作业。

        :param depend_layer: The depend_layer of this ShowFactoryJobDependInstancesResponseBody.
        :type depend_layer: str
        """
        self._depend_layer = depend_layer

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业所在的工作空间名称。

        :return: The workspace_name of this ShowFactoryJobDependInstancesResponseBody.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this ShowFactoryJobDependInstancesResponseBody.

        依赖的作业所在的工作空间名称。

        :param workspace_name: The workspace_name of this ShowFactoryJobDependInstancesResponseBody.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def owner(self):
        r"""Gets the owner of this ShowFactoryJobDependInstancesResponseBody.

        作业责任人。创建作业时指定的作业负责人。

        :return: The owner of this ShowFactoryJobDependInstancesResponseBody.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowFactoryJobDependInstancesResponseBody.

        作业责任人。创建作业时指定的作业负责人。

        :param owner: The owner of this ShowFactoryJobDependInstancesResponseBody.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, ShowFactoryJobDependInstancesResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
