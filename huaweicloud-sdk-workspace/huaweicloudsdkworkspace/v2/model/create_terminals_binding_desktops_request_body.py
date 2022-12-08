# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTerminalsBindingDesktopsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bind_list': 'list[CreateTerminalsBindingDesktopsInfo]'
    }

    attribute_map = {
        'bind_list': 'bind_list'
    }

    def __init__(self, bind_list=None):
        """CreateTerminalsBindingDesktopsRequestBody

        The model defined in huaweicloud sdk

        :param bind_list: 需要新增的MAC绑定VM策略信息列表
        :type bind_list: list[:class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsInfo`]
        """
        
        

        self._bind_list = None
        self.discriminator = None

        if bind_list is not None:
            self.bind_list = bind_list

    @property
    def bind_list(self):
        """Gets the bind_list of this CreateTerminalsBindingDesktopsRequestBody.

        需要新增的MAC绑定VM策略信息列表

        :return: The bind_list of this CreateTerminalsBindingDesktopsRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsInfo`]
        """
        return self._bind_list

    @bind_list.setter
    def bind_list(self, bind_list):
        """Sets the bind_list of this CreateTerminalsBindingDesktopsRequestBody.

        需要新增的MAC绑定VM策略信息列表

        :param bind_list: The bind_list of this CreateTerminalsBindingDesktopsRequestBody.
        :type bind_list: list[:class:`huaweicloudsdkworkspace.v2.CreateTerminalsBindingDesktopsInfo`]
        """
        self._bind_list = bind_list

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
        if not isinstance(other, CreateTerminalsBindingDesktopsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
