# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNamespaceResponse(SdkResponse):

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
        'creator_name': 'str',
        'auth': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creator_name': 'creator_name',
        'auth': 'auth'
    }

    def __init__(self, id=None, name=None, creator_name=None, auth=None):
        """ShowNamespaceResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type name: str
        :param creator_name: IAM用户名
        :type creator_name: str
        :param auth: 用户权限。7表示管理权限，3表示编辑权限，1表示读取权限。
        :type auth: int
        """
        
        super(ShowNamespaceResponse, self).__init__()

        self._id = None
        self._name = None
        self._creator_name = None
        self._auth = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if creator_name is not None:
            self.creator_name = creator_name
        if auth is not None:
            self.auth = auth

    @property
    def id(self):
        """Gets the id of this ShowNamespaceResponse.

        id

        :return: The id of this ShowNamespaceResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowNamespaceResponse.

        id

        :param id: The id of this ShowNamespaceResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowNamespaceResponse.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The name of this ShowNamespaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowNamespaceResponse.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param name: The name of this ShowNamespaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowNamespaceResponse.

        IAM用户名

        :return: The creator_name of this ShowNamespaceResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowNamespaceResponse.

        IAM用户名

        :param creator_name: The creator_name of this ShowNamespaceResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def auth(self):
        """Gets the auth of this ShowNamespaceResponse.

        用户权限。7表示管理权限，3表示编辑权限，1表示读取权限。

        :return: The auth of this ShowNamespaceResponse.
        :rtype: int
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this ShowNamespaceResponse.

        用户权限。7表示管理权限，3表示编辑权限，1表示读取权限。

        :param auth: The auth of this ShowNamespaceResponse.
        :type auth: int
        """
        self._auth = auth

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
        if not isinstance(other, ShowNamespaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
