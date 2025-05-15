# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionPoint:

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
        'project_id': 'str',
        'region_id': 'str',
        'site_code': 'str',
        'instance_id': 'str',
        'parent_instance_id': 'str',
        'type': 'ConnectionPointTypeEnum'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'site_code': 'site_code',
        'instance_id': 'instance_id',
        'parent_instance_id': 'parent_instance_id',
        'type': 'type'
    }

    def __init__(self, id=None, project_id=None, region_id=None, site_code=None, instance_id=None, parent_instance_id=None, type=None):
        r"""ConnectionPoint

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param region_id: RegionID。
        :type region_id: str
        :param site_code: 站点编码。
        :type site_code: str
        :param instance_id: 连接点的实例ID。
        :type instance_id: str
        :param parent_instance_id: 连接点的实例的父资源ID。
        :type parent_instance_id: str
        :param type: 
        :type type: :class:`huaweicloudsdkcc.v3.ConnectionPointTypeEnum`
        """
        
        

        self._id = None
        self._project_id = None
        self._region_id = None
        self._site_code = None
        self._instance_id = None
        self._parent_instance_id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.region_id = region_id
        self.site_code = site_code
        self.instance_id = instance_id
        if parent_instance_id is not None:
            self.parent_instance_id = parent_instance_id
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this ConnectionPoint.

        实例ID。

        :return: The id of this ConnectionPoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectionPoint.

        实例ID。

        :param id: The id of this ConnectionPoint.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ConnectionPoint.

        实例所属项目ID。

        :return: The project_id of this ConnectionPoint.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConnectionPoint.

        实例所属项目ID。

        :param project_id: The project_id of this ConnectionPoint.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ConnectionPoint.

        RegionID。

        :return: The region_id of this ConnectionPoint.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ConnectionPoint.

        RegionID。

        :param region_id: The region_id of this ConnectionPoint.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def site_code(self):
        r"""Gets the site_code of this ConnectionPoint.

        站点编码。

        :return: The site_code of this ConnectionPoint.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this ConnectionPoint.

        站点编码。

        :param site_code: The site_code of this ConnectionPoint.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ConnectionPoint.

        连接点的实例ID。

        :return: The instance_id of this ConnectionPoint.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ConnectionPoint.

        连接点的实例ID。

        :param instance_id: The instance_id of this ConnectionPoint.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def parent_instance_id(self):
        r"""Gets the parent_instance_id of this ConnectionPoint.

        连接点的实例的父资源ID。

        :return: The parent_instance_id of this ConnectionPoint.
        :rtype: str
        """
        return self._parent_instance_id

    @parent_instance_id.setter
    def parent_instance_id(self, parent_instance_id):
        r"""Sets the parent_instance_id of this ConnectionPoint.

        连接点的实例的父资源ID。

        :param parent_instance_id: The parent_instance_id of this ConnectionPoint.
        :type parent_instance_id: str
        """
        self._parent_instance_id = parent_instance_id

    @property
    def type(self):
        r"""Gets the type of this ConnectionPoint.

        :return: The type of this ConnectionPoint.
        :rtype: :class:`huaweicloudsdkcc.v3.ConnectionPointTypeEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConnectionPoint.

        :param type: The type of this ConnectionPoint.
        :type type: :class:`huaweicloudsdkcc.v3.ConnectionPointTypeEnum`
        """
        self._type = type

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
        if not isinstance(other, ConnectionPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
