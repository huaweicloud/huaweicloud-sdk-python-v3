# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'id': 'str',
        'statement': 'list[Statement]'
    }

    attribute_map = {
        'version': 'Version',
        'id': 'Id',
        'statement': 'Statement'
    }

    def __init__(self, version=None, id=None, statement=None):
        """AccessPolicy

        The model defined in huaweicloud sdk

        :param version: 访问策略规范版本。目前只支持“2016-09-07”。
        :type version: str
        :param id: 策略的唯一标识。不能为空。
        :type id: str
        :param statement: 访问策略是通过Statement语句来定义的。一个访问策略可包含一条或多条Statement语句。通过Statement语句向其他用户或云服务授权对主题的操作。
        :type statement: list[:class:`huaweicloudsdksmn.v2.Statement`]
        """
        
        

        self._version = None
        self._id = None
        self._statement = None
        self.discriminator = None

        self.version = version
        self.id = id
        self.statement = statement

    @property
    def version(self):
        """Gets the version of this AccessPolicy.

        访问策略规范版本。目前只支持“2016-09-07”。

        :return: The version of this AccessPolicy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AccessPolicy.

        访问策略规范版本。目前只支持“2016-09-07”。

        :param version: The version of this AccessPolicy.
        :type version: str
        """
        self._version = version

    @property
    def id(self):
        """Gets the id of this AccessPolicy.

        策略的唯一标识。不能为空。

        :return: The id of this AccessPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessPolicy.

        策略的唯一标识。不能为空。

        :param id: The id of this AccessPolicy.
        :type id: str
        """
        self._id = id

    @property
    def statement(self):
        """Gets the statement of this AccessPolicy.

        访问策略是通过Statement语句来定义的。一个访问策略可包含一条或多条Statement语句。通过Statement语句向其他用户或云服务授权对主题的操作。

        :return: The statement of this AccessPolicy.
        :rtype: list[:class:`huaweicloudsdksmn.v2.Statement`]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this AccessPolicy.

        访问策略是通过Statement语句来定义的。一个访问策略可包含一条或多条Statement语句。通过Statement语句向其他用户或云服务授权对主题的操作。

        :param statement: The statement of this AccessPolicy.
        :type statement: list[:class:`huaweicloudsdksmn.v2.Statement`]
        """
        self._statement = statement

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
        if not isinstance(other, AccessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
