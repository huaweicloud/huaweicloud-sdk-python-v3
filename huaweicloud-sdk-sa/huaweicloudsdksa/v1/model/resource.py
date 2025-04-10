# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'provider': 'str',
        'region_id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'tags': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'provider': 'provider',
        'region_id': 'region_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, type=None, provider=None, region_id=None, domain_id=None, project_id=None, ep_id=None, ep_name=None, tags=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param id: 资源ID。
        :type id: str
        :param name: 资源名称；最大长度255个字符。
        :type name: str
        :param type: 资源类型。
        :type type: str
        :param provider: 云服务名称。
        :type provider: str
        :param region_id: 区域。
        :type region_id: str
        :param domain_id: 资源所属租户账号ID。
        :type domain_id: str
        :param project_id: 资源所属项目ID。
        :type project_id: str
        :param ep_id: 企业项目ID。
        :type ep_id: str
        :param ep_name: 企业项目名称。
        :type ep_name: str
        :param tags: 资源标签 1、最多50个key/values对。 2、values：最大255字符。 3、取值范围：字母数字、空格、“+”、“-”、“&#x3D;”、“.”、“_”、“:”、“/”、“@”。
        :type tags: object
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._provider = None
        self._region_id = None
        self._domain_id = None
        self._project_id = None
        self._ep_id = None
        self._ep_name = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.provider = provider
        if region_id is not None:
            self.region_id = region_id
        self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this Resource.

        资源ID。

        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Resource.

        资源ID。

        :param id: The id of this Resource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Resource.

        资源名称；最大长度255个字符。

        :return: The name of this Resource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Resource.

        资源名称；最大长度255个字符。

        :param name: The name of this Resource.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this Resource.

        资源类型。

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Resource.

        资源类型。

        :param type: The type of this Resource.
        :type type: str
        """
        self._type = type

    @property
    def provider(self):
        r"""Gets the provider of this Resource.

        云服务名称。

        :return: The provider of this Resource.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this Resource.

        云服务名称。

        :param provider: The provider of this Resource.
        :type provider: str
        """
        self._provider = provider

    @property
    def region_id(self):
        r"""Gets the region_id of this Resource.

        区域。

        :return: The region_id of this Resource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this Resource.

        区域。

        :param region_id: The region_id of this Resource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Resource.

        资源所属租户账号ID。

        :return: The domain_id of this Resource.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Resource.

        资源所属租户账号ID。

        :param domain_id: The domain_id of this Resource.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this Resource.

        资源所属项目ID。

        :return: The project_id of this Resource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Resource.

        资源所属项目ID。

        :param project_id: The project_id of this Resource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this Resource.

        企业项目ID。

        :return: The ep_id of this Resource.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this Resource.

        企业项目ID。

        :param ep_id: The ep_id of this Resource.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this Resource.

        企业项目名称。

        :return: The ep_name of this Resource.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this Resource.

        企业项目名称。

        :param ep_name: The ep_name of this Resource.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def tags(self):
        r"""Gets the tags of this Resource.

        资源标签 1、最多50个key/values对。 2、values：最大255字符。 3、取值范围：字母数字、空格、“+”、“-”、“=”、“.”、“_”、“:”、“/”、“@”。

        :return: The tags of this Resource.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Resource.

        资源标签 1、最多50个key/values对。 2、values：最大255字符。 3、取值范围：字母数字、空格、“+”、“-”、“=”、“.”、“_”、“:”、“/”、“@”。

        :param tags: The tags of this Resource.
        :type tags: object
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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
