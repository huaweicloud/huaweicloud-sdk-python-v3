# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResDatastructRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'data_config': 'DataConfig',
        'specs_config': 'SpecsConfig'
    }

    attribute_map = {
        'name': 'name',
        'data_config': 'data_config',
        'specs_config': 'specs_config'
    }

    def __init__(self, name=None, data_config=None, specs_config=None):
        """UpdateResDatastructRequestBody

        The model defined in huaweicloud sdk

        :param name: 数据源名称:，1-64位字母、数字、下划线、中划线组合。
        :type name: str
        :param data_config: 
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        
        

        self._name = None
        self._data_config = None
        self._specs_config = None
        self.discriminator = None

        self.name = name
        self.data_config = data_config
        self.specs_config = specs_config

    @property
    def name(self):
        """Gets the name of this UpdateResDatastructRequestBody.

        数据源名称:，1-64位字母、数字、下划线、中划线组合。

        :return: The name of this UpdateResDatastructRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateResDatastructRequestBody.

        数据源名称:，1-64位字母、数字、下划线、中划线组合。

        :param name: The name of this UpdateResDatastructRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def data_config(self):
        """Gets the data_config of this UpdateResDatastructRequestBody.


        :return: The data_config of this UpdateResDatastructRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """Sets the data_config of this UpdateResDatastructRequestBody.


        :param data_config: The data_config of this UpdateResDatastructRequestBody.
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        self._data_config = data_config

    @property
    def specs_config(self):
        """Gets the specs_config of this UpdateResDatastructRequestBody.


        :return: The specs_config of this UpdateResDatastructRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        """Sets the specs_config of this UpdateResDatastructRequestBody.


        :param specs_config: The specs_config of this UpdateResDatastructRequestBody.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

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
        if not isinstance(other, UpdateResDatastructRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
