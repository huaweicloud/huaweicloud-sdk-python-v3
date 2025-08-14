# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudStorageAssignmentRequest:

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
        'attach': 'str',
        'attach_names': 'list[str]',
        'capacity_filter': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'storage_id': 'storage_id',
        'claim_mode': 'claim_mode',
        'attach': 'attach',
        'attach_names': 'attach_names',
        'capacity_filter': 'capacity_filter'
    }

    def __init__(self, offset=None, limit=None, storage_id=None, claim_mode=None, attach=None, attach_names=None, capacity_filter=None):
        r"""ListCloudStorageAssignmentRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param storage_id: WKS存储ID。
        :type storage_id: str
        :param claim_mode: 存储声明的类型,目前只支持USER,后面可以拓展。 * &#x60;USER&#x60; -  个人文件夹 * &#x60;SHARE&#x60; -  共享文件夹
        :type claim_mode: str
        :param attach: 被分配的个体或组的名称，当传attach_names时，本字段不生效。
        :type attach: str
        :param attach_names: 被分配的个体或组的名称。
        :type attach_names: list[str]
        :param capacity_filter: 是否查询容量过滤： - true : 是。 - false: 否。
        :type capacity_filter: str
        """
        
        

        self._offset = None
        self._limit = None
        self._storage_id = None
        self._claim_mode = None
        self._attach = None
        self._attach_names = None
        self._capacity_filter = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.storage_id = storage_id
        self.claim_mode = claim_mode
        if attach is not None:
            self.attach = attach
        if attach_names is not None:
            self.attach_names = attach_names
        if capacity_filter is not None:
            self.capacity_filter = capacity_filter

    @property
    def offset(self):
        r"""Gets the offset of this ListCloudStorageAssignmentRequest.

        查询的偏移量。

        :return: The offset of this ListCloudStorageAssignmentRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCloudStorageAssignmentRequest.

        查询的偏移量。

        :param offset: The offset of this ListCloudStorageAssignmentRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudStorageAssignmentRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListCloudStorageAssignmentRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudStorageAssignmentRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListCloudStorageAssignmentRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def storage_id(self):
        r"""Gets the storage_id of this ListCloudStorageAssignmentRequest.

        WKS存储ID。

        :return: The storage_id of this ListCloudStorageAssignmentRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        r"""Sets the storage_id of this ListCloudStorageAssignmentRequest.

        WKS存储ID。

        :param storage_id: The storage_id of this ListCloudStorageAssignmentRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def claim_mode(self):
        r"""Gets the claim_mode of this ListCloudStorageAssignmentRequest.

        存储声明的类型,目前只支持USER,后面可以拓展。 * `USER` -  个人文件夹 * `SHARE` -  共享文件夹

        :return: The claim_mode of this ListCloudStorageAssignmentRequest.
        :rtype: str
        """
        return self._claim_mode

    @claim_mode.setter
    def claim_mode(self, claim_mode):
        r"""Sets the claim_mode of this ListCloudStorageAssignmentRequest.

        存储声明的类型,目前只支持USER,后面可以拓展。 * `USER` -  个人文件夹 * `SHARE` -  共享文件夹

        :param claim_mode: The claim_mode of this ListCloudStorageAssignmentRequest.
        :type claim_mode: str
        """
        self._claim_mode = claim_mode

    @property
    def attach(self):
        r"""Gets the attach of this ListCloudStorageAssignmentRequest.

        被分配的个体或组的名称，当传attach_names时，本字段不生效。

        :return: The attach of this ListCloudStorageAssignmentRequest.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        r"""Sets the attach of this ListCloudStorageAssignmentRequest.

        被分配的个体或组的名称，当传attach_names时，本字段不生效。

        :param attach: The attach of this ListCloudStorageAssignmentRequest.
        :type attach: str
        """
        self._attach = attach

    @property
    def attach_names(self):
        r"""Gets the attach_names of this ListCloudStorageAssignmentRequest.

        被分配的个体或组的名称。

        :return: The attach_names of this ListCloudStorageAssignmentRequest.
        :rtype: list[str]
        """
        return self._attach_names

    @attach_names.setter
    def attach_names(self, attach_names):
        r"""Sets the attach_names of this ListCloudStorageAssignmentRequest.

        被分配的个体或组的名称。

        :param attach_names: The attach_names of this ListCloudStorageAssignmentRequest.
        :type attach_names: list[str]
        """
        self._attach_names = attach_names

    @property
    def capacity_filter(self):
        r"""Gets the capacity_filter of this ListCloudStorageAssignmentRequest.

        是否查询容量过滤： - true : 是。 - false: 否。

        :return: The capacity_filter of this ListCloudStorageAssignmentRequest.
        :rtype: str
        """
        return self._capacity_filter

    @capacity_filter.setter
    def capacity_filter(self, capacity_filter):
        r"""Sets the capacity_filter of this ListCloudStorageAssignmentRequest.

        是否查询容量过滤： - true : 是。 - false: 否。

        :param capacity_filter: The capacity_filter of this ListCloudStorageAssignmentRequest.
        :type capacity_filter: str
        """
        self._capacity_filter = capacity_filter

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
        if not isinstance(other, ListCloudStorageAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
