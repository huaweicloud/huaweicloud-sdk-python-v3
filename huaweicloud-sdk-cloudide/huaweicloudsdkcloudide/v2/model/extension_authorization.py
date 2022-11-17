# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionAuthorization:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_version': 'str',
        'identifier': 'str',
        'instance_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'extension_version': 'extension_version',
        'identifier': 'identifier',
        'instance_id': 'instance_id',
        'status': 'status'
    }

    def __init__(self, extension_version=None, identifier=None, instance_id=None, status=None):
        """ExtensionAuthorization

        The model defined in huaweicloud sdk

        :param extension_version: 插件版本
        :type extension_version: str
        :param identifier: 插件标识(发布者.插件名)
        :type identifier: str
        :param instance_id: CloudIDE实例ID
        :type instance_id: str
        :param status: 插件状态。 - AGREE 同意 - REJECT 不同意 - UNKNOWN 未知（下次重新询问）
        :type status: str
        """
        
        

        self._extension_version = None
        self._identifier = None
        self._instance_id = None
        self._status = None
        self.discriminator = None

        self.extension_version = extension_version
        self.identifier = identifier
        if instance_id is not None:
            self.instance_id = instance_id
        self.status = status

    @property
    def extension_version(self):
        """Gets the extension_version of this ExtensionAuthorization.

        插件版本

        :return: The extension_version of this ExtensionAuthorization.
        :rtype: str
        """
        return self._extension_version

    @extension_version.setter
    def extension_version(self, extension_version):
        """Sets the extension_version of this ExtensionAuthorization.

        插件版本

        :param extension_version: The extension_version of this ExtensionAuthorization.
        :type extension_version: str
        """
        self._extension_version = extension_version

    @property
    def identifier(self):
        """Gets the identifier of this ExtensionAuthorization.

        插件标识(发布者.插件名)

        :return: The identifier of this ExtensionAuthorization.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExtensionAuthorization.

        插件标识(发布者.插件名)

        :param identifier: The identifier of this ExtensionAuthorization.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def instance_id(self):
        """Gets the instance_id of this ExtensionAuthorization.

        CloudIDE实例ID

        :return: The instance_id of this ExtensionAuthorization.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExtensionAuthorization.

        CloudIDE实例ID

        :param instance_id: The instance_id of this ExtensionAuthorization.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this ExtensionAuthorization.

        插件状态。 - AGREE 同意 - REJECT 不同意 - UNKNOWN 未知（下次重新询问）

        :return: The status of this ExtensionAuthorization.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExtensionAuthorization.

        插件状态。 - AGREE 同意 - REJECT 不同意 - UNKNOWN 未知（下次重新询问）

        :param status: The status of this ExtensionAuthorization.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ExtensionAuthorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
