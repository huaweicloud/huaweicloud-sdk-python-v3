# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSwitchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'status': 'status'
    }

    def __init__(self, ids=None, status=None):
        r"""BatchSwitchesRequest

        The model defined in huaweicloud sdk

        :param ids: 规则ID,多个ID中间逗号分隔。可在查询风险规则策略接口ID字段获取。
        :type ids: str
        :param status: 开关状态 - OFF: 关闭 - ON: 开启
        :type status: str
        """
        
        

        self._ids = None
        self._status = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if status is not None:
            self.status = status

    @property
    def ids(self):
        r"""Gets the ids of this BatchSwitchesRequest.

        规则ID,多个ID中间逗号分隔。可在查询风险规则策略接口ID字段获取。

        :return: The ids of this BatchSwitchesRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchSwitchesRequest.

        规则ID,多个ID中间逗号分隔。可在查询风险规则策略接口ID字段获取。

        :param ids: The ids of this BatchSwitchesRequest.
        :type ids: str
        """
        self._ids = ids

    @property
    def status(self):
        r"""Gets the status of this BatchSwitchesRequest.

        开关状态 - OFF: 关闭 - ON: 开启

        :return: The status of this BatchSwitchesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchSwitchesRequest.

        开关状态 - OFF: 关闭 - ON: 开启

        :param status: The status of this BatchSwitchesRequest.
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
        if not isinstance(other, BatchSwitchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
