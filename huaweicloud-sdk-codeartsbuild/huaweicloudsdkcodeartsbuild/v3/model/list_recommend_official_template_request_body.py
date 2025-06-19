# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecommendOfficialTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'git_url': 'str',
        'branch': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'git_url': 'git_url',
        'branch': 'branch',
        'tags': 'tags'
    }

    def __init__(self, git_url=None, branch=None, tags=None):
        r"""ListRecommendOfficialTemplateRequestBody

        The model defined in huaweicloud sdk

        :param git_url: 代码仓地址
        :type git_url: str
        :param branch: 代码仓分支名称你
        :type branch: str
        :param tags: 代码仓TAG
        :type tags: str
        """
        
        

        self._git_url = None
        self._branch = None
        self._tags = None
        self.discriminator = None

        if git_url is not None:
            self.git_url = git_url
        if branch is not None:
            self.branch = branch
        if tags is not None:
            self.tags = tags

    @property
    def git_url(self):
        r"""Gets the git_url of this ListRecommendOfficialTemplateRequestBody.

        代码仓地址

        :return: The git_url of this ListRecommendOfficialTemplateRequestBody.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this ListRecommendOfficialTemplateRequestBody.

        代码仓地址

        :param git_url: The git_url of this ListRecommendOfficialTemplateRequestBody.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def branch(self):
        r"""Gets the branch of this ListRecommendOfficialTemplateRequestBody.

        代码仓分支名称你

        :return: The branch of this ListRecommendOfficialTemplateRequestBody.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ListRecommendOfficialTemplateRequestBody.

        代码仓分支名称你

        :param branch: The branch of this ListRecommendOfficialTemplateRequestBody.
        :type branch: str
        """
        self._branch = branch

    @property
    def tags(self):
        r"""Gets the tags of this ListRecommendOfficialTemplateRequestBody.

        代码仓TAG

        :return: The tags of this ListRecommendOfficialTemplateRequestBody.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListRecommendOfficialTemplateRequestBody.

        代码仓TAG

        :param tags: The tags of this ListRecommendOfficialTemplateRequestBody.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListRecommendOfficialTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
