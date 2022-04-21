# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cluster_uid': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'extend_param': 'dict(str, str)',
        'sub_jobs': 'list[Job]'
    }

    attribute_map = {
        'type': 'type',
        'cluster_uid': 'clusterUID',
        'resource_id': 'resourceID',
        'resource_name': 'resourceName',
        'extend_param': 'extendParam',
        'sub_jobs': 'subJobs'
    }

    def __init__(self, type=None, cluster_uid=None, resource_id=None, resource_name=None, extend_param=None, sub_jobs=None):
        """JobSpec

        The model defined in huaweicloud sdk

        :param type: 任务的类型，例：“CreateCluster”- 创建集群。
        :type type: str
        :param cluster_uid: 任务所在的集群的ID。
        :type cluster_uid: str
        :param resource_id: 任务操作的资源ID。
        :type resource_id: str
        :param resource_name: 任务操作的资源名称。
        :type resource_name: str
        :param extend_param: 扩展参数。
        :type extend_param: dict(str, str)
        :param sub_jobs: 子任务的列表。  - 包含了所有子任务的详细信息 - 在创建集群、节点等场景下，通常会由多个子任务共同组成创建任务，在子任务都完成后，任务才会完成 
        :type sub_jobs: list[:class:`huaweicloudsdkcce.v3.Job`]
        """
        
        

        self._type = None
        self._cluster_uid = None
        self._resource_id = None
        self._resource_name = None
        self._extend_param = None
        self._sub_jobs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if cluster_uid is not None:
            self.cluster_uid = cluster_uid
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if extend_param is not None:
            self.extend_param = extend_param
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def type(self):
        """Gets the type of this JobSpec.

        任务的类型，例：“CreateCluster”- 创建集群。

        :return: The type of this JobSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobSpec.

        任务的类型，例：“CreateCluster”- 创建集群。

        :param type: The type of this JobSpec.
        :type type: str
        """
        self._type = type

    @property
    def cluster_uid(self):
        """Gets the cluster_uid of this JobSpec.

        任务所在的集群的ID。

        :return: The cluster_uid of this JobSpec.
        :rtype: str
        """
        return self._cluster_uid

    @cluster_uid.setter
    def cluster_uid(self, cluster_uid):
        """Sets the cluster_uid of this JobSpec.

        任务所在的集群的ID。

        :param cluster_uid: The cluster_uid of this JobSpec.
        :type cluster_uid: str
        """
        self._cluster_uid = cluster_uid

    @property
    def resource_id(self):
        """Gets the resource_id of this JobSpec.

        任务操作的资源ID。

        :return: The resource_id of this JobSpec.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this JobSpec.

        任务操作的资源ID。

        :param resource_id: The resource_id of this JobSpec.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this JobSpec.

        任务操作的资源名称。

        :return: The resource_name of this JobSpec.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this JobSpec.

        任务操作的资源名称。

        :param resource_name: The resource_name of this JobSpec.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def extend_param(self):
        """Gets the extend_param of this JobSpec.

        扩展参数。

        :return: The extend_param of this JobSpec.
        :rtype: dict(str, str)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this JobSpec.

        扩展参数。

        :param extend_param: The extend_param of this JobSpec.
        :type extend_param: dict(str, str)
        """
        self._extend_param = extend_param

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this JobSpec.

        子任务的列表。  - 包含了所有子任务的详细信息 - 在创建集群、节点等场景下，通常会由多个子任务共同组成创建任务，在子任务都完成后，任务才会完成 

        :return: The sub_jobs of this JobSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Job`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this JobSpec.

        子任务的列表。  - 包含了所有子任务的详细信息 - 在创建集群、节点等场景下，通常会由多个子任务共同组成创建任务，在子任务都完成后，任务才会完成 

        :param sub_jobs: The sub_jobs of this JobSpec.
        :type sub_jobs: list[:class:`huaweicloudsdkcce.v3.Job`]
        """
        self._sub_jobs = sub_jobs

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
        if not isinstance(other, JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
