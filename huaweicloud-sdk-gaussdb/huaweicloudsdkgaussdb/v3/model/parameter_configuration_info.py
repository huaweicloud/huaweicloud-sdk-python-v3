# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterConfigurationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_version_name': 'str',
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'datastore_version_name': 'datastore_version_name',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, datastore_version_name=None, datastore_name=None, created=None, updated=None):
        """ParameterConfigurationInfo

        The model defined in huaweicloud sdk

        :param datastore_version_name: 数据库版本名称。
        :type datastore_version_name: str
        :param datastore_name: 数据库名称。
        :type datastore_name: str
        :param created: 创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type updated: str
        """
        
        

        self._datastore_version_name = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if datastore_version_name is not None:
            self.datastore_version_name = datastore_version_name
        if datastore_name is not None:
            self.datastore_name = datastore_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def datastore_version_name(self):
        """Gets the datastore_version_name of this ParameterConfigurationInfo.

        数据库版本名称。

        :return: The datastore_version_name of this ParameterConfigurationInfo.
        :rtype: str
        """
        return self._datastore_version_name

    @datastore_version_name.setter
    def datastore_version_name(self, datastore_version_name):
        """Sets the datastore_version_name of this ParameterConfigurationInfo.

        数据库版本名称。

        :param datastore_version_name: The datastore_version_name of this ParameterConfigurationInfo.
        :type datastore_version_name: str
        """
        self._datastore_version_name = datastore_version_name

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ParameterConfigurationInfo.

        数据库名称。

        :return: The datastore_name of this ParameterConfigurationInfo.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ParameterConfigurationInfo.

        数据库名称。

        :param datastore_name: The datastore_name of this ParameterConfigurationInfo.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ParameterConfigurationInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The created of this ParameterConfigurationInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ParameterConfigurationInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param created: The created of this ParameterConfigurationInfo.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ParameterConfigurationInfo.

        更新时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The updated of this ParameterConfigurationInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ParameterConfigurationInfo.

        更新时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param updated: The updated of this ParameterConfigurationInfo.
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
        if not isinstance(other, ParameterConfigurationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
