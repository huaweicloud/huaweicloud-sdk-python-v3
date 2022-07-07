# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HaConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ha_type': 'str',
        'active_standby_config': 'ActiveStandbyConfigDTO'
    }

    attribute_map = {
        'ha_type': 'ha_type',
        'active_standby_config': 'active_standby_config'
    }

    def __init__(self, ha_type=None, active_standby_config=None):
        """HaConfigDTO

        The model defined in huaweicloud sdk

        :param ha_type: 节点高可用类型双活或者主备
        :type ha_type: str
        :param active_standby_config: 
        :type active_standby_config: :class:`huaweicloudsdkiotedge.v2.ActiveStandbyConfigDTO`
        """
        
        

        self._ha_type = None
        self._active_standby_config = None
        self.discriminator = None

        if ha_type is not None:
            self.ha_type = ha_type
        if active_standby_config is not None:
            self.active_standby_config = active_standby_config

    @property
    def ha_type(self):
        """Gets the ha_type of this HaConfigDTO.

        节点高可用类型双活或者主备

        :return: The ha_type of this HaConfigDTO.
        :rtype: str
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        """Sets the ha_type of this HaConfigDTO.

        节点高可用类型双活或者主备

        :param ha_type: The ha_type of this HaConfigDTO.
        :type ha_type: str
        """
        self._ha_type = ha_type

    @property
    def active_standby_config(self):
        """Gets the active_standby_config of this HaConfigDTO.


        :return: The active_standby_config of this HaConfigDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ActiveStandbyConfigDTO`
        """
        return self._active_standby_config

    @active_standby_config.setter
    def active_standby_config(self, active_standby_config):
        """Sets the active_standby_config of this HaConfigDTO.


        :param active_standby_config: The active_standby_config of this HaConfigDTO.
        :type active_standby_config: :class:`huaweicloudsdkiotedge.v2.ActiveStandbyConfigDTO`
        """
        self._active_standby_config = active_standby_config

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
        if not isinstance(other, HaConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
