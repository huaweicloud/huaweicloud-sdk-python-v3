# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceDatabaseVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore': 'InstanceDatabaseVersionInfo',
        'upgrade_flag': 'bool'
    }

    attribute_map = {
        'datastore': 'datastore',
        'upgrade_flag': 'upgrade_flag'
    }

    def __init__(self, datastore=None, upgrade_flag=None):
        r"""ShowInstanceDatabaseVersionResponse

        The model defined in huaweicloud sdk

        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.InstanceDatabaseVersionInfo`
        :param upgrade_flag: 是否可升级。 - true：是。 - false：否。
        :type upgrade_flag: bool
        """
        
        super(ShowInstanceDatabaseVersionResponse, self).__init__()

        self._datastore = None
        self._upgrade_flag = None
        self.discriminator = None

        if datastore is not None:
            self.datastore = datastore
        if upgrade_flag is not None:
            self.upgrade_flag = upgrade_flag

    @property
    def datastore(self):
        r"""Gets the datastore of this ShowInstanceDatabaseVersionResponse.

        :return: The datastore of this ShowInstanceDatabaseVersionResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.InstanceDatabaseVersionInfo`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ShowInstanceDatabaseVersionResponse.

        :param datastore: The datastore of this ShowInstanceDatabaseVersionResponse.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.InstanceDatabaseVersionInfo`
        """
        self._datastore = datastore

    @property
    def upgrade_flag(self):
        r"""Gets the upgrade_flag of this ShowInstanceDatabaseVersionResponse.

        是否可升级。 - true：是。 - false：否。

        :return: The upgrade_flag of this ShowInstanceDatabaseVersionResponse.
        :rtype: bool
        """
        return self._upgrade_flag

    @upgrade_flag.setter
    def upgrade_flag(self, upgrade_flag):
        r"""Sets the upgrade_flag of this ShowInstanceDatabaseVersionResponse.

        是否可升级。 - true：是。 - false：否。

        :param upgrade_flag: The upgrade_flag of this ShowInstanceDatabaseVersionResponse.
        :type upgrade_flag: bool
        """
        self._upgrade_flag = upgrade_flag

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
        if not isinstance(other, ShowInstanceDatabaseVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
