# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clusters': 'list[Cluster]'
    }

    attribute_map = {
        'clusters': 'clusters'
    }

    def __init__(self, clusters=None):
        r"""ListInstancesResponse

        The model defined in huaweicloud sdk

        :param clusters: 实例列表
        :type clusters: list[:class:`huaweicloudsdkdbss.v1.Cluster`]
        """
        
        super().__init__()

        self._clusters = None
        self.discriminator = None

        if clusters is not None:
            self.clusters = clusters

    @property
    def clusters(self):
        r"""Gets the clusters of this ListInstancesResponse.

        实例列表

        :return: The clusters of this ListInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.Cluster`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this ListInstancesResponse.

        实例列表

        :param clusters: The clusters of this ListInstancesResponse.
        :type clusters: list[:class:`huaweicloudsdkdbss.v1.Cluster`]
        """
        self._clusters = clusters

    def to_dict(self):
        import warnings
        warnings.warn("ListInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
