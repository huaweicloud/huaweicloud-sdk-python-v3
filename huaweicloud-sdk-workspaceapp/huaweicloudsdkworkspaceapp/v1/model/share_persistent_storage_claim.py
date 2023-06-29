# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharePersistentStorageClaim:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_claim_id': 'str',
        'folder_path': 'str',
        'delimiter': 'str',
        'claim_mode': 'ClaimMode',
        'count': 'dict(str, int)'
    }

    attribute_map = {
        'storage_claim_id': 'storage_claim_id',
        'folder_path': 'folder_path',
        'delimiter': 'delimiter',
        'claim_mode': 'claim_mode',
        'count': 'count'
    }

    def __init__(self, storage_claim_id=None, folder_path=None, delimiter=None, claim_mode=None, count=None):
        """SharePersistentStorageClaim

        The model defined in huaweicloud sdk

        :param storage_claim_id: WKS存储目录声明ID
        :type storage_claim_id: str
        :param folder_path: 存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/
        :type folder_path: str
        :param delimiter: 路径分隔符
        :type delimiter: str
        :param claim_mode: 
        :type claim_mode: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        :param count: 共享目录的关联用户、用户组数量
        :type count: dict(str, int)
        """
        
        

        self._storage_claim_id = None
        self._folder_path = None
        self._delimiter = None
        self._claim_mode = None
        self._count = None
        self.discriminator = None

        if storage_claim_id is not None:
            self.storage_claim_id = storage_claim_id
        if folder_path is not None:
            self.folder_path = folder_path
        if delimiter is not None:
            self.delimiter = delimiter
        if claim_mode is not None:
            self.claim_mode = claim_mode
        if count is not None:
            self.count = count

    @property
    def storage_claim_id(self):
        """Gets the storage_claim_id of this SharePersistentStorageClaim.

        WKS存储目录声明ID

        :return: The storage_claim_id of this SharePersistentStorageClaim.
        :rtype: str
        """
        return self._storage_claim_id

    @storage_claim_id.setter
    def storage_claim_id(self, storage_claim_id):
        """Sets the storage_claim_id of this SharePersistentStorageClaim.

        WKS存储目录声明ID

        :param storage_claim_id: The storage_claim_id of this SharePersistentStorageClaim.
        :type storage_claim_id: str
        """
        self._storage_claim_id = storage_claim_id

    @property
    def folder_path(self):
        """Gets the folder_path of this SharePersistentStorageClaim.

        存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/

        :return: The folder_path of this SharePersistentStorageClaim.
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this SharePersistentStorageClaim.

        存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/

        :param folder_path: The folder_path of this SharePersistentStorageClaim.
        :type folder_path: str
        """
        self._folder_path = folder_path

    @property
    def delimiter(self):
        """Gets the delimiter of this SharePersistentStorageClaim.

        路径分隔符

        :return: The delimiter of this SharePersistentStorageClaim.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this SharePersistentStorageClaim.

        路径分隔符

        :param delimiter: The delimiter of this SharePersistentStorageClaim.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def claim_mode(self):
        """Gets the claim_mode of this SharePersistentStorageClaim.

        :return: The claim_mode of this SharePersistentStorageClaim.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        """
        return self._claim_mode

    @claim_mode.setter
    def claim_mode(self, claim_mode):
        """Sets the claim_mode of this SharePersistentStorageClaim.

        :param claim_mode: The claim_mode of this SharePersistentStorageClaim.
        :type claim_mode: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        """
        self._claim_mode = claim_mode

    @property
    def count(self):
        """Gets the count of this SharePersistentStorageClaim.

        共享目录的关联用户、用户组数量

        :return: The count of this SharePersistentStorageClaim.
        :rtype: dict(str, int)
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SharePersistentStorageClaim.

        共享目录的关联用户、用户组数量

        :param count: The count of this SharePersistentStorageClaim.
        :type count: dict(str, int)
        """
        self._count = count

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
        if not isinstance(other, SharePersistentStorageClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
