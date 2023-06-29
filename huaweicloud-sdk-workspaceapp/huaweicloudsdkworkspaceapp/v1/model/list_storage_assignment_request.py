# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStorageAssignmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'storage_id': 'str',
        'claim_mode': 'str',
        'storage_claim_id': 'str',
        'attach': 'str',
        'attach_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'storage_id': 'storage_id',
        'claim_mode': 'claim_mode',
        'storage_claim_id': 'storage_claim_id',
        'attach': 'attach',
        'attach_type': 'attach_type'
    }

    def __init__(self, offset=None, limit=None, storage_id=None, claim_mode=None, storage_claim_id=None, attach=None, attach_type=None):
        """ListStorageAssignmentRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量
        :type offset: int
        :param limit: 单次查询的大小[1-100]
        :type limit: int
        :param storage_id: WKS存储ID
        :type storage_id: str
        :param claim_mode: 存储声明的类型,claim_mode为share时,storage_claim_id必填 * &#x60;USER&#x60; -  用户目录 * &#x60;SHARE&#x60; - 共享目录
        :type claim_mode: str
        :param storage_claim_id: WKS存储目录声明ID
        :type storage_claim_id: str
        :param attach: 成员
        :type attach: str
        :param attach_type: 关联对象类型 * &#x60;USER&#x60; -  用户 * &#x60;USER_GROUP&#x60; - 用户组
        :type attach_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._storage_id = None
        self._claim_mode = None
        self._storage_claim_id = None
        self._attach = None
        self._attach_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.storage_id = storage_id
        self.claim_mode = claim_mode
        if storage_claim_id is not None:
            self.storage_claim_id = storage_claim_id
        if attach is not None:
            self.attach = attach
        if attach_type is not None:
            self.attach_type = attach_type

    @property
    def offset(self):
        """Gets the offset of this ListStorageAssignmentRequest.

        查询的偏移量

        :return: The offset of this ListStorageAssignmentRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListStorageAssignmentRequest.

        查询的偏移量

        :param offset: The offset of this ListStorageAssignmentRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListStorageAssignmentRequest.

        单次查询的大小[1-100]

        :return: The limit of this ListStorageAssignmentRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStorageAssignmentRequest.

        单次查询的大小[1-100]

        :param limit: The limit of this ListStorageAssignmentRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def storage_id(self):
        """Gets the storage_id of this ListStorageAssignmentRequest.

        WKS存储ID

        :return: The storage_id of this ListStorageAssignmentRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this ListStorageAssignmentRequest.

        WKS存储ID

        :param storage_id: The storage_id of this ListStorageAssignmentRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def claim_mode(self):
        """Gets the claim_mode of this ListStorageAssignmentRequest.

        存储声明的类型,claim_mode为share时,storage_claim_id必填 * `USER` -  用户目录 * `SHARE` - 共享目录

        :return: The claim_mode of this ListStorageAssignmentRequest.
        :rtype: str
        """
        return self._claim_mode

    @claim_mode.setter
    def claim_mode(self, claim_mode):
        """Sets the claim_mode of this ListStorageAssignmentRequest.

        存储声明的类型,claim_mode为share时,storage_claim_id必填 * `USER` -  用户目录 * `SHARE` - 共享目录

        :param claim_mode: The claim_mode of this ListStorageAssignmentRequest.
        :type claim_mode: str
        """
        self._claim_mode = claim_mode

    @property
    def storage_claim_id(self):
        """Gets the storage_claim_id of this ListStorageAssignmentRequest.

        WKS存储目录声明ID

        :return: The storage_claim_id of this ListStorageAssignmentRequest.
        :rtype: str
        """
        return self._storage_claim_id

    @storage_claim_id.setter
    def storage_claim_id(self, storage_claim_id):
        """Sets the storage_claim_id of this ListStorageAssignmentRequest.

        WKS存储目录声明ID

        :param storage_claim_id: The storage_claim_id of this ListStorageAssignmentRequest.
        :type storage_claim_id: str
        """
        self._storage_claim_id = storage_claim_id

    @property
    def attach(self):
        """Gets the attach of this ListStorageAssignmentRequest.

        成员

        :return: The attach of this ListStorageAssignmentRequest.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        """Sets the attach of this ListStorageAssignmentRequest.

        成员

        :param attach: The attach of this ListStorageAssignmentRequest.
        :type attach: str
        """
        self._attach = attach

    @property
    def attach_type(self):
        """Gets the attach_type of this ListStorageAssignmentRequest.

        关联对象类型 * `USER` -  用户 * `USER_GROUP` - 用户组

        :return: The attach_type of this ListStorageAssignmentRequest.
        :rtype: str
        """
        return self._attach_type

    @attach_type.setter
    def attach_type(self, attach_type):
        """Sets the attach_type of this ListStorageAssignmentRequest.

        关联对象类型 * `USER` -  用户 * `USER_GROUP` - 用户组

        :param attach_type: The attach_type of this ListStorageAssignmentRequest.
        :type attach_type: str
        """
        self._attach_type = attach_type

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
        if not isinstance(other, ListStorageAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
