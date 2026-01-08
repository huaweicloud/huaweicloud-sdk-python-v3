# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifyQosVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_ids': 'list[str]',
        'qos': 'Qos'
    }

    attribute_map = {
        'volume_ids': 'volume_ids',
        'qos': 'qos'
    }

    def __init__(self, volume_ids=None, qos=None):
        r"""BatchModifyQosVolumesReq

        The model defined in huaweicloud sdk

        :param volume_ids: 修改QOS磁盘ids。
        :type volume_ids: list[str]
        :param qos: 
        :type qos: :class:`huaweicloudsdkworkspace.v2.Qos`
        """
        
        

        self._volume_ids = None
        self._qos = None
        self.discriminator = None

        self.volume_ids = volume_ids
        self.qos = qos

    @property
    def volume_ids(self):
        r"""Gets the volume_ids of this BatchModifyQosVolumesReq.

        修改QOS磁盘ids。

        :return: The volume_ids of this BatchModifyQosVolumesReq.
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        r"""Sets the volume_ids of this BatchModifyQosVolumesReq.

        修改QOS磁盘ids。

        :param volume_ids: The volume_ids of this BatchModifyQosVolumesReq.
        :type volume_ids: list[str]
        """
        self._volume_ids = volume_ids

    @property
    def qos(self):
        r"""Gets the qos of this BatchModifyQosVolumesReq.

        :return: The qos of this BatchModifyQosVolumesReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Qos`
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        r"""Sets the qos of this BatchModifyQosVolumesReq.

        :param qos: The qos of this BatchModifyQosVolumesReq.
        :type qos: :class:`huaweicloudsdkworkspace.v2.Qos`
        """
        self._qos = qos

    def to_dict(self):
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
        if not isinstance(other, BatchModifyQosVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
