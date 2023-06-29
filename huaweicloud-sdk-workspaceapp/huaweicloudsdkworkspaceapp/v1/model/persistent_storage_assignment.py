# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistentStorageAssignment:

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
        'storage_metadata': 'StorageMetadata',
        'policy_statement': 'PolicyStatement',
        'attachment': 'Attachment'
    }

    attribute_map = {
        'storage_claim_id': 'storage_claim_id',
        'folder_path': 'folder_path',
        'delimiter': 'delimiter',
        'claim_mode': 'claim_mode',
        'storage_metadata': 'storage_metadata',
        'policy_statement': 'policy_statement',
        'attachment': 'attachment'
    }

    def __init__(self, storage_claim_id=None, folder_path=None, delimiter=None, claim_mode=None, storage_metadata=None, policy_statement=None, attachment=None):
        """PersistentStorageAssignment

        The model defined in huaweicloud sdk

        :param storage_claim_id: WKS存储目录声明ID
        :type storage_claim_id: str
        :param folder_path: 存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/
        :type folder_path: str
        :param delimiter: 路径分隔符
        :type delimiter: str
        :param claim_mode: 
        :type claim_mode: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        :param storage_metadata: 
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        :param policy_statement: 
        :type policy_statement: :class:`huaweicloudsdkworkspaceapp.v1.PolicyStatement`
        :param attachment: 
        :type attachment: :class:`huaweicloudsdkworkspaceapp.v1.Attachment`
        """
        
        

        self._storage_claim_id = None
        self._folder_path = None
        self._delimiter = None
        self._claim_mode = None
        self._storage_metadata = None
        self._policy_statement = None
        self._attachment = None
        self.discriminator = None

        if storage_claim_id is not None:
            self.storage_claim_id = storage_claim_id
        if folder_path is not None:
            self.folder_path = folder_path
        if delimiter is not None:
            self.delimiter = delimiter
        if claim_mode is not None:
            self.claim_mode = claim_mode
        if storage_metadata is not None:
            self.storage_metadata = storage_metadata
        if policy_statement is not None:
            self.policy_statement = policy_statement
        if attachment is not None:
            self.attachment = attachment

    @property
    def storage_claim_id(self):
        """Gets the storage_claim_id of this PersistentStorageAssignment.

        WKS存储目录声明ID

        :return: The storage_claim_id of this PersistentStorageAssignment.
        :rtype: str
        """
        return self._storage_claim_id

    @storage_claim_id.setter
    def storage_claim_id(self, storage_claim_id):
        """Sets the storage_claim_id of this PersistentStorageAssignment.

        WKS存储目录声明ID

        :param storage_claim_id: The storage_claim_id of this PersistentStorageAssignment.
        :type storage_claim_id: str
        """
        self._storage_claim_id = storage_claim_id

    @property
    def folder_path(self):
        """Gets the folder_path of this PersistentStorageAssignment.

        存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/

        :return: The folder_path of this PersistentStorageAssignment.
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this PersistentStorageAssignment.

        存储对象路径 注: path是对象在系统中的完整路径 例如系统中存在如下目录结构的数据. SFS-Tmp: └─shares   ├─image   └─video image的路径: shares/image/ video的路径: shares/video/

        :param folder_path: The folder_path of this PersistentStorageAssignment.
        :type folder_path: str
        """
        self._folder_path = folder_path

    @property
    def delimiter(self):
        """Gets the delimiter of this PersistentStorageAssignment.

        路径分隔符

        :return: The delimiter of this PersistentStorageAssignment.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this PersistentStorageAssignment.

        路径分隔符

        :param delimiter: The delimiter of this PersistentStorageAssignment.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def claim_mode(self):
        """Gets the claim_mode of this PersistentStorageAssignment.

        :return: The claim_mode of this PersistentStorageAssignment.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        """
        return self._claim_mode

    @claim_mode.setter
    def claim_mode(self, claim_mode):
        """Sets the claim_mode of this PersistentStorageAssignment.

        :param claim_mode: The claim_mode of this PersistentStorageAssignment.
        :type claim_mode: :class:`huaweicloudsdkworkspaceapp.v1.ClaimMode`
        """
        self._claim_mode = claim_mode

    @property
    def storage_metadata(self):
        """Gets the storage_metadata of this PersistentStorageAssignment.

        :return: The storage_metadata of this PersistentStorageAssignment.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        """
        return self._storage_metadata

    @storage_metadata.setter
    def storage_metadata(self, storage_metadata):
        """Sets the storage_metadata of this PersistentStorageAssignment.

        :param storage_metadata: The storage_metadata of this PersistentStorageAssignment.
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.StorageMetadata`
        """
        self._storage_metadata = storage_metadata

    @property
    def policy_statement(self):
        """Gets the policy_statement of this PersistentStorageAssignment.

        :return: The policy_statement of this PersistentStorageAssignment.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PolicyStatement`
        """
        return self._policy_statement

    @policy_statement.setter
    def policy_statement(self, policy_statement):
        """Sets the policy_statement of this PersistentStorageAssignment.

        :param policy_statement: The policy_statement of this PersistentStorageAssignment.
        :type policy_statement: :class:`huaweicloudsdkworkspaceapp.v1.PolicyStatement`
        """
        self._policy_statement = policy_statement

    @property
    def attachment(self):
        """Gets the attachment of this PersistentStorageAssignment.

        :return: The attachment of this PersistentStorageAssignment.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Attachment`
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this PersistentStorageAssignment.

        :param attachment: The attachment of this PersistentStorageAssignment.
        :type attachment: :class:`huaweicloudsdkworkspaceapp.v1.Attachment`
        """
        self._attachment = attachment

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
        if not isinstance(other, PersistentStorageAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
