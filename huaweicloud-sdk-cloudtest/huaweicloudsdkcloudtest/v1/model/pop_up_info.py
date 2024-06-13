# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PopUpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'popup': 'bool',
        'time_limit': 'object'
    }

    attribute_map = {
        'popup': 'popup',
        'time_limit': 'time_limit'
    }

    def __init__(self, popup=None, time_limit=None):
        """PopUpInfo

        The model defined in huaweicloud sdk

        :param popup: 是否弹窗
        :type popup: bool
        :param time_limit: 包周期计费时长上限
        :type time_limit: object
        """
        
        

        self._popup = None
        self._time_limit = None
        self.discriminator = None

        if popup is not None:
            self.popup = popup
        if time_limit is not None:
            self.time_limit = time_limit

    @property
    def popup(self):
        """Gets the popup of this PopUpInfo.

        是否弹窗

        :return: The popup of this PopUpInfo.
        :rtype: bool
        """
        return self._popup

    @popup.setter
    def popup(self, popup):
        """Sets the popup of this PopUpInfo.

        是否弹窗

        :param popup: The popup of this PopUpInfo.
        :type popup: bool
        """
        self._popup = popup

    @property
    def time_limit(self):
        """Gets the time_limit of this PopUpInfo.

        包周期计费时长上限

        :return: The time_limit of this PopUpInfo.
        :rtype: object
        """
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit):
        """Sets the time_limit of this PopUpInfo.

        包周期计费时长上限

        :param time_limit: The time_limit of this PopUpInfo.
        :type time_limit: object
        """
        self._time_limit = time_limit

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
        if not isinstance(other, PopUpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
