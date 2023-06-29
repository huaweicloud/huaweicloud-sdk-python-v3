# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_access_agent': 'bool'
    }

    attribute_map = {
        'update_access_agent': 'update_access_agent'
    }

    def __init__(self, update_access_agent=None):
        """ReinstallServerReq

        The model defined in huaweicloud sdk

        :param update_access_agent: 是否自动升级hda版本
        :type update_access_agent: bool
        """
        
        

        self._update_access_agent = None
        self.discriminator = None

        if update_access_agent is not None:
            self.update_access_agent = update_access_agent

    @property
    def update_access_agent(self):
        """Gets the update_access_agent of this ReinstallServerReq.

        是否自动升级hda版本

        :return: The update_access_agent of this ReinstallServerReq.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        """Sets the update_access_agent of this ReinstallServerReq.

        是否自动升级hda版本

        :param update_access_agent: The update_access_agent of this ReinstallServerReq.
        :type update_access_agent: bool
        """
        self._update_access_agent = update_access_agent

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
        if not isinstance(other, ReinstallServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
