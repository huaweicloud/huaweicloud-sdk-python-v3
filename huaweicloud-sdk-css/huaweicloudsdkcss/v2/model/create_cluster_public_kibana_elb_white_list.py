# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterPublicKibanaElbWhiteList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'white_list': 'str',
        'enable_white_list': 'bool'
    }

    attribute_map = {
        'white_list': 'whiteList',
        'enable_white_list': 'enableWhiteList'
    }

    def __init__(self, white_list=None, enable_white_list=None):
        r"""CreateClusterPublicKibanaElbWhiteList

        The model defined in huaweicloud sdk

        :param white_list: 白名单。需要添加白名单的网段或ip，以逗号隔开，不可重复。
        :type white_list: str
        :param enable_white_list: 是否开启kibana访问控制。
        :type enable_white_list: bool
        """
        
        

        self._white_list = None
        self._enable_white_list = None
        self.discriminator = None

        self.white_list = white_list
        self.enable_white_list = enable_white_list

    @property
    def white_list(self):
        r"""Gets the white_list of this CreateClusterPublicKibanaElbWhiteList.

        白名单。需要添加白名单的网段或ip，以逗号隔开，不可重复。

        :return: The white_list of this CreateClusterPublicKibanaElbWhiteList.
        :rtype: str
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        r"""Sets the white_list of this CreateClusterPublicKibanaElbWhiteList.

        白名单。需要添加白名单的网段或ip，以逗号隔开，不可重复。

        :param white_list: The white_list of this CreateClusterPublicKibanaElbWhiteList.
        :type white_list: str
        """
        self._white_list = white_list

    @property
    def enable_white_list(self):
        r"""Gets the enable_white_list of this CreateClusterPublicKibanaElbWhiteList.

        是否开启kibana访问控制。

        :return: The enable_white_list of this CreateClusterPublicKibanaElbWhiteList.
        :rtype: bool
        """
        return self._enable_white_list

    @enable_white_list.setter
    def enable_white_list(self, enable_white_list):
        r"""Sets the enable_white_list of this CreateClusterPublicKibanaElbWhiteList.

        是否开启kibana访问控制。

        :param enable_white_list: The enable_white_list of this CreateClusterPublicKibanaElbWhiteList.
        :type enable_white_list: bool
        """
        self._enable_white_list = enable_white_list

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
        if not isinstance(other, CreateClusterPublicKibanaElbWhiteList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
