# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceArtifactVulnerabilitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'namespace_name': 'str',
        'repository_name': 'str',
        'reference': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'repository_name': 'repository_name',
        'reference': 'reference'
    }

    def __init__(self, instance_id=None, namespace_name=None, repository_name=None, reference=None):
        r"""ListInstanceArtifactVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param repository_name: 仓库名称
        :type repository_name: str
        :param reference: 制品摘要
        :type reference: str
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._repository_name = None
        self._reference = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repository_name = repository_name
        self.reference = reference

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceArtifactVulnerabilitiesRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceArtifactVulnerabilitiesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceArtifactVulnerabilitiesRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceArtifactVulnerabilitiesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ListInstanceArtifactVulnerabilitiesRequest.

        命名空间名称

        :return: The namespace_name of this ListInstanceArtifactVulnerabilitiesRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ListInstanceArtifactVulnerabilitiesRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this ListInstanceArtifactVulnerabilitiesRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ListInstanceArtifactVulnerabilitiesRequest.

        仓库名称

        :return: The repository_name of this ListInstanceArtifactVulnerabilitiesRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ListInstanceArtifactVulnerabilitiesRequest.

        仓库名称

        :param repository_name: The repository_name of this ListInstanceArtifactVulnerabilitiesRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def reference(self):
        r"""Gets the reference of this ListInstanceArtifactVulnerabilitiesRequest.

        制品摘要

        :return: The reference of this ListInstanceArtifactVulnerabilitiesRequest.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this ListInstanceArtifactVulnerabilitiesRequest.

        制品摘要

        :param reference: The reference of this ListInstanceArtifactVulnerabilitiesRequest.
        :type reference: str
        """
        self._reference = reference

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
        if not isinstance(other, ListInstanceArtifactVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
