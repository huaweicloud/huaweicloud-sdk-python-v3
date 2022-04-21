# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectV3:

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
        'name': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'management_permission': 'bool',
        'is_stock': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'management_permission': 'management_permission',
        'is_stock': 'is_stock'
    }

    def __init__(self, project_id=None, name=None, region_id=None, region_name=None, management_permission=None, is_stock=None):
        """ProjectV3

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param name: 项目名
        :type name: str
        :param region_id: 区域编码
        :type region_id: str
        :param region_name: 区域名称
        :type region_name: str
        :param management_permission: 管理权限
        :type management_permission: bool
        :param is_stock: 是否是存量项目
        :type is_stock: bool
        """
        
        

        self._project_id = None
        self._name = None
        self._region_id = None
        self._region_name = None
        self._management_permission = None
        self._is_stock = None
        self.discriminator = None

        self.project_id = project_id
        self.name = name
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if management_permission is not None:
            self.management_permission = management_permission
        if is_stock is not None:
            self.is_stock = is_stock

    @property
    def project_id(self):
        """Gets the project_id of this ProjectV3.

        项目id

        :return: The project_id of this ProjectV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectV3.

        项目id

        :param project_id: The project_id of this ProjectV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ProjectV3.

        项目名

        :return: The name of this ProjectV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectV3.

        项目名

        :param name: The name of this ProjectV3.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this ProjectV3.

        区域编码

        :return: The region_id of this ProjectV3.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ProjectV3.

        区域编码

        :param region_id: The region_id of this ProjectV3.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this ProjectV3.

        区域名称

        :return: The region_name of this ProjectV3.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ProjectV3.

        区域名称

        :param region_name: The region_name of this ProjectV3.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def management_permission(self):
        """Gets the management_permission of this ProjectV3.

        管理权限

        :return: The management_permission of this ProjectV3.
        :rtype: bool
        """
        return self._management_permission

    @management_permission.setter
    def management_permission(self, management_permission):
        """Sets the management_permission of this ProjectV3.

        管理权限

        :param management_permission: The management_permission of this ProjectV3.
        :type management_permission: bool
        """
        self._management_permission = management_permission

    @property
    def is_stock(self):
        """Gets the is_stock of this ProjectV3.

        是否是存量项目

        :return: The is_stock of this ProjectV3.
        :rtype: bool
        """
        return self._is_stock

    @is_stock.setter
    def is_stock(self, is_stock):
        """Sets the is_stock of this ProjectV3.

        是否是存量项目

        :param is_stock: The is_stock of this ProjectV3.
        :type is_stock: bool
        """
        self._is_stock = is_stock

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
        if not isinstance(other, ProjectV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
