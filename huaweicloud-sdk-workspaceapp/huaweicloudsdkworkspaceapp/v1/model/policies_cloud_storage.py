# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesCloudStorage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_storage_enable': 'bool',
        'options': 'CloudStorageOptions'
    }

    attribute_map = {
        'cloud_storage_enable': 'cloud_storage_enable',
        'options': 'options'
    }

    def __init__(self, cloud_storage_enable=None, options=None):
        r"""PoliciesCloudStorage

        The model defined in huaweicloud sdk

        :param cloud_storage_enable: 云存储配置开关： false: 表示关闭 true: 表示开启
        :type cloud_storage_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.CloudStorageOptions`
        """
        
        

        self._cloud_storage_enable = None
        self._options = None
        self.discriminator = None

        if cloud_storage_enable is not None:
            self.cloud_storage_enable = cloud_storage_enable
        if options is not None:
            self.options = options

    @property
    def cloud_storage_enable(self):
        r"""Gets the cloud_storage_enable of this PoliciesCloudStorage.

        云存储配置开关： false: 表示关闭 true: 表示开启

        :return: The cloud_storage_enable of this PoliciesCloudStorage.
        :rtype: bool
        """
        return self._cloud_storage_enable

    @cloud_storage_enable.setter
    def cloud_storage_enable(self, cloud_storage_enable):
        r"""Sets the cloud_storage_enable of this PoliciesCloudStorage.

        云存储配置开关： false: 表示关闭 true: 表示开启

        :param cloud_storage_enable: The cloud_storage_enable of this PoliciesCloudStorage.
        :type cloud_storage_enable: bool
        """
        self._cloud_storage_enable = cloud_storage_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesCloudStorage.

        :return: The options of this PoliciesCloudStorage.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CloudStorageOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesCloudStorage.

        :param options: The options of this PoliciesCloudStorage.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.CloudStorageOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesCloudStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
