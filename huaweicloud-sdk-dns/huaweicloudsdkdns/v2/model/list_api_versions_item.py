# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiVersionsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'id': 'str',
        'links': 'list[LinksItem]'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, status=None, id=None, links=None):
        """ListApiVersionsItem

        The model defined in huaweicloud sdk

        :param status: 版本状态，包含：  CURRENT：表示该版本为主推版本。 SUPPORTED：表示为老版本，但是现在还在继续支持。 DEPRECATED：表示为废弃版本，存在后续删除的可能。
        :type status: str
        :param id: 版本号。
        :type id: str
        :param links: 指向当前版本的url。
        :type links: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        """
        
        

        self._status = None
        self._id = None
        self._links = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links

    @property
    def status(self):
        """Gets the status of this ListApiVersionsItem.

        版本状态，包含：  CURRENT：表示该版本为主推版本。 SUPPORTED：表示为老版本，但是现在还在继续支持。 DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :return: The status of this ListApiVersionsItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListApiVersionsItem.

        版本状态，包含：  CURRENT：表示该版本为主推版本。 SUPPORTED：表示为老版本，但是现在还在继续支持。 DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :param status: The status of this ListApiVersionsItem.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this ListApiVersionsItem.

        版本号。

        :return: The id of this ListApiVersionsItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListApiVersionsItem.

        版本号。

        :param id: The id of this ListApiVersionsItem.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this ListApiVersionsItem.

        指向当前版本的url。

        :return: The links of this ListApiVersionsItem.
        :rtype: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListApiVersionsItem.

        指向当前版本的url。

        :param links: The links of this ListApiVersionsItem.
        :type links: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        """
        self._links = links

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
        if not isinstance(other, ListApiVersionsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
