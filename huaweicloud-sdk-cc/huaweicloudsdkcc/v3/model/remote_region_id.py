# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteRegionId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remote_region_id': 'str'
    }

    attribute_map = {
        'remote_region_id': 'remote_region_id'
    }

    def __init__(self, remote_region_id=None):
        r"""RemoteRegionId

        The model defined in huaweicloud sdk

        :param remote_region_id: RegionID。
        :type remote_region_id: str
        """
        
        

        self._remote_region_id = None
        self.discriminator = None

        self.remote_region_id = remote_region_id

    @property
    def remote_region_id(self):
        r"""Gets the remote_region_id of this RemoteRegionId.

        RegionID。

        :return: The remote_region_id of this RemoteRegionId.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        r"""Sets the remote_region_id of this RemoteRegionId.

        RegionID。

        :param remote_region_id: The remote_region_id of this RemoteRegionId.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

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
        if not isinstance(other, RemoteRegionId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
