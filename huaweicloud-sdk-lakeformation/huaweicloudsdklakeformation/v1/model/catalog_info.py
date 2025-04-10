# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[DatabaseInfo]',
        'name': 'str'
    }

    attribute_map = {
        'databases': 'databases',
        'name': 'name'
    }

    def __init__(self, databases=None, name=None):
        r"""CatalogInfo

        The model defined in huaweicloud sdk

        :param databases: 子数据库信息
        :type databases: list[:class:`huaweicloudsdklakeformation.v1.DatabaseInfo`]
        :param name: catalog名
        :type name: str
        """
        
        

        self._databases = None
        self._name = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        self.name = name

    @property
    def databases(self):
        r"""Gets the databases of this CatalogInfo.

        子数据库信息

        :return: The databases of this CatalogInfo.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.DatabaseInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this CatalogInfo.

        子数据库信息

        :param databases: The databases of this CatalogInfo.
        :type databases: list[:class:`huaweicloudsdklakeformation.v1.DatabaseInfo`]
        """
        self._databases = databases

    @property
    def name(self):
        r"""Gets the name of this CatalogInfo.

        catalog名

        :return: The name of this CatalogInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CatalogInfo.

        catalog名

        :param name: The name of this CatalogInfo.
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
        if not isinstance(other, CatalogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
