# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTargetParamsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group': 'str',
        'params': 'list[ParamsReqBean]'
    }

    attribute_map = {
        'group': 'group',
        'params': 'params'
    }

    def __init__(self, group=None, params=None):
        """ModifyTargetParamsReq

        The model defined in huaweicloud sdk

        :param group: 参数分组
        :type group: str
        :param params: 修改的参数信息
        :type params: list[:class:`huaweicloudsdkdrs.v3.ParamsReqBean`]
        """
        
        

        self._group = None
        self._params = None
        self.discriminator = None

        self.group = group
        self.params = params

    @property
    def group(self):
        """Gets the group of this ModifyTargetParamsReq.

        参数分组

        :return: The group of this ModifyTargetParamsReq.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ModifyTargetParamsReq.

        参数分组

        :param group: The group of this ModifyTargetParamsReq.
        :type group: str
        """
        self._group = group

    @property
    def params(self):
        """Gets the params of this ModifyTargetParamsReq.

        修改的参数信息

        :return: The params of this ModifyTargetParamsReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ParamsReqBean`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ModifyTargetParamsReq.

        修改的参数信息

        :param params: The params of this ModifyTargetParamsReq.
        :type params: list[:class:`huaweicloudsdkdrs.v3.ParamsReqBean`]
        """
        self._params = params

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
        if not isinstance(other, ModifyTargetParamsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
