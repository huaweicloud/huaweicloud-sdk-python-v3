# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpReferenceTablesRequest:

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
        'name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page': 'page',
        'pagesize': 'pagesize',
        'name': 'name'
    }

    def __init__(self, enterprise_project_id=None, page=None, pagesize=None, name=None):
        r"""ShowHttpReferenceTablesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param page: 分页查询参数，第page页
        :type page: int
        :param pagesize: 分页查询参数，每页pagesize条记录
        :type pagesize: int
        :param name: 模糊查询引用表名称
        :type name: str
        """
        
        

        self._enterprise_project_id = None
        self._page = None
        self._pagesize = None
        self._name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if name is not None:
            self.name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowHttpReferenceTablesRequest.

        您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ShowHttpReferenceTablesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowHttpReferenceTablesRequest.

        您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowHttpReferenceTablesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page(self):
        r"""Gets the page of this ShowHttpReferenceTablesRequest.

        分页查询参数，第page页

        :return: The page of this ShowHttpReferenceTablesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowHttpReferenceTablesRequest.

        分页查询参数，第page页

        :param page: The page of this ShowHttpReferenceTablesRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ShowHttpReferenceTablesRequest.

        分页查询参数，每页pagesize条记录

        :return: The pagesize of this ShowHttpReferenceTablesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ShowHttpReferenceTablesRequest.

        分页查询参数，每页pagesize条记录

        :param pagesize: The pagesize of this ShowHttpReferenceTablesRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def name(self):
        r"""Gets the name of this ShowHttpReferenceTablesRequest.

        模糊查询引用表名称

        :return: The name of this ShowHttpReferenceTablesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowHttpReferenceTablesRequest.

        模糊查询引用表名称

        :param name: The name of this ShowHttpReferenceTablesRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ShowHttpReferenceTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
