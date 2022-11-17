# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEncryptdatasRequest:

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
        'limit': 'int',
        'offset': 'int',
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, name=None, limit=None, offset=None, ief_instance_id=None):
        """ListEncryptdatasRequest

        The model defined in huaweicloud sdk

        :param name: 加密数据名称
        :type name: str
        :param limit: 查询返回记录的数量限制
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        """
        
        

        self._name = None
        self._limit = None
        self._offset = None
        self._ief_instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id

    @property
    def name(self):
        """Gets the name of this ListEncryptdatasRequest.

        加密数据名称

        :return: The name of this ListEncryptdatasRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEncryptdatasRequest.

        加密数据名称

        :param name: The name of this ListEncryptdatasRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListEncryptdatasRequest.

        查询返回记录的数量限制

        :return: The limit of this ListEncryptdatasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEncryptdatasRequest.

        查询返回记录的数量限制

        :param limit: The limit of this ListEncryptdatasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEncryptdatasRequest.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this ListEncryptdatasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEncryptdatasRequest.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this ListEncryptdatasRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListEncryptdatasRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListEncryptdatasRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListEncryptdatasRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListEncryptdatasRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, ListEncryptdatasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
