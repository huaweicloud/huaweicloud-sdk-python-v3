# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHotkeyAutoscanConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'enable_auto_scan': 'bool',
        'schedule_at': 'list[str]',
        'updated_at': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'enable_auto_scan': 'enable_auto_scan',
        'schedule_at': 'schedule_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, instance_id=None, enable_auto_scan=None, schedule_at=None, updated_at=None):
        """ShowHotkeyAutoscanConfigResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param enable_auto_scan: 是否开启自动分析
        :type enable_auto_scan: bool
        :param schedule_at: 每日分析时间，时间格式为21:00
        :type schedule_at: list[str]
        :param updated_at: 配置更新时间，时间格式为2020-06-15T02:21:18.669Z
        :type updated_at: str
        """
        
        super(ShowHotkeyAutoscanConfigResponse, self).__init__()

        self._instance_id = None
        self._enable_auto_scan = None
        self._schedule_at = None
        self._updated_at = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if enable_auto_scan is not None:
            self.enable_auto_scan = enable_auto_scan
        if schedule_at is not None:
            self.schedule_at = schedule_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowHotkeyAutoscanConfigResponse.

        实例ID

        :return: The instance_id of this ShowHotkeyAutoscanConfigResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowHotkeyAutoscanConfigResponse.

        实例ID

        :param instance_id: The instance_id of this ShowHotkeyAutoscanConfigResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def enable_auto_scan(self):
        """Gets the enable_auto_scan of this ShowHotkeyAutoscanConfigResponse.

        是否开启自动分析

        :return: The enable_auto_scan of this ShowHotkeyAutoscanConfigResponse.
        :rtype: bool
        """
        return self._enable_auto_scan

    @enable_auto_scan.setter
    def enable_auto_scan(self, enable_auto_scan):
        """Sets the enable_auto_scan of this ShowHotkeyAutoscanConfigResponse.

        是否开启自动分析

        :param enable_auto_scan: The enable_auto_scan of this ShowHotkeyAutoscanConfigResponse.
        :type enable_auto_scan: bool
        """
        self._enable_auto_scan = enable_auto_scan

    @property
    def schedule_at(self):
        """Gets the schedule_at of this ShowHotkeyAutoscanConfigResponse.

        每日分析时间，时间格式为21:00

        :return: The schedule_at of this ShowHotkeyAutoscanConfigResponse.
        :rtype: list[str]
        """
        return self._schedule_at

    @schedule_at.setter
    def schedule_at(self, schedule_at):
        """Sets the schedule_at of this ShowHotkeyAutoscanConfigResponse.

        每日分析时间，时间格式为21:00

        :param schedule_at: The schedule_at of this ShowHotkeyAutoscanConfigResponse.
        :type schedule_at: list[str]
        """
        self._schedule_at = schedule_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowHotkeyAutoscanConfigResponse.

        配置更新时间，时间格式为2020-06-15T02:21:18.669Z

        :return: The updated_at of this ShowHotkeyAutoscanConfigResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowHotkeyAutoscanConfigResponse.

        配置更新时间，时间格式为2020-06-15T02:21:18.669Z

        :param updated_at: The updated_at of this ShowHotkeyAutoscanConfigResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ShowHotkeyAutoscanConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
