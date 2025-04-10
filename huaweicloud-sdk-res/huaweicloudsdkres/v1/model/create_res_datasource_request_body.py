# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResDatasourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_name': 'str',
        'specs_config': 'SpecsConfig',
        'data_config': 'DataConfig'
    }

    attribute_map = {
        'datasource_name': 'datasource_name',
        'specs_config': 'specs_config',
        'data_config': 'data_config'
    }

    def __init__(self, datasource_name=None, specs_config=None, data_config=None):
        r"""CreateResDatasourceRequestBody

        The model defined in huaweicloud sdk

        :param datasource_name: 数据源名称，1-64位字母、数字、下划线、中划线组合。
        :type datasource_name: str
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        :param data_config: 
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        
        

        self._datasource_name = None
        self._specs_config = None
        self._data_config = None
        self.discriminator = None

        self.datasource_name = datasource_name
        self.specs_config = specs_config
        self.data_config = data_config

    @property
    def datasource_name(self):
        r"""Gets the datasource_name of this CreateResDatasourceRequestBody.

        数据源名称，1-64位字母、数字、下划线、中划线组合。

        :return: The datasource_name of this CreateResDatasourceRequestBody.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        r"""Sets the datasource_name of this CreateResDatasourceRequestBody.

        数据源名称，1-64位字母、数字、下划线、中划线组合。

        :param datasource_name: The datasource_name of this CreateResDatasourceRequestBody.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def specs_config(self):
        r"""Gets the specs_config of this CreateResDatasourceRequestBody.

        :return: The specs_config of this CreateResDatasourceRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        r"""Sets the specs_config of this CreateResDatasourceRequestBody.

        :param specs_config: The specs_config of this CreateResDatasourceRequestBody.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

    @property
    def data_config(self):
        r"""Gets the data_config of this CreateResDatasourceRequestBody.

        :return: The data_config of this CreateResDatasourceRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        r"""Sets the data_config of this CreateResDatasourceRequestBody.

        :param data_config: The data_config of this CreateResDatasourceRequestBody.
        :type data_config: :class:`huaweicloudsdkres.v1.DataConfig`
        """
        self._data_config = data_config

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
        if not isinstance(other, CreateResDatasourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
