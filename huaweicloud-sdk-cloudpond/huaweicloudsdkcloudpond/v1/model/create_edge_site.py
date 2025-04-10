# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'description': 'str',
        'location': 'CreateLocation',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'description': 'description',
        'location': 'location',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, region_id=None, project_id=None, description=None, location=None, enterprise_project_id=None):
        r"""CreateEdgeSite

        The model defined in huaweicloud sdk

        :param name: 边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）
        :type name: str
        :param region_id: 边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）
        :type region_id: str
        :param project_id: 边缘小站所属项目ID
        :type project_id: str
        :param description: 边缘小站描述，最大支持长度为255个字节，不允许包含&lt;&gt;
        :type description: str
        :param location: 
        :type location: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        :param enterprise_project_id: 企业项目Id
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._region_id = None
        self._project_id = None
        self._description = None
        self._location = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        self.location = location
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateEdgeSite.

        边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :return: The name of this CreateEdgeSite.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEdgeSite.

        边缘小站名称，最大支持长度为64个字节。只包含中文字符、英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :param name: The name of this CreateEdgeSite.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateEdgeSite.

        边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :return: The region_id of this CreateEdgeSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateEdgeSite.

        边缘小站所属区域ID，最大长度为64个字节。只包含英文字母（a-z、A-Z）、数字（0-9）、下划线（_）、中划线（-）

        :param region_id: The region_id of this CreateEdgeSite.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateEdgeSite.

        边缘小站所属项目ID

        :return: The project_id of this CreateEdgeSite.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateEdgeSite.

        边缘小站所属项目ID

        :param project_id: The project_id of this CreateEdgeSite.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        r"""Gets the description of this CreateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :return: The description of this CreateEdgeSite.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :param description: The description of this CreateEdgeSite.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        r"""Gets the location of this CreateEdgeSite.

        :return: The location of this CreateEdgeSite.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this CreateEdgeSite.

        :param location: The location of this CreateEdgeSite.
        :type location: :class:`huaweicloudsdkcloudpond.v1.CreateLocation`
        """
        self._location = location

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateEdgeSite.

        企业项目Id

        :return: The enterprise_project_id of this CreateEdgeSite.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateEdgeSite.

        企业项目Id

        :param enterprise_project_id: The enterprise_project_id of this CreateEdgeSite.
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
        if not isinstance(other, CreateEdgeSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
