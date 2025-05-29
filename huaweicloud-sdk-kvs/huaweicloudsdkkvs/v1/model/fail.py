# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Fail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oper_id': 'int',
        'status': 'str'
    }

    attribute_map = {
        'oper_id': 'oper_id',
        'status': 'status'
    }

    def __init__(self, oper_id=None, status=None):
        r"""Fail

        The model defined in huaweicloud sdk

        :param oper_id: 失败的操作标识，1个或多个。
        :type oper_id: int
        :param status: 处理失败操作提示。
        :type status: str
        """
        
        

        self._oper_id = None
        self._status = None
        self.discriminator = None

        self.oper_id = oper_id
        self.status = status

    @property
    def oper_id(self):
        r"""Gets the oper_id of this Fail.

        失败的操作标识，1个或多个。

        :return: The oper_id of this Fail.
        :rtype: int
        """
        return self._oper_id

    @oper_id.setter
    def oper_id(self, oper_id):
        r"""Sets the oper_id of this Fail.

        失败的操作标识，1个或多个。

        :param oper_id: The oper_id of this Fail.
        :type oper_id: int
        """
        self._oper_id = oper_id

    @property
    def status(self):
        r"""Gets the status of this Fail.

        处理失败操作提示。

        :return: The status of this Fail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Fail.

        处理失败操作提示。

        :param status: The status of this Fail.
        :type status: str
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
        if not isinstance(other, Fail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
