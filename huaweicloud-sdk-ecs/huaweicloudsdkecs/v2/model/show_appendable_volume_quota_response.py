# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppendableVolumeQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_scsi': 'int',
        'count': 'int',
        'free_blk': 'int'
    }

    attribute_map = {
        'free_scsi': 'free_scsi',
        'count': 'count',
        'free_blk': 'free_blk'
    }

    def __init__(self, free_scsi=None, count=None, free_blk=None):
        r"""ShowAppendableVolumeQuotaResponse

        The model defined in huaweicloud sdk

        :param free_scsi: 
        :type free_scsi: int
        :param count: 
        :type count: int
        :param free_blk: 
        :type free_blk: int
        """
        
        super(ShowAppendableVolumeQuotaResponse, self).__init__()

        self._free_scsi = None
        self._count = None
        self._free_blk = None
        self.discriminator = None

        if free_scsi is not None:
            self.free_scsi = free_scsi
        if count is not None:
            self.count = count
        if free_blk is not None:
            self.free_blk = free_blk

    @property
    def free_scsi(self):
        r"""Gets the free_scsi of this ShowAppendableVolumeQuotaResponse.

        :return: The free_scsi of this ShowAppendableVolumeQuotaResponse.
        :rtype: int
        """
        return self._free_scsi

    @free_scsi.setter
    def free_scsi(self, free_scsi):
        r"""Sets the free_scsi of this ShowAppendableVolumeQuotaResponse.

        :param free_scsi: The free_scsi of this ShowAppendableVolumeQuotaResponse.
        :type free_scsi: int
        """
        self._free_scsi = free_scsi

    @property
    def count(self):
        r"""Gets the count of this ShowAppendableVolumeQuotaResponse.

        :return: The count of this ShowAppendableVolumeQuotaResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowAppendableVolumeQuotaResponse.

        :param count: The count of this ShowAppendableVolumeQuotaResponse.
        :type count: int
        """
        self._count = count

    @property
    def free_blk(self):
        r"""Gets the free_blk of this ShowAppendableVolumeQuotaResponse.

        :return: The free_blk of this ShowAppendableVolumeQuotaResponse.
        :rtype: int
        """
        return self._free_blk

    @free_blk.setter
    def free_blk(self, free_blk):
        r"""Sets the free_blk of this ShowAppendableVolumeQuotaResponse.

        :param free_blk: The free_blk of this ShowAppendableVolumeQuotaResponse.
        :type free_blk: int
        """
        self._free_blk = free_blk

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
        if not isinstance(other, ShowAppendableVolumeQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
