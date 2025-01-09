# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreBatchAttachInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[AttachInstancesDesktopInfo]',
        'users': 'list[AttachInstancesUserInfo]',
        'assign_model': 'AssignModelInfo'
    }

    attribute_map = {
        'desktops': 'desktops',
        'users': 'users',
        'assign_model': 'assign_model'
    }

    def __init__(self, desktops=None, users=None, assign_model=None):
        """PreBatchAttachInstancesReq

        The model defined in huaweicloud sdk

        :param desktops: 桌面信息列表。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        :param users: 用户信息列表。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        :param assign_model: 
        :type assign_model: :class:`huaweicloudsdkworkspace.v2.AssignModelInfo`
        """
        
        

        self._desktops = None
        self._users = None
        self._assign_model = None
        self.discriminator = None

        if desktops is not None:
            self.desktops = desktops
        if users is not None:
            self.users = users
        if assign_model is not None:
            self.assign_model = assign_model

    @property
    def desktops(self):
        """Gets the desktops of this PreBatchAttachInstancesReq.

        桌面信息列表。

        :return: The desktops of this PreBatchAttachInstancesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this PreBatchAttachInstancesReq.

        桌面信息列表。

        :param desktops: The desktops of this PreBatchAttachInstancesReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        self._desktops = desktops

    @property
    def users(self):
        """Gets the users of this PreBatchAttachInstancesReq.

        用户信息列表。

        :return: The users of this PreBatchAttachInstancesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this PreBatchAttachInstancesReq.

        用户信息列表。

        :param users: The users of this PreBatchAttachInstancesReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._users = users

    @property
    def assign_model(self):
        """Gets the assign_model of this PreBatchAttachInstancesReq.

        :return: The assign_model of this PreBatchAttachInstancesReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssignModelInfo`
        """
        return self._assign_model

    @assign_model.setter
    def assign_model(self, assign_model):
        """Sets the assign_model of this PreBatchAttachInstancesReq.

        :param assign_model: The assign_model of this PreBatchAttachInstancesReq.
        :type assign_model: :class:`huaweicloudsdkworkspace.v2.AssignModelInfo`
        """
        self._assign_model = assign_model

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
        if not isinstance(other, PreBatchAttachInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
