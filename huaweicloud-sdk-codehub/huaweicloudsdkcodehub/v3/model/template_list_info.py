# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repos': 'list[DevstarRepoInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'repos': 'repos',
        'total_count': 'total_count'
    }

    def __init__(self, repos=None, total_count=None):
        """TemplateListInfo

        The model defined in huaweicloud sdk

        :param repos: 仓库列表
        :type repos: list[:class:`huaweicloudsdkcodehub.v3.DevstarRepoInfo`]
        :param total_count: 仓库总数
        :type total_count: int
        """
        
        

        self._repos = None
        self._total_count = None
        self.discriminator = None

        if repos is not None:
            self.repos = repos
        if total_count is not None:
            self.total_count = total_count

    @property
    def repos(self):
        """Gets the repos of this TemplateListInfo.

        仓库列表

        :return: The repos of this TemplateListInfo.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.DevstarRepoInfo`]
        """
        return self._repos

    @repos.setter
    def repos(self, repos):
        """Sets the repos of this TemplateListInfo.

        仓库列表

        :param repos: The repos of this TemplateListInfo.
        :type repos: list[:class:`huaweicloudsdkcodehub.v3.DevstarRepoInfo`]
        """
        self._repos = repos

    @property
    def total_count(self):
        """Gets the total_count of this TemplateListInfo.

        仓库总数

        :return: The total_count of this TemplateListInfo.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this TemplateListInfo.

        仓库总数

        :param total_count: The total_count of this TemplateListInfo.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, TemplateListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
