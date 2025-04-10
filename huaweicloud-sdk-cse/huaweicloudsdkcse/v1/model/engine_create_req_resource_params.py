# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineCreateReqResourceParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_auto_renew': 'int'
    }

    attribute_map = {
        'is_auto_renew': 'isAutoRenew'
    }

    def __init__(self, is_auto_renew=None):
        r"""EngineCreateReqResourceParams

        The model defined in huaweicloud sdk

        :param is_auto_renew: 是否自动刷新
        :type is_auto_renew: int
        """
        
        

        self._is_auto_renew = None
        self.discriminator = None

        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this EngineCreateReqResourceParams.

        是否自动刷新

        :return: The is_auto_renew of this EngineCreateReqResourceParams.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this EngineCreateReqResourceParams.

        是否自动刷新

        :param is_auto_renew: The is_auto_renew of this EngineCreateReqResourceParams.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

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
        if not isinstance(other, EngineCreateReqResourceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
