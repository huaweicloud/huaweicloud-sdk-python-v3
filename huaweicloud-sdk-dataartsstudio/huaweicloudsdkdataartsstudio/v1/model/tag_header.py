# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagHeader:

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
        'dexcription': 'object',
        'display_text': 'str',
        'relation_guid': 'str',
        'tag_guid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'dexcription': 'dexcription',
        'display_text': 'display_text',
        'relation_guid': 'relation_guid',
        'tag_guid': 'tag_guid'
    }

    def __init__(self, name=None, dexcription=None, display_text=None, relation_guid=None, tag_guid=None):
        r"""TagHeader

        The model defined in huaweicloud sdk

        :param name: 资产名称
        :type name: str
        :param dexcription: 标签描述
        :type dexcription: object
        :param display_text: 标签的名称
        :type display_text: str
        :param relation_guid: 关联的guid
        :type relation_guid: str
        :param tag_guid: 标签关联的guid
        :type tag_guid: str
        """
        
        

        self._name = None
        self._dexcription = None
        self._display_text = None
        self._relation_guid = None
        self._tag_guid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dexcription is not None:
            self.dexcription = dexcription
        if display_text is not None:
            self.display_text = display_text
        if relation_guid is not None:
            self.relation_guid = relation_guid
        if tag_guid is not None:
            self.tag_guid = tag_guid

    @property
    def name(self):
        r"""Gets the name of this TagHeader.

        资产名称

        :return: The name of this TagHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TagHeader.

        资产名称

        :param name: The name of this TagHeader.
        :type name: str
        """
        self._name = name

    @property
    def dexcription(self):
        r"""Gets the dexcription of this TagHeader.

        标签描述

        :return: The dexcription of this TagHeader.
        :rtype: object
        """
        return self._dexcription

    @dexcription.setter
    def dexcription(self, dexcription):
        r"""Sets the dexcription of this TagHeader.

        标签描述

        :param dexcription: The dexcription of this TagHeader.
        :type dexcription: object
        """
        self._dexcription = dexcription

    @property
    def display_text(self):
        r"""Gets the display_text of this TagHeader.

        标签的名称

        :return: The display_text of this TagHeader.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        r"""Sets the display_text of this TagHeader.

        标签的名称

        :param display_text: The display_text of this TagHeader.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def relation_guid(self):
        r"""Gets the relation_guid of this TagHeader.

        关联的guid

        :return: The relation_guid of this TagHeader.
        :rtype: str
        """
        return self._relation_guid

    @relation_guid.setter
    def relation_guid(self, relation_guid):
        r"""Sets the relation_guid of this TagHeader.

        关联的guid

        :param relation_guid: The relation_guid of this TagHeader.
        :type relation_guid: str
        """
        self._relation_guid = relation_guid

    @property
    def tag_guid(self):
        r"""Gets the tag_guid of this TagHeader.

        标签关联的guid

        :return: The tag_guid of this TagHeader.
        :rtype: str
        """
        return self._tag_guid

    @tag_guid.setter
    def tag_guid(self, tag_guid):
        r"""Sets the tag_guid of this TagHeader.

        标签关联的guid

        :param tag_guid: The tag_guid of this TagHeader.
        :type tag_guid: str
        """
        self._tag_guid = tag_guid

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
        if not isinstance(other, TagHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
