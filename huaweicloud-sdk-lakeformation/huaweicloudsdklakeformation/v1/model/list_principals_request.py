# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrincipalsRequest:

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
        'principal_pattern': 'str',
        'limit': 'int',
        'marker': 'str',
        'reverse_page': 'bool',
        'role_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'principal_pattern': 'principal_pattern',
        'limit': 'limit',
        'marker': 'marker',
        'reverse_page': 'reverse_page',
        'role_name': 'role_name'
    }

    def __init__(self, instance_id=None, principal_pattern=None, limit=None, marker=None, reverse_page=None, role_name=None):
        """ListPrincipalsRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param principal_pattern: 模糊匹配主体名称。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~49个字符。
        :type principal_pattern: str
        :param limit: 查询返回条数。默认值为100。最小值为1，最大值为1000。
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0，最大长度为1024。
        :type marker: str
        :param reverse_page: 是否查询上一页。默认为false。
        :type reverse_page: bool
        :param role_name: 角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。
        :type role_name: str
        """
        
        

        self._instance_id = None
        self._principal_pattern = None
        self._limit = None
        self._marker = None
        self._reverse_page = None
        self._role_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if principal_pattern is not None:
            self.principal_pattern = principal_pattern
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if reverse_page is not None:
            self.reverse_page = reverse_page
        self.role_name = role_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPrincipalsRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListPrincipalsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPrincipalsRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListPrincipalsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def principal_pattern(self):
        """Gets the principal_pattern of this ListPrincipalsRequest.

        模糊匹配主体名称。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~49个字符。

        :return: The principal_pattern of this ListPrincipalsRequest.
        :rtype: str
        """
        return self._principal_pattern

    @principal_pattern.setter
    def principal_pattern(self, principal_pattern):
        """Sets the principal_pattern of this ListPrincipalsRequest.

        模糊匹配主体名称。只能包含中文、字母、数字和_|*.-特殊字符，且长度为1~49个字符。

        :param principal_pattern: The principal_pattern of this ListPrincipalsRequest.
        :type principal_pattern: str
        """
        self._principal_pattern = principal_pattern

    @property
    def limit(self):
        """Gets the limit of this ListPrincipalsRequest.

        查询返回条数。默认值为100。最小值为1，最大值为1000。

        :return: The limit of this ListPrincipalsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPrincipalsRequest.

        查询返回条数。默认值为100。最小值为1，最大值为1000。

        :param limit: The limit of this ListPrincipalsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPrincipalsRequest.

        查询的起始记录ID。最小长度为0，最大长度为1024。

        :return: The marker of this ListPrincipalsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPrincipalsRequest.

        查询的起始记录ID。最小长度为0，最大长度为1024。

        :param marker: The marker of this ListPrincipalsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def reverse_page(self):
        """Gets the reverse_page of this ListPrincipalsRequest.

        是否查询上一页。默认为false。

        :return: The reverse_page of this ListPrincipalsRequest.
        :rtype: bool
        """
        return self._reverse_page

    @reverse_page.setter
    def reverse_page(self, reverse_page):
        """Sets the reverse_page of this ListPrincipalsRequest.

        是否查询上一页。默认为false。

        :param reverse_page: The reverse_page of this ListPrincipalsRequest.
        :type reverse_page: bool
        """
        self._reverse_page = reverse_page

    @property
    def role_name(self):
        """Gets the role_name of this ListPrincipalsRequest.

        角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。

        :return: The role_name of this ListPrincipalsRequest.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ListPrincipalsRequest.

        角色名称。只能包含字母、数字和下划线，且长度为1~255个字符。

        :param role_name: The role_name of this ListPrincipalsRequest.
        :type role_name: str
        """
        self._role_name = role_name

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
        if not isinstance(other, ListPrincipalsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
