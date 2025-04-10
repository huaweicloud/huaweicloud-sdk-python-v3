# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'warm_up_num': 'int',
        'max_num': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'warm_up_num': 'warm_up_num',
        'max_num': 'max_num'
    }

    def __init__(self, spec_code=None, warm_up_num=None, max_num=None):
        r"""ResourceDef

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格编码,从查询规格列表ListSpecs接口获取
        :type spec_code: str
        :param warm_up_num: 预热资源量
        :type warm_up_num: int
        :param max_num: 最大资源量，不填默认为预热资源量，即不使用弹性资源
        :type max_num: int
        """
        
        

        self._spec_code = None
        self._warm_up_num = None
        self._max_num = None
        self.discriminator = None

        self.spec_code = spec_code
        self.warm_up_num = warm_up_num
        if max_num is not None:
            self.max_num = max_num

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ResourceDef.

        资源规格编码,从查询规格列表ListSpecs接口获取

        :return: The spec_code of this ResourceDef.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ResourceDef.

        资源规格编码,从查询规格列表ListSpecs接口获取

        :param spec_code: The spec_code of this ResourceDef.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def warm_up_num(self):
        r"""Gets the warm_up_num of this ResourceDef.

        预热资源量

        :return: The warm_up_num of this ResourceDef.
        :rtype: int
        """
        return self._warm_up_num

    @warm_up_num.setter
    def warm_up_num(self, warm_up_num):
        r"""Sets the warm_up_num of this ResourceDef.

        预热资源量

        :param warm_up_num: The warm_up_num of this ResourceDef.
        :type warm_up_num: int
        """
        self._warm_up_num = warm_up_num

    @property
    def max_num(self):
        r"""Gets the max_num of this ResourceDef.

        最大资源量，不填默认为预热资源量，即不使用弹性资源

        :return: The max_num of this ResourceDef.
        :rtype: int
        """
        return self._max_num

    @max_num.setter
    def max_num(self, max_num):
        r"""Sets the max_num of this ResourceDef.

        最大资源量，不填默认为预热资源量，即不使用弹性资源

        :param max_num: The max_num of this ResourceDef.
        :type max_num: int
        """
        self._max_num = max_num

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
        if not isinstance(other, ResourceDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
