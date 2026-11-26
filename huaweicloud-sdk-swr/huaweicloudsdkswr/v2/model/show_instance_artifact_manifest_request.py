# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceArtifactManifestRequest:

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
        r"""ShowInstanceArtifactManifestRequest

        The model defined in huaweicloud sdk

        :param instance_id: 注册表实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param repository_name: 制品仓库名称, 如果您的镜像名称repository_name参数中有/，请先把 / 替换成 %2F 再进行请求。注意：使用curl命令请求，需要把 / 替换成 %252F(即 %2F 的 % 被编码为 %25)再次请求。
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
        r"""Gets the instance_id of this ShowInstanceArtifactManifestRequest.

        注册表实例ID

        :return: The instance_id of this ShowInstanceArtifactManifestRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceArtifactManifestRequest.

        注册表实例ID

        :param instance_id: The instance_id of this ShowInstanceArtifactManifestRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ShowInstanceArtifactManifestRequest.

        命名空间名称

        :return: The namespace_name of this ShowInstanceArtifactManifestRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ShowInstanceArtifactManifestRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this ShowInstanceArtifactManifestRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ShowInstanceArtifactManifestRequest.

        制品仓库名称, 如果您的镜像名称repository_name参数中有/，请先把 / 替换成 %2F 再进行请求。注意：使用curl命令请求，需要把 / 替换成 %252F(即 %2F 的 % 被编码为 %25)再次请求。

        :return: The repository_name of this ShowInstanceArtifactManifestRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ShowInstanceArtifactManifestRequest.

        制品仓库名称, 如果您的镜像名称repository_name参数中有/，请先把 / 替换成 %2F 再进行请求。注意：使用curl命令请求，需要把 / 替换成 %252F(即 %2F 的 % 被编码为 %25)再次请求。

        :param repository_name: The repository_name of this ShowInstanceArtifactManifestRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def reference(self):
        r"""Gets the reference of this ShowInstanceArtifactManifestRequest.

        制品摘要

        :return: The reference of this ShowInstanceArtifactManifestRequest.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this ShowInstanceArtifactManifestRequest.

        制品摘要

        :param reference: The reference of this ShowInstanceArtifactManifestRequest.
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
        if not isinstance(other, ShowInstanceArtifactManifestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
