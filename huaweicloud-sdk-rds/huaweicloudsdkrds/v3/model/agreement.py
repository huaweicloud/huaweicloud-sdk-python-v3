# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Agreement:

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
        'name': 'str',
        'language': 'str',
        'version': 'str',
        'provision_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'language': 'language',
        'version': 'version',
        'provision_url': 'provision_url'
    }

    def __init__(self, id=None, name=None, language=None, version=None, provision_url=None):
        r"""Agreement

        The model defined in huaweicloud sdk

        :param id: 许可ID。
        :type id: str
        :param name: 许可名称。
        :type name: str
        :param language: 许可语言类型。
        :type language: str
        :param version: 许可版本。
        :type version: str
        :param provision_url: 许可链接。
        :type provision_url: str
        """
        
        

        self._id = None
        self._name = None
        self._language = None
        self._version = None
        self._provision_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if language is not None:
            self.language = language
        if version is not None:
            self.version = version
        if provision_url is not None:
            self.provision_url = provision_url

    @property
    def id(self):
        r"""Gets the id of this Agreement.

        许可ID。

        :return: The id of this Agreement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Agreement.

        许可ID。

        :param id: The id of this Agreement.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Agreement.

        许可名称。

        :return: The name of this Agreement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Agreement.

        许可名称。

        :param name: The name of this Agreement.
        :type name: str
        """
        self._name = name

    @property
    def language(self):
        r"""Gets the language of this Agreement.

        许可语言类型。

        :return: The language of this Agreement.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this Agreement.

        许可语言类型。

        :param language: The language of this Agreement.
        :type language: str
        """
        self._language = language

    @property
    def version(self):
        r"""Gets the version of this Agreement.

        许可版本。

        :return: The version of this Agreement.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Agreement.

        许可版本。

        :param version: The version of this Agreement.
        :type version: str
        """
        self._version = version

    @property
    def provision_url(self):
        r"""Gets the provision_url of this Agreement.

        许可链接。

        :return: The provision_url of this Agreement.
        :rtype: str
        """
        return self._provision_url

    @provision_url.setter
    def provision_url(self, provision_url):
        r"""Sets the provision_url of this Agreement.

        许可链接。

        :param provision_url: The provision_url of this Agreement.
        :type provision_url: str
        """
        self._provision_url = provision_url

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
        if not isinstance(other, Agreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
