# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiffRefDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_sha': 'str',
        'head_sha': 'str',
        'start_sha': 'str'
    }

    attribute_map = {
        'base_sha': 'base_sha',
        'head_sha': 'head_sha',
        'start_sha': 'start_sha'
    }

    def __init__(self, base_sha=None, head_sha=None, start_sha=None):
        r"""DiffRefDto

        The model defined in huaweicloud sdk

        :param base_sha: 目标分支以及源分支的共同祖先commitId
        :type base_sha: str
        :param head_sha: 源分支的最新commitId
        :type head_sha: str
        :param start_sha: 目标分支的最新commitId
        :type start_sha: str
        """
        
        

        self._base_sha = None
        self._head_sha = None
        self._start_sha = None
        self.discriminator = None

        if base_sha is not None:
            self.base_sha = base_sha
        if head_sha is not None:
            self.head_sha = head_sha
        if start_sha is not None:
            self.start_sha = start_sha

    @property
    def base_sha(self):
        r"""Gets the base_sha of this DiffRefDto.

        目标分支以及源分支的共同祖先commitId

        :return: The base_sha of this DiffRefDto.
        :rtype: str
        """
        return self._base_sha

    @base_sha.setter
    def base_sha(self, base_sha):
        r"""Sets the base_sha of this DiffRefDto.

        目标分支以及源分支的共同祖先commitId

        :param base_sha: The base_sha of this DiffRefDto.
        :type base_sha: str
        """
        self._base_sha = base_sha

    @property
    def head_sha(self):
        r"""Gets the head_sha of this DiffRefDto.

        源分支的最新commitId

        :return: The head_sha of this DiffRefDto.
        :rtype: str
        """
        return self._head_sha

    @head_sha.setter
    def head_sha(self, head_sha):
        r"""Sets the head_sha of this DiffRefDto.

        源分支的最新commitId

        :param head_sha: The head_sha of this DiffRefDto.
        :type head_sha: str
        """
        self._head_sha = head_sha

    @property
    def start_sha(self):
        r"""Gets the start_sha of this DiffRefDto.

        目标分支的最新commitId

        :return: The start_sha of this DiffRefDto.
        :rtype: str
        """
        return self._start_sha

    @start_sha.setter
    def start_sha(self, start_sha):
        r"""Sets the start_sha of this DiffRefDto.

        目标分支的最新commitId

        :param start_sha: The start_sha of this DiffRefDto.
        :type start_sha: str
        """
        self._start_sha = start_sha

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
        if not isinstance(other, DiffRefDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
