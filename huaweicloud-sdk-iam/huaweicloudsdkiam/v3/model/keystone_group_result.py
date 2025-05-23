# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneGroupResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'links': 'Links',
        'create_time': 'int'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'domain_id': 'domain_id',
        'name': 'name',
        'links': 'links',
        'create_time': 'create_time'
    }

    def __init__(self, description=None, id=None, domain_id=None, name=None, links=None, create_time=None):
        r"""KeystoneGroupResult

        The model defined in huaweicloud sdk

        :param description: 用户组描述信息。
        :type description: str
        :param id: 用户组ID。
        :type id: str
        :param domain_id: 用户组所属账号ID。
        :type domain_id: str
        :param name: 用户组名称。
        :type name: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param create_time: 用户组创建时间。
        :type create_time: int
        """
        
        

        self._description = None
        self._id = None
        self._domain_id = None
        self._name = None
        self._links = None
        self._create_time = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.links = links
        self.create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this KeystoneGroupResult.

        用户组描述信息。

        :return: The description of this KeystoneGroupResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this KeystoneGroupResult.

        用户组描述信息。

        :param description: The description of this KeystoneGroupResult.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this KeystoneGroupResult.

        用户组ID。

        :return: The id of this KeystoneGroupResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KeystoneGroupResult.

        用户组ID。

        :param id: The id of this KeystoneGroupResult.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeystoneGroupResult.

        用户组所属账号ID。

        :return: The domain_id of this KeystoneGroupResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeystoneGroupResult.

        用户组所属账号ID。

        :param domain_id: The domain_id of this KeystoneGroupResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this KeystoneGroupResult.

        用户组名称。

        :return: The name of this KeystoneGroupResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KeystoneGroupResult.

        用户组名称。

        :param name: The name of this KeystoneGroupResult.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        r"""Gets the links of this KeystoneGroupResult.

        :return: The links of this KeystoneGroupResult.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this KeystoneGroupResult.

        :param links: The links of this KeystoneGroupResult.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def create_time(self):
        r"""Gets the create_time of this KeystoneGroupResult.

        用户组创建时间。

        :return: The create_time of this KeystoneGroupResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this KeystoneGroupResult.

        用户组创建时间。

        :param create_time: The create_time of this KeystoneGroupResult.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, KeystoneGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
