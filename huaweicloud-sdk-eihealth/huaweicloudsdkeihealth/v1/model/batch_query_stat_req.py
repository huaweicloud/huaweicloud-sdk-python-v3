# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchQueryStatReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'from_time': 'int',
        'to_time': 'int',
        'period': 'MonitorPeriod',
        'method': 'MonitorMethod',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'from_time': 'from_time',
        'to_time': 'to_time',
        'period': 'period',
        'method': 'method',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, from_time=None, to_time=None, period=None, method=None, resource_ids=None):
        """BatchQueryStatReq

        The model defined in huaweicloud sdk

        :param from_time: 查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type from_time: int
        :param to_time: 查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type to_time: int
        :param period: 
        :type period: :class:`huaweicloudsdkeihealth.v1.MonitorPeriod`
        :param method: 
        :type method: :class:`huaweicloudsdkeihealth.v1.MonitorMethod`
        :param resource_ids: 查询的监控资源对象id集合
        :type resource_ids: list[str]
        """
        
        

        self._from_time = None
        self._to_time = None
        self._period = None
        self._method = None
        self._resource_ids = None
        self.discriminator = None

        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time
        if period is not None:
            self.period = period
        if method is not None:
            self.method = method
        self.resource_ids = resource_ids

    @property
    def from_time(self):
        """Gets the from_time of this BatchQueryStatReq.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The from_time of this BatchQueryStatReq.
        :rtype: int
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this BatchQueryStatReq.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param from_time: The from_time of this BatchQueryStatReq.
        :type from_time: int
        """
        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this BatchQueryStatReq.

        查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The to_time of this BatchQueryStatReq.
        :rtype: int
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this BatchQueryStatReq.

        查询数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param to_time: The to_time of this BatchQueryStatReq.
        :type to_time: int
        """
        self._to_time = to_time

    @property
    def period(self):
        """Gets the period of this BatchQueryStatReq.

        :return: The period of this BatchQueryStatReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MonitorPeriod`
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BatchQueryStatReq.

        :param period: The period of this BatchQueryStatReq.
        :type period: :class:`huaweicloudsdkeihealth.v1.MonitorPeriod`
        """
        self._period = period

    @property
    def method(self):
        """Gets the method of this BatchQueryStatReq.

        :return: The method of this BatchQueryStatReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MonitorMethod`
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BatchQueryStatReq.

        :param method: The method of this BatchQueryStatReq.
        :type method: :class:`huaweicloudsdkeihealth.v1.MonitorMethod`
        """
        self._method = method

    @property
    def resource_ids(self):
        """Gets the resource_ids of this BatchQueryStatReq.

        查询的监控资源对象id集合

        :return: The resource_ids of this BatchQueryStatReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this BatchQueryStatReq.

        查询的监控资源对象id集合

        :param resource_ids: The resource_ids of this BatchQueryStatReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, BatchQueryStatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
