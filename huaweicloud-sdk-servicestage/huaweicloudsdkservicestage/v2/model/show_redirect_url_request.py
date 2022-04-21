# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRedirectUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repo_type': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'repo_type': 'repo_type',
        'tag': 'tag'
    }

    def __init__(self, repo_type=None, tag=None):
        """ShowRedirectUrlRequest

        The model defined in huaweicloud sdk

        :param repo_type: 仓库类型。 取值范围：github、gitlab、gitee、bitbucket。
        :type repo_type: str
        :param tag: 站点标签。 比如国际站的，?tag&#x3D;intl。 默认为空。
        :type tag: str
        """
        
        

        self._repo_type = None
        self._tag = None
        self.discriminator = None

        self.repo_type = repo_type
        if tag is not None:
            self.tag = tag

    @property
    def repo_type(self):
        """Gets the repo_type of this ShowRedirectUrlRequest.

        仓库类型。 取值范围：github、gitlab、gitee、bitbucket。

        :return: The repo_type of this ShowRedirectUrlRequest.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this ShowRedirectUrlRequest.

        仓库类型。 取值范围：github、gitlab、gitee、bitbucket。

        :param repo_type: The repo_type of this ShowRedirectUrlRequest.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def tag(self):
        """Gets the tag of this ShowRedirectUrlRequest.

        站点标签。 比如国际站的，?tag=intl。 默认为空。

        :return: The tag of this ShowRedirectUrlRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ShowRedirectUrlRequest.

        站点标签。 比如国际站的，?tag=intl。 默认为空。

        :param tag: The tag of this ShowRedirectUrlRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ShowRedirectUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
