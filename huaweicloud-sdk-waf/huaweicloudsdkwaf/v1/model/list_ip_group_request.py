# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpGroupRequest:

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
        'page': 'int',
        'pagesize': 'int',
        'name': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name',
        'ip': 'ip'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, name=None, ip=None):
        """ListIpGroupRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param page: 页码，默认值为1
        :type page: int
        :param pagesize: 每页的条数，单页条数限制100，默认值为10
        :type pagesize: int
        :param name: ip地址组名称，支持模糊查询
        :type name: str
        :param ip: ip地址或ip段，传入该参数将查询包含传入的ip地址或ip段的地址组
        :type ip: str
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._name = None
        self._ip = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListIpGroupRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListIpGroupRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListIpGroupRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListIpGroupRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        """Gets the page of this ListIpGroupRequest.

        页码，默认值为1

        :return: The page of this ListIpGroupRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListIpGroupRequest.

        页码，默认值为1

        :param page: The page of this ListIpGroupRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        """Gets the pagesize of this ListIpGroupRequest.

        每页的条数，单页条数限制100，默认值为10

        :return: The pagesize of this ListIpGroupRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        """Sets the pagesize of this ListIpGroupRequest.

        每页的条数，单页条数限制100，默认值为10

        :param pagesize: The pagesize of this ListIpGroupRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        """Gets the name of this ListIpGroupRequest.

        ip地址组名称，支持模糊查询

        :return: The name of this ListIpGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIpGroupRequest.

        ip地址组名称，支持模糊查询

        :param name: The name of this ListIpGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        """Gets the ip of this ListIpGroupRequest.

        ip地址或ip段，传入该参数将查询包含传入的ip地址或ip段的地址组

        :return: The ip of this ListIpGroupRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListIpGroupRequest.

        ip地址或ip段，传入该参数将查询包含传入的ip地址或ip段的地址组

        :param ip: The ip of this ListIpGroupRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ListIpGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
