# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'volumes_links': 'list[Link]',
        'volumes': 'list[VolumeDetail]'
    }

    attribute_map = {
        'count': 'count',
        'volumes_links': 'volumes_links',
        'volumes': 'volumes'
    }

    def __init__(self, count=None, volumes_links=None, volumes=None):
        """ListVolumesResponse

        The model defined in huaweicloud sdk

        :param count: 查询到的云硬盘总数量，不受分页影响。
        :type count: int
        :param volumes_links: 云硬盘列表查询位置标记。如果本次查询只返回部分列表信息时，会返回查询到的当前磁盘mark标记的url，可以继续使用这个url查询剩余列表信息。
        :type volumes_links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param volumes: 查询请求返回的云硬盘列表。
        :type volumes: list[:class:`huaweicloudsdkevs.v2.VolumeDetail`]
        """
        
        super(ListVolumesResponse, self).__init__()

        self._count = None
        self._volumes_links = None
        self._volumes = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if volumes_links is not None:
            self.volumes_links = volumes_links
        if volumes is not None:
            self.volumes = volumes

    @property
    def count(self):
        """Gets the count of this ListVolumesResponse.

        查询到的云硬盘总数量，不受分页影响。

        :return: The count of this ListVolumesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListVolumesResponse.

        查询到的云硬盘总数量，不受分页影响。

        :param count: The count of this ListVolumesResponse.
        :type count: int
        """
        self._count = count

    @property
    def volumes_links(self):
        """Gets the volumes_links of this ListVolumesResponse.

        云硬盘列表查询位置标记。如果本次查询只返回部分列表信息时，会返回查询到的当前磁盘mark标记的url，可以继续使用这个url查询剩余列表信息。

        :return: The volumes_links of this ListVolumesResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._volumes_links

    @volumes_links.setter
    def volumes_links(self, volumes_links):
        """Sets the volumes_links of this ListVolumesResponse.

        云硬盘列表查询位置标记。如果本次查询只返回部分列表信息时，会返回查询到的当前磁盘mark标记的url，可以继续使用这个url查询剩余列表信息。

        :param volumes_links: The volumes_links of this ListVolumesResponse.
        :type volumes_links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._volumes_links = volumes_links

    @property
    def volumes(self):
        """Gets the volumes of this ListVolumesResponse.

        查询请求返回的云硬盘列表。

        :return: The volumes of this ListVolumesResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.VolumeDetail`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ListVolumesResponse.

        查询请求返回的云硬盘列表。

        :param volumes: The volumes of this ListVolumesResponse.
        :type volumes: list[:class:`huaweicloudsdkevs.v2.VolumeDetail`]
        """
        self._volumes = volumes

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
        if not isinstance(other, ListVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
