# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'vpc_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, marker=None, vpc_id=None, enterprise_project_id=None):
        """ListSecurityGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param vpc_id: 按照vpc_id过滤查询
        :type vpc_id: str
        :param enterprise_project_id: 功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的安全组。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的安全组，或者企业项目子账号需要进行安全组列表展示，请传参all_granted_eps。
        :type enterprise_project_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListSecurityGroupsRequest.

        每页返回的个数

        :return: The limit of this ListSecurityGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityGroupsRequest.

        每页返回的个数

        :param limit: The limit of this ListSecurityGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSecurityGroupsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListSecurityGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecurityGroupsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListSecurityGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListSecurityGroupsRequest.

        按照vpc_id过滤查询

        :return: The vpc_id of this ListSecurityGroupsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListSecurityGroupsRequest.

        按照vpc_id过滤查询

        :param vpc_id: The vpc_id of this ListSecurityGroupsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSecurityGroupsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的安全组。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的安全组，或者企业项目子账号需要进行安全组列表展示，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListSecurityGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSecurityGroupsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的安全组。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的安全组，或者企业项目子账号需要进行安全组列表展示，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListSecurityGroupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListSecurityGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
