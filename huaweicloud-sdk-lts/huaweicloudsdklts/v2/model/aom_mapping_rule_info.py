# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AomMappingRuleInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'deployments': 'list[str]',
        'namespace': 'str',
        'container_name': 'str',
        'files': 'list[AomMappingfilesInfo]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'deployments': 'deployments',
        'namespace': 'namespace',
        'container_name': 'container_name',
        'files': 'files'
    }

    def __init__(self, cluster_id=None, cluster_name=None, deployments=None, namespace=None, container_name=None, files=None):
        """AomMappingRuleInfo - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._deployments = None
        self._namespace = None
        self._container_name = None
        self._files = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.deployments = deployments
        self.namespace = namespace
        self.container_name = container_name
        self.files = files

    @property
    def cluster_id(self):
        """Gets the cluster_id of this AomMappingRuleInfo.

        集群id

        :return: The cluster_id of this AomMappingRuleInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this AomMappingRuleInfo.

        集群id

        :param cluster_id: The cluster_id of this AomMappingRuleInfo.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this AomMappingRuleInfo.

        集群名称

        :return: The cluster_name of this AomMappingRuleInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this AomMappingRuleInfo.

        集群名称

        :param cluster_name: The cluster_name of this AomMappingRuleInfo.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def deployments(self):
        """Gets the deployments of this AomMappingRuleInfo.

        工作负载

        :return: The deployments of this AomMappingRuleInfo.
        :rtype: list[str]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this AomMappingRuleInfo.

        工作负载

        :param deployments: The deployments of this AomMappingRuleInfo.
        :type: list[str]
        """
        self._deployments = deployments

    @property
    def namespace(self):
        """Gets the namespace of this AomMappingRuleInfo.

        命名空间

        :return: The namespace of this AomMappingRuleInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AomMappingRuleInfo.

        命名空间

        :param namespace: The namespace of this AomMappingRuleInfo.
        :type: str
        """
        self._namespace = namespace

    @property
    def container_name(self):
        """Gets the container_name of this AomMappingRuleInfo.

        容器名称

        :return: The container_name of this AomMappingRuleInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this AomMappingRuleInfo.

        容器名称

        :param container_name: The container_name of this AomMappingRuleInfo.
        :type: str
        """
        self._container_name = container_name

    @property
    def files(self):
        """Gets the files of this AomMappingRuleInfo.

        接入规则详情

        :return: The files of this AomMappingRuleInfo.
        :rtype: list[AomMappingfilesInfo]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this AomMappingRuleInfo.

        接入规则详情

        :param files: The files of this AomMappingRuleInfo.
        :type: list[AomMappingfilesInfo]
        """
        self._files = files

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
        if not isinstance(other, AomMappingRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
