# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterRecoverStartSimulationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'xlog_keep_ratio': 'int',
        'disaster_type': 'str'
    }

    attribute_map = {
        'xlog_keep_ratio': 'xlog_keep_ratio',
        'disaster_type': 'disaster_type'
    }

    def __init__(self, xlog_keep_ratio=None, disaster_type=None):
        r"""DisasterRecoverStartSimulationRequestBody

        The model defined in huaweicloud sdk

        :param xlog_keep_ratio: 主实例下发容灾演练时必填，备实例下发容灾演练是不必填   - 日志保留空间占可使用剩余磁盘容量的比例, 可设置范围为1-100。
        :type xlog_keep_ratio: int
        :param disaster_type: 容灾类型。
        :type disaster_type: str
        """
        
        

        self._xlog_keep_ratio = None
        self._disaster_type = None
        self.discriminator = None

        if xlog_keep_ratio is not None:
            self.xlog_keep_ratio = xlog_keep_ratio
        self.disaster_type = disaster_type

    @property
    def xlog_keep_ratio(self):
        r"""Gets the xlog_keep_ratio of this DisasterRecoverStartSimulationRequestBody.

        主实例下发容灾演练时必填，备实例下发容灾演练是不必填   - 日志保留空间占可使用剩余磁盘容量的比例, 可设置范围为1-100。

        :return: The xlog_keep_ratio of this DisasterRecoverStartSimulationRequestBody.
        :rtype: int
        """
        return self._xlog_keep_ratio

    @xlog_keep_ratio.setter
    def xlog_keep_ratio(self, xlog_keep_ratio):
        r"""Sets the xlog_keep_ratio of this DisasterRecoverStartSimulationRequestBody.

        主实例下发容灾演练时必填，备实例下发容灾演练是不必填   - 日志保留空间占可使用剩余磁盘容量的比例, 可设置范围为1-100。

        :param xlog_keep_ratio: The xlog_keep_ratio of this DisasterRecoverStartSimulationRequestBody.
        :type xlog_keep_ratio: int
        """
        self._xlog_keep_ratio = xlog_keep_ratio

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this DisasterRecoverStartSimulationRequestBody.

        容灾类型。

        :return: The disaster_type of this DisasterRecoverStartSimulationRequestBody.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this DisasterRecoverStartSimulationRequestBody.

        容灾类型。

        :param disaster_type: The disaster_type of this DisasterRecoverStartSimulationRequestBody.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

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
        if not isinstance(other, DisasterRecoverStartSimulationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
