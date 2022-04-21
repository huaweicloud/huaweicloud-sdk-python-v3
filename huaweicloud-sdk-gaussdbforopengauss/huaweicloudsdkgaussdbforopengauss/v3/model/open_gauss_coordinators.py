# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussCoordinators:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'az_code': 'str'
    }

    attribute_map = {
        'az_code': 'az_code'
    }

    def __init__(self, az_code=None):
        """OpenGaussCoordinators

        The model defined in huaweicloud sdk

        :param az_code: 新增CN横向扩容每个节点的可用区。如果需要扩容多个CN，请分别填写待扩容CN所在的可用区。  不同区域的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)。  说明： 扩容后，实例中CN节点的数量必须小于或等于两倍的分片数量。
        :type az_code: str
        """
        
        

        self._az_code = None
        self.discriminator = None

        self.az_code = az_code

    @property
    def az_code(self):
        """Gets the az_code of this OpenGaussCoordinators.

        新增CN横向扩容每个节点的可用区。如果需要扩容多个CN，请分别填写待扩容CN所在的可用区。  不同区域的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)。  说明： 扩容后，实例中CN节点的数量必须小于或等于两倍的分片数量。

        :return: The az_code of this OpenGaussCoordinators.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this OpenGaussCoordinators.

        新增CN横向扩容每个节点的可用区。如果需要扩容多个CN，请分别填写待扩容CN所在的可用区。  不同区域的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)。  说明： 扩容后，实例中CN节点的数量必须小于或等于两倍的分片数量。

        :param az_code: The az_code of this OpenGaussCoordinators.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, OpenGaussCoordinators):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
