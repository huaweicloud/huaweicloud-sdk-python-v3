# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserRepositoryAuthResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'self_auth': 'UserAuth',
        'others_auths': 'list[UserAuth]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'self_auth': 'self_auth',
        'others_auths': 'others_auths'
    }

    def __init__(self, id=None, name=None, self_auth=None, others_auths=None):
        r"""ShowUserRepositoryAuthResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type name: str
        :param self_auth: 
        :type self_auth: :class:`huaweicloudsdkswr.v2.UserAuth`
        :param others_auths: 其他用户的权限
        :type others_auths: list[:class:`huaweicloudsdkswr.v2.UserAuth`]
        """
        
        super(ShowUserRepositoryAuthResponse, self).__init__()

        self._id = None
        self._name = None
        self._self_auth = None
        self._others_auths = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if self_auth is not None:
            self.self_auth = self_auth
        if others_auths is not None:
            self.others_auths = others_auths

    @property
    def id(self):
        r"""Gets the id of this ShowUserRepositoryAuthResponse.

        id

        :return: The id of this ShowUserRepositoryAuthResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowUserRepositoryAuthResponse.

        id

        :param id: The id of this ShowUserRepositoryAuthResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowUserRepositoryAuthResponse.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The name of this ShowUserRepositoryAuthResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowUserRepositoryAuthResponse.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param name: The name of this ShowUserRepositoryAuthResponse.
        :type name: str
        """
        self._name = name

    @property
    def self_auth(self):
        r"""Gets the self_auth of this ShowUserRepositoryAuthResponse.

        :return: The self_auth of this ShowUserRepositoryAuthResponse.
        :rtype: :class:`huaweicloudsdkswr.v2.UserAuth`
        """
        return self._self_auth

    @self_auth.setter
    def self_auth(self, self_auth):
        r"""Sets the self_auth of this ShowUserRepositoryAuthResponse.

        :param self_auth: The self_auth of this ShowUserRepositoryAuthResponse.
        :type self_auth: :class:`huaweicloudsdkswr.v2.UserAuth`
        """
        self._self_auth = self_auth

    @property
    def others_auths(self):
        r"""Gets the others_auths of this ShowUserRepositoryAuthResponse.

        其他用户的权限

        :return: The others_auths of this ShowUserRepositoryAuthResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.UserAuth`]
        """
        return self._others_auths

    @others_auths.setter
    def others_auths(self, others_auths):
        r"""Sets the others_auths of this ShowUserRepositoryAuthResponse.

        其他用户的权限

        :param others_auths: The others_auths of this ShowUserRepositoryAuthResponse.
        :type others_auths: list[:class:`huaweicloudsdkswr.v2.UserAuth`]
        """
        self._others_auths = others_auths

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
        if not isinstance(other, ShowUserRepositoryAuthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
