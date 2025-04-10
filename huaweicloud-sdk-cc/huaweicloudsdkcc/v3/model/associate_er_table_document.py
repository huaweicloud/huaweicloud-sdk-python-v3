# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateErTableDocument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'region_id': 'str',
        'enterprise_router_id': 'str',
        'enterprise_router_table_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'region_id': 'region_id',
        'enterprise_router_id': 'enterprise_router_id',
        'enterprise_router_table_id': 'enterprise_router_table_id'
    }

    def __init__(self, project_id=None, region_id=None, enterprise_router_id=None, enterprise_router_table_id=None):
        r"""AssociateErTableDocument

        The model defined in huaweicloud sdk

        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param region_id: RegionID。
        :type region_id: str
        :param enterprise_router_id: 企业路由器的ID。
        :type enterprise_router_id: str
        :param enterprise_router_table_id: 企业路由器的路由表ID。
        :type enterprise_router_table_id: str
        """
        
        

        self._project_id = None
        self._region_id = None
        self._enterprise_router_id = None
        self._enterprise_router_table_id = None
        self.discriminator = None

        self.project_id = project_id
        self.region_id = region_id
        self.enterprise_router_id = enterprise_router_id
        self.enterprise_router_table_id = enterprise_router_table_id

    @property
    def project_id(self):
        r"""Gets the project_id of this AssociateErTableDocument.

        实例所属项目ID。

        :return: The project_id of this AssociateErTableDocument.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AssociateErTableDocument.

        实例所属项目ID。

        :param project_id: The project_id of this AssociateErTableDocument.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this AssociateErTableDocument.

        RegionID。

        :return: The region_id of this AssociateErTableDocument.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AssociateErTableDocument.

        RegionID。

        :param region_id: The region_id of this AssociateErTableDocument.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this AssociateErTableDocument.

        企业路由器的ID。

        :return: The enterprise_router_id of this AssociateErTableDocument.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this AssociateErTableDocument.

        企业路由器的ID。

        :param enterprise_router_id: The enterprise_router_id of this AssociateErTableDocument.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def enterprise_router_table_id(self):
        r"""Gets the enterprise_router_table_id of this AssociateErTableDocument.

        企业路由器的路由表ID。

        :return: The enterprise_router_table_id of this AssociateErTableDocument.
        :rtype: str
        """
        return self._enterprise_router_table_id

    @enterprise_router_table_id.setter
    def enterprise_router_table_id(self, enterprise_router_table_id):
        r"""Sets the enterprise_router_table_id of this AssociateErTableDocument.

        企业路由器的路由表ID。

        :param enterprise_router_table_id: The enterprise_router_table_id of this AssociateErTableDocument.
        :type enterprise_router_table_id: str
        """
        self._enterprise_router_table_id = enterprise_router_table_id

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
        if not isinstance(other, AssociateErTableDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
