# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_tags': 'list[CmdbTagEntity]',
        'total_count': 'int'
    }

    attribute_map = {
        'env_tags': 'env_tags',
        'total_count': 'total_count'
    }

    def __init__(self, env_tags=None, total_count=None):
        """ListEnvTagsResponse

        The model defined in huaweicloud sdk

        :param env_tags: 环境标签数据列表。
        :type env_tags: list[:class:`huaweicloudsdkapm.v1.CmdbTagEntity`]
        :param total_count: 总条数。
        :type total_count: int
        """
        
        super(ListEnvTagsResponse, self).__init__()

        self._env_tags = None
        self._total_count = None
        self.discriminator = None

        if env_tags is not None:
            self.env_tags = env_tags
        if total_count is not None:
            self.total_count = total_count

    @property
    def env_tags(self):
        """Gets the env_tags of this ListEnvTagsResponse.

        环境标签数据列表。

        :return: The env_tags of this ListEnvTagsResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.CmdbTagEntity`]
        """
        return self._env_tags

    @env_tags.setter
    def env_tags(self, env_tags):
        """Sets the env_tags of this ListEnvTagsResponse.

        环境标签数据列表。

        :param env_tags: The env_tags of this ListEnvTagsResponse.
        :type env_tags: list[:class:`huaweicloudsdkapm.v1.CmdbTagEntity`]
        """
        self._env_tags = env_tags

    @property
    def total_count(self):
        """Gets the total_count of this ListEnvTagsResponse.

        总条数。

        :return: The total_count of this ListEnvTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnvTagsResponse.

        总条数。

        :param total_count: The total_count of this ListEnvTagsResponse.
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
        if not isinstance(other, ListEnvTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
