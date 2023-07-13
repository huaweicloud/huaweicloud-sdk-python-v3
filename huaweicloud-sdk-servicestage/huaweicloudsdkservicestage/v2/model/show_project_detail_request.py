# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_repo_auth': 'str',
        'clone_url': 'str'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth',
        'clone_url': 'clone_url'
    }

    def __init__(self, x_repo_auth=None, clone_url=None):
        """ShowProjectDetailRequest

        The model defined in huaweicloud sdk

        :param x_repo_auth: 授权名称。
        :type x_repo_auth: str
        :param clone_url: 仓库克隆URL。
        :type clone_url: str
        """
        
        

        self._x_repo_auth = None
        self._clone_url = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth
        self.clone_url = clone_url

    @property
    def x_repo_auth(self):
        """Gets the x_repo_auth of this ShowProjectDetailRequest.

        授权名称。

        :return: The x_repo_auth of this ShowProjectDetailRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        """Sets the x_repo_auth of this ShowProjectDetailRequest.

        授权名称。

        :param x_repo_auth: The x_repo_auth of this ShowProjectDetailRequest.
        :type x_repo_auth: str
        """
        self._x_repo_auth = x_repo_auth

    @property
    def clone_url(self):
        """Gets the clone_url of this ShowProjectDetailRequest.

        仓库克隆URL。

        :return: The clone_url of this ShowProjectDetailRequest.
        :rtype: str
        """
        return self._clone_url

    @clone_url.setter
    def clone_url(self, clone_url):
        """Sets the clone_url of this ShowProjectDetailRequest.

        仓库克隆URL。

        :param clone_url: The clone_url of this ShowProjectDetailRequest.
        :type clone_url: str
        """
        self._clone_url = clone_url

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
        if not isinstance(other, ShowProjectDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
