# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpFrequencyLimit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'qps': 'int'
    }

    attribute_map = {
        'status': 'status',
        'qps': 'qps'
    }

    def __init__(self, status=None, qps=None):
        """IpFrequencyLimit

        The model defined in huaweicloud sdk

        :param status: 状态，on：打开，off：关闭。
        :type status: str
        :param qps: 访问阈值,单位：次/秒，取值范围：1-100000。   &gt; 当开启ip限频时，访问阈值必填。
        :type qps: int
        """
        
        

        self._status = None
        self._qps = None
        self.discriminator = None

        self.status = status
        if qps is not None:
            self.qps = qps

    @property
    def status(self):
        """Gets the status of this IpFrequencyLimit.

        状态，on：打开，off：关闭。

        :return: The status of this IpFrequencyLimit.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IpFrequencyLimit.

        状态，on：打开，off：关闭。

        :param status: The status of this IpFrequencyLimit.
        :type status: str
        """
        self._status = status

    @property
    def qps(self):
        """Gets the qps of this IpFrequencyLimit.

        访问阈值,单位：次/秒，取值范围：1-100000。   > 当开启ip限频时，访问阈值必填。

        :return: The qps of this IpFrequencyLimit.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this IpFrequencyLimit.

        访问阈值,单位：次/秒，取值范围：1-100000。   > 当开启ip限频时，访问阈值必填。

        :param qps: The qps of this IpFrequencyLimit.
        :type qps: int
        """
        self._qps = qps

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
        if not isinstance(other, IpFrequencyLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
