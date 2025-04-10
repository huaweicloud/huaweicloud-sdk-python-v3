# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndividualParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mobiles': 'list[str]',
        'dync_params': 'list[IndividualContentParam]'
    }

    attribute_map = {
        'mobiles': 'mobiles',
        'dync_params': 'dync_params'
    }

    def __init__(self, mobiles=None, dync_params=None):
        r"""IndividualParam

        The model defined in huaweicloud sdk

        :param mobiles: 个性化动态参数号码列表，最多支持5000个号码。  &gt; 长度指的是单个号码的长度。 
        :type mobiles: list[str]
        :param dync_params: 个性化动态参数数组。 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 
        :type dync_params: list[:class:`huaweicloudsdkkoomessage.v1.IndividualContentParam`]
        """
        
        

        self._mobiles = None
        self._dync_params = None
        self.discriminator = None

        self.mobiles = mobiles
        self.dync_params = dync_params

    @property
    def mobiles(self):
        r"""Gets the mobiles of this IndividualParam.

        个性化动态参数号码列表，最多支持5000个号码。  > 长度指的是单个号码的长度。 

        :return: The mobiles of this IndividualParam.
        :rtype: list[str]
        """
        return self._mobiles

    @mobiles.setter
    def mobiles(self, mobiles):
        r"""Sets the mobiles of this IndividualParam.

        个性化动态参数号码列表，最多支持5000个号码。  > 长度指的是单个号码的长度。 

        :param mobiles: The mobiles of this IndividualParam.
        :type mobiles: list[str]
        """
        self._mobiles = mobiles

    @property
    def dync_params(self):
        r"""Gets the dync_params of this IndividualParam.

        个性化动态参数数组。 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 

        :return: The dync_params of this IndividualParam.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.IndividualContentParam`]
        """
        return self._dync_params

    @dync_params.setter
    def dync_params(self, dync_params):
        r"""Sets the dync_params of this IndividualParam.

        个性化动态参数数组。 参数顺序按照模板创建时参数占位符的顺序传入，例如创建模板时设置动参有#p_1#、#p_2#、#p_3#，则传入的参数数组顺序第一个元素为#p_1#，第二个元素是#p_2#，第三个元素为#p_3#。 

        :param dync_params: The dync_params of this IndividualParam.
        :type dync_params: list[:class:`huaweicloudsdkkoomessage.v1.IndividualContentParam`]
        """
        self._dync_params = dync_params

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
        if not isinstance(other, IndividualParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
