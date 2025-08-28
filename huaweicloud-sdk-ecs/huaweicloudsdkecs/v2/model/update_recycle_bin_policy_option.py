# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecycleBinPolicyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_hour': 'int',
        'recycle_threshold_day': 'int'
    }

    attribute_map = {
        'retention_hour': 'retention_hour',
        'recycle_threshold_day': 'recycle_threshold_day'
    }

    def __init__(self, retention_hour=None, recycle_threshold_day=None):
        r"""UpdateRecycleBinPolicyOption

        The model defined in huaweicloud sdk

        :param retention_hour: 虚拟机进入回收站后多久删除
        :type retention_hour: int
        :param recycle_threshold_day: 创建多久的虚拟机可以进入回收站
        :type recycle_threshold_day: int
        """
        
        

        self._retention_hour = None
        self._recycle_threshold_day = None
        self.discriminator = None

        self.retention_hour = retention_hour
        self.recycle_threshold_day = recycle_threshold_day

    @property
    def retention_hour(self):
        r"""Gets the retention_hour of this UpdateRecycleBinPolicyOption.

        虚拟机进入回收站后多久删除

        :return: The retention_hour of this UpdateRecycleBinPolicyOption.
        :rtype: int
        """
        return self._retention_hour

    @retention_hour.setter
    def retention_hour(self, retention_hour):
        r"""Sets the retention_hour of this UpdateRecycleBinPolicyOption.

        虚拟机进入回收站后多久删除

        :param retention_hour: The retention_hour of this UpdateRecycleBinPolicyOption.
        :type retention_hour: int
        """
        self._retention_hour = retention_hour

    @property
    def recycle_threshold_day(self):
        r"""Gets the recycle_threshold_day of this UpdateRecycleBinPolicyOption.

        创建多久的虚拟机可以进入回收站

        :return: The recycle_threshold_day of this UpdateRecycleBinPolicyOption.
        :rtype: int
        """
        return self._recycle_threshold_day

    @recycle_threshold_day.setter
    def recycle_threshold_day(self, recycle_threshold_day):
        r"""Sets the recycle_threshold_day of this UpdateRecycleBinPolicyOption.

        创建多久的虚拟机可以进入回收站

        :param recycle_threshold_day: The recycle_threshold_day of this UpdateRecycleBinPolicyOption.
        :type recycle_threshold_day: int
        """
        self._recycle_threshold_day = recycle_threshold_day

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
        if not isinstance(other, UpdateRecycleBinPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
