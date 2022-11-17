# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModMemberDTO:

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
        'english_name': 'str',
        'signature': 'str',
        'title': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'english_name': 'englishName',
        'signature': 'signature',
        'title': 'title',
        'desc': 'desc'
    }

    def __init__(self, name=None, english_name=None, signature=None, title=None, desc=None):
        """ModMemberDTO

        The model defined in huaweicloud sdk

        :param name: 名称。
        :type name: str
        :param english_name: 英文名称。
        :type english_name: str
        :param signature: 签名。
        :type signature: str
        :param title: 职位。
        :type title: str
        :param desc: 备注。
        :type desc: str
        """
        
        

        self._name = None
        self._english_name = None
        self._signature = None
        self._title = None
        self._desc = None
        self.discriminator = None

        self.name = name
        if english_name is not None:
            self.english_name = english_name
        if signature is not None:
            self.signature = signature
        if title is not None:
            self.title = title
        if desc is not None:
            self.desc = desc

    @property
    def name(self):
        """Gets the name of this ModMemberDTO.

        名称。

        :return: The name of this ModMemberDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModMemberDTO.

        名称。

        :param name: The name of this ModMemberDTO.
        :type name: str
        """
        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this ModMemberDTO.

        英文名称。

        :return: The english_name of this ModMemberDTO.
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this ModMemberDTO.

        英文名称。

        :param english_name: The english_name of this ModMemberDTO.
        :type english_name: str
        """
        self._english_name = english_name

    @property
    def signature(self):
        """Gets the signature of this ModMemberDTO.

        签名。

        :return: The signature of this ModMemberDTO.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ModMemberDTO.

        签名。

        :param signature: The signature of this ModMemberDTO.
        :type signature: str
        """
        self._signature = signature

    @property
    def title(self):
        """Gets the title of this ModMemberDTO.

        职位。

        :return: The title of this ModMemberDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ModMemberDTO.

        职位。

        :param title: The title of this ModMemberDTO.
        :type title: str
        """
        self._title = title

    @property
    def desc(self):
        """Gets the desc of this ModMemberDTO.

        备注。

        :return: The desc of this ModMemberDTO.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ModMemberDTO.

        备注。

        :param desc: The desc of this ModMemberDTO.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, ModMemberDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
