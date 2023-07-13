# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePersonalTemplateStateDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_state': 'int'
    }

    attribute_map = {
        'tpl_state': 'tpl_state'
    }

    def __init__(self, tpl_state=None):
        """UpdatePersonalTemplateStateDataRequest

        The model defined in huaweicloud sdk

        :param tpl_state: 状态。 - 0：禁用 - 1：启用 
        :type tpl_state: int
        """
        
        

        self._tpl_state = None
        self.discriminator = None

        if tpl_state is not None:
            self.tpl_state = tpl_state

    @property
    def tpl_state(self):
        """Gets the tpl_state of this UpdatePersonalTemplateStateDataRequest.

        状态。 - 0：禁用 - 1：启用 

        :return: The tpl_state of this UpdatePersonalTemplateStateDataRequest.
        :rtype: int
        """
        return self._tpl_state

    @tpl_state.setter
    def tpl_state(self, tpl_state):
        """Sets the tpl_state of this UpdatePersonalTemplateStateDataRequest.

        状态。 - 0：禁用 - 1：启用 

        :param tpl_state: The tpl_state of this UpdatePersonalTemplateStateDataRequest.
        :type tpl_state: int
        """
        self._tpl_state = tpl_state

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
        if not isinstance(other, UpdatePersonalTemplateStateDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
