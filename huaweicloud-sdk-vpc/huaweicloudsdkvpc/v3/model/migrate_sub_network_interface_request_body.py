# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateSubNetworkInterfaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'migration_info': 'MigrateSubNetworkInterfaceOption'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'migration_info': 'migration_info'
    }

    def __init__(self, dry_run=None, migration_info=None):
        """MigrateSubNetworkInterfaceRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。
        :type dry_run: bool
        :param migration_info: 
        :type migration_info: :class:`huaweicloudsdkvpc.v3.MigrateSubNetworkInterfaceOption`
        """
        
        

        self._dry_run = None
        self._migration_info = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.migration_info = migration_info

    @property
    def dry_run(self):
        """Gets the dry_run of this MigrateSubNetworkInterfaceRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。

        :return: The dry_run of this MigrateSubNetworkInterfaceRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this MigrateSubNetworkInterfaceRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。

        :param dry_run: The dry_run of this MigrateSubNetworkInterfaceRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def migration_info(self):
        """Gets the migration_info of this MigrateSubNetworkInterfaceRequestBody.


        :return: The migration_info of this MigrateSubNetworkInterfaceRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.MigrateSubNetworkInterfaceOption`
        """
        return self._migration_info

    @migration_info.setter
    def migration_info(self, migration_info):
        """Sets the migration_info of this MigrateSubNetworkInterfaceRequestBody.


        :param migration_info: The migration_info of this MigrateSubNetworkInterfaceRequestBody.
        :type migration_info: :class:`huaweicloudsdkvpc.v3.MigrateSubNetworkInterfaceOption`
        """
        self._migration_info = migration_info

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
        if not isinstance(other, MigrateSubNetworkInterfaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
