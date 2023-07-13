# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseCommentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[UpdateDatabaseComment]'
    }

    attribute_map = {
        'databases': 'databases'
    }

    def __init__(self, databases=None):
        """UpdateDatabaseCommentRequest

        The model defined in huaweicloud sdk

        :param databases: 准备修改备注的数据库列表，列表最大长度为50。
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.UpdateDatabaseComment`]
        """
        
        

        self._databases = None
        self.discriminator = None

        self.databases = databases

    @property
    def databases(self):
        """Gets the databases of this UpdateDatabaseCommentRequest.

        准备修改备注的数据库列表，列表最大长度为50。

        :return: The databases of this UpdateDatabaseCommentRequest.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.UpdateDatabaseComment`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this UpdateDatabaseCommentRequest.

        准备修改备注的数据库列表，列表最大长度为50。

        :param databases: The databases of this UpdateDatabaseCommentRequest.
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.UpdateDatabaseComment`]
        """
        self._databases = databases

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
        if not isinstance(other, UpdateDatabaseCommentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
