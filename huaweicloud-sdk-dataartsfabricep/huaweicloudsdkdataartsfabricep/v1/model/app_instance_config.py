# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppInstanceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pgsql_instance_config': 'PGSQLInstanceConfig',
        'model_instance_config': 'ModelServiceInstanceConfig'
    }

    attribute_map = {
        'pgsql_instance_config': 'pgsql_instance_config',
        'model_instance_config': 'model_instance_config'
    }

    def __init__(self, pgsql_instance_config=None, model_instance_config=None):
        r"""AppInstanceConfig

        The model defined in huaweicloud sdk

        :param pgsql_instance_config: 
        :type pgsql_instance_config: :class:`huaweicloudsdkdataartsfabricep.v1.PGSQLInstanceConfig`
        :param model_instance_config: 
        :type model_instance_config: :class:`huaweicloudsdkdataartsfabricep.v1.ModelServiceInstanceConfig`
        """
        
        

        self._pgsql_instance_config = None
        self._model_instance_config = None
        self.discriminator = None

        if pgsql_instance_config is not None:
            self.pgsql_instance_config = pgsql_instance_config
        if model_instance_config is not None:
            self.model_instance_config = model_instance_config

    @property
    def pgsql_instance_config(self):
        r"""Gets the pgsql_instance_config of this AppInstanceConfig.

        :return: The pgsql_instance_config of this AppInstanceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.PGSQLInstanceConfig`
        """
        return self._pgsql_instance_config

    @pgsql_instance_config.setter
    def pgsql_instance_config(self, pgsql_instance_config):
        r"""Sets the pgsql_instance_config of this AppInstanceConfig.

        :param pgsql_instance_config: The pgsql_instance_config of this AppInstanceConfig.
        :type pgsql_instance_config: :class:`huaweicloudsdkdataartsfabricep.v1.PGSQLInstanceConfig`
        """
        self._pgsql_instance_config = pgsql_instance_config

    @property
    def model_instance_config(self):
        r"""Gets the model_instance_config of this AppInstanceConfig.

        :return: The model_instance_config of this AppInstanceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ModelServiceInstanceConfig`
        """
        return self._model_instance_config

    @model_instance_config.setter
    def model_instance_config(self, model_instance_config):
        r"""Sets the model_instance_config of this AppInstanceConfig.

        :param model_instance_config: The model_instance_config of this AppInstanceConfig.
        :type model_instance_config: :class:`huaweicloudsdkdataartsfabricep.v1.ModelServiceInstanceConfig`
        """
        self._model_instance_config = model_instance_config

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
        if not isinstance(other, AppInstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
