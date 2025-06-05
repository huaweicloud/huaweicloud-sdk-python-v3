# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelatedProjectInfoResultProjectInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'name': 'str',
        'author_id': 'str',
        'status': 'int',
        'author_domain_id': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'author_id': 'author_id',
        'status': 'status',
        'author_domain_id': 'author_domain_id'
    }

    def __init__(self, identifier=None, name=None, author_id=None, status=None, author_domain_id=None):
        r"""ListRelatedProjectInfoResultProjectInfoList

        The model defined in huaweicloud sdk

        :param identifier: 唯一标识
        :type identifier: str
        :param name: 项目名
        :type name: str
        :param author_id: 用户ID
        :type author_id: str
        :param status: 状态
        :type status: int
        :param author_domain_id: 项目创建者租户ID
        :type author_domain_id: str
        """
        
        

        self._identifier = None
        self._name = None
        self._author_id = None
        self._status = None
        self._author_domain_id = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if author_id is not None:
            self.author_id = author_id
        if status is not None:
            self.status = status
        if author_domain_id is not None:
            self.author_domain_id = author_domain_id

    @property
    def identifier(self):
        r"""Gets the identifier of this ListRelatedProjectInfoResultProjectInfoList.

        唯一标识

        :return: The identifier of this ListRelatedProjectInfoResultProjectInfoList.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this ListRelatedProjectInfoResultProjectInfoList.

        唯一标识

        :param identifier: The identifier of this ListRelatedProjectInfoResultProjectInfoList.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def name(self):
        r"""Gets the name of this ListRelatedProjectInfoResultProjectInfoList.

        项目名

        :return: The name of this ListRelatedProjectInfoResultProjectInfoList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRelatedProjectInfoResultProjectInfoList.

        项目名

        :param name: The name of this ListRelatedProjectInfoResultProjectInfoList.
        :type name: str
        """
        self._name = name

    @property
    def author_id(self):
        r"""Gets the author_id of this ListRelatedProjectInfoResultProjectInfoList.

        用户ID

        :return: The author_id of this ListRelatedProjectInfoResultProjectInfoList.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ListRelatedProjectInfoResultProjectInfoList.

        用户ID

        :param author_id: The author_id of this ListRelatedProjectInfoResultProjectInfoList.
        :type author_id: str
        """
        self._author_id = author_id

    @property
    def status(self):
        r"""Gets the status of this ListRelatedProjectInfoResultProjectInfoList.

        状态

        :return: The status of this ListRelatedProjectInfoResultProjectInfoList.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRelatedProjectInfoResultProjectInfoList.

        状态

        :param status: The status of this ListRelatedProjectInfoResultProjectInfoList.
        :type status: int
        """
        self._status = status

    @property
    def author_domain_id(self):
        r"""Gets the author_domain_id of this ListRelatedProjectInfoResultProjectInfoList.

        项目创建者租户ID

        :return: The author_domain_id of this ListRelatedProjectInfoResultProjectInfoList.
        :rtype: str
        """
        return self._author_domain_id

    @author_domain_id.setter
    def author_domain_id(self, author_domain_id):
        r"""Sets the author_domain_id of this ListRelatedProjectInfoResultProjectInfoList.

        项目创建者租户ID

        :param author_domain_id: The author_domain_id of this ListRelatedProjectInfoResultProjectInfoList.
        :type author_domain_id: str
        """
        self._author_domain_id = author_domain_id

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
        if not isinstance(other, ListRelatedProjectInfoResultProjectInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
