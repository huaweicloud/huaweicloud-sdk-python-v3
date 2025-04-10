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
        r"""CreateBucketRequestBody

        The model defined in huaweicloud sdk

        :param location: Region where the bucket will be created. When the endpoint of the CN North-Beijing1 region is used for bucket creation: If **location** is not specified, the bucket will be created in CN North-Beijing1 (cn-north-1) by default. If another region, for example, CN North-Beijing4 (cn-north-4), is specified for **location**, the bucket will be created in the CN North-Beijing4 region. When the endpoint of a region other than CN North-Beijing1 is used for bucket creation, **location** must be set to the region that the used endpoint corresponds to. For example, if **obs.cn-north-4.myhuaweicloud.com is used**, you must set **location** to **cn-north-4**.  For more information, see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint?all).
        :type location: str
        """
        
        

        self._location = None
        self.discriminator = None

        if location is not None:
            self.location = location

    @property
    def location(self):
        r"""Gets the location of this CreateBucketRequestBody.

        Region where the bucket will be created. When the endpoint of the CN North-Beijing1 region is used for bucket creation: If **location** is not specified, the bucket will be created in CN North-Beijing1 (cn-north-1) by default. If another region, for example, CN North-Beijing4 (cn-north-4), is specified for **location**, the bucket will be created in the CN North-Beijing4 region. When the endpoint of a region other than CN North-Beijing1 is used for bucket creation, **location** must be set to the region that the used endpoint corresponds to. For example, if **obs.cn-north-4.myhuaweicloud.com is used**, you must set **location** to **cn-north-4**.  For more information, see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint?all).

        :return: The location of this CreateBucketRequestBody.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this CreateBucketRequestBody.

        Region where the bucket will be created. When the endpoint of the CN North-Beijing1 region is used for bucket creation: If **location** is not specified, the bucket will be created in CN North-Beijing1 (cn-north-1) by default. If another region, for example, CN North-Beijing4 (cn-north-4), is specified for **location**, the bucket will be created in the CN North-Beijing4 region. When the endpoint of a region other than CN North-Beijing1 is used for bucket creation, **location** must be set to the region that the used endpoint corresponds to. For example, if **obs.cn-north-4.myhuaweicloud.com is used**, you must set **location** to **cn-north-4**.  For more information, see [Regions and Endpoints](https://developer.huaweicloud.com/intl/en-us/endpoint?all).

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
