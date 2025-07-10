# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumeProductInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'volume_type': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'volume_type': 'volume_type'
    }

    def __init__(self, availability_zone=None, volume_type=None):
        r"""ListVolumeProductInfoRequest

        The model defined in huaweicloud sdk

        :param availability_zone: 可用分区。
        :type availability_zone: str
        :param volume_type: 磁盘类型（多个磁盘类型用逗号隔开）： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘
        :type volume_type: str
        """
        
        

        self._availability_zone = None
        self._volume_type = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListVolumeProductInfoRequest.

        可用分区。

        :return: The availability_zone of this ListVolumeProductInfoRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListVolumeProductInfoRequest.

        可用分区。

        :param availability_zone: The availability_zone of this ListVolumeProductInfoRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ListVolumeProductInfoRequest.

        磁盘类型（多个磁盘类型用逗号隔开）： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘

        :return: The volume_type of this ListVolumeProductInfoRequest.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ListVolumeProductInfoRequest.

        磁盘类型（多个磁盘类型用逗号隔开）： - SATA: 普通IO磁盘 - SAS：高IO磁盘 - SSD：超高IO磁盘

        :param volume_type: The volume_type of this ListVolumeProductInfoRequest.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, ListVolumeProductInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
