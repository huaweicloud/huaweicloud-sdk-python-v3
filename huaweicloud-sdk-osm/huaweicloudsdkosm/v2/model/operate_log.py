# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'oper': 'str',
        'operate_time': 'str'
    }

    attribute_map = {
        'oper': 'oper',
        'operate_time': 'operate_time'
    }

    def __init__(self, oper=None, operate_time=None):
        """OperateLog

        The model defined in huaweicloud sdk

        :param oper: 操作指令
        :type oper: str
        :param operate_time: 操作时间
        :type operate_time: str
        """
        
        

        self._oper = None
        self._operate_time = None
        self.discriminator = None

        if oper is not None:
            self.oper = oper
        if operate_time is not None:
            self.operate_time = operate_time

    @property
    def oper(self):
        """Gets the oper of this OperateLog.

        操作指令

        :return: The oper of this OperateLog.
        :rtype: str
        """
        return self._oper

    @oper.setter
    def oper(self, oper):
        """Sets the oper of this OperateLog.

        操作指令

        :param oper: The oper of this OperateLog.
        :type oper: str
        """
        self._oper = oper

    @property
    def operate_time(self):
        """Gets the operate_time of this OperateLog.

        操作时间

        :return: The operate_time of this OperateLog.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this OperateLog.

        操作时间

        :param operate_time: The operate_time of this OperateLog.
        :type operate_time: str
        """
        self._operate_time = operate_time

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
        if not isinstance(other, OperateLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
