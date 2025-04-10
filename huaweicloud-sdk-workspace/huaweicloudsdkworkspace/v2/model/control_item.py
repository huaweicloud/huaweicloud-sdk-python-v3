# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ControlItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'desktop_status': 'str',
        'pool_id': 'str',
        'attach_user_infos': 'list[AttachInstancesUserInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'desktop_status': 'desktop_status',
        'pool_id': 'pool_id',
        'attach_user_infos': 'attach_user_infos'
    }

    def __init__(self, desktop_id=None, desktop_name=None, desktop_status=None, pool_id=None, attach_user_infos=None):
        r"""ControlItem

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param desktop_status: 桌面状态。
        :type desktop_status: str
        :param pool_id: 池id。
        :type pool_id: str
        :param attach_user_infos: 桌面已分配的用户信息列表。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._desktop_status = None
        self._pool_id = None
        self._attach_user_infos = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_status is not None:
            self.desktop_status = desktop_status
        if pool_id is not None:
            self.pool_id = pool_id
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ControlItem.

        桌面id。

        :return: The desktop_id of this ControlItem.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ControlItem.

        桌面id。

        :param desktop_id: The desktop_id of this ControlItem.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ControlItem.

        桌面名称。

        :return: The desktop_name of this ControlItem.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ControlItem.

        桌面名称。

        :param desktop_name: The desktop_name of this ControlItem.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_status(self):
        r"""Gets the desktop_status of this ControlItem.

        桌面状态。

        :return: The desktop_status of this ControlItem.
        :rtype: str
        """
        return self._desktop_status

    @desktop_status.setter
    def desktop_status(self, desktop_status):
        r"""Sets the desktop_status of this ControlItem.

        桌面状态。

        :param desktop_status: The desktop_status of this ControlItem.
        :type desktop_status: str
        """
        self._desktop_status = desktop_status

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ControlItem.

        池id。

        :return: The pool_id of this ControlItem.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ControlItem.

        池id。

        :param pool_id: The pool_id of this ControlItem.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def attach_user_infos(self):
        r"""Gets the attach_user_infos of this ControlItem.

        桌面已分配的用户信息列表。

        :return: The attach_user_infos of this ControlItem.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        r"""Sets the attach_user_infos of this ControlItem.

        桌面已分配的用户信息列表。

        :param attach_user_infos: The attach_user_infos of this ControlItem.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._attach_user_infos = attach_user_infos

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
        if not isinstance(other, ControlItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
