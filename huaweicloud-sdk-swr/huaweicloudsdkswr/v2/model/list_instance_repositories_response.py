# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRepositoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'repositories': 'list[Repository]'
    }

    attribute_map = {
        'total': 'total',
        'repositories': 'repositories'
    }

    def __init__(self, total=None, repositories=None):
        r"""ListInstanceRepositoriesResponse

        The model defined in huaweicloud sdk

        :param total: 仓库总数
        :type total: int
        :param repositories: 仓库列表详情
        :type repositories: list[:class:`huaweicloudsdkswr.v2.Repository`]
        """
        
        super(ListInstanceRepositoriesResponse, self).__init__()

        self._total = None
        self._repositories = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if repositories is not None:
            self.repositories = repositories

    @property
    def total(self):
        r"""Gets the total of this ListInstanceRepositoriesResponse.

        仓库总数

        :return: The total of this ListInstanceRepositoriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceRepositoriesResponse.

        仓库总数

        :param total: The total of this ListInstanceRepositoriesResponse.
        :type total: int
        """
        self._total = total

    @property
    def repositories(self):
        r"""Gets the repositories of this ListInstanceRepositoriesResponse.

        仓库列表详情

        :return: The repositories of this ListInstanceRepositoriesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Repository`]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this ListInstanceRepositoriesResponse.

        仓库列表详情

        :param repositories: The repositories of this ListInstanceRepositoriesResponse.
        :type repositories: list[:class:`huaweicloudsdkswr.v2.Repository`]
        """
        self._repositories = repositories

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
        if not isinstance(other, ListInstanceRepositoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
