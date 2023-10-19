# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateErInstanceDocument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_router_id': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'enterprise_router_id': 'enterprise_router_id',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, enterprise_router_id=None, project_id=None, region_id=None):
        """AssociateErInstanceDocument

        The model defined in huaweicloud sdk

        :param enterprise_router_id: 资源ID标识符。
        :type enterprise_router_id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param region_id: RegionID。
        :type region_id: str
        """
        
        

        self._enterprise_router_id = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        self.enterprise_router_id = enterprise_router_id
        self.project_id = project_id
        self.region_id = region_id

    @property
    def enterprise_router_id(self):
        """Gets the enterprise_router_id of this AssociateErInstanceDocument.

        资源ID标识符。

        :return: The enterprise_router_id of this AssociateErInstanceDocument.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        """Sets the enterprise_router_id of this AssociateErInstanceDocument.

        资源ID标识符。

        :param enterprise_router_id: The enterprise_router_id of this AssociateErInstanceDocument.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def project_id(self):
        """Gets the project_id of this AssociateErInstanceDocument.

        实例所属项目ID。

        :return: The project_id of this AssociateErInstanceDocument.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssociateErInstanceDocument.

        实例所属项目ID。

        :param project_id: The project_id of this AssociateErInstanceDocument.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this AssociateErInstanceDocument.

        RegionID。

        :return: The region_id of this AssociateErInstanceDocument.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AssociateErInstanceDocument.

        RegionID。

        :param region_id: The region_id of this AssociateErInstanceDocument.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, AssociateErInstanceDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
