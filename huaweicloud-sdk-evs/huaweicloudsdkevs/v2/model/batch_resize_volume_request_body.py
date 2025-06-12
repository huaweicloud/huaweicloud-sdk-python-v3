# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResizeVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volumes': 'list[VolumesForBatchResizeVolume]',
        'bss_param': 'PrepaidParamForBatchResizeVolume'
    }

    attribute_map = {
        'volumes': 'volumes',
        'bss_param': 'bss_param'
    }

    def __init__(self, volumes=None, bss_param=None):
        r"""BatchResizeVolumeRequestBody

        The model defined in huaweicloud sdk

        :param volumes: The list of disks to be expanded.
        :type volumes: list[:class:`huaweicloudsdkevs.v2.VolumesForBatchResizeVolume`]
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkevs.v2.PrepaidParamForBatchResizeVolume`
        """
        
        

        self._volumes = None
        self._bss_param = None
        self.discriminator = None

        self.volumes = volumes
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def volumes(self):
        r"""Gets the volumes of this BatchResizeVolumeRequestBody.

        The list of disks to be expanded.

        :return: The volumes of this BatchResizeVolumeRequestBody.
        :rtype: list[:class:`huaweicloudsdkevs.v2.VolumesForBatchResizeVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this BatchResizeVolumeRequestBody.

        The list of disks to be expanded.

        :param volumes: The volumes of this BatchResizeVolumeRequestBody.
        :type volumes: list[:class:`huaweicloudsdkevs.v2.VolumesForBatchResizeVolume`]
        """
        self._volumes = volumes

    @property
    def bss_param(self):
        r"""Gets the bss_param of this BatchResizeVolumeRequestBody.

        :return: The bss_param of this BatchResizeVolumeRequestBody.
        :rtype: :class:`huaweicloudsdkevs.v2.PrepaidParamForBatchResizeVolume`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        r"""Sets the bss_param of this BatchResizeVolumeRequestBody.

        :param bss_param: The bss_param of this BatchResizeVolumeRequestBody.
        :type bss_param: :class:`huaweicloudsdkevs.v2.PrepaidParamForBatchResizeVolume`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, BatchResizeVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
