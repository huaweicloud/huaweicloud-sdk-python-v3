# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVifPeer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'remote_ep_group': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'remote_ep_group': 'remote_ep_group'
    }

    def __init__(self, name=None, description=None, remote_ep_group=None):
        r"""UpdateVifPeer

        The model defined in huaweicloud sdk

        :param name: VIF对等体名字
        :type name: str
        :param description: VIF对等体名字描述信息
        :type description: str
        :param remote_ep_group: 远端子网列表，记录用户侧的cidrs
        :type remote_ep_group: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._remote_ep_group = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if remote_ep_group is not None:
            self.remote_ep_group = remote_ep_group

    @property
    def name(self):
        r"""Gets the name of this UpdateVifPeer.

        VIF对等体名字

        :return: The name of this UpdateVifPeer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateVifPeer.

        VIF对等体名字

        :param name: The name of this UpdateVifPeer.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateVifPeer.

        VIF对等体名字描述信息

        :return: The description of this UpdateVifPeer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateVifPeer.

        VIF对等体名字描述信息

        :param description: The description of this UpdateVifPeer.
        :type description: str
        """
        self._description = description

    @property
    def remote_ep_group(self):
        r"""Gets the remote_ep_group of this UpdateVifPeer.

        远端子网列表，记录用户侧的cidrs

        :return: The remote_ep_group of this UpdateVifPeer.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        r"""Sets the remote_ep_group of this UpdateVifPeer.

        远端子网列表，记录用户侧的cidrs

        :param remote_ep_group: The remote_ep_group of this UpdateVifPeer.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

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
        if not isinstance(other, UpdateVifPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
