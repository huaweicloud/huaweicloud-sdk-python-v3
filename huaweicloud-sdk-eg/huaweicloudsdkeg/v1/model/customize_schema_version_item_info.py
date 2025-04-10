# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSchemaVersionItemInfo:

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
        'version': 'int',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, version=None, created_time=None, updated_time=None):
        r"""CustomizeSchemaVersionItemInfo

        The model defined in huaweicloud sdk

        :param id: 事件模型版本ID
        :type id: str
        :param version: 事件模型版本号
        :type version: int
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        """
        
        

        self._id = None
        self._version = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        r"""Gets the id of this CustomizeSchemaVersionItemInfo.

        事件模型版本ID

        :return: The id of this CustomizeSchemaVersionItemInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomizeSchemaVersionItemInfo.

        事件模型版本ID

        :param id: The id of this CustomizeSchemaVersionItemInfo.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this CustomizeSchemaVersionItemInfo.

        事件模型版本号

        :return: The version of this CustomizeSchemaVersionItemInfo.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CustomizeSchemaVersionItemInfo.

        事件模型版本号

        :param version: The version of this CustomizeSchemaVersionItemInfo.
        :type version: int
        """
        self._version = version

    @property
    def created_time(self):
        r"""Gets the created_time of this CustomizeSchemaVersionItemInfo.

        创建时间

        :return: The created_time of this CustomizeSchemaVersionItemInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CustomizeSchemaVersionItemInfo.

        创建时间

        :param created_time: The created_time of this CustomizeSchemaVersionItemInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CustomizeSchemaVersionItemInfo.

        更新时间

        :return: The updated_time of this CustomizeSchemaVersionItemInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CustomizeSchemaVersionItemInfo.

        更新时间

        :param updated_time: The updated_time of this CustomizeSchemaVersionItemInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, CustomizeSchemaVersionItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
