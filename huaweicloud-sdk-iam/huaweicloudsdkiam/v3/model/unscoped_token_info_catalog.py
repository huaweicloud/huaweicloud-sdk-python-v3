# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnscopedTokenInfoCatalog:

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
        'interface': 'str',
        'region': 'str',
        'region_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'interface': 'interface',
        'region': 'region',
        'region_id': 'region_id',
        'url': 'url'
    }

    def __init__(self, id=None, interface=None, region=None, region_id=None, url=None):
        """UnscopedTokenInfoCatalog

        The model defined in huaweicloud sdk

        :param id: 终端节点ID。
        :type id: str
        :param interface: 接口类型，描述接口在该终端节点的可见性。值为“public”，表示该接口为公开接口。
        :type interface: str
        :param region: 终端节点所属区域。
        :type region: str
        :param region_id: 终端节点所属区域ID。
        :type region_id: str
        :param url: 终端节点的URL。
        :type url: str
        """
        
        

        self._id = None
        self._interface = None
        self._region = None
        self._region_id = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if interface is not None:
            self.interface = interface
        if region is not None:
            self.region = region
        if region_id is not None:
            self.region_id = region_id
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this UnscopedTokenInfoCatalog.

        终端节点ID。

        :return: The id of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnscopedTokenInfoCatalog.

        终端节点ID。

        :param id: The id of this UnscopedTokenInfoCatalog.
        :type id: str
        """
        self._id = id

    @property
    def interface(self):
        """Gets the interface of this UnscopedTokenInfoCatalog.

        接口类型，描述接口在该终端节点的可见性。值为“public”，表示该接口为公开接口。

        :return: The interface of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this UnscopedTokenInfoCatalog.

        接口类型，描述接口在该终端节点的可见性。值为“public”，表示该接口为公开接口。

        :param interface: The interface of this UnscopedTokenInfoCatalog.
        :type interface: str
        """
        self._interface = interface

    @property
    def region(self):
        """Gets the region of this UnscopedTokenInfoCatalog.

        终端节点所属区域。

        :return: The region of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UnscopedTokenInfoCatalog.

        终端节点所属区域。

        :param region: The region of this UnscopedTokenInfoCatalog.
        :type region: str
        """
        self._region = region

    @property
    def region_id(self):
        """Gets the region_id of this UnscopedTokenInfoCatalog.

        终端节点所属区域ID。

        :return: The region_id of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this UnscopedTokenInfoCatalog.

        终端节点所属区域ID。

        :param region_id: The region_id of this UnscopedTokenInfoCatalog.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def url(self):
        """Gets the url of this UnscopedTokenInfoCatalog.

        终端节点的URL。

        :return: The url of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UnscopedTokenInfoCatalog.

        终端节点的URL。

        :param url: The url of this UnscopedTokenInfoCatalog.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, UnscopedTokenInfoCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
