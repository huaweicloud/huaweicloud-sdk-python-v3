# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerModifyAutoEnlargePolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'bool',
        'limit_size': 'int',
        'trigger_threshold': 'int'
    }

    attribute_map = {
        'switch_option': 'switch_option',
        'limit_size': 'limit_size',
        'trigger_threshold': 'trigger_threshold'
    }

    def __init__(self, switch_option=None, limit_size=None, trigger_threshold=None):
        """CustomerModifyAutoEnlargePolicyReq

        The model defined in huaweicloud sdk

        :param switch_option: 是否开启自动扩容,true为开启,false为关闭
        :type switch_option: bool
        :param limit_size: 扩容上限，单位GB, 取值范围40~4000，需要大于等于实例当前存储空间总大小，switch_option为true必填
        :type limit_size: int
        :param trigger_threshold: 可用存储空间百分比，小于等于此值或者10GB时触发扩容，switch_option为true时必填
        :type trigger_threshold: int
        """
        
        

        self._switch_option = None
        self._limit_size = None
        self._trigger_threshold = None
        self.discriminator = None

        self.switch_option = switch_option
        if limit_size is not None:
            self.limit_size = limit_size
        if trigger_threshold is not None:
            self.trigger_threshold = trigger_threshold

    @property
    def switch_option(self):
        """Gets the switch_option of this CustomerModifyAutoEnlargePolicyReq.

        是否开启自动扩容,true为开启,false为关闭

        :return: The switch_option of this CustomerModifyAutoEnlargePolicyReq.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        """Sets the switch_option of this CustomerModifyAutoEnlargePolicyReq.

        是否开启自动扩容,true为开启,false为关闭

        :param switch_option: The switch_option of this CustomerModifyAutoEnlargePolicyReq.
        :type switch_option: bool
        """
        self._switch_option = switch_option

    @property
    def limit_size(self):
        """Gets the limit_size of this CustomerModifyAutoEnlargePolicyReq.

        扩容上限，单位GB, 取值范围40~4000，需要大于等于实例当前存储空间总大小，switch_option为true必填

        :return: The limit_size of this CustomerModifyAutoEnlargePolicyReq.
        :rtype: int
        """
        return self._limit_size

    @limit_size.setter
    def limit_size(self, limit_size):
        """Sets the limit_size of this CustomerModifyAutoEnlargePolicyReq.

        扩容上限，单位GB, 取值范围40~4000，需要大于等于实例当前存储空间总大小，switch_option为true必填

        :param limit_size: The limit_size of this CustomerModifyAutoEnlargePolicyReq.
        :type limit_size: int
        """
        self._limit_size = limit_size

    @property
    def trigger_threshold(self):
        """Gets the trigger_threshold of this CustomerModifyAutoEnlargePolicyReq.

        可用存储空间百分比，小于等于此值或者10GB时触发扩容，switch_option为true时必填

        :return: The trigger_threshold of this CustomerModifyAutoEnlargePolicyReq.
        :rtype: int
        """
        return self._trigger_threshold

    @trigger_threshold.setter
    def trigger_threshold(self, trigger_threshold):
        """Sets the trigger_threshold of this CustomerModifyAutoEnlargePolicyReq.

        可用存储空间百分比，小于等于此值或者10GB时触发扩容，switch_option为true时必填

        :param trigger_threshold: The trigger_threshold of this CustomerModifyAutoEnlargePolicyReq.
        :type trigger_threshold: int
        """
        self._trigger_threshold = trigger_threshold

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
        if not isinstance(other, CustomerModifyAutoEnlargePolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
