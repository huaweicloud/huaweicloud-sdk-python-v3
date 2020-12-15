# coding: utf-8

import pprint
import re

import six





class CCEJobSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_uid': 'str',
        'extend_param': 'dict(str, str)',
        'resource_id': 'str',
        'resource_name': 'str',
        'sub_jobs': 'list[CCEJob]',
        'type': 'str'
    }

    attribute_map = {
        'cluster_uid': 'clusterUID',
        'extend_param': 'extendParam',
        'resource_id': 'resourceID',
        'resource_name': 'resourceName',
        'sub_jobs': 'subJobs',
        'type': 'type'
    }

    def __init__(self, cluster_uid=None, extend_param=None, resource_id=None, resource_name=None, sub_jobs=None, type=None):
        """CCEJobSpec - a model defined in huaweicloud sdk"""
        
        

        self._cluster_uid = None
        self._extend_param = None
        self._resource_id = None
        self._resource_name = None
        self._sub_jobs = None
        self._type = None
        self.discriminator = None

        if cluster_uid is not None:
            self.cluster_uid = cluster_uid
        if extend_param is not None:
            self.extend_param = extend_param
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs
        if type is not None:
            self.type = type

    @property
    def cluster_uid(self):
        """Gets the cluster_uid of this CCEJobSpec.

        作业所在的集群的ID。

        :return: The cluster_uid of this CCEJobSpec.
        :rtype: str
        """
        return self._cluster_uid

    @cluster_uid.setter
    def cluster_uid(self, cluster_uid):
        """Sets the cluster_uid of this CCEJobSpec.

        作业所在的集群的ID。

        :param cluster_uid: The cluster_uid of this CCEJobSpec.
        :type: str
        """
        self._cluster_uid = cluster_uid

    @property
    def extend_param(self):
        """Gets the extend_param of this CCEJobSpec.

        扩展参数。

        :return: The extend_param of this CCEJobSpec.
        :rtype: dict(str, str)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CCEJobSpec.

        扩展参数。

        :param extend_param: The extend_param of this CCEJobSpec.
        :type: dict(str, str)
        """
        self._extend_param = extend_param

    @property
    def resource_id(self):
        """Gets the resource_id of this CCEJobSpec.

        作业操作的资源ID。

        :return: The resource_id of this CCEJobSpec.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CCEJobSpec.

        作业操作的资源ID。

        :param resource_id: The resource_id of this CCEJobSpec.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this CCEJobSpec.

        作业操作的资源名称。

        :return: The resource_name of this CCEJobSpec.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this CCEJobSpec.

        作业操作的资源名称。

        :param resource_name: The resource_name of this CCEJobSpec.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this CCEJobSpec.

        子作业的列表。  - 包含了所有子作业的详细信息 - 在创建集群、节点等场景下，通常会由多个子作业共同组成创建作业，在子作业都完成后，作业才会完成 

        :return: The sub_jobs of this CCEJobSpec.
        :rtype: list[CCEJob]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this CCEJobSpec.

        子作业的列表。  - 包含了所有子作业的详细信息 - 在创建集群、节点等场景下，通常会由多个子作业共同组成创建作业，在子作业都完成后，作业才会完成 

        :param sub_jobs: The sub_jobs of this CCEJobSpec.
        :type: list[CCEJob]
        """
        self._sub_jobs = sub_jobs

    @property
    def type(self):
        """Gets the type of this CCEJobSpec.

        作业的类型，例：“CreateCluster”- 创建集群。

        :return: The type of this CCEJobSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CCEJobSpec.

        作业的类型，例：“CreateCluster”- 创建集群。

        :param type: The type of this CCEJobSpec.
        :type: str
        """
        self._type = type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CCEJobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
