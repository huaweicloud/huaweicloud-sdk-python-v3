# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomConnectorFromOpenapiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_version_id': 'str',
        'created_time': 'datetime',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'updated_time': 'datetime',
        'version': 'str'
    }

    attribute_map = {
        'connector_version_id': 'connector_version_id',
        'created_time': 'created_time',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'updated_time': 'updated_time',
        'version': 'version'
    }

    def __init__(self, connector_version_id=None, created_time=None, description=None, id=None, name=None, updated_time=None, version=None):
        r"""CreateCustomConnectorFromOpenapiResponse

        The model defined in huaweicloud sdk

        :param connector_version_id: 自定义连接器版本ID
        :type connector_version_id: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param description: 
        :type description: str
        :param id: 自定义连接器ID
        :type id: str
        :param name: 自定义连接器名称
        :type name: str
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param version: 
        :type version: str
        """
        
        super(CreateCustomConnectorFromOpenapiResponse, self).__init__()

        self._connector_version_id = None
        self._created_time = None
        self._description = None
        self._id = None
        self._name = None
        self._updated_time = None
        self._version = None
        self.discriminator = None

        if connector_version_id is not None:
            self.connector_version_id = connector_version_id
        if created_time is not None:
            self.created_time = created_time
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if updated_time is not None:
            self.updated_time = updated_time
        if version is not None:
            self.version = version

    @property
    def connector_version_id(self):
        r"""Gets the connector_version_id of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器版本ID

        :return: The connector_version_id of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: str
        """
        return self._connector_version_id

    @connector_version_id.setter
    def connector_version_id(self, connector_version_id):
        r"""Sets the connector_version_id of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器版本ID

        :param connector_version_id: The connector_version_id of this CreateCustomConnectorFromOpenapiResponse.
        :type connector_version_id: str
        """
        self._connector_version_id = connector_version_id

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateCustomConnectorFromOpenapiResponse.

        创建时间

        :return: The created_time of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateCustomConnectorFromOpenapiResponse.

        创建时间

        :param created_time: The created_time of this CreateCustomConnectorFromOpenapiResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def description(self):
        r"""Gets the description of this CreateCustomConnectorFromOpenapiResponse.

        :return: The description of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCustomConnectorFromOpenapiResponse.

        :param description: The description of this CreateCustomConnectorFromOpenapiResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器ID

        :return: The id of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器ID

        :param id: The id of this CreateCustomConnectorFromOpenapiResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器名称

        :return: The name of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCustomConnectorFromOpenapiResponse.

        自定义连接器名称

        :param name: The name of this CreateCustomConnectorFromOpenapiResponse.
        :type name: str
        """
        self._name = name

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CreateCustomConnectorFromOpenapiResponse.

        修改时间

        :return: The updated_time of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CreateCustomConnectorFromOpenapiResponse.

        修改时间

        :param updated_time: The updated_time of this CreateCustomConnectorFromOpenapiResponse.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def version(self):
        r"""Gets the version of this CreateCustomConnectorFromOpenapiResponse.

        :return: The version of this CreateCustomConnectorFromOpenapiResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateCustomConnectorFromOpenapiResponse.

        :param version: The version of this CreateCustomConnectorFromOpenapiResponse.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, CreateCustomConnectorFromOpenapiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
