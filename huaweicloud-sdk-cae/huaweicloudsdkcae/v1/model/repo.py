# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Repo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_name': 'str',
        'branch': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'auth_name': 'auth_name',
        'branch': 'branch',
        'namespace': 'namespace'
    }

    def __init__(self, auth_name=None, branch=None, namespace=None):
        """Repo

        The model defined in huaweicloud sdk

        :param auth_name: 授权名。
        :type auth_name: str
        :param branch: 分支。
        :type branch: str
        :param namespace: 命名空间。
        :type namespace: str
        """
        
        

        self._auth_name = None
        self._branch = None
        self._namespace = None
        self.discriminator = None

        if auth_name is not None:
            self.auth_name = auth_name
        if branch is not None:
            self.branch = branch
        if namespace is not None:
            self.namespace = namespace

    @property
    def auth_name(self):
        """Gets the auth_name of this Repo.

        授权名。

        :return: The auth_name of this Repo.
        :rtype: str
        """
        return self._auth_name

    @auth_name.setter
    def auth_name(self, auth_name):
        """Sets the auth_name of this Repo.

        授权名。

        :param auth_name: The auth_name of this Repo.
        :type auth_name: str
        """
        self._auth_name = auth_name

    @property
    def branch(self):
        """Gets the branch of this Repo.

        分支。

        :return: The branch of this Repo.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this Repo.

        分支。

        :param branch: The branch of this Repo.
        :type branch: str
        """
        self._branch = branch

    @property
    def namespace(self):
        """Gets the namespace of this Repo.

        命名空间。

        :return: The namespace of this Repo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Repo.

        命名空间。

        :param namespace: The namespace of this Repo.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, Repo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
