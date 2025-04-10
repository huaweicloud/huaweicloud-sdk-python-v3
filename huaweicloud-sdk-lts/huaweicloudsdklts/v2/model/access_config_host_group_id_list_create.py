# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigHostGroupIdListCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_group_id_list': 'list[str]'
    }

    attribute_map = {
        'host_group_id_list': 'host_group_id_list'
    }

    def __init__(self, host_group_id_list=None):
        r"""AccessConfigHostGroupIdListCreate

        The model defined in huaweicloud sdk

        :param host_group_id_list: 主机组ID列表
        :type host_group_id_list: list[str]
        """
        
        

        self._host_group_id_list = None
        self.discriminator = None

        self.host_group_id_list = host_group_id_list

    @property
    def host_group_id_list(self):
        r"""Gets the host_group_id_list of this AccessConfigHostGroupIdListCreate.

        主机组ID列表

        :return: The host_group_id_list of this AccessConfigHostGroupIdListCreate.
        :rtype: list[str]
        """
        return self._host_group_id_list

    @host_group_id_list.setter
    def host_group_id_list(self, host_group_id_list):
        r"""Sets the host_group_id_list of this AccessConfigHostGroupIdListCreate.

        主机组ID列表

        :param host_group_id_list: The host_group_id_list of this AccessConfigHostGroupIdListCreate.
        :type host_group_id_list: list[str]
        """
        self._host_group_id_list = host_group_id_list

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
        if not isinstance(other, AccessConfigHostGroupIdListCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
