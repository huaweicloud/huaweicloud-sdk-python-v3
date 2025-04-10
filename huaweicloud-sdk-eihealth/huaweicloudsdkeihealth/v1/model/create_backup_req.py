# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBackupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'sub_paths': 'list[str]',
        'storage_type': 'StorageType',
        'delete_archived_data': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'sub_paths': 'sub_paths',
        'storage_type': 'storage_type',
        'delete_archived_data': 'delete_archived_data'
    }

    def __init__(self, description=None, name=None, sub_paths=None, storage_type=None, delete_archived_data=None):
        r"""CreateBackupReq

        The model defined in huaweicloud sdk

        :param description: 归档描述，最大长度为1000
        :type description: str
        :param name: 归档名称,最大长度为100
        :type name: str
        :param sub_paths: 归档路径集
        :type sub_paths: list[str]
        :param storage_type: 
        :type storage_type: :class:`huaweicloudsdkeihealth.v1.StorageType`
        :param delete_archived_data: 是否删除已归档数据
        :type delete_archived_data: bool
        """
        
        

        self._description = None
        self._name = None
        self._sub_paths = None
        self._storage_type = None
        self._delete_archived_data = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.sub_paths = sub_paths
        if storage_type is not None:
            self.storage_type = storage_type
        if delete_archived_data is not None:
            self.delete_archived_data = delete_archived_data

    @property
    def description(self):
        r"""Gets the description of this CreateBackupReq.

        归档描述，最大长度为1000

        :return: The description of this CreateBackupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateBackupReq.

        归档描述，最大长度为1000

        :param description: The description of this CreateBackupReq.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreateBackupReq.

        归档名称,最大长度为100

        :return: The name of this CreateBackupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBackupReq.

        归档名称,最大长度为100

        :param name: The name of this CreateBackupReq.
        :type name: str
        """
        self._name = name

    @property
    def sub_paths(self):
        r"""Gets the sub_paths of this CreateBackupReq.

        归档路径集

        :return: The sub_paths of this CreateBackupReq.
        :rtype: list[str]
        """
        return self._sub_paths

    @sub_paths.setter
    def sub_paths(self, sub_paths):
        r"""Sets the sub_paths of this CreateBackupReq.

        归档路径集

        :param sub_paths: The sub_paths of this CreateBackupReq.
        :type sub_paths: list[str]
        """
        self._sub_paths = sub_paths

    @property
    def storage_type(self):
        r"""Gets the storage_type of this CreateBackupReq.

        :return: The storage_type of this CreateBackupReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.StorageType`
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this CreateBackupReq.

        :param storage_type: The storage_type of this CreateBackupReq.
        :type storage_type: :class:`huaweicloudsdkeihealth.v1.StorageType`
        """
        self._storage_type = storage_type

    @property
    def delete_archived_data(self):
        r"""Gets the delete_archived_data of this CreateBackupReq.

        是否删除已归档数据

        :return: The delete_archived_data of this CreateBackupReq.
        :rtype: bool
        """
        return self._delete_archived_data

    @delete_archived_data.setter
    def delete_archived_data(self, delete_archived_data):
        r"""Sets the delete_archived_data of this CreateBackupReq.

        是否删除已归档数据

        :param delete_archived_data: The delete_archived_data of this CreateBackupReq.
        :type delete_archived_data: bool
        """
        self._delete_archived_data = delete_archived_data

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
        if not isinstance(other, CreateBackupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
