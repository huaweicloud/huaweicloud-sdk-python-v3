# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRolesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'user_name': 'str',
        'body': 'list[RoleInfoInput]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user_name': 'user_name',
        'body': 'body'
    }

    def __init__(self, instance_id=None, user_name=None, body=None):
        r"""AssociateRolesRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param user_name: 用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。
        :type user_name: str
        :param body: Body of the AssociateRolesRequest
        :type body: list[:class:`huaweicloudsdklakeformation.v1.RoleInfoInput`]
        """
        
        

        self._instance_id = None
        self._user_name = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.user_name = user_name
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AssociateRolesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this AssociateRolesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AssociateRolesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this AssociateRolesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        r"""Gets the user_name of this AssociateRolesRequest.

        用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。

        :return: The user_name of this AssociateRolesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AssociateRolesRequest.

        用户名。只能包含字母、数字、下划线和中划线，且长度为1~256个字符。

        :param user_name: The user_name of this AssociateRolesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def body(self):
        r"""Gets the body of this AssociateRolesRequest.

        :return: The body of this AssociateRolesRequest.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.RoleInfoInput`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AssociateRolesRequest.

        :param body: The body of this AssociateRolesRequest.
        :type body: list[:class:`huaweicloudsdklakeformation.v1.RoleInfoInput`]
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
        if not isinstance(other, AssociateRolesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
