# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterVolumeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duplicate': 'int',
        'disk_info_list': 'list[DiskInfoResponse]'
    }

    attribute_map = {
        'duplicate': 'duplicate',
        'disk_info_list': 'disk_info_list'
    }

    def __init__(self, duplicate=None, disk_info_list=None):
        r"""ShowClusterVolumeResponse

        The model defined in huaweicloud sdk

        :param duplicate: **参数解释**： 单节点磁盘数量。 **取值范围**： 不涉及。
        :type duplicate: int
        :param disk_info_list: **参数解释**： 节点容量详情。 **取值范围**： 不涉及。
        :type disk_info_list: list[:class:`huaweicloudsdkdws.v2.DiskInfoResponse`]
        """
        
        super(ShowClusterVolumeResponse, self).__init__()

        self._duplicate = None
        self._disk_info_list = None
        self.discriminator = None

        if duplicate is not None:
            self.duplicate = duplicate
        if disk_info_list is not None:
            self.disk_info_list = disk_info_list

    @property
    def duplicate(self):
        r"""Gets the duplicate of this ShowClusterVolumeResponse.

        **参数解释**： 单节点磁盘数量。 **取值范围**： 不涉及。

        :return: The duplicate of this ShowClusterVolumeResponse.
        :rtype: int
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        r"""Sets the duplicate of this ShowClusterVolumeResponse.

        **参数解释**： 单节点磁盘数量。 **取值范围**： 不涉及。

        :param duplicate: The duplicate of this ShowClusterVolumeResponse.
        :type duplicate: int
        """
        self._duplicate = duplicate

    @property
    def disk_info_list(self):
        r"""Gets the disk_info_list of this ShowClusterVolumeResponse.

        **参数解释**： 节点容量详情。 **取值范围**： 不涉及。

        :return: The disk_info_list of this ShowClusterVolumeResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DiskInfoResponse`]
        """
        return self._disk_info_list

    @disk_info_list.setter
    def disk_info_list(self, disk_info_list):
        r"""Sets the disk_info_list of this ShowClusterVolumeResponse.

        **参数解释**： 节点容量详情。 **取值范围**： 不涉及。

        :param disk_info_list: The disk_info_list of this ShowClusterVolumeResponse.
        :type disk_info_list: list[:class:`huaweicloudsdkdws.v2.DiskInfoResponse`]
        """
        self._disk_info_list = disk_info_list

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
        if not isinstance(other, ShowClusterVolumeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
