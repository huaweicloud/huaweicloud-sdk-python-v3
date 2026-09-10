# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectInstanceStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'abnormal_num': 'int',
        'disk_full_num': 'int',
        'frozen_num': 'int',
        'normal_num': 'int',
        'wait_reboot_num': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'abnormal_num': 'abnormal_num',
        'disk_full_num': 'disk_full_num',
        'frozen_num': 'frozen_num',
        'normal_num': 'normal_num',
        'wait_reboot_num': 'wait_reboot_num'
    }

    def __init__(self, total_num=None, abnormal_num=None, disk_full_num=None, frozen_num=None, normal_num=None, wait_reboot_num=None):
        r"""CollectInstanceStatisticResponse

        The model defined in huaweicloud sdk

        :param total_num: 实例总数
        :type total_num: int
        :param abnormal_num: 异常实例数
        :type abnormal_num: int
        :param disk_full_num: 磁盘不足实例数
        :type disk_full_num: int
        :param frozen_num: 冻结实例数
        :type frozen_num: int
        :param normal_num: 运行中实例数
        :type normal_num: int
        :param wait_reboot_num: 等待重启实例数
        :type wait_reboot_num: int
        """
        
        super().__init__()

        self._total_num = None
        self._abnormal_num = None
        self._disk_full_num = None
        self._frozen_num = None
        self._normal_num = None
        self._wait_reboot_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if abnormal_num is not None:
            self.abnormal_num = abnormal_num
        if disk_full_num is not None:
            self.disk_full_num = disk_full_num
        if frozen_num is not None:
            self.frozen_num = frozen_num
        if normal_num is not None:
            self.normal_num = normal_num
        if wait_reboot_num is not None:
            self.wait_reboot_num = wait_reboot_num

    @property
    def total_num(self):
        r"""Gets the total_num of this CollectInstanceStatisticResponse.

        实例总数

        :return: The total_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this CollectInstanceStatisticResponse.

        实例总数

        :param total_num: The total_num of this CollectInstanceStatisticResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def abnormal_num(self):
        r"""Gets the abnormal_num of this CollectInstanceStatisticResponse.

        异常实例数

        :return: The abnormal_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._abnormal_num

    @abnormal_num.setter
    def abnormal_num(self, abnormal_num):
        r"""Sets the abnormal_num of this CollectInstanceStatisticResponse.

        异常实例数

        :param abnormal_num: The abnormal_num of this CollectInstanceStatisticResponse.
        :type abnormal_num: int
        """
        self._abnormal_num = abnormal_num

    @property
    def disk_full_num(self):
        r"""Gets the disk_full_num of this CollectInstanceStatisticResponse.

        磁盘不足实例数

        :return: The disk_full_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._disk_full_num

    @disk_full_num.setter
    def disk_full_num(self, disk_full_num):
        r"""Sets the disk_full_num of this CollectInstanceStatisticResponse.

        磁盘不足实例数

        :param disk_full_num: The disk_full_num of this CollectInstanceStatisticResponse.
        :type disk_full_num: int
        """
        self._disk_full_num = disk_full_num

    @property
    def frozen_num(self):
        r"""Gets the frozen_num of this CollectInstanceStatisticResponse.

        冻结实例数

        :return: The frozen_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._frozen_num

    @frozen_num.setter
    def frozen_num(self, frozen_num):
        r"""Sets the frozen_num of this CollectInstanceStatisticResponse.

        冻结实例数

        :param frozen_num: The frozen_num of this CollectInstanceStatisticResponse.
        :type frozen_num: int
        """
        self._frozen_num = frozen_num

    @property
    def normal_num(self):
        r"""Gets the normal_num of this CollectInstanceStatisticResponse.

        运行中实例数

        :return: The normal_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._normal_num

    @normal_num.setter
    def normal_num(self, normal_num):
        r"""Sets the normal_num of this CollectInstanceStatisticResponse.

        运行中实例数

        :param normal_num: The normal_num of this CollectInstanceStatisticResponse.
        :type normal_num: int
        """
        self._normal_num = normal_num

    @property
    def wait_reboot_num(self):
        r"""Gets the wait_reboot_num of this CollectInstanceStatisticResponse.

        等待重启实例数

        :return: The wait_reboot_num of this CollectInstanceStatisticResponse.
        :rtype: int
        """
        return self._wait_reboot_num

    @wait_reboot_num.setter
    def wait_reboot_num(self, wait_reboot_num):
        r"""Sets the wait_reboot_num of this CollectInstanceStatisticResponse.

        等待重启实例数

        :param wait_reboot_num: The wait_reboot_num of this CollectInstanceStatisticResponse.
        :type wait_reboot_num: int
        """
        self._wait_reboot_num = wait_reboot_num

    def to_dict(self):
        import warnings
        warnings.warn("CollectInstanceStatisticResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CollectInstanceStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
