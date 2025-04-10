# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopSlowLogTopSlowLogList:

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
        'instance_name': 'str',
        'slow_log_num': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'slow_log_num': 'slow_log_num'
    }

    def __init__(self, instance_id=None, instance_name=None, slow_log_num=None):
        r"""TopSlowLogTopSlowLogList

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例数量
        :type instance_name: str
        :param slow_log_num: 慢SQL数量
        :type slow_log_num: int
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._slow_log_num = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if slow_log_num is not None:
            self.slow_log_num = slow_log_num

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TopSlowLogTopSlowLogList.

        实例ID

        :return: The instance_id of this TopSlowLogTopSlowLogList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TopSlowLogTopSlowLogList.

        实例ID

        :param instance_id: The instance_id of this TopSlowLogTopSlowLogList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this TopSlowLogTopSlowLogList.

        实例数量

        :return: The instance_name of this TopSlowLogTopSlowLogList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this TopSlowLogTopSlowLogList.

        实例数量

        :param instance_name: The instance_name of this TopSlowLogTopSlowLogList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def slow_log_num(self):
        r"""Gets the slow_log_num of this TopSlowLogTopSlowLogList.

        慢SQL数量

        :return: The slow_log_num of this TopSlowLogTopSlowLogList.
        :rtype: int
        """
        return self._slow_log_num

    @slow_log_num.setter
    def slow_log_num(self, slow_log_num):
        r"""Sets the slow_log_num of this TopSlowLogTopSlowLogList.

        慢SQL数量

        :param slow_log_num: The slow_log_num of this TopSlowLogTopSlowLogList.
        :type slow_log_num: int
        """
        self._slow_log_num = slow_log_num

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
        if not isinstance(other, TopSlowLogTopSlowLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
