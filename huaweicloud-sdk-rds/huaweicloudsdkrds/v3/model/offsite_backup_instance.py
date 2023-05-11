# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OffsiteBackupInstance:

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
        'name': 'str',
        'source_region': 'str',
        'source_project_id': 'str',
        'datastore': 'ParaGroupDatastore',
        'destination_region': 'str',
        'destination_project_id': 'str',
        'keep_days': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'source_region': 'source_region',
        'source_project_id': 'source_project_id',
        'datastore': 'datastore',
        'destination_region': 'destination_region',
        'destination_project_id': 'destination_project_id',
        'keep_days': 'keep_days'
    }

    def __init__(self, id=None, name=None, source_region=None, source_project_id=None, datastore=None, destination_region=None, destination_project_id=None, keep_days=None):
        """OffsiteBackupInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param source_region: 源区域。
        :type source_region: str
        :param source_project_id: 租户在源区域下的project ID。
        :type source_project_id: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        :param destination_region: 跨区域备份所在区域。
        :type destination_region: str
        :param destination_project_id: 租户在目标区域下的project ID。
        :type destination_project_id: str
        :param keep_days: 跨区域备份保留天数。
        :type keep_days: int
        """
        
        

        self._id = None
        self._name = None
        self._source_region = None
        self._source_project_id = None
        self._datastore = None
        self._destination_region = None
        self._destination_project_id = None
        self._keep_days = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if source_region is not None:
            self.source_region = source_region
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if datastore is not None:
            self.datastore = datastore
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if keep_days is not None:
            self.keep_days = keep_days

    @property
    def id(self):
        """Gets the id of this OffsiteBackupInstance.

        实例ID。

        :return: The id of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OffsiteBackupInstance.

        实例ID。

        :param id: The id of this OffsiteBackupInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this OffsiteBackupInstance.

        创建的实例名称。

        :return: The name of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OffsiteBackupInstance.

        创建的实例名称。

        :param name: The name of this OffsiteBackupInstance.
        :type name: str
        """
        self._name = name

    @property
    def source_region(self):
        """Gets the source_region of this OffsiteBackupInstance.

        源区域。

        :return: The source_region of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this OffsiteBackupInstance.

        源区域。

        :param source_region: The source_region of this OffsiteBackupInstance.
        :type source_region: str
        """
        self._source_region = source_region

    @property
    def source_project_id(self):
        """Gets the source_project_id of this OffsiteBackupInstance.

        租户在源区域下的project ID。

        :return: The source_project_id of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this OffsiteBackupInstance.

        租户在源区域下的project ID。

        :param source_project_id: The source_project_id of this OffsiteBackupInstance.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def datastore(self):
        """Gets the datastore of this OffsiteBackupInstance.

        :return: The datastore of this OffsiteBackupInstance.
        :rtype: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this OffsiteBackupInstance.

        :param datastore: The datastore of this OffsiteBackupInstance.
        :type datastore: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        """
        self._datastore = datastore

    @property
    def destination_region(self):
        """Gets the destination_region of this OffsiteBackupInstance.

        跨区域备份所在区域。

        :return: The destination_region of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this OffsiteBackupInstance.

        跨区域备份所在区域。

        :param destination_region: The destination_region of this OffsiteBackupInstance.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this OffsiteBackupInstance.

        租户在目标区域下的project ID。

        :return: The destination_project_id of this OffsiteBackupInstance.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this OffsiteBackupInstance.

        租户在目标区域下的project ID。

        :param destination_project_id: The destination_project_id of this OffsiteBackupInstance.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def keep_days(self):
        """Gets the keep_days of this OffsiteBackupInstance.

        跨区域备份保留天数。

        :return: The keep_days of this OffsiteBackupInstance.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this OffsiteBackupInstance.

        跨区域备份保留天数。

        :param keep_days: The keep_days of this OffsiteBackupInstance.
        :type keep_days: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, OffsiteBackupInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
