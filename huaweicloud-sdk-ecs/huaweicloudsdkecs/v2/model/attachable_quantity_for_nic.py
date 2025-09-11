# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachableQuantityForNic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_efi_nic': 'int',
        'free_scsi': 'int',
        'free_blk': 'int',
        'free_disk': 'int',
        'free_nic': 'int'
    }

    attribute_map = {
        'free_efi_nic': 'free_efi_nic',
        'free_scsi': 'free_scsi',
        'free_blk': 'free_blk',
        'free_disk': 'free_disk',
        'free_nic': 'free_nic'
    }

    def __init__(self, free_efi_nic=None, free_scsi=None, free_blk=None, free_disk=None, free_nic=None):
        r"""AttachableQuantityForNic

        The model defined in huaweicloud sdk

        :param free_efi_nic: 
        :type free_efi_nic: int
        :param free_scsi: 
        :type free_scsi: int
        :param free_blk: 
        :type free_blk: int
        :param free_disk: 
        :type free_disk: int
        :param free_nic: 
        :type free_nic: int
        """
        
        

        self._free_efi_nic = None
        self._free_scsi = None
        self._free_blk = None
        self._free_disk = None
        self._free_nic = None
        self.discriminator = None

        if free_efi_nic is not None:
            self.free_efi_nic = free_efi_nic
        if free_scsi is not None:
            self.free_scsi = free_scsi
        if free_blk is not None:
            self.free_blk = free_blk
        if free_disk is not None:
            self.free_disk = free_disk
        if free_nic is not None:
            self.free_nic = free_nic

    @property
    def free_efi_nic(self):
        r"""Gets the free_efi_nic of this AttachableQuantityForNic.

        :return: The free_efi_nic of this AttachableQuantityForNic.
        :rtype: int
        """
        return self._free_efi_nic

    @free_efi_nic.setter
    def free_efi_nic(self, free_efi_nic):
        r"""Sets the free_efi_nic of this AttachableQuantityForNic.

        :param free_efi_nic: The free_efi_nic of this AttachableQuantityForNic.
        :type free_efi_nic: int
        """
        self._free_efi_nic = free_efi_nic

    @property
    def free_scsi(self):
        r"""Gets the free_scsi of this AttachableQuantityForNic.

        :return: The free_scsi of this AttachableQuantityForNic.
        :rtype: int
        """
        return self._free_scsi

    @free_scsi.setter
    def free_scsi(self, free_scsi):
        r"""Sets the free_scsi of this AttachableQuantityForNic.

        :param free_scsi: The free_scsi of this AttachableQuantityForNic.
        :type free_scsi: int
        """
        self._free_scsi = free_scsi

    @property
    def free_blk(self):
        r"""Gets the free_blk of this AttachableQuantityForNic.

        :return: The free_blk of this AttachableQuantityForNic.
        :rtype: int
        """
        return self._free_blk

    @free_blk.setter
    def free_blk(self, free_blk):
        r"""Sets the free_blk of this AttachableQuantityForNic.

        :param free_blk: The free_blk of this AttachableQuantityForNic.
        :type free_blk: int
        """
        self._free_blk = free_blk

    @property
    def free_disk(self):
        r"""Gets the free_disk of this AttachableQuantityForNic.

        :return: The free_disk of this AttachableQuantityForNic.
        :rtype: int
        """
        return self._free_disk

    @free_disk.setter
    def free_disk(self, free_disk):
        r"""Sets the free_disk of this AttachableQuantityForNic.

        :param free_disk: The free_disk of this AttachableQuantityForNic.
        :type free_disk: int
        """
        self._free_disk = free_disk

    @property
    def free_nic(self):
        r"""Gets the free_nic of this AttachableQuantityForNic.

        :return: The free_nic of this AttachableQuantityForNic.
        :rtype: int
        """
        return self._free_nic

    @free_nic.setter
    def free_nic(self, free_nic):
        r"""Sets the free_nic of this AttachableQuantityForNic.

        :param free_nic: The free_nic of this AttachableQuantityForNic.
        :type free_nic: int
        """
        self._free_nic = free_nic

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
        if not isinstance(other, AttachableQuantityForNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
