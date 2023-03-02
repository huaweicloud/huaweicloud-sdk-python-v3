# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'bucket_name': 'str',
        'object_key': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'bucket_name': 'bucket_name',
        'object_key': 'object_key'
    }

    def __init__(self, region_name=None, bucket_name=None, object_key=None):
        """ObsLocation

        The model defined in huaweicloud sdk

        :param region_name: **参数说明**：OBS所在区域。您可以从[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)中查询服务的终端节点。 **取值范围**：长度不超过256，只允许字母、数字、连接符（-）的组合。
        :type region_name: str
        :param bucket_name: **参数说明**：OBS桶名称。 **取值范围**：长度最小为3，最大为63，只允许小写字母、数字、连接符（-）、英文点（.）的组合。
        :type bucket_name: str
        :param object_key: **参数说明**：OBS对象名称(包含文件夹路径)。 **取值范围**：长度不超过1024。
        :type object_key: str
        """
        
        

        self._region_name = None
        self._bucket_name = None
        self._object_key = None
        self.discriminator = None

        self.region_name = region_name
        self.bucket_name = bucket_name
        self.object_key = object_key

    @property
    def region_name(self):
        """Gets the region_name of this ObsLocation.

        **参数说明**：OBS所在区域。您可以从[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)中查询服务的终端节点。 **取值范围**：长度不超过256，只允许字母、数字、连接符（-）的组合。

        :return: The region_name of this ObsLocation.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ObsLocation.

        **参数说明**：OBS所在区域。您可以从[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)中查询服务的终端节点。 **取值范围**：长度不超过256，只允许字母、数字、连接符（-）的组合。

        :param region_name: The region_name of this ObsLocation.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsLocation.

        **参数说明**：OBS桶名称。 **取值范围**：长度最小为3，最大为63，只允许小写字母、数字、连接符（-）、英文点（.）的组合。

        :return: The bucket_name of this ObsLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsLocation.

        **参数说明**：OBS桶名称。 **取值范围**：长度最小为3，最大为63，只允许小写字母、数字、连接符（-）、英文点（.）的组合。

        :param bucket_name: The bucket_name of this ObsLocation.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this ObsLocation.

        **参数说明**：OBS对象名称(包含文件夹路径)。 **取值范围**：长度不超过1024。

        :return: The object_key of this ObsLocation.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this ObsLocation.

        **参数说明**：OBS对象名称(包含文件夹路径)。 **取值范围**：长度不超过1024。

        :param object_key: The object_key of this ObsLocation.
        :type object_key: str
        """
        self._object_key = object_key

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
        if not isinstance(other, ObsLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
