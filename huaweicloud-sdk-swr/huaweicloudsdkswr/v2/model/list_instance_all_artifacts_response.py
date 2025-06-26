# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceAllArtifactsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'artifacts': 'list[Artifact]',
        'next_marker': 'int'
    }

    attribute_map = {
        'artifacts': 'artifacts',
        'next_marker': 'next_marker'
    }

    def __init__(self, artifacts=None, next_marker=None):
        r"""ListInstanceAllArtifactsResponse

        The model defined in huaweicloud sdk

        :param artifacts: 制品列表
        :type artifacts: list[:class:`huaweicloudsdkswr.v2.Artifact`]
        :param next_marker: 下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕
        :type next_marker: int
        """
        
        super(ListInstanceAllArtifactsResponse, self).__init__()

        self._artifacts = None
        self._next_marker = None
        self.discriminator = None

        if artifacts is not None:
            self.artifacts = artifacts
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def artifacts(self):
        r"""Gets the artifacts of this ListInstanceAllArtifactsResponse.

        制品列表

        :return: The artifacts of this ListInstanceAllArtifactsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Artifact`]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        r"""Sets the artifacts of this ListInstanceAllArtifactsResponse.

        制品列表

        :param artifacts: The artifacts of this ListInstanceAllArtifactsResponse.
        :type artifacts: list[:class:`huaweicloudsdkswr.v2.Artifact`]
        """
        self._artifacts = artifacts

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListInstanceAllArtifactsResponse.

        下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕

        :return: The next_marker of this ListInstanceAllArtifactsResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListInstanceAllArtifactsResponse.

        下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕

        :param next_marker: The next_marker of this ListInstanceAllArtifactsResponse.
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
        if not isinstance(other, ListInstanceAllArtifactsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
