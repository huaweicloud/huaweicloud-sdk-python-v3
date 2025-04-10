# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAttachSharableVolumesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serverinfo': 'list[BatchAttachSharableVolumesOption]'
    }

    attribute_map = {
        'serverinfo': 'serverinfo'
    }

    def __init__(self, serverinfo=None):
        r"""BatchAttachSharableVolumesRequestBody

        The model defined in huaweicloud sdk

        :param serverinfo: 共享磁盘需要挂载的弹性云服务器列表。
        :type serverinfo: list[:class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesOption`]
        """
        
        

        self._serverinfo = None
        self.discriminator = None

        self.serverinfo = serverinfo

    @property
    def serverinfo(self):
        r"""Gets the serverinfo of this BatchAttachSharableVolumesRequestBody.

        共享磁盘需要挂载的弹性云服务器列表。

        :return: The serverinfo of this BatchAttachSharableVolumesRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesOption`]
        """
        return self._serverinfo

    @serverinfo.setter
    def serverinfo(self, serverinfo):
        r"""Sets the serverinfo of this BatchAttachSharableVolumesRequestBody.

        共享磁盘需要挂载的弹性云服务器列表。

        :param serverinfo: The serverinfo of this BatchAttachSharableVolumesRequestBody.
        :type serverinfo: list[:class:`huaweicloudsdkecs.v2.BatchAttachSharableVolumesOption`]
        """
        self._serverinfo = serverinfo

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
        if not isinstance(other, BatchAttachSharableVolumesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
