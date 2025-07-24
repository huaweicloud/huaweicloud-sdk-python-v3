# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaultHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fault_date': 'datetime',
        'new_fault_host': 'int',
        'fault_host': 'list[str]'
    }

    attribute_map = {
        'fault_date': 'fault_date',
        'new_fault_host': 'new_fault_host',
        'fault_host': 'fault_host'
    }

    def __init__(self, fault_date=None, new_fault_host=None, fault_host=None):
        r"""FaultHostInfo

        The model defined in huaweicloud sdk

        :param fault_date: 告警时间
        :type fault_date: datetime
        :param new_fault_host: 新增故障机器数
        :type new_fault_host: int
        :param fault_host: 故障机器SN
        :type fault_host: list[str]
        """
        
        

        self._fault_date = None
        self._new_fault_host = None
        self._fault_host = None
        self.discriminator = None

        if fault_date is not None:
            self.fault_date = fault_date
        if new_fault_host is not None:
            self.new_fault_host = new_fault_host
        if fault_host is not None:
            self.fault_host = fault_host

    @property
    def fault_date(self):
        r"""Gets the fault_date of this FaultHostInfo.

        告警时间

        :return: The fault_date of this FaultHostInfo.
        :rtype: datetime
        """
        return self._fault_date

    @fault_date.setter
    def fault_date(self, fault_date):
        r"""Sets the fault_date of this FaultHostInfo.

        告警时间

        :param fault_date: The fault_date of this FaultHostInfo.
        :type fault_date: datetime
        """
        self._fault_date = fault_date

    @property
    def new_fault_host(self):
        r"""Gets the new_fault_host of this FaultHostInfo.

        新增故障机器数

        :return: The new_fault_host of this FaultHostInfo.
        :rtype: int
        """
        return self._new_fault_host

    @new_fault_host.setter
    def new_fault_host(self, new_fault_host):
        r"""Sets the new_fault_host of this FaultHostInfo.

        新增故障机器数

        :param new_fault_host: The new_fault_host of this FaultHostInfo.
        :type new_fault_host: int
        """
        self._new_fault_host = new_fault_host

    @property
    def fault_host(self):
        r"""Gets the fault_host of this FaultHostInfo.

        故障机器SN

        :return: The fault_host of this FaultHostInfo.
        :rtype: list[str]
        """
        return self._fault_host

    @fault_host.setter
    def fault_host(self, fault_host):
        r"""Sets the fault_host of this FaultHostInfo.

        故障机器SN

        :param fault_host: The fault_host of this FaultHostInfo.
        :type fault_host: list[str]
        """
        self._fault_host = fault_host

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
        if not isinstance(other, FaultHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
