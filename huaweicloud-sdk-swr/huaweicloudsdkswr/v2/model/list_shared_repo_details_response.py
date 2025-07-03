# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharedRepoDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repos': 'list[ShowReposRespV3]',
        'next_marker': 'int'
    }

    attribute_map = {
        'repos': 'repos',
        'next_marker': 'nextMarker'
    }

    def __init__(self, repos=None, next_marker=None):
        r"""ListSharedRepoDetailsResponse

        The model defined in huaweicloud sdk

        :param repos: 镜像仓库列表.
        :type repos: list[:class:`huaweicloudsdkswr.v2.ShowReposRespV3`]
        :param next_marker: 分页查询时,查询下一页数据的起始位置。
        :type next_marker: int
        """
        
        super(ListSharedRepoDetailsResponse, self).__init__()

        self._repos = None
        self._next_marker = None
        self.discriminator = None

        if repos is not None:
            self.repos = repos
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def repos(self):
        r"""Gets the repos of this ListSharedRepoDetailsResponse.

        镜像仓库列表.

        :return: The repos of this ListSharedRepoDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ShowReposRespV3`]
        """
        return self._repos

    @repos.setter
    def repos(self, repos):
        r"""Sets the repos of this ListSharedRepoDetailsResponse.

        镜像仓库列表.

        :param repos: The repos of this ListSharedRepoDetailsResponse.
        :type repos: list[:class:`huaweicloudsdkswr.v2.ShowReposRespV3`]
        """
        self._repos = repos

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListSharedRepoDetailsResponse.

        分页查询时,查询下一页数据的起始位置。

        :return: The next_marker of this ListSharedRepoDetailsResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListSharedRepoDetailsResponse.

        分页查询时,查询下一页数据的起始位置。

        :param next_marker: The next_marker of this ListSharedRepoDetailsResponse.
        :type next_marker: int
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListSharedRepoDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
