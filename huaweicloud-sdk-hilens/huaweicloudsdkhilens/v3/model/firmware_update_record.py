# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirmwareUpdateRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'firmware_name': 'str',
        'firmware_version': 'str',
        'firmware_size': 'int',
        'firmware_upgrade_time': 'str',
        'status': 'int'
    }

    attribute_map = {
        'firmware_name': 'firmware_name',
        'firmware_version': 'firmware_version',
        'firmware_size': 'firmware_size',
        'firmware_upgrade_time': 'firmware_upgrade_time',
        'status': 'status'
    }

    def __init__(self, firmware_name=None, firmware_version=None, firmware_size=None, firmware_upgrade_time=None, status=None):
        r"""FirmwareUpdateRecord

        The model defined in huaweicloud sdk

        :param firmware_name: 固件名称
        :type firmware_name: str
        :param firmware_version: 固件版本
        :type firmware_version: str
        :param firmware_size: 固件大小
        :type firmware_size: int
        :param firmware_upgrade_time: 固件升级时间
        :type firmware_upgrade_time: str
        :param status: 固件升级状态
        :type status: int
        """
        
        

        self._firmware_name = None
        self._firmware_version = None
        self._firmware_size = None
        self._firmware_upgrade_time = None
        self._status = None
        self.discriminator = None

        if firmware_name is not None:
            self.firmware_name = firmware_name
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if firmware_size is not None:
            self.firmware_size = firmware_size
        if firmware_upgrade_time is not None:
            self.firmware_upgrade_time = firmware_upgrade_time
        if status is not None:
            self.status = status

    @property
    def firmware_name(self):
        r"""Gets the firmware_name of this FirmwareUpdateRecord.

        固件名称

        :return: The firmware_name of this FirmwareUpdateRecord.
        :rtype: str
        """
        return self._firmware_name

    @firmware_name.setter
    def firmware_name(self, firmware_name):
        r"""Sets the firmware_name of this FirmwareUpdateRecord.

        固件名称

        :param firmware_name: The firmware_name of this FirmwareUpdateRecord.
        :type firmware_name: str
        """
        self._firmware_name = firmware_name

    @property
    def firmware_version(self):
        r"""Gets the firmware_version of this FirmwareUpdateRecord.

        固件版本

        :return: The firmware_version of this FirmwareUpdateRecord.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        r"""Sets the firmware_version of this FirmwareUpdateRecord.

        固件版本

        :param firmware_version: The firmware_version of this FirmwareUpdateRecord.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def firmware_size(self):
        r"""Gets the firmware_size of this FirmwareUpdateRecord.

        固件大小

        :return: The firmware_size of this FirmwareUpdateRecord.
        :rtype: int
        """
        return self._firmware_size

    @firmware_size.setter
    def firmware_size(self, firmware_size):
        r"""Sets the firmware_size of this FirmwareUpdateRecord.

        固件大小

        :param firmware_size: The firmware_size of this FirmwareUpdateRecord.
        :type firmware_size: int
        """
        self._firmware_size = firmware_size

    @property
    def firmware_upgrade_time(self):
        r"""Gets the firmware_upgrade_time of this FirmwareUpdateRecord.

        固件升级时间

        :return: The firmware_upgrade_time of this FirmwareUpdateRecord.
        :rtype: str
        """
        return self._firmware_upgrade_time

    @firmware_upgrade_time.setter
    def firmware_upgrade_time(self, firmware_upgrade_time):
        r"""Sets the firmware_upgrade_time of this FirmwareUpdateRecord.

        固件升级时间

        :param firmware_upgrade_time: The firmware_upgrade_time of this FirmwareUpdateRecord.
        :type firmware_upgrade_time: str
        """
        self._firmware_upgrade_time = firmware_upgrade_time

    @property
    def status(self):
        r"""Gets the status of this FirmwareUpdateRecord.

        固件升级状态

        :return: The status of this FirmwareUpdateRecord.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FirmwareUpdateRecord.

        固件升级状态

        :param status: The status of this FirmwareUpdateRecord.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, FirmwareUpdateRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
