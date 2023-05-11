# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatePermissionReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_id': 'str',
        'replace': 'bool'
    }

    attribute_map = {
        'permission_id': 'permission_id',
        'replace': 'replace'
    }

    def __init__(self, permission_id=None, replace=None):
        """AssociatePermissionReqBody

        The model defined in huaweicloud sdk

        :param permission_id: 共享资源权限的ID。
        :type permission_id: str
        :param replace: 指定特定的权限替换或绑定到与资源共享实例关联的现有资源类型。设置为\&quot;true\&quot;可将相同的资源类型的权限替换为当前权限。设置为\&quot;false\&quot;将权限绑定到当前资源类型。默认值为\&quot;false\&quot;。资源共享实例中的每个资源类型只能绑定一个权限。如果资源共享实例中已具有指定资源类型的权限，并且将\&quot;replace\&quot;设置为\&quot;false\&quot;，则操作返回错误。这有助于防止意外覆盖权限。
        :type replace: bool
        """
        
        

        self._permission_id = None
        self._replace = None
        self.discriminator = None

        self.permission_id = permission_id
        if replace is not None:
            self.replace = replace

    @property
    def permission_id(self):
        """Gets the permission_id of this AssociatePermissionReqBody.

        共享资源权限的ID。

        :return: The permission_id of this AssociatePermissionReqBody.
        :rtype: str
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        """Sets the permission_id of this AssociatePermissionReqBody.

        共享资源权限的ID。

        :param permission_id: The permission_id of this AssociatePermissionReqBody.
        :type permission_id: str
        """
        self._permission_id = permission_id

    @property
    def replace(self):
        """Gets the replace of this AssociatePermissionReqBody.

        指定特定的权限替换或绑定到与资源共享实例关联的现有资源类型。设置为\"true\"可将相同的资源类型的权限替换为当前权限。设置为\"false\"将权限绑定到当前资源类型。默认值为\"false\"。资源共享实例中的每个资源类型只能绑定一个权限。如果资源共享实例中已具有指定资源类型的权限，并且将\"replace\"设置为\"false\"，则操作返回错误。这有助于防止意外覆盖权限。

        :return: The replace of this AssociatePermissionReqBody.
        :rtype: bool
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        """Sets the replace of this AssociatePermissionReqBody.

        指定特定的权限替换或绑定到与资源共享实例关联的现有资源类型。设置为\"true\"可将相同的资源类型的权限替换为当前权限。设置为\"false\"将权限绑定到当前资源类型。默认值为\"false\"。资源共享实例中的每个资源类型只能绑定一个权限。如果资源共享实例中已具有指定资源类型的权限，并且将\"replace\"设置为\"false\"，则操作返回错误。这有助于防止意外覆盖权限。

        :param replace: The replace of this AssociatePermissionReqBody.
        :type replace: bool
        """
        self._replace = replace

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
        if not isinstance(other, AssociatePermissionReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
