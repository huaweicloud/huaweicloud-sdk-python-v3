# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonParamV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'param_key': 'str',
        'param_name': 'str',
        'is_show': 'int',
        'is_required': 'int'
    }

    attribute_map = {
        'param_key': 'param_key',
        'param_name': 'param_name',
        'is_show': 'is_show',
        'is_required': 'is_required'
    }

    def __init__(self, param_key=None, param_name=None, is_show=None, is_required=None):
        """CommonParamV2

        The model defined in huaweicloud sdk

        :param param_key: 参数标识
        :type param_key: str
        :param param_name: 参数名称
        :type param_name: str
        :param is_show: 是否展示
        :type is_show: int
        :param is_required: 是否必填
        :type is_required: int
        """
        
        

        self._param_key = None
        self._param_name = None
        self._is_show = None
        self._is_required = None
        self.discriminator = None

        if param_key is not None:
            self.param_key = param_key
        if param_name is not None:
            self.param_name = param_name
        if is_show is not None:
            self.is_show = is_show
        if is_required is not None:
            self.is_required = is_required

    @property
    def param_key(self):
        """Gets the param_key of this CommonParamV2.

        参数标识

        :return: The param_key of this CommonParamV2.
        :rtype: str
        """
        return self._param_key

    @param_key.setter
    def param_key(self, param_key):
        """Sets the param_key of this CommonParamV2.

        参数标识

        :param param_key: The param_key of this CommonParamV2.
        :type param_key: str
        """
        self._param_key = param_key

    @property
    def param_name(self):
        """Gets the param_name of this CommonParamV2.

        参数名称

        :return: The param_name of this CommonParamV2.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this CommonParamV2.

        参数名称

        :param param_name: The param_name of this CommonParamV2.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def is_show(self):
        """Gets the is_show of this CommonParamV2.

        是否展示

        :return: The is_show of this CommonParamV2.
        :rtype: int
        """
        return self._is_show

    @is_show.setter
    def is_show(self, is_show):
        """Sets the is_show of this CommonParamV2.

        是否展示

        :param is_show: The is_show of this CommonParamV2.
        :type is_show: int
        """
        self._is_show = is_show

    @property
    def is_required(self):
        """Gets the is_required of this CommonParamV2.

        是否必填

        :return: The is_required of this CommonParamV2.
        :rtype: int
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this CommonParamV2.

        是否必填

        :param is_required: The is_required of this CommonParamV2.
        :type is_required: int
        """
        self._is_required = is_required

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
        if not isinstance(other, CommonParamV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
