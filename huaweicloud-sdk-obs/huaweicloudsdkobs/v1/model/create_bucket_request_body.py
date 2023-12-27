# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBucketRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CreateBucketConfiguration"

    sensitive_list = []

    openapi_types = {
        'location': 'str'
    }

    attribute_map = {
        'location': 'Location'
    }

    def __init__(self, location=None):
        """CreateBucketRequestBody

        The model defined in huaweicloud sdk

        :param location: 指定Bucket在哪个区域被创建。 使用华北-北京一的终端节点创桶时 不携带Location，桶将默认创建在华北-北京一（cn-north-1） 在Location中指定其它区域，例如华北-北京四（cn-north-4），桶将创建在指定区域 使用华北-北京一以外其它区域的终端节点创桶时，必须携带Location，并且Location只能指定为该终端节点对应的区域。 例如使用obs.cn-north-4.myhuaweicloud.com终端节点创桶时，必须指定Location为cn-north-4。  有关OBS区域和终端节点的更多信息，请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)。 
        :type location: str
        """
        
        

        self._location = None
        self.discriminator = None

        if location is not None:
            self.location = location

    @property
    def location(self):
        """Gets the location of this CreateBucketRequestBody.

        指定Bucket在哪个区域被创建。 使用华北-北京一的终端节点创桶时 不携带Location，桶将默认创建在华北-北京一（cn-north-1） 在Location中指定其它区域，例如华北-北京四（cn-north-4），桶将创建在指定区域 使用华北-北京一以外其它区域的终端节点创桶时，必须携带Location，并且Location只能指定为该终端节点对应的区域。 例如使用obs.cn-north-4.myhuaweicloud.com终端节点创桶时，必须指定Location为cn-north-4。  有关OBS区域和终端节点的更多信息，请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)。 

        :return: The location of this CreateBucketRequestBody.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateBucketRequestBody.

        指定Bucket在哪个区域被创建。 使用华北-北京一的终端节点创桶时 不携带Location，桶将默认创建在华北-北京一（cn-north-1） 在Location中指定其它区域，例如华北-北京四（cn-north-4），桶将创建在指定区域 使用华北-北京一以外其它区域的终端节点创桶时，必须携带Location，并且Location只能指定为该终端节点对应的区域。 例如使用obs.cn-north-4.myhuaweicloud.com终端节点创桶时，必须指定Location为cn-north-4。  有关OBS区域和终端节点的更多信息，请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?OBS)。 

        :param location: The location of this CreateBucketRequestBody.
        :type location: str
        """
        self._location = location

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
        if not isinstance(other, CreateBucketRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
