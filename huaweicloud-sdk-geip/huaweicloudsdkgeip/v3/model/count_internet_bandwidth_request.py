# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountInternetBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'size': 'list[int]',
        'name': 'list[str]',
        'name_like': 'str',
        'access_site': 'list[str]',
        'status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'name': 'name',
        'name_like': 'name_like',
        'access_site': 'access_site',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, size=None, name=None, name_like=None, access_site=None, status=None, enterprise_project_id=None, tags=None):
        """CountInternetBandwidthRequest

        The model defined in huaweicloud sdk

        :param id: 根据ID过滤
        :type id: list[str]
        :param size: 根据全域公网带宽大小过滤
        :type size: list[int]
        :param name: 根据名称过滤
        :type name: list[str]
        :param name_like: 根据名称模糊匹配
        :type name_like: str
        :param access_site: 根据接入点过滤
        :type access_site: list[str]
        :param status: 根据资源状态过滤
        :type status: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤
        :type enterprise_project_id: list[str]
        :param tags: 根据标签过滤
        :type tags: list[str]
        """
        
        

        self._id = None
        self._size = None
        self._name = None
        self._name_like = None
        self._access_site = None
        self._status = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if name_like is not None:
            self.name_like = name_like
        if access_site is not None:
            self.access_site = access_site
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this CountInternetBandwidthRequest.

        根据ID过滤

        :return: The id of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CountInternetBandwidthRequest.

        根据ID过滤

        :param id: The id of this CountInternetBandwidthRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this CountInternetBandwidthRequest.

        根据全域公网带宽大小过滤

        :return: The size of this CountInternetBandwidthRequest.
        :rtype: list[int]
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CountInternetBandwidthRequest.

        根据全域公网带宽大小过滤

        :param size: The size of this CountInternetBandwidthRequest.
        :type size: list[int]
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this CountInternetBandwidthRequest.

        根据名称过滤

        :return: The name of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountInternetBandwidthRequest.

        根据名称过滤

        :param name: The name of this CountInternetBandwidthRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def name_like(self):
        """Gets the name_like of this CountInternetBandwidthRequest.

        根据名称模糊匹配

        :return: The name_like of this CountInternetBandwidthRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this CountInternetBandwidthRequest.

        根据名称模糊匹配

        :param name_like: The name_like of this CountInternetBandwidthRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def access_site(self):
        """Gets the access_site of this CountInternetBandwidthRequest.

        根据接入点过滤

        :return: The access_site of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this CountInternetBandwidthRequest.

        根据接入点过滤

        :param access_site: The access_site of this CountInternetBandwidthRequest.
        :type access_site: list[str]
        """
        self._access_site = access_site

    @property
    def status(self):
        """Gets the status of this CountInternetBandwidthRequest.

        根据资源状态过滤

        :return: The status of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CountInternetBandwidthRequest.

        根据资源状态过滤

        :param status: The status of this CountInternetBandwidthRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CountInternetBandwidthRequest.

        根据企业项目ID过滤

        :return: The enterprise_project_id of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CountInternetBandwidthRequest.

        根据企业项目ID过滤

        :param enterprise_project_id: The enterprise_project_id of this CountInternetBandwidthRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CountInternetBandwidthRequest.

        根据标签过滤

        :return: The tags of this CountInternetBandwidthRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CountInternetBandwidthRequest.

        根据标签过滤

        :param tags: The tags of this CountInternetBandwidthRequest.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CountInternetBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
