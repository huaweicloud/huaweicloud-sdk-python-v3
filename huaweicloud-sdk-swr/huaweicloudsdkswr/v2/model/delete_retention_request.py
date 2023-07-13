# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRetentionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'retention_id': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'retention_id': 'retention_id'
    }

    def __init__(self, namespace=None, repository=None, retention_id=None):
        """DeleteRetentionRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param retention_id: 镜像老化规则id
        :type retention_id: int
        """
        
        

        self._namespace = None
        self._repository = None
        self._retention_id = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.retention_id = retention_id

    @property
    def namespace(self):
        """Gets the namespace of this DeleteRetentionRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this DeleteRetentionRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeleteRetentionRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this DeleteRetentionRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this DeleteRetentionRequest.

        镜像仓库名称

        :return: The repository of this DeleteRetentionRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this DeleteRetentionRequest.

        镜像仓库名称

        :param repository: The repository of this DeleteRetentionRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def retention_id(self):
        """Gets the retention_id of this DeleteRetentionRequest.

        镜像老化规则id

        :return: The retention_id of this DeleteRetentionRequest.
        :rtype: int
        """
        return self._retention_id

    @retention_id.setter
    def retention_id(self, retention_id):
        """Sets the retention_id of this DeleteRetentionRequest.

        镜像老化规则id

        :param retention_id: The retention_id of this DeleteRetentionRequest.
        :type retention_id: int
        """
        self._retention_id = retention_id

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
        if not isinstance(other, DeleteRetentionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
