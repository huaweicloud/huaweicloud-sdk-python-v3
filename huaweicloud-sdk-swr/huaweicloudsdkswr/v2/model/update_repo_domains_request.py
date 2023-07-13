# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepoDomainsRequest:

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
        'access_domain': 'str',
        'body': 'UpdateRepoDomainsRequestBody'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'access_domain': 'access_domain',
        'body': 'body'
    }

    def __init__(self, namespace=None, repository=None, access_domain=None, body=None):
        """UpdateRepoDomainsRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param access_domain: 共享帐号
        :type access_domain: str
        :param body: Body of the UpdateRepoDomainsRequest
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsRequestBody`
        """
        
        

        self._namespace = None
        self._repository = None
        self._access_domain = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.access_domain = access_domain
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this UpdateRepoDomainsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdateRepoDomainsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this UpdateRepoDomainsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this UpdateRepoDomainsRequest.

        镜像仓库名称

        :return: The repository of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this UpdateRepoDomainsRequest.

        镜像仓库名称

        :param repository: The repository of this UpdateRepoDomainsRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def access_domain(self):
        """Gets the access_domain of this UpdateRepoDomainsRequest.

        共享帐号

        :return: The access_domain of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this UpdateRepoDomainsRequest.

        共享帐号

        :param access_domain: The access_domain of this UpdateRepoDomainsRequest.
        :type access_domain: str
        """
        self._access_domain = access_domain

    @property
    def body(self):
        """Gets the body of this UpdateRepoDomainsRequest.

        :return: The body of this UpdateRepoDomainsRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRepoDomainsRequest.

        :param body: The body of this UpdateRepoDomainsRequest.
        :type body: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsRequestBody`
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
        if not isinstance(other, UpdateRepoDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
