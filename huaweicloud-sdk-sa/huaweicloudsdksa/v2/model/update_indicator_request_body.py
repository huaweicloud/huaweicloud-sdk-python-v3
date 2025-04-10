# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIndicatorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_flag': 'bool',
        'data_object': 'IndicatorDataObjectDetail'
    }

    attribute_map = {
        'trigger_flag': 'trigger_flag',
        'data_object': 'data_object'
    }

    def __init__(self, trigger_flag=None, data_object=None):
        r"""UpdateIndicatorRequestBody

        The model defined in huaweicloud sdk

        :param trigger_flag: 触发标志
        :type trigger_flag: bool
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        """
        
        

        self._trigger_flag = None
        self._data_object = None
        self.discriminator = None

        if trigger_flag is not None:
            self.trigger_flag = trigger_flag
        if data_object is not None:
            self.data_object = data_object

    @property
    def trigger_flag(self):
        r"""Gets the trigger_flag of this UpdateIndicatorRequestBody.

        触发标志

        :return: The trigger_flag of this UpdateIndicatorRequestBody.
        :rtype: bool
        """
        return self._trigger_flag

    @trigger_flag.setter
    def trigger_flag(self, trigger_flag):
        r"""Sets the trigger_flag of this UpdateIndicatorRequestBody.

        触发标志

        :param trigger_flag: The trigger_flag of this UpdateIndicatorRequestBody.
        :type trigger_flag: bool
        """
        self._trigger_flag = trigger_flag

    @property
    def data_object(self):
        r"""Gets the data_object of this UpdateIndicatorRequestBody.

        :return: The data_object of this UpdateIndicatorRequestBody.
        :rtype: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        r"""Sets the data_object of this UpdateIndicatorRequestBody.

        :param data_object: The data_object of this UpdateIndicatorRequestBody.
        :type data_object: :class:`huaweicloudsdksa.v2.IndicatorDataObjectDetail`
        """
        self._data_object = data_object

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
        if not isinstance(other, UpdateIndicatorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
