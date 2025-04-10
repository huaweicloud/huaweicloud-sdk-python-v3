# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationSummary2:

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
        'description': 'str',
        'datastore': 'DatastoreResult',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore': 'datastore',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, description=None, datastore=None, created=None, updated=None):
        r"""ConfigurationSummary2

        The model defined in huaweicloud sdk

        :param id: 参数组ID。
        :type id: str
        :param name: 参数组名称。
        :type name: str
        :param description: 参数组描述。
        :type description: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.DatastoreResult`
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量。
        :type updated: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if datastore is not None:
            self.datastore = datastore
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        r"""Gets the id of this ConfigurationSummary2.

        参数组ID。

        :return: The id of this ConfigurationSummary2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConfigurationSummary2.

        参数组ID。

        :param id: The id of this ConfigurationSummary2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ConfigurationSummary2.

        参数组名称。

        :return: The name of this ConfigurationSummary2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationSummary2.

        参数组名称。

        :param name: The name of this ConfigurationSummary2.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ConfigurationSummary2.

        参数组描述。

        :return: The description of this ConfigurationSummary2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationSummary2.

        参数组描述。

        :param description: The description of this ConfigurationSummary2.
        :type description: str
        """
        self._description = description

    @property
    def datastore(self):
        r"""Gets the datastore of this ConfigurationSummary2.

        :return: The datastore of this ConfigurationSummary2.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ConfigurationSummary2.

        :param datastore: The datastore of this ConfigurationSummary2.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.DatastoreResult`
        """
        self._datastore = datastore

    @property
    def created(self):
        r"""Gets the created of this ConfigurationSummary2.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量。

        :return: The created of this ConfigurationSummary2.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ConfigurationSummary2.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量。

        :param created: The created of this ConfigurationSummary2.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ConfigurationSummary2.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量。

        :return: The updated of this ConfigurationSummary2.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ConfigurationSummary2.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量。

        :param updated: The updated of this ConfigurationSummary2.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, ConfigurationSummary2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
