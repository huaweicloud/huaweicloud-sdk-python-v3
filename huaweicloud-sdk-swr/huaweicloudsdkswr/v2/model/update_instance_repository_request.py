# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRepositoryRequest:

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
        'body': 'UpdateRepoConfigRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'repository_name': 'repository_name',
        'body': 'body'
    }

    def __init__(self, instance_id=None, namespace_name=None, repository_name=None, body=None):
        r"""UpdateInstanceRepositoryRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param repository_name: 制品仓库名称
        :type repository_name: str
        :param body: Body of the UpdateInstanceRepositoryRequest
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRepoConfigRequestBody`
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._repository_name = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repository_name = repository_name
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateInstanceRepositoryRequest.

        企业仓库实例ID

        :return: The instance_id of this UpdateInstanceRepositoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateInstanceRepositoryRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this UpdateInstanceRepositoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this UpdateInstanceRepositoryRequest.

        命名空间名称

        :return: The namespace_name of this UpdateInstanceRepositoryRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this UpdateInstanceRepositoryRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this UpdateInstanceRepositoryRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def repository_name(self):
        r"""Gets the repository_name of this UpdateInstanceRepositoryRequest.

        制品仓库名称

        :return: The repository_name of this UpdateInstanceRepositoryRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this UpdateInstanceRepositoryRequest.

        制品仓库名称

        :param repository_name: The repository_name of this UpdateInstanceRepositoryRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def body(self):
        r"""Gets the body of this UpdateInstanceRepositoryRequest.

        :return: The body of this UpdateInstanceRepositoryRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateInstanceRepositoryRequest.

        :param body: The body of this UpdateInstanceRepositoryRequest.
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRepoConfigRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateInstanceRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
