# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEncryptdataNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encryptdata_id': 'str',
        'limit': 'int',
        'ief_instance_id': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'encryptdata_id': 'encryptdata_id',
        'limit': 'limit',
        'ief_instance_id': 'ief-instance-id',
        'offset': 'offset'
    }

    def __init__(self, encryptdata_id=None, limit=None, ief_instance_id=None, offset=None):
        """ListEncryptdataNodesRequest

        The model defined in huaweicloud sdk

        :param encryptdata_id: 加密数据ID
        :type encryptdata_id: str
        :param limit: 查询返回记录的数量限制
        :type limit: int
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        """
        
        

        self._encryptdata_id = None
        self._limit = None
        self._ief_instance_id = None
        self._offset = None
        self.discriminator = None

        self.encryptdata_id = encryptdata_id
        if limit is not None:
            self.limit = limit
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if offset is not None:
            self.offset = offset

    @property
    def encryptdata_id(self):
        """Gets the encryptdata_id of this ListEncryptdataNodesRequest.

        加密数据ID

        :return: The encryptdata_id of this ListEncryptdataNodesRequest.
        :rtype: str
        """
        return self._encryptdata_id

    @encryptdata_id.setter
    def encryptdata_id(self, encryptdata_id):
        """Sets the encryptdata_id of this ListEncryptdataNodesRequest.

        加密数据ID

        :param encryptdata_id: The encryptdata_id of this ListEncryptdataNodesRequest.
        :type encryptdata_id: str
        """
        self._encryptdata_id = encryptdata_id

    @property
    def limit(self):
        """Gets the limit of this ListEncryptdataNodesRequest.

        查询返回记录的数量限制

        :return: The limit of this ListEncryptdataNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEncryptdataNodesRequest.

        查询返回记录的数量限制

        :param limit: The limit of this ListEncryptdataNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListEncryptdataNodesRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListEncryptdataNodesRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListEncryptdataNodesRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListEncryptdataNodesRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def offset(self):
        """Gets the offset of this ListEncryptdataNodesRequest.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this ListEncryptdataNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEncryptdataNodesRequest.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this ListEncryptdataNodesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListEncryptdataNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
