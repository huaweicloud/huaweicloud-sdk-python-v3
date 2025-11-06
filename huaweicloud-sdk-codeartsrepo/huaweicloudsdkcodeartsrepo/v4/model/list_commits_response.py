# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommitsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commits': 'list[CommitDto]',
        'date_title': 'list[DateTitleDto]'
    }

    attribute_map = {
        'commits': 'commits',
        'date_title': 'date_title'
    }

    def __init__(self, commits=None, date_title=None):
        r"""ListCommitsResponse

        The model defined in huaweicloud sdk

        :param commits: 提交列表
        :type commits: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitDto`]
        :param date_title: 按天统计信息
        :type date_title: list[:class:`huaweicloudsdkcodeartsrepo.v4.DateTitleDto`]
        """
        
        super().__init__()

        self._commits = None
        self._date_title = None
        self.discriminator = None

        if commits is not None:
            self.commits = commits
        if date_title is not None:
            self.date_title = date_title

    @property
    def commits(self):
        r"""Gets the commits of this ListCommitsResponse.

        提交列表

        :return: The commits of this ListCommitsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitDto`]
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        r"""Sets the commits of this ListCommitsResponse.

        提交列表

        :param commits: The commits of this ListCommitsResponse.
        :type commits: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitDto`]
        """
        self._commits = commits

    @property
    def date_title(self):
        r"""Gets the date_title of this ListCommitsResponse.

        按天统计信息

        :return: The date_title of this ListCommitsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.DateTitleDto`]
        """
        return self._date_title

    @date_title.setter
    def date_title(self, date_title):
        r"""Sets the date_title of this ListCommitsResponse.

        按天统计信息

        :param date_title: The date_title of this ListCommitsResponse.
        :type date_title: list[:class:`huaweicloudsdkcodeartsrepo.v4.DateTitleDto`]
        """
        self._date_title = date_title

    def to_dict(self):
        import warnings
        warnings.warn("ListCommitsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListCommitsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
