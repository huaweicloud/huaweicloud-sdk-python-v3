# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GitRepositoryRef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'str'
    }

    attribute_map = {
        'branch': 'branch'
    }

    def __init__(self, branch=None):
        r"""GitRepositoryRef

        The model defined in huaweicloud sdk

        :param branch: 用于指定要检出的Git分支。如果未定义其他字段，则默认检出&#39;master&#39;分支。
        :type branch: str
        """
        
        

        self._branch = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch

    @property
    def branch(self):
        r"""Gets the branch of this GitRepositoryRef.

        用于指定要检出的Git分支。如果未定义其他字段，则默认检出'master'分支。

        :return: The branch of this GitRepositoryRef.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this GitRepositoryRef.

        用于指定要检出的Git分支。如果未定义其他字段，则默认检出'master'分支。

        :param branch: The branch of this GitRepositoryRef.
        :type branch: str
        """
        self._branch = branch

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
        if not isinstance(other, GitRepositoryRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
