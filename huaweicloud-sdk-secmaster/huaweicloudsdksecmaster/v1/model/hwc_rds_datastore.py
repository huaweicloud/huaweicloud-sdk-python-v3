# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcRdsDatastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'complete_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'complete_version': 'complete_version'
    }

    def __init__(self, type=None, version=None, complete_version=None):
        r"""HwcRdsDatastore

        The model defined in huaweicloud sdk

        :param type: 数据库引擎，不区分大小写： MySQL PostgreSQL SQLServer
        :type type: str
        :param version: 数据库版本。
        :type version: str
        :param complete_version: 数据库完整版本号。仅在数据库引擎是“PostgreSQL”时返回。
        :type complete_version: str
        """
        
        

        self._type = None
        self._version = None
        self._complete_version = None
        self.discriminator = None

        self.type = type
        self.version = version
        if complete_version is not None:
            self.complete_version = complete_version

    @property
    def type(self):
        r"""Gets the type of this HwcRdsDatastore.

        数据库引擎，不区分大小写： MySQL PostgreSQL SQLServer

        :return: The type of this HwcRdsDatastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HwcRdsDatastore.

        数据库引擎，不区分大小写： MySQL PostgreSQL SQLServer

        :param type: The type of this HwcRdsDatastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this HwcRdsDatastore.

        数据库版本。

        :return: The version of this HwcRdsDatastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HwcRdsDatastore.

        数据库版本。

        :param version: The version of this HwcRdsDatastore.
        :type version: str
        """
        self._version = version

    @property
    def complete_version(self):
        r"""Gets the complete_version of this HwcRdsDatastore.

        数据库完整版本号。仅在数据库引擎是“PostgreSQL”时返回。

        :return: The complete_version of this HwcRdsDatastore.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        r"""Sets the complete_version of this HwcRdsDatastore.

        数据库完整版本号。仅在数据库引擎是“PostgreSQL”时返回。

        :param complete_version: The complete_version of this HwcRdsDatastore.
        :type complete_version: str
        """
        self._complete_version = complete_version

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcRdsDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
