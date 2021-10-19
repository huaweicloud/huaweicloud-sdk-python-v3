# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoutetableInfoError:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bind_failed': 'RoutetableInfoErrorDetial',
        'unbind_failed': 'RoutetableInfoErrorDetial'
    }

    attribute_map = {
        'bind_failed': 'bind_failed',
        'unbind_failed': 'unbind_failed'
    }

    def __init__(self, bind_failed=None, unbind_failed=None):
        """RoutetableInfoError - a model defined in huaweicloud sdk"""
        
        

        self._bind_failed = None
        self._unbind_failed = None
        self.discriminator = None

        if bind_failed is not None:
            self.bind_failed = bind_failed
        if unbind_failed is not None:
            self.unbind_failed = unbind_failed

    @property
    def bind_failed(self):
        """Gets the bind_failed of this RoutetableInfoError.


        :return: The bind_failed of this RoutetableInfoError.
        :rtype: RoutetableInfoErrorDetial
        """
        return self._bind_failed

    @bind_failed.setter
    def bind_failed(self, bind_failed):
        """Sets the bind_failed of this RoutetableInfoError.


        :param bind_failed: The bind_failed of this RoutetableInfoError.
        :type: RoutetableInfoErrorDetial
        """
        self._bind_failed = bind_failed

    @property
    def unbind_failed(self):
        """Gets the unbind_failed of this RoutetableInfoError.


        :return: The unbind_failed of this RoutetableInfoError.
        :rtype: RoutetableInfoErrorDetial
        """
        return self._unbind_failed

    @unbind_failed.setter
    def unbind_failed(self, unbind_failed):
        """Sets the unbind_failed of this RoutetableInfoError.


        :param unbind_failed: The unbind_failed of this RoutetableInfoError.
        :type: RoutetableInfoErrorDetial
        """
        self._unbind_failed = unbind_failed

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
        if not isinstance(other, RoutetableInfoError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
