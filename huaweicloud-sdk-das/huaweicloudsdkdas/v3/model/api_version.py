# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiVersion:

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
        'status': 'str',
        'updated': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, id=None, status=None, updated=None, version=None):
        """ApiVersion

        The model defined in huaweicloud sdk

        :param id: API版本号，如v3。
        :type id: str
        :param status: 版本状态。 取值“CURRENT”，表示该版本为主推版本。取值“SUPPORTED”，表示为老版本，但是现在还继续支持。 取值“DEPRECATED”，表示为废弃版本，存在后续删除的可能。
        :type status: str
        :param updated: 版本发布时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。
        :type updated: str
        :param version: API的微版本，如果不支持微版本，则为空
        :type version: str
        """
        
        

        self._id = None
        self._status = None
        self._updated = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.updated = updated
        self.version = version

    @property
    def id(self):
        """Gets the id of this ApiVersion.

        API版本号，如v3。

        :return: The id of this ApiVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiVersion.

        API版本号，如v3。

        :param id: The id of this ApiVersion.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ApiVersion.

        版本状态。 取值“CURRENT”，表示该版本为主推版本。取值“SUPPORTED”，表示为老版本，但是现在还继续支持。 取值“DEPRECATED”，表示为废弃版本，存在后续删除的可能。

        :return: The status of this ApiVersion.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiVersion.

        版本状态。 取值“CURRENT”，表示该版本为主推版本。取值“SUPPORTED”，表示为老版本，但是现在还继续支持。 取值“DEPRECATED”，表示为废弃版本，存在后续删除的可能。

        :param status: The status of this ApiVersion.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ApiVersion.

        版本发布时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。

        :return: The updated of this ApiVersion.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApiVersion.

        版本发布时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。

        :param updated: The updated of this ApiVersion.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this ApiVersion.

        API的微版本，如果不支持微版本，则为空

        :return: The version of this ApiVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiVersion.

        API的微版本，如果不支持微版本，则为空

        :param version: The version of this ApiVersion.
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
        if not isinstance(other, ApiVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
