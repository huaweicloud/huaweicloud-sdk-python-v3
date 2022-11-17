# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourceUsagesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resource_ids': 'list[str]'
    }

    attribute_map = {
        'free_resource_ids': 'free_resource_ids'
    }

    def __init__(self, free_resource_ids=None):
        """ListFreeResourceUsagesReq

        The model defined in huaweicloud sdk

        :param free_resource_ids: 资源项ID列表，每个最大64字节。 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。
        :type free_resource_ids: list[str]
        """
        
        

        self._free_resource_ids = None
        self.discriminator = None

        self.free_resource_ids = free_resource_ids

    @property
    def free_resource_ids(self):
        """Gets the free_resource_ids of this ListFreeResourceUsagesReq.

        资源项ID列表，每个最大64字节。 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。

        :return: The free_resource_ids of this ListFreeResourceUsagesReq.
        :rtype: list[str]
        """
        return self._free_resource_ids

    @free_resource_ids.setter
    def free_resource_ids(self, free_resource_ids):
        """Sets the free_resource_ids of this ListFreeResourceUsagesReq.

        资源项ID列表，每个最大64字节。 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。资源项ID来自查询资源包列表接口的响应。

        :param free_resource_ids: The free_resource_ids of this ListFreeResourceUsagesReq.
        :type free_resource_ids: list[str]
        """
        self._free_resource_ids = free_resource_ids

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
        if not isinstance(other, ListFreeResourceUsagesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
