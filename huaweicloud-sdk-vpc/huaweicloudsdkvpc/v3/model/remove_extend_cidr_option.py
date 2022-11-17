# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveExtendCidrOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extend_cidrs': 'list[str]'
    }

    attribute_map = {
        'extend_cidrs': 'extend_cidrs'
    }

    def __init__(self, extend_cidrs=None):
        """RemoveExtendCidrOption

        The model defined in huaweicloud sdk

        :param extend_cidrs: 功能说明：移除VPC扩展网段 取值范围：该VPC已经存在的扩展网段 约束：移除扩展网段前，请先清理该VPC下对应cidr范围内的subnet；当前只支持一个一个移除
        :type extend_cidrs: list[str]
        """
        
        

        self._extend_cidrs = None
        self.discriminator = None

        self.extend_cidrs = extend_cidrs

    @property
    def extend_cidrs(self):
        """Gets the extend_cidrs of this RemoveExtendCidrOption.

        功能说明：移除VPC扩展网段 取值范围：该VPC已经存在的扩展网段 约束：移除扩展网段前，请先清理该VPC下对应cidr范围内的subnet；当前只支持一个一个移除

        :return: The extend_cidrs of this RemoveExtendCidrOption.
        :rtype: list[str]
        """
        return self._extend_cidrs

    @extend_cidrs.setter
    def extend_cidrs(self, extend_cidrs):
        """Sets the extend_cidrs of this RemoveExtendCidrOption.

        功能说明：移除VPC扩展网段 取值范围：该VPC已经存在的扩展网段 约束：移除扩展网段前，请先清理该VPC下对应cidr范围内的subnet；当前只支持一个一个移除

        :param extend_cidrs: The extend_cidrs of this RemoveExtendCidrOption.
        :type extend_cidrs: list[str]
        """
        self._extend_cidrs = extend_cidrs

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
        if not isinstance(other, RemoveExtendCidrOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
