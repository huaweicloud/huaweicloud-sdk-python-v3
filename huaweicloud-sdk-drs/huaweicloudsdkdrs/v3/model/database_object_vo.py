# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseObjectVO:

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
        'select': 'str'
    }

    attribute_map = {
        'id': 'id',
        'select': 'select'
    }

    def __init__(self, id=None, select=None):
        """DatabaseObjectVO

        The model defined in huaweicloud sdk

        :param id: 数据库对象和数据库表名称，例如格式为hec-*-*-drs_test1。
        :type id: str
        :param select: 是否选择高级配置，值为true。
        :type select: str
        """
        
        

        self._id = None
        self._select = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if select is not None:
            self.select = select

    @property
    def id(self):
        """Gets the id of this DatabaseObjectVO.

        数据库对象和数据库表名称，例如格式为hec-*-*-drs_test1。

        :return: The id of this DatabaseObjectVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseObjectVO.

        数据库对象和数据库表名称，例如格式为hec-*-*-drs_test1。

        :param id: The id of this DatabaseObjectVO.
        :type id: str
        """
        self._id = id

    @property
    def select(self):
        """Gets the select of this DatabaseObjectVO.

        是否选择高级配置，值为true。

        :return: The select of this DatabaseObjectVO.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this DatabaseObjectVO.

        是否选择高级配置，值为true。

        :param select: The select of this DatabaseObjectVO.
        :type select: str
        """
        self._select = select

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
        if not isinstance(other, DatabaseObjectVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
