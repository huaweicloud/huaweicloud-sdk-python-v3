# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAutopilotReleaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chart_name': 'str',
        'chart_public': 'bool',
        'chart_version': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'create_at': 'str',
        'description': 'str',
        'name': 'str',
        'namespace': 'str',
        'parameters': 'str',
        'resources': 'str',
        'status': 'str',
        'status_description': 'str',
        'update_at': 'str',
        'values': 'str',
        'version': 'int'
    }

    attribute_map = {
        'chart_name': 'chart_name',
        'chart_public': 'chart_public',
        'chart_version': 'chart_version',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'create_at': 'create_at',
        'description': 'description',
        'name': 'name',
        'namespace': 'namespace',
        'parameters': 'parameters',
        'resources': 'resources',
        'status': 'status',
        'status_description': 'status_description',
        'update_at': 'update_at',
        'values': 'values',
        'version': 'version'
    }

    def __init__(self, chart_name=None, chart_public=None, chart_version=None, cluster_id=None, cluster_name=None, create_at=None, description=None, name=None, namespace=None, parameters=None, resources=None, status=None, status_description=None, update_at=None, values=None, version=None):
        r"""UpdateAutopilotReleaseResponse

        The model defined in huaweicloud sdk

        :param chart_name: 模板名称
        :type chart_name: str
        :param chart_public: 是否公开模板
        :type chart_public: bool
        :param chart_version: 模板版本
        :type chart_version: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param create_at: 创建时间
        :type create_at: str
        :param description: 模板实例描述
        :type description: str
        :param name: 模板实例名称
        :type name: str
        :param namespace: 模板实例所在的命名空间
        :type namespace: str
        :param parameters: 模板实例参数
        :type parameters: str
        :param resources: 模板实例需要的资源
        :type resources: str
        :param status: 模板实例状态
        :type status: str
        :param status_description: 模板实例状态描述
        :type status_description: str
        :param update_at: 更新时间
        :type update_at: str
        :param values: 模板实例的值
        :type values: str
        :param version: 模板实例版本
        :type version: int
        """
        
        super(UpdateAutopilotReleaseResponse, self).__init__()

        self._chart_name = None
        self._chart_public = None
        self._chart_version = None
        self._cluster_id = None
        self._cluster_name = None
        self._create_at = None
        self._description = None
        self._name = None
        self._namespace = None
        self._parameters = None
        self._resources = None
        self._status = None
        self._status_description = None
        self._update_at = None
        self._values = None
        self._version = None
        self.discriminator = None

        if chart_name is not None:
            self.chart_name = chart_name
        if chart_public is not None:
            self.chart_public = chart_public
        if chart_version is not None:
            self.chart_version = chart_version
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if create_at is not None:
            self.create_at = create_at
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if parameters is not None:
            self.parameters = parameters
        if resources is not None:
            self.resources = resources
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description
        if update_at is not None:
            self.update_at = update_at
        if values is not None:
            self.values = values
        if version is not None:
            self.version = version

    @property
    def chart_name(self):
        r"""Gets the chart_name of this UpdateAutopilotReleaseResponse.

        模板名称

        :return: The chart_name of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._chart_name

    @chart_name.setter
    def chart_name(self, chart_name):
        r"""Sets the chart_name of this UpdateAutopilotReleaseResponse.

        模板名称

        :param chart_name: The chart_name of this UpdateAutopilotReleaseResponse.
        :type chart_name: str
        """
        self._chart_name = chart_name

    @property
    def chart_public(self):
        r"""Gets the chart_public of this UpdateAutopilotReleaseResponse.

        是否公开模板

        :return: The chart_public of this UpdateAutopilotReleaseResponse.
        :rtype: bool
        """
        return self._chart_public

    @chart_public.setter
    def chart_public(self, chart_public):
        r"""Sets the chart_public of this UpdateAutopilotReleaseResponse.

        是否公开模板

        :param chart_public: The chart_public of this UpdateAutopilotReleaseResponse.
        :type chart_public: bool
        """
        self._chart_public = chart_public

    @property
    def chart_version(self):
        r"""Gets the chart_version of this UpdateAutopilotReleaseResponse.

        模板版本

        :return: The chart_version of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._chart_version

    @chart_version.setter
    def chart_version(self, chart_version):
        r"""Sets the chart_version of this UpdateAutopilotReleaseResponse.

        模板版本

        :param chart_version: The chart_version of this UpdateAutopilotReleaseResponse.
        :type chart_version: str
        """
        self._chart_version = chart_version

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateAutopilotReleaseResponse.

        集群ID

        :return: The cluster_id of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateAutopilotReleaseResponse.

        集群ID

        :param cluster_id: The cluster_id of this UpdateAutopilotReleaseResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this UpdateAutopilotReleaseResponse.

        集群名称

        :return: The cluster_name of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this UpdateAutopilotReleaseResponse.

        集群名称

        :param cluster_name: The cluster_name of this UpdateAutopilotReleaseResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_at(self):
        r"""Gets the create_at of this UpdateAutopilotReleaseResponse.

        创建时间

        :return: The create_at of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this UpdateAutopilotReleaseResponse.

        创建时间

        :param create_at: The create_at of this UpdateAutopilotReleaseResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def description(self):
        r"""Gets the description of this UpdateAutopilotReleaseResponse.

        模板实例描述

        :return: The description of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAutopilotReleaseResponse.

        模板实例描述

        :param description: The description of this UpdateAutopilotReleaseResponse.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateAutopilotReleaseResponse.

        模板实例名称

        :return: The name of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAutopilotReleaseResponse.

        模板实例名称

        :param name: The name of this UpdateAutopilotReleaseResponse.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateAutopilotReleaseResponse.

        模板实例所在的命名空间

        :return: The namespace of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateAutopilotReleaseResponse.

        模板实例所在的命名空间

        :param namespace: The namespace of this UpdateAutopilotReleaseResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def parameters(self):
        r"""Gets the parameters of this UpdateAutopilotReleaseResponse.

        模板实例参数

        :return: The parameters of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this UpdateAutopilotReleaseResponse.

        模板实例参数

        :param parameters: The parameters of this UpdateAutopilotReleaseResponse.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def resources(self):
        r"""Gets the resources of this UpdateAutopilotReleaseResponse.

        模板实例需要的资源

        :return: The resources of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this UpdateAutopilotReleaseResponse.

        模板实例需要的资源

        :param resources: The resources of this UpdateAutopilotReleaseResponse.
        :type resources: str
        """
        self._resources = resources

    @property
    def status(self):
        r"""Gets the status of this UpdateAutopilotReleaseResponse.

        模板实例状态

        :return: The status of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAutopilotReleaseResponse.

        模板实例状态

        :param status: The status of this UpdateAutopilotReleaseResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_description(self):
        r"""Gets the status_description of this UpdateAutopilotReleaseResponse.

        模板实例状态描述

        :return: The status_description of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        r"""Sets the status_description of this UpdateAutopilotReleaseResponse.

        模板实例状态描述

        :param status_description: The status_description of this UpdateAutopilotReleaseResponse.
        :type status_description: str
        """
        self._status_description = status_description

    @property
    def update_at(self):
        r"""Gets the update_at of this UpdateAutopilotReleaseResponse.

        更新时间

        :return: The update_at of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this UpdateAutopilotReleaseResponse.

        更新时间

        :param update_at: The update_at of this UpdateAutopilotReleaseResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def values(self):
        r"""Gets the values of this UpdateAutopilotReleaseResponse.

        模板实例的值

        :return: The values of this UpdateAutopilotReleaseResponse.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpdateAutopilotReleaseResponse.

        模板实例的值

        :param values: The values of this UpdateAutopilotReleaseResponse.
        :type values: str
        """
        self._values = values

    @property
    def version(self):
        r"""Gets the version of this UpdateAutopilotReleaseResponse.

        模板实例版本

        :return: The version of this UpdateAutopilotReleaseResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateAutopilotReleaseResponse.

        模板实例版本

        :param version: The version of this UpdateAutopilotReleaseResponse.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, UpdateAutopilotReleaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
