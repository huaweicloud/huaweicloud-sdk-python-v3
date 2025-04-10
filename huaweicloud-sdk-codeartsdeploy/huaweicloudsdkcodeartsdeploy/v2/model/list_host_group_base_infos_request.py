# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostGroupBaseInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'project_uuid': 'str',
        'os': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'name': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'project_uuid': 'project_uuid',
        'os': 'os',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'name': 'name'
    }

    def __init__(self, application_id=None, project_uuid=None, os=None, page_index=None, page_size=None, name=None):
        r"""ListHostGroupBaseInfosRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param project_uuid: 项目id
        :type project_uuid: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param page_index: 分页页码
        :type page_index: int
        :param page_size: 分页查询每页条数
        :type page_size: int
        :param name: 按主机集群名称搜索关键字
        :type name: str
        """
        
        

        self._application_id = None
        self._project_uuid = None
        self._os = None
        self._page_index = None
        self._page_size = None
        self._name = None
        self.discriminator = None

        self.application_id = application_id
        self.project_uuid = project_uuid
        if os is not None:
            self.os = os
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if name is not None:
            self.name = name

    @property
    def application_id(self):
        r"""Gets the application_id of this ListHostGroupBaseInfosRequest.

        应用id

        :return: The application_id of this ListHostGroupBaseInfosRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListHostGroupBaseInfosRequest.

        应用id

        :param application_id: The application_id of this ListHostGroupBaseInfosRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListHostGroupBaseInfosRequest.

        项目id

        :return: The project_uuid of this ListHostGroupBaseInfosRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListHostGroupBaseInfosRequest.

        项目id

        :param project_uuid: The project_uuid of this ListHostGroupBaseInfosRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def os(self):
        r"""Gets the os of this ListHostGroupBaseInfosRequest.

        操作系统：windows|linux

        :return: The os of this ListHostGroupBaseInfosRequest.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ListHostGroupBaseInfosRequest.

        操作系统：windows|linux

        :param os: The os of this ListHostGroupBaseInfosRequest.
        :type os: str
        """
        self._os = os

    @property
    def page_index(self):
        r"""Gets the page_index of this ListHostGroupBaseInfosRequest.

        分页页码

        :return: The page_index of this ListHostGroupBaseInfosRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListHostGroupBaseInfosRequest.

        分页页码

        :param page_index: The page_index of this ListHostGroupBaseInfosRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListHostGroupBaseInfosRequest.

        分页查询每页条数

        :return: The page_size of this ListHostGroupBaseInfosRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListHostGroupBaseInfosRequest.

        分页查询每页条数

        :param page_size: The page_size of this ListHostGroupBaseInfosRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def name(self):
        r"""Gets the name of this ListHostGroupBaseInfosRequest.

        按主机集群名称搜索关键字

        :return: The name of this ListHostGroupBaseInfosRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListHostGroupBaseInfosRequest.

        按主机集群名称搜索关键字

        :param name: The name of this ListHostGroupBaseInfosRequest.
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
        if not isinstance(other, ListHostGroupBaseInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
