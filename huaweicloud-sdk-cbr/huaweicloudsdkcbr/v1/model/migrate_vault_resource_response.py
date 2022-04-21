# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateVaultResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'migrated_resources': 'list[str]'
    }

    attribute_map = {
        'migrated_resources': 'migrated_resources'
    }

    def __init__(self, migrated_resources=None):
        """MigrateVaultResourceResponse

        The model defined in huaweicloud sdk

        :param migrated_resources: 
        :type migrated_resources: list[str]
        """
        
        super(MigrateVaultResourceResponse, self).__init__()

        self._migrated_resources = None
        self.discriminator = None

        if migrated_resources is not None:
            self.migrated_resources = migrated_resources

    @property
    def migrated_resources(self):
        """Gets the migrated_resources of this MigrateVaultResourceResponse.

        

        :return: The migrated_resources of this MigrateVaultResourceResponse.
        :rtype: list[str]
        """
        return self._migrated_resources

    @migrated_resources.setter
    def migrated_resources(self, migrated_resources):
        """Sets the migrated_resources of this MigrateVaultResourceResponse.

        

        :param migrated_resources: The migrated_resources of this MigrateVaultResourceResponse.
        :type migrated_resources: list[str]
        """
        self._migrated_resources = migrated_resources

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
        if not isinstance(other, MigrateVaultResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
