# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_user_id': 'str',
        'role': 'str',
        'settings': 'UserSettingDto'
    }

    attribute_map = {
        'iam_user_id': 'iam_user_id',
        'role': 'role',
        'settings': 'settings'
    }

    def __init__(self, iam_user_id=None, role=None, settings=None):
        r"""ImportUserReq

        The model defined in huaweicloud sdk

        :param iam_user_id: IAM用户id
        :type iam_user_id: str
        :param role: 角色类型：管理员(ADMIN)、操作者(OPERATOR)
        :type role: str
        :param settings: 
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        
        

        self._iam_user_id = None
        self._role = None
        self._settings = None
        self.discriminator = None

        self.iam_user_id = iam_user_id
        self.role = role
        if settings is not None:
            self.settings = settings

    @property
    def iam_user_id(self):
        r"""Gets the iam_user_id of this ImportUserReq.

        IAM用户id

        :return: The iam_user_id of this ImportUserReq.
        :rtype: str
        """
        return self._iam_user_id

    @iam_user_id.setter
    def iam_user_id(self, iam_user_id):
        r"""Sets the iam_user_id of this ImportUserReq.

        IAM用户id

        :param iam_user_id: The iam_user_id of this ImportUserReq.
        :type iam_user_id: str
        """
        self._iam_user_id = iam_user_id

    @property
    def role(self):
        r"""Gets the role of this ImportUserReq.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :return: The role of this ImportUserReq.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ImportUserReq.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :param role: The role of this ImportUserReq.
        :type role: str
        """
        self._role = role

    @property
    def settings(self):
        r"""Gets the settings of this ImportUserReq.

        :return: The settings of this ImportUserReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        r"""Sets the settings of this ImportUserReq.

        :param settings: The settings of this ImportUserReq.
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        self._settings = settings

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
        if not isinstance(other, ImportUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
