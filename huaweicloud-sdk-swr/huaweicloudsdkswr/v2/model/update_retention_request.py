# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRetentionRequest:

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
        'retention_id': 'int',
        'body': 'UpdateRetentionRequestBody'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'retention_id': 'retention_id',
        'body': 'body'
    }

    def __init__(self, namespace=None, repository=None, retention_id=None, body=None):
        r"""UpdateRetentionRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param retention_id: 镜像老化规则id
        :type retention_id: int
        :param body: Body of the UpdateRetentionRequest
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRetentionRequestBody`
        """
        
        

        self._namespace = None
        self._repository = None
        self._retention_id = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.retention_id = retention_id
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateRetentionRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this UpdateRetentionRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateRetentionRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this UpdateRetentionRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this UpdateRetentionRequest.

        镜像仓库名称

        :return: The repository of this UpdateRetentionRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this UpdateRetentionRequest.

        镜像仓库名称

        :param repository: The repository of this UpdateRetentionRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def retention_id(self):
        r"""Gets the retention_id of this UpdateRetentionRequest.

        镜像老化规则id

        :return: The retention_id of this UpdateRetentionRequest.
        :rtype: int
        """
        return self._retention_id

    @retention_id.setter
    def retention_id(self, retention_id):
        r"""Sets the retention_id of this UpdateRetentionRequest.

        镜像老化规则id

        :param retention_id: The retention_id of this UpdateRetentionRequest.
        :type retention_id: int
        """
        self._retention_id = retention_id

    @property
    def body(self):
        r"""Gets the body of this UpdateRetentionRequest.

        :return: The body of this UpdateRetentionRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRetentionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRetentionRequest.

        :param body: The body of this UpdateRetentionRequest.
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRetentionRequestBody`
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
        if not isinstance(other, UpdateRetentionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
