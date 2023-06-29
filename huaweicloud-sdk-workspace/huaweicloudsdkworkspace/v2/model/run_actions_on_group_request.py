# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunActionsOnGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'body': 'ActionsOfUsersInGroupRequest'
    }

    attribute_map = {
        'group_id': 'group_id',
        'body': 'body'
    }

    def __init__(self, group_id=None, body=None):
        """RunActionsOnGroupRequest

        The model defined in huaweicloud sdk

        :param group_id: 桌面用户组ID。
        :type group_id: str
        :param body: Body of the RunActionsOnGroupRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.ActionsOfUsersInGroupRequest`
        """
        
        

        self._group_id = None
        self._body = None
        self.discriminator = None

        self.group_id = group_id
        if body is not None:
            self.body = body

    @property
    def group_id(self):
        """Gets the group_id of this RunActionsOnGroupRequest.

        桌面用户组ID。

        :return: The group_id of this RunActionsOnGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this RunActionsOnGroupRequest.

        桌面用户组ID。

        :param group_id: The group_id of this RunActionsOnGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body(self):
        """Gets the body of this RunActionsOnGroupRequest.

        :return: The body of this RunActionsOnGroupRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ActionsOfUsersInGroupRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RunActionsOnGroupRequest.

        :param body: The body of this RunActionsOnGroupRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.ActionsOfUsersInGroupRequest`
        """
        self._body = body

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
        if not isinstance(other, RunActionsOnGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
