# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceEngineDistributionListInstanceInfos:

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
        'num': 'int'
    }

    attribute_map = {
        'status': 'status',
        'num': 'num'
    }

    def __init__(self, status=None, num=None):
        r"""InstanceEngineDistributionListInstanceInfos

        The model defined in huaweicloud sdk

        :param status: 实例状态
        :type status: str
        :param num: 实例数量
        :type num: int
        """
        
        

        self._status = None
        self._num = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if num is not None:
            self.num = num

    @property
    def status(self):
        r"""Gets the status of this InstanceEngineDistributionListInstanceInfos.

        实例状态

        :return: The status of this InstanceEngineDistributionListInstanceInfos.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceEngineDistributionListInstanceInfos.

        实例状态

        :param status: The status of this InstanceEngineDistributionListInstanceInfos.
        :type status: str
        """
        self._status = status

    @property
    def num(self):
        r"""Gets the num of this InstanceEngineDistributionListInstanceInfos.

        实例数量

        :return: The num of this InstanceEngineDistributionListInstanceInfos.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this InstanceEngineDistributionListInstanceInfos.

        实例数量

        :param num: The num of this InstanceEngineDistributionListInstanceInfos.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, InstanceEngineDistributionListInstanceInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
