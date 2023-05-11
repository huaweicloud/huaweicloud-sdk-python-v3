# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency': 'str',
        'identifier_type': 'str',
        'identifiers': 'list[str]',
        'agency_id': 'str'
    }

    attribute_map = {
        'agency': 'agency',
        'identifier_type': 'identifier_type',
        'identifiers': 'identifiers',
        'agency_id': 'agency_id'
    }

    def __init__(self, agency=None, identifier_type=None, identifiers=None, agency_id=None):
        """AgencyMapping

        The model defined in huaweicloud sdk

        :param agency: 该映射绑定的IAM委托名称。
        :type agency: str
        :param identifier_type: 委托类型，分为“User”和“Group”两种。 - User表示该映射关系为针对用户的映射，identifiers中填写用户名称列表。 - Group表示该映射关系为针对用户组的映射，identifiers中填写用户组名称列表。
        :type identifier_type: str
        :param identifiers: IAM委托映射的用户（组）名称列表。请前往IAM，单击“用户（组）”按钮，获取用户（组）名称列表。
        :type identifiers: list[str]
        :param agency_id: 该映射关系绑定的委托的的唯一标识码。请前往IAM，单击“委托”按钮，进入委托页面，将鼠标放置委托名称上，在弹窗中获取委托唯一标识码。
        :type agency_id: str
        """
        
        

        self._agency = None
        self._identifier_type = None
        self._identifiers = None
        self._agency_id = None
        self.discriminator = None

        self.agency = agency
        self.identifier_type = identifier_type
        self.identifiers = identifiers
        self.agency_id = agency_id

    @property
    def agency(self):
        """Gets the agency of this AgencyMapping.

        该映射绑定的IAM委托名称。

        :return: The agency of this AgencyMapping.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this AgencyMapping.

        该映射绑定的IAM委托名称。

        :param agency: The agency of this AgencyMapping.
        :type agency: str
        """
        self._agency = agency

    @property
    def identifier_type(self):
        """Gets the identifier_type of this AgencyMapping.

        委托类型，分为“User”和“Group”两种。 - User表示该映射关系为针对用户的映射，identifiers中填写用户名称列表。 - Group表示该映射关系为针对用户组的映射，identifiers中填写用户组名称列表。

        :return: The identifier_type of this AgencyMapping.
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this AgencyMapping.

        委托类型，分为“User”和“Group”两种。 - User表示该映射关系为针对用户的映射，identifiers中填写用户名称列表。 - Group表示该映射关系为针对用户组的映射，identifiers中填写用户组名称列表。

        :param identifier_type: The identifier_type of this AgencyMapping.
        :type identifier_type: str
        """
        self._identifier_type = identifier_type

    @property
    def identifiers(self):
        """Gets the identifiers of this AgencyMapping.

        IAM委托映射的用户（组）名称列表。请前往IAM，单击“用户（组）”按钮，获取用户（组）名称列表。

        :return: The identifiers of this AgencyMapping.
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this AgencyMapping.

        IAM委托映射的用户（组）名称列表。请前往IAM，单击“用户（组）”按钮，获取用户（组）名称列表。

        :param identifiers: The identifiers of this AgencyMapping.
        :type identifiers: list[str]
        """
        self._identifiers = identifiers

    @property
    def agency_id(self):
        """Gets the agency_id of this AgencyMapping.

        该映射关系绑定的委托的的唯一标识码。请前往IAM，单击“委托”按钮，进入委托页面，将鼠标放置委托名称上，在弹窗中获取委托唯一标识码。

        :return: The agency_id of this AgencyMapping.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this AgencyMapping.

        该映射关系绑定的委托的的唯一标识码。请前往IAM，单击“委托”按钮，进入委托页面，将鼠标放置委托名称上，在弹窗中获取委托唯一标识码。

        :param agency_id: The agency_id of this AgencyMapping.
        :type agency_id: str
        """
        self._agency_id = agency_id

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
        if not isinstance(other, AgencyMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
