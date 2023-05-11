# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrganizationalUnitReqBody:

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
        'parent_id': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, parent_id=None, tags=None):
        """CreateOrganizationalUnitReqBody

        The model defined in huaweicloud sdk

        :param name: 要分配给新组织单元的名称。
        :type name: str
        :param parent_id: 要在其中创建新组织单元的根或组织单元的唯一标识符。
        :type parent_id: str
        :param tags: 要附加到新创建的组织单元的标签列表。
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        
        

        self._name = None
        self._parent_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.parent_id = parent_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateOrganizationalUnitReqBody.

        要分配给新组织单元的名称。

        :return: The name of this CreateOrganizationalUnitReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrganizationalUnitReqBody.

        要分配给新组织单元的名称。

        :param name: The name of this CreateOrganizationalUnitReqBody.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateOrganizationalUnitReqBody.

        要在其中创建新组织单元的根或组织单元的唯一标识符。

        :return: The parent_id of this CreateOrganizationalUnitReqBody.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateOrganizationalUnitReqBody.

        要在其中创建新组织单元的根或组织单元的唯一标识符。

        :param parent_id: The parent_id of this CreateOrganizationalUnitReqBody.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def tags(self):
        """Gets the tags of this CreateOrganizationalUnitReqBody.

        要附加到新创建的组织单元的标签列表。

        :return: The tags of this CreateOrganizationalUnitReqBody.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateOrganizationalUnitReqBody.

        要附加到新创建的组织单元的标签列表。

        :param tags: The tags of this CreateOrganizationalUnitReqBody.
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateOrganizationalUnitReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
