# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ViewWorkspaceResponseGrants:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'user_name': 'str',
        'user_type': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_type': 'user_type'
    }

    def __init__(self, user_id=None, user_name=None, user_type=None):
        r"""ViewWorkspaceResponseGrants

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。此参数与user_name必填一个。两者都填优先使用user_id。
        :type user_id: str
        :param user_name: IAM用户名称。此参数与user_id必填一个。
        :type user_name: str
        :param user_type: 参数解释： 授权用户类型。 约束限制： 如果是联邦用户或者委托用户的话必填。 取值范围： IAM:IAM用户, FEDERATE：联邦用户, AGENCY：委托用户。 默认取值： IAM。
        :type user_type: str
        """
        
        

        self._user_id = None
        self._user_name = None
        self._user_type = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type

    @property
    def user_id(self):
        r"""Gets the user_id of this ViewWorkspaceResponseGrants.

        IAM用户ID。此参数与user_name必填一个。两者都填优先使用user_id。

        :return: The user_id of this ViewWorkspaceResponseGrants.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ViewWorkspaceResponseGrants.

        IAM用户ID。此参数与user_name必填一个。两者都填优先使用user_id。

        :param user_id: The user_id of this ViewWorkspaceResponseGrants.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ViewWorkspaceResponseGrants.

        IAM用户名称。此参数与user_id必填一个。

        :return: The user_name of this ViewWorkspaceResponseGrants.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ViewWorkspaceResponseGrants.

        IAM用户名称。此参数与user_id必填一个。

        :param user_name: The user_name of this ViewWorkspaceResponseGrants.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_type(self):
        r"""Gets the user_type of this ViewWorkspaceResponseGrants.

        参数解释： 授权用户类型。 约束限制： 如果是联邦用户或者委托用户的话必填。 取值范围： IAM:IAM用户, FEDERATE：联邦用户, AGENCY：委托用户。 默认取值： IAM。

        :return: The user_type of this ViewWorkspaceResponseGrants.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this ViewWorkspaceResponseGrants.

        参数解释： 授权用户类型。 约束限制： 如果是联邦用户或者委托用户的话必填。 取值范围： IAM:IAM用户, FEDERATE：联邦用户, AGENCY：委托用户。 默认取值： IAM。

        :param user_type: The user_type of this ViewWorkspaceResponseGrants.
        :type user_type: str
        """
        self._user_type = user_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ViewWorkspaceResponseGrants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
