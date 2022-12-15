# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulnerabilitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'type': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, type=None, vul_id=None, vul_name=None, limit=None, offset=None):
        """ListVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业租户ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞
        :type type: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._vul_id = None
        self._vul_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVulnerabilitiesRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVulnerabilitiesRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this ListVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞

        :return: The type of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞

        :param type: The type of this ListVulnerabilitiesRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_id(self):
        """Gets the vul_id of this ListVulnerabilitiesRequest.

        漏洞ID

        :return: The vul_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this ListVulnerabilitiesRequest.

        漏洞ID

        :param vul_id: The vul_id of this ListVulnerabilitiesRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        """Gets the vul_name of this ListVulnerabilitiesRequest.

        漏洞名称

        :return: The vul_name of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        """Sets the vul_name of this ListVulnerabilitiesRequest.

        漏洞名称

        :param vul_name: The vul_name of this ListVulnerabilitiesRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def limit(self):
        """Gets the limit of this ListVulnerabilitiesRequest.

        每页显示个数

        :return: The limit of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVulnerabilitiesRequest.

        每页显示个数

        :param limit: The limit of this ListVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
