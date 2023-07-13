# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsBucketInfoOwner:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id'
    }

    def __init__(self, display_name=None, id=None):
        """ObsBucketInfoOwner

        The model defined in huaweicloud sdk

        :param display_name: 显示名称
        :type display_name: str
        :param id: 用户的DomainID（帐号ID）
        :type id: str
        """
        
        

        self._display_name = None
        self._id = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id

    @property
    def display_name(self):
        """Gets the display_name of this ObsBucketInfoOwner.

        显示名称

        :return: The display_name of this ObsBucketInfoOwner.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ObsBucketInfoOwner.

        显示名称

        :param display_name: The display_name of this ObsBucketInfoOwner.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this ObsBucketInfoOwner.

        用户的DomainID（帐号ID）

        :return: The id of this ObsBucketInfoOwner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObsBucketInfoOwner.

        用户的DomainID（帐号ID）

        :param id: The id of this ObsBucketInfoOwner.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ObsBucketInfoOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
