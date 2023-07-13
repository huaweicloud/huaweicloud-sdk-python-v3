# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoEnlargePolicyResponse(SdkResponse):

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
        """ShowAutoEnlargePolicyResponse

        The model defined in huaweicloud sdk

        :param switch_option: 是否已开启自动扩容，true为开启
        :type switch_option: bool
        :param limit_size: 扩容上限，单位GB
        :type limit_size: int
        :param trigger_threshold: 可用空间百分比，小于等于此值或者10GB时触发扩容
        :type trigger_threshold: int
        """
        
        super(ShowAutoEnlargePolicyResponse, self).__init__()

        self._switch_option = None
        self._limit_size = None
        self._trigger_threshold = None
        self.discriminator = None

        if switch_option is not None:
            self.switch_option = switch_option
        if limit_size is not None:
            self.limit_size = limit_size
        if trigger_threshold is not None:
            self.trigger_threshold = trigger_threshold

    @property
    def switch_option(self):
        """Gets the switch_option of this ShowAutoEnlargePolicyResponse.

        是否已开启自动扩容，true为开启

        :return: The switch_option of this ShowAutoEnlargePolicyResponse.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        """Sets the switch_option of this ShowAutoEnlargePolicyResponse.

        是否已开启自动扩容，true为开启

        :param switch_option: The switch_option of this ShowAutoEnlargePolicyResponse.
        :type switch_option: bool
        """
        self._switch_option = switch_option

    @property
    def limit_size(self):
        """Gets the limit_size of this ShowAutoEnlargePolicyResponse.

        扩容上限，单位GB

        :return: The limit_size of this ShowAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._limit_size

    @limit_size.setter
    def limit_size(self, limit_size):
        """Sets the limit_size of this ShowAutoEnlargePolicyResponse.

        扩容上限，单位GB

        :param limit_size: The limit_size of this ShowAutoEnlargePolicyResponse.
        :type limit_size: int
        """
        self._limit_size = limit_size

    @property
    def trigger_threshold(self):
        """Gets the trigger_threshold of this ShowAutoEnlargePolicyResponse.

        可用空间百分比，小于等于此值或者10GB时触发扩容

        :return: The trigger_threshold of this ShowAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._trigger_threshold

    @trigger_threshold.setter
    def trigger_threshold(self, trigger_threshold):
        """Sets the trigger_threshold of this ShowAutoEnlargePolicyResponse.

        可用空间百分比，小于等于此值或者10GB时触发扩容

        :param trigger_threshold: The trigger_threshold of this ShowAutoEnlargePolicyResponse.
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
        if not isinstance(other, ShowAutoEnlargePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
