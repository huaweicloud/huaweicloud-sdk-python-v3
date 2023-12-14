# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogicalClusterVolumesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volumes': 'list[LogicalClusterVolume]',
        'count': 'int'
    }

    attribute_map = {
        'volumes': 'volumes',
        'count': 'count'
    }

    def __init__(self, volumes=None, count=None):
        """ListLogicalClusterVolumesResponse

        The model defined in huaweicloud sdk

        :param volumes: 逻辑集群磁盘信息列表
        :type volumes: list[:class:`huaweicloudsdkdws.v2.LogicalClusterVolume`]
        :param count: 逻辑集群磁盘总数
        :type count: int
        """
        
        super(ListLogicalClusterVolumesResponse, self).__init__()

        self._volumes = None
        self._count = None
        self.discriminator = None

        if volumes is not None:
            self.volumes = volumes
        if count is not None:
            self.count = count

    @property
    def volumes(self):
        """Gets the volumes of this ListLogicalClusterVolumesResponse.

        逻辑集群磁盘信息列表

        :return: The volumes of this ListLogicalClusterVolumesResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ListLogicalClusterVolumesResponse.

        逻辑集群磁盘信息列表

        :param volumes: The volumes of this ListLogicalClusterVolumesResponse.
        :type volumes: list[:class:`huaweicloudsdkdws.v2.LogicalClusterVolume`]
        """
        self._volumes = volumes

    @property
    def count(self):
        """Gets the count of this ListLogicalClusterVolumesResponse.

        逻辑集群磁盘总数

        :return: The count of this ListLogicalClusterVolumesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListLogicalClusterVolumesResponse.

        逻辑集群磁盘总数

        :param count: The count of this ListLogicalClusterVolumesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListLogicalClusterVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
