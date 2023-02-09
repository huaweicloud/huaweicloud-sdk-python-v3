# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCatalogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'description': 'str',
        'location': 'str',
        'database_location_list': 'list[str]'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'description': 'description',
        'location': 'location',
        'database_location_list': 'database_location_list'
    }

    def __init__(self, catalog_name=None, description=None, location=None, database_location_list=None):
        """CreateCatalogResponse

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名字
        :type catalog_name: str
        :param description: 描述信息
        :type description: str
        :param location: 路径地址
        :type location: str
        :param database_location_list: database路径列表
        :type database_location_list: list[str]
        """
        
        super(CreateCatalogResponse, self).__init__()

        self._catalog_name = None
        self._description = None
        self._location = None
        self._database_location_list = None
        self.discriminator = None

        if catalog_name is not None:
            self.catalog_name = catalog_name
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if database_location_list is not None:
            self.database_location_list = database_location_list

    @property
    def catalog_name(self):
        """Gets the catalog_name of this CreateCatalogResponse.

        catalog名字

        :return: The catalog_name of this CreateCatalogResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this CreateCatalogResponse.

        catalog名字

        :param catalog_name: The catalog_name of this CreateCatalogResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def description(self):
        """Gets the description of this CreateCatalogResponse.

        描述信息

        :return: The description of this CreateCatalogResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCatalogResponse.

        描述信息

        :param description: The description of this CreateCatalogResponse.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        """Gets the location of this CreateCatalogResponse.

        路径地址

        :return: The location of this CreateCatalogResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateCatalogResponse.

        路径地址

        :param location: The location of this CreateCatalogResponse.
        :type location: str
        """
        self._location = location

    @property
    def database_location_list(self):
        """Gets the database_location_list of this CreateCatalogResponse.

        database路径列表

        :return: The database_location_list of this CreateCatalogResponse.
        :rtype: list[str]
        """
        return self._database_location_list

    @database_location_list.setter
    def database_location_list(self, database_location_list):
        """Sets the database_location_list of this CreateCatalogResponse.

        database路径列表

        :param database_location_list: The database_location_list of this CreateCatalogResponse.
        :type database_location_list: list[str]
        """
        self._database_location_list = database_location_list

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
        if not isinstance(other, CreateCatalogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
